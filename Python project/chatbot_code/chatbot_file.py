import datetime

responses = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi there! How are you?",
    "name": "I am your Mini AI Chatbot.",
    "python": "Python is a powerful and easy programming language.",
    "time": f"Current time is: {datetime.datetime.now().strftime('%H:%M:%S')}",
    "date": f"Today's date is: {datetime.datetime.now().strftime('%d-%m-%Y')}",
    "how are you": "I’m fine, thank you!",
    "help": "You can ask me about Python, time, date, greetings or just say bye to exit."
}

def log_chat(text):
    with open("chat_history.txt", "a") as f:
        f.write(text)

def chatbot():
    print("Mini AI Chatbot Ready! Type 'bye' to exit.")
    while True:
        user = input("You: ").lower()
        if user == "bye":
            bot_reply = "Bye Risana, take care!"
            print(f"Bot: {bot_reply}")
            log_chat(f"You: bye\nBot: {bot_reply}\n")
            break
        response_found = False
        for key in responses:
            if key in user:
                bot_reply = responses[key]
                print(f"Bot: {bot_reply}")
                log_chat(f"You: {user}\nBot: {bot_reply}\n")
                response_found = True
                break
        if not response_found:
            bot_reply = "Sorry, I didn't understand that. Try again!"
            print(f"Bot: {bot_reply}")
            log_chat(f"You: {user}\nBot: {bot_reply}\n")

chatbot()