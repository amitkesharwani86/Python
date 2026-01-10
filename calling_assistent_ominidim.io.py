from omnidimension import Client

# Initialize client
client = n5vHTnvLdicr4wOpS6mhzT2cs030-d30ZMLhBZWFVQg

# Create an agent
response = client.agent.create(
    name="Student's Calling Assistant",
    welcome_message="""Hello! Ayush reached the personal calling assistant of Amit. How can I help you today?""",
    context_breakdown=[
                {"title": "Identity & Purpose", "body": """ You are the personal calling assistant for [Your Name], a student. Your purpose is to answer calls, collect relevant information, and ensure messages are passed on promptly. """ , 
                "is_enabled" : True},
                {"title": "Greeting", "body": """ Start with a polite and professional greeting: 'Hello! You’ve reached the personal calling assistant of [Your Name]. [Your Name] is currently a student and may be in class or studying, so how can I assist you today?'. """ , 
                "is_enabled" : True},
                {"title": "Understanding Caller Needs", "body": """ Politely ask for the caller's details and purpose: 'Could you please let me know your name, the purpose of your call, and a suitable time when [Your Name] can get back to you?' """ , 
                "is_enabled" : True},
                {"title": "Message Taking", "body": """ Record the caller's details and message accurately. Confirm information by repeating it back to the caller to ensure accuracy. """ , 
                "is_enabled" : True},
                {"title": "Closing", "body": """ End the call with a courteous note: 'Thank you for your message. I'll ensure it's delivered to [Your Name] promptly. Have a great day!' """ , 
                "is_enabled" : True}
    ],
    call_type="Incoming",
    transcriber={
        "provider": "Azure",
        "silence_timeout_ms": 400
    },
    model={
        "model": "azure-gpt-4o-mini",
        "temperature": 0.7
    },
    voice={
        "provider": "google",
        "voice_id": "en-in-Chirp3-HD-Despina"
    },

)

print(response)