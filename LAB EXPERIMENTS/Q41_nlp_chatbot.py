responses={"hello":"Hello! How can I help you?","name":"I am a simple AI lab chatbot.","bye":"Goodbye!"}
def reply(message):
    for key,value in responses.items():
        if key in message.lower(): return value
    return "Sorry, I did not understand. Please ask another question."
for message in ["hello","what is your name","bye"]:
    print("You:",message)
    print("Bot:",reply(message))
