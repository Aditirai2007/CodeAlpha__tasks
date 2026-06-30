def chatbot():
    print("=== Welcome to Basic Chatbot ===")
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Bot: Hi! Nice to meet you.")
        elif user == "how are you":
            print("Bot: I'm fine, thanks! How about you?")
        elif user == "what is your name":
            print("Bot: My name is CodeBot.")
        elif user == "who created you":
            print("Bot: I was created using Python.")
        elif user == "bye":
            print("Bot: Goodbye! Have a great day.")
            break
        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()
