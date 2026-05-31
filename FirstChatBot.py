def start_chat():
    """A simple rule-based chatbot."""
    
    print("Chatbot: Hello! I am a simple chatbot. (Type 'bye' to exit)")
    
    # Loop keeps the conversation going until the user says 'bye'
    while True:
        # Get input from the user, convert to lowercase, and strip extra spaces
        user_input = input("You: ").lower().strip()
        
        # Rule-based responses using if-elif-else
        if user_input == "hello":
            print("Chatbot: Hi!")
            
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")
            
        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break  # Exits the loop and ends the program
            
        else:
            # Fallback response for inputs the bot doesn't recognize
            print("Chatbot: I only understand 'hello', 'how are you', or 'bye'.")

# Call the function to start the chatbot
if __name__ == "__main__":
    start_chat()
