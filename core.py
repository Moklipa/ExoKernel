# core.py
import torch
import torch.nn as nn
from transformers import AutoModelForCausalLM

class ExoKernelCore(nn.Module):
    def __init__(self, model_name="Qwen/Qwen2.5-0.5B-Instruct"):
        super().__init__()
        print(f"[ExoKernel-Core] Загрузка Instruct-микроядра '{model_name}'...")
        self.base_model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
            device_map="auto"
        )
        self.config = self.base_model.config

    def forward(self, input_ids, labels=None, **kwargs):
        return self.base_model(input_ids=input_ids, labels=labels, **kwargs)

    def generate(self, *args, **kwargs):
        return self.base_model.generate(*args, **kwargs)

def build_exokernel_core():
    return ExoKernelCore()
