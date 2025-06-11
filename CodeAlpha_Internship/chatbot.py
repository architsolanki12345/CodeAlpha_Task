def chatbot():
    responses = {
        "hello": "Hi there!",
        "hi": "Hello!",
        "how are you": "I'm fine, thanks!",
        "bye": "Goodbye! Have a nice day!",
        "help": "Try saying 'hello', 'how are you', or 'bye'."
    }

    print("💬 Welcome to ChatBot! Type 'exit' to stop.")

    while True:
        user_input = input("You: ").lower()
        if user_input == "exit":
            print("Bot: See you next time!")
            break
        print("Bot:", responses.get(user_input, "I don't understand that."))

chatbot()
