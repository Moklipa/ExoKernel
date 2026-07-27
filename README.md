# ExoKernel
ExoKernel — экспериментальная модульная архитектура ИИ, разделяющая разговорное микроядро и подключаемые доменные графы (код, логика, системы).

<div align="center">

# 🧬 ExoKernel Architecture

**Experimental Modular Neural Architecture with Dynamic Domain Splicing & Concept Routing**

[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Transformers-FFD21E?style=for-the-badge)](https://huggingface.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![VRAM](https://img.shields.io/badge/VRAM-2GB%20Friendly-green?style=for-the-badge&logo=nvidia)](https://nvidia.com)

[Основы](#-основы-и-концепция) • [Архитектура](#-архитектура-системы) • [Быстрый старт](#-быстрый-старт) • [Структура](#-структура-проекта) • [Roadmap](#-дорожная-карта-roadmap)

</div>

---

> [!NOTE]
> **ExoKernel** — это концептуальное исследование (Proof of Concept). Проект демонстрирует, как разделить общее разговорное микроядро и специализированные предметные графы без гигантских затрат VRAM.

---

## 💡 Основы и концепция

Традиционные LLM пытаются вместить все знания мира в единый монолитный массив весов. `ExoKernel` предлагает принципиально иной, модульный подход:

| Традиционный подход (Monolithic LLM) | Подход ExoKernel (Split-Kernel Architecture) |
| :--- | :--- |
| ❌ Требует десятки гигабайт VRAM | ✅ Работает даже на GPU с 2 ГБ VRAM |
| ❌ Переобучение затрагивает всю модель | ✅ Домены подключаются и обновляются независимо |
| ❌ Скорость генерации падает с ростом весов | ✅ Разговорное ядро всегда остаётся лёгким |

---

## 🏗️ Архитектура системы

```text
                     ┌───────────────────────────┐
                     │        User Input         │
                     └─────────────┬─────────────┘
                                   │
                                   ▼
                   ┌───────────────────────────────┐
                   │        ExoKernel Core         │
                   │   (Instruct / Conversation)   │
                   └───────────────┬───────────────┘
                                   │
                 ┌─────────────────┴─────────────────┐
                 ▼                                   ▼
      ┌────────────────────┐               ┌────────────────────┐
      │  Dynamic Splicer   │ ◄───────────► │   Domain Graphs    │
      │ (Concept Routing)  │               │ (Code / Sys / Math)│
      └────────────────────┘               └────────────────────┘
```

    [!IMPORTANT]
    Как это работает:

        Core (Разговорное ядро): Удерживает контекст беседы, отвечает за диалоговый синтаксис и понимание намерений пользователя.

        Dynamic Splicer: Оценивает эмбеддинги запроса и "на лету" подмешивает токены/представления нужного домена.

        Domain Engines: Автономные легковесные модули (программирование, системные команды Linux, математика).

🚀 Быстрый старт

    [!TIP]
    Для запуска достаточно обычной видеокарты начального уровня или даже CPU!

1. Клонирование и установка зависимостей
Bash

# Клонируем репозиторий
git clone [https://github.com/YOUR_USERNAME/exokernel.git](https://github.com/YOUR_USERNAME/exokernel.git)
cd exokernel

# Создаем виртуальное окружение
python3 -m venv venv
source venv/bin/activate  # Для Linux (Mint/Arch)

# Устанавливаем пакеты
pip install -r requirements.txt

2. Запуск терминального чата
Bash

python3 chat.py

📂 Структура проекта
Plaintext

exokernel/
├── 📄 core.py              # Инициализация и сборка ExoKernel Core (Qwen2.5 Instruct)
├── 📄 tokenizer_utils.py   # Настройка токенизатора и служебных токенов
├── 📄 chat.py              # Интерактивный терминальный интерфейс (CLI Chat)
├── 📄 pretrain_core.py     # Скрипт экспериментального базового обучения
├── 📄 train_chat.py        # Скрипт SFT-дообучения
├── 📄 requirements.txt     # Зависимости проекта
└── 📄 README.md            # Документация

🗺️ Дорожная карта (Roadmap)

    [x] Этап 1: Базовая концепция и интеграция Instruct-микроядра (Qwen2.5-0.5B-Instruct).

    [x] Этап 2: Стабильный интерактивный CLI-чат с защитой от зацикливания.

    [ ] Этап 3: Реализация прототипа Dynamic Splicer для маршрутизации запросов.

    [ ] Этап 4: Подключение первого доменного графа (C++ / System Admin code generation).

    [ ] Этап 5: Публикация контрольных точек (checkpoints) подмодулей.

    [!WARNING]
    Проект находится в стадии активной разработки. Pull Request'ы и идеи по улучшению архитектуры только приветствуются!

Made with ❤️ & PyTorch
