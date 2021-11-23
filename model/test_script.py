from transformers import pipeline, PreTrainedTokenizerFast, GPT2LMHeadModel
import torch
model = GPT2LMHeadModel.from_pretrained("/root/CS408-Team-2/model/run/", local_files_only = True)

tokenizer = PreTrainedTokenizerFast.from_pretrained("skt/kogpt2-base-v2",
    bos_token='</s>', eos_token='</s>', unk_token='<unk>',
    pad_token='<pad>', mask_token='<mask>')

def forward(text):
    input_ids = tokenizer.encode(text)
    gen_ids = model.generate(torch.tensor([input_ids]),
        max_length=128,
        repetition_penalty=2.0,
        pad_token_id=tokenizer.pad_token_id,
        eos_token_id=tokenizer.eos_token_id,
        bos_token_id=tokenizer.bos_token_id,
        use_cache=True)
    generated = tokenizer.decode(gen_ids[0,:].tolist())
    return generated

context = ""
while True:
    inp = input("Please write your own story: ")
    out = forward((context+inp)[:256])
    context = context + out
    print(out)