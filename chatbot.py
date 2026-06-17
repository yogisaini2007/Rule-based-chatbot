# CloneAi - A Simple Rule-Based AI Chatbot
# Authors: Aryan Mali
# Internship Project 1

print("Welcome to AI Chatbot")
print("Type 'bye' or 'exit' to stop the chatbot")

while True:

    user_input = input("You: ")
    user_input = user_input.lower().strip()
    user_input = " ".join(user_input.lower().strip().split())
    

    if user_input == "hello" or user_input == "hi" or user_input == "hey" or user_input == "hii":
        print("Bot: Hello! Nice to meet you")

    elif user_input == "how are you":
        print("Bot: I am fine, thanks for asking")

    elif user_input == "who are you":
        print("Bot: I am a simple AI chatbot")

    elif user_input == "help":
        print("Bot: You can ask me basic questions")

    elif user_input == "what is your name":
        print("Bot: My name is CloneAi")

    elif user_input == "bye" or user_input == "exit":
        print("Bot: Goodbye! Have a nice day")
        break

    else:
        print("Bot: Sorry, I don't understand that")