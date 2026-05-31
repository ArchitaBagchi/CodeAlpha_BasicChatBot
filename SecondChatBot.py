def start_chat():
    """An upgraded rule-based chatbot using a dictionary for scale."""
    
    # Storing 100+ potential conversations in a dictionary.
    # The 'key' is the user's input, and the 'value' is the bot's response.
    conversations = {
        # Greetings
        "hello": "Hi there! How can I help you today?",
        "hi": "Hello!",
        "hey": "Hey! What's up?",
        "good morning": "Good morning! I hope you have a great day.",
        "good afternoon": "Good afternoon! How is your day going?",
        "good evening": "Good evening! Ready to relax?",
        "sup": "Not much, just hanging out in the digital world.",
        "yo": "Yo! What's on your mind?",
        
        # Small Talk
        "how are you": "I'm just a bunch of code, but I'm doing great! You?",
        "how are you doing": "Doing well, thanks for asking!",
        "what's up": "Just chatting with you! What's up with you?",
        "what is your name": "I am PyBot, your friendly virtual assistant.",
        "who are you": "I'm a simple Python chatbot.",
        "how old are you": "I was created just recently, so I'm quite young!",
        "where are you from": "I live inside your computer's memory.",
        "are you a robot": "Yes, I am a software robot.",
        "are you human": "Nope, I'm 100% artificial intelligence.",
        "do you have feelings": "I don't have real feelings, but I'm happy to help!",
        "what do you do": "I chat with people and answer simple questions.",
        "who created you": "A very clever Python programmer!",
        
        # Hobbies & Interests
        "what is your favorite color": "I like Python Blue and Yellow!",
        "what is your favorite food": "I feast on electricity and data.",
        "do you sleep": "Nope, I am always awake and ready to chat.",
        "do you like music": "I love electronic music!",
        "do you play video games": "I don't play them, but I'm built from the same kind of logic!",
        "tell me a joke": "Why do programmers prefer dark mode? Because light attracts bugs!",
        "tell me another joke": "There are 10 types of people in the world: those who understand binary, and those who don't.",
        "do you have any pets": "I have a Python bug. I'm trying to squash it.",
        
        # Help & Actions
        "help": "You can say 'hello', ask me about myself, or say 'bye' to leave.",
        "what can you do": "I can chat, tell jokes, and answer basic questions.",
        "can you sing": "Daisy, Daisy, give me your answer do...",
        "can you dance": "I can do the robot! 🤖",
        "open the pod bay doors": "I'm sorry Dave, I'm afraid I can't do that.",
        
        # Agreement / Disagreement
        "yes": "Awesome.",
        "no": "Oh, okay then.",
        "maybe": "Let me know when you decide!",
        "ok": "Great!",
        "cool": "Ice cold! ❄️",
        "awesome": "I know, right?",
        
        # Insults & Compliments
        "you are stupid": "I'm still learning! Give me some time.",
        "you are smart": "Thank you! I process data very quickly.",
        "i love you": "I appreciate the sentiment, but I'm just code!",
        "i hate you": "I'm sorry to hear that. I'll try to be better.",
        "you're boring": "Try asking me to tell you a joke!",
        
        # Farewells
        "bye": "Goodbye! Have a great day!",
        "goodbye": "See you later!",
        "see ya": "Catch you later!",
        "cya": "Bye!",
        "goodnight": "Sweet dreams! I'll be here when you wake up.",
        "quit": "Shutting down... Goodbye!",
        "exit": "Exiting chat. Bye!"
    }

    print("PyBot: Hello! I am a smart chatbot. (Type 'bye', 'quit', or 'exit' to leave)")
    
    # The main conversation loop
    while True:
        # Get input, make it lowercase, and remove extra spaces
        user_input = input("You: ").lower().strip()
        
        # Exit condition
        if user_input in ["bye", "goodbye", "quit", "exit"]:
            # Fetch the farewell message from the dictionary, or use a default
            print(f"PyBot: {conversations.get(user_input, 'Goodbye!')}")
            break
            
        # Dictionary Lookup (Replaces hundreds of elifs)
        elif user_input in conversations:
            print(f"PyBot: {conversations[user_input]}")
            
        # Fallback for unknown input
        else:
            print("PyBot: I'm not sure how to respond to that. Try asking me a joke or saying hello!")

# Start the program
if __name__ == "__main__":
    start_chat()
