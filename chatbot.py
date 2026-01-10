import re  

# Define a simple chatbot class  
class SimpleChatbot:  
    def __init__(self):  
        self.patterns = {  
            r'hi|hello|hey': "Hello! How can I assist you today?",  
            r'how are you': "I'm just a program, but thanks for asking!",  
            r'goodbye|bye': "Goodbye! Have a great day!",  
            r'i need (.*)': "Why do you need {0}?",  
            r'what is your name': "I am a simple chatbot created by you!",  
            r'(.*)': "I'm sorry, I didn't understand that."  
        }  
    
    def respond(self, user_input):  
        for pattern, response in self.patterns.items():  
            if re.search(pattern, user_input, re.IGNORECASE):  
                return response.format(*re.findall(pattern, user_input))  
        return "I'm not sure how to respond to that."  

# Main function to run the chatbot  
def main():  
    chatbot = SimpleChatbot()  
    print("Chatbot: Hi! I'm a simple chatbot. (Type 'exit' to stop)")  
    
    while True:  
        user_input = input("You: ")  
        if user_input.lower() == 'exit':  
            print("Chatbot: Goodbye!")  
            break  
        response = chatbot.respond(user_input)  
        print(f"Chatbot: {response}")  

if __name__ == "__main__":  
    main()  