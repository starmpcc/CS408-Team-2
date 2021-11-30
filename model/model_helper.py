from transformers import pipeline, PreTrainedTokenizerFast, GPT2LMHeadModel
import torch


"""
Model that generate model from user input with pretrained model
See usage in __main__ part
"""
class Model:

    def __init__(self, model_path = "/root/CS408-Team-2/model/run/"):
        self.model = GPT2LMHeadModel.from_pretrained(model_path, local_files_only = True)
        self.tokenizer = PreTrainedTokenizerFast.from_pretrained("skt/kogpt2-base-v2",
            bos_token='</s>', eos_token='</s>', unk_token='<unk>',
            pad_token='<pad>', mask_token='<mask>')


    def generate(self, inp, context):
        estimated_num_tokens = len(inp.split(' '))
        if estimated_num_tokens > 50:
            inp = " ".join(inp.split(' ')[-50:])
        else:
            inp = context[max(-(50-estimated_num_tokens), -len(context)+1):] + inp
        out = self.forward(inp)

        end_out = max([out.rfind('.'), out.rfind('!'), out.rfind('?')])
        out = out[len(inp)+1:end_out+1]
        context = context + inp + out
        if len(context) > 1000: context = context[-1000:]
        return out, context

    def forward(self, inp):
        input_ids = self.tokenizer.encode(inp)
        gen_ids = self.model.generate(torch.tensor([input_ids]),
            max_length=128,
            repetition_penalty=2.0,
            pad_token_id=self.tokenizer.pad_token_id,
            eos_token_id=self.tokenizer.eos_token_id,
            bos_token_id=self.tokenizer.bos_token_id,
            use_cache=True)
        out = self.tokenizer.decode(gen_ids[0,:].tolist())

        return out

if __name__ == "__main__":
    model = Model()
    context = ""

    while True:
        inp = input("소설을 작성해 주세요: ")
        out, context = model.generate(inp, context)
        print(out)
