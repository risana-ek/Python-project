def chatbot():
    print("Mini AI Chatbot Ready! Type 'bye' to exit.")
    while True:
        user = input("You: ").lower()
        if user == "bye":
            print("Bot: Bye Risana, take care!")
            break
        elif "hello" in user or "hi" in user:
            print("Bot: Hello! How can I help you?")
        elif "name" in user:
            print("Bot: I am your Mini AI Chatbot.")
        elif "python" in user:
            print("Bot: Python is a powerful and easy programming language.")
        elif "time" in user:
            print("Bot: Sorry, I cannot show real time now, but I can tell you time logic!")
        elif "how are you" in user:
            print("Bot: I’m fine, thank you!")
        else:
            print("Bot: Sorry, I didn't understand that. Try again!")

chatbot()