from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create and configure the chatbot
chatbot = ChatBot(
    "SimpleBot",
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation'
    ],
    database_uri='sqlite:///database.sqlite3'  # Database to store learned conversations
)

# Train the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')  # Train with English data

print("ChatBot is ready! Type 'exit' to end the conversation.\n")

# Start chatting
while True:
    try:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = chatbot.get_response(user_input)
        print(f"Bot: {response}")
    except Exception as e:
        print(f"Error: {e}")