import torch
import torch.nn as nn
from transformers import PreTrainedTokenizerFast, GPT2LMHeadModel, Trainer, default_data_collator
from datasets import load_dataset
import math

assert torch.cuda.is_available()

NUM_WORKERS = 4
TRAIN_TEST_RATIO = 0.9
BLOCK_SIZE = 1024
NUM_EPOCHS = 2

tokenizer = PreTrainedTokenizerFast.from_pretrained("skt/kogpt2-base-v2",
    bos_token='</s>', eos_token='</s>', unk_token='<unk>',
    pad_token='<pad>', mask_token='<mask>')

koGPT2 = GPT2LMHeadModel.from_pretrained('skt/kogpt2-base-v2')

dataset = load_dataset("data.raw")
dataset["train"] = load_dataset("data.raw", split = TRAIN_TEST_RATIO)
dataset["val"] = load_dataset("data.raw", split = 1 - TRAIN_TEST_RATIO)
col_names = dataset["train"].column_names

#Tokenize dataset
tokenized_dataset = dataset.map(
        tokenizer,
        batched = True,
        num_proc = NUM_WORKERS,
        remove_columns = col_names
)

def group_text(text):
    concated_text = {k: sum(text[k], []) for k in text.keys()}
    length = len(concated_text[list(text.keys())[0]])
    length = length // BLOCK_SIZE * BLOCK_SIZE
    groupped = {
        k: [l[i: i+ BLOCK_SIZE] for i in range(0, length, BLOCK_SIZE)]
        for k, l in concated_text.items()
    }
    groupped["labels"] = groupped["input_ids"].copy()
    return groupped

groupped_dataset = tokenized_dataset.map(
    group_text,
    batched = True,
    num_proc= NUM_WORKERS,
)

trainer = Trainer(
    model = koGPT2,
    train_dataset = groupped_dataset["train"],
    eval_dataset = groupped_dataset["val"],
    tokenizer = tokenizer,
    data_collator = default_data_collator
)

for i in range(NUM_EPOCHS):
    train_result = trainer.train()

    trainer.save_model()
    trainer.log_metrics("train", train_result.metrics)
    trainer.save_metrics("train", train_result.metrics)
    trainer.save_state()

    val_result = trainer.evaluate()

    try:
        perplexity = math.exp(val_result["eval_loss"])
    except OverflowError:
        perplexity = float("inf")
    val_result["perplexity"] = perplexity

    trainer.log_metrics("eval", val_result)
    trainer.save_metrics("eval", val_result)

    trainer.create_model_card()