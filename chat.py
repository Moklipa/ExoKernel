# chat.py
import torch
from core import build_exokernel_core
from tokenizer_utils import get_exokernel_tokenizer

def chat():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"[ExoKernel] Инициализация системы...")

    tokenizer = get_exokernel_tokenizer()
    model = build_exokernel_core()
    model.eval()

    print("\n" + "="*50)
    print(" Готовое микроядро ExoKernel запущенно! (Напиши 'exit' для выхода)")
    print("="*50 + "\n")

    system_prompt = "Ты — ExoKernel, умный и дружелюбный ассистент."

    while True:
        try:
            user_input = input("You > ").strip()
            if not user_input:
                continue
            if user_input.lower() in ["exit", "quit", "q"]:
                break

            # Форматируем промпт в понятный для модели вид
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ]
            
            prompt_text = tokenizer.apply_chat_template(
                messages, 
                tokenize=False, 
                add_generation_prompt=True
            )

            inputs = tokenizer(prompt_text, return_tensors="pt").to(device)

            with torch.no_grad():
                outputs = model.generate(
                    **inputs,
                    max_new_tokens=128,
                    do_sample=True,
                    temperature=0.6,
                    top_p=0.9,
                    repetition_penalty=1.15,
                    pad_token_id=tokenizer.pad_token_id,
                    eos_token_id=tokenizer.eos_token_id
                )

            # Декодируем только ответ модели
            generated_ids = outputs[0][inputs["input_ids"].shape[1]:]
            response = tokenizer.decode(generated_ids, skip_special_tokens=True)

            print(f"\nExoKernel > {response}\n")
            print("-" * 50)

        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    chat()
