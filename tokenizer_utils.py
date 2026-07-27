# tokenizer_utils.py
from transformers import AutoTokenizer

def get_exokernel_tokenizer():
    # Загружаем токенизатор от Instruct-версии
    tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-0.5B-Instruct")
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    return tokenizer
