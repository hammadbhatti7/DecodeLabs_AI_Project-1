# Rule-Based AI Chatbot — DecodeLabs Project 1 🤖

**Author:** Hammad Bhatti  
**Batch:** 2026  
**Internship:** DecodeLabs  
**Project:** Artificial Intelligence — Project 1

## 📌 Project Overview

This project implements a simple **rule-based AI chatbot** in Python.

It follows the DecodeLabs Project 1 requirements by using explicit **if-else control flow**, handling greetings and exit commands, and running a continuous conversation loop.

## 🎯 Objectives

- Handle greeting commands
- Handle exit commands
- Use `if`, `elif`, and `else` decision-making logic
- Run in a continuous interaction loop
- Demonstrate basic rule-based AI concepts

## 🧠 How It Works

```text
User Input → Normalize → Check Rules → Generate Response
                         ↓
                    Exit command?
                    ↓          ↓
                   Yes         No
                    ↓          ↓
                   End       Continue
```

The chatbot uses predefined rules rather than machine learning or external APIs.

## 💬 Supported Inputs

**Greetings**
```text
hi
hello
hey
salam
assalam o alaikum
```

**Conversation**
```text
what is your name?
who are you?
how are you?
```

**Help**
```text
help
what can you do?
```

**Project information**
```text
tell me about decodelabs
what is project 1?
```

**Exit**
```text
bye
goodbye
exit
quit
```

## 🛠️ Technology

- Python 3
- `if` / `elif` / `else`
- `while` loop
- Functions
- String processing
- Console input/output
- No third-party packages required

## 📁 Project Structure

```text
DecodeLabs-AI-Project1/
├── chatbot.py
└── README.md
```

## 🚀 How to Run

Check Python:

```bash
python --version
```

Run the chatbot:

```bash
python chatbot.py
```

## 🧪 Example Run

```text
==========================================================
🤖 DecodeBot — Rule-Based AI Chatbot
Type 'bye', 'exit', or 'quit' to end the conversation.
==========================================================
You: hello
DecodeBot: Hello! 👋 I am DecodeBot. How can I help you today?

You: what is your name?
DecodeBot: I am DecodeBot, a simple rule-based AI chatbot created for DecodeLabs Project 1.

You: how are you?
DecodeBot: I'm doing great! Thanks for asking. 😊

You: bye
DecodeBot: Goodbye! 👋 Thanks for chatting with DecodeBot.
```

## ✅ Validation

The code was validated for:

- Python syntax
- Greeting handling
- Basic conversation
- Help handling
- Unknown-input fallback
- Exit command handling
- Continuous-loop termination

No external dependencies are required.

## 📚 DecodeLabs Requirement Mapping

| Requirement | Implementation |
|---|---|
| Handle greetings | Greeting rules |
| Handle exit commands | `bye`, `goodbye`, `exit`, `quit` |
| Use if-else logic | `if` / `elif` / `else` |
| Continuous loop | `while True` |
| Control flow | Conditional decision-making |
| Basic AI concepts | Predefined rule-based responses |

## 👨‍💻 Author

**Hammad Bhatti**  
Batch 2026 — DecodeLabs AI Internship

## 📌 Project Status

**Completed and Tested ✅**
