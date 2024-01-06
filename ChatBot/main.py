def simple_chatbot():
    responses = {
        "hi": "Hello!",
        "how are you?": "I'm doing well, thank you!",
        "what is your name?": "I'm a Simple chatbot. You can call me Gaitonde!",
        "bye": "Goodbye! Have a nice day!"
    }

    print("Welcome! Ask me anything or say 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()
        if user_input == 'bye':
            print(responses[user_input])
            break
        
        if user_input in responses:
            print("ChatBot:", responses[user_input])
        else:
            print("ChatBot: I'm sorry, I don't understand that. Can you ask something else?")

if __name__ == "__main__":
    simple_chatbot()
