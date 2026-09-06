"""DecodeLabs AI Internship - Project 1: Rule-Based AI Chatbot."""

def get_response(user_input: str) -> str:
    """Return a response using explicit rule-based if/elif/else logic."""
    message = user_input.strip().lower()

    if not message:
        return "Please type a message so I can help you."
    elif message in {"hi", "hello", "hey", "salam", "assalam o alaikum"}:
        return "Hello! 👋 I am DecodeBot. How can I help you today?"
    elif "your name" in message or "who are you" in message:
        return "I am DecodeBot, a simple rule-based AI chatbot created for DecodeLabs Project 1."
    elif "how are you" in message:
        return "I'm doing great! Thanks for asking. 😊"
    elif "help" in message or "what can you do" in message:
        return ("I can respond to greetings, tell you about myself, and answer a few "
                "predefined questions. Try 'What is your name?' or 'How are you?'")
    elif "decodelabs" in message or "project 1" in message:
        return ("This is DecodeLabs Artificial Intelligence Project 1: "
                "a Rule-Based AI Chatbot built using control flow and if-else logic.")
    elif message in {"bye", "goodbye", "exit", "quit"}:
        return "Goodbye! 👋 Thanks for chatting with DecodeBot."
    else:
        return ("I'm sorry, I don't understand that yet. "
                "Try 'hello', 'help', 'what is your name?', or 'bye'.")


def run_chatbot() -> None:
    """Run continuously until the user enters an exit command."""
    print("=" * 58)
    print("🤖 DecodeBot — Rule-Based AI Chatbot")
    print("Type 'bye', 'exit', or 'quit' to end the conversation.")
    print("=" * 58)

    while True:
        try:
            user_input = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print("\nDecodeBot: Goodbye! 👋")
            break

        print(f"DecodeBot: {get_response(user_input)}")
        if user_input.strip().lower() in {"bye", "goodbye", "exit", "quit"}:
            break


if __name__ == "__main__":
    run_chatbot()
