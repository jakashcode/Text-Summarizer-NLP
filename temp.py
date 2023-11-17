from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch

tokenizer = AutoTokenizer.from_pretrained("artifacts/model_trainer/tokenizer")

device = "cuda" if torch.cuda.is_available() else "cpu"
model_pegasus = AutoModelForSeq2SeqLM.from_pretrained("artifacts/model_trainer/pegasus-samsum-model") 

print(tokenizer)
print()
print(model_pegasus)