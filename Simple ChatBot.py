import random

class Bot:
    def __init__(self):
        self.context = {}

    def greeting(self):
        return random.choice(["Hi there!", "Hello!", "Hey!"])

    def basic_questions(self, user_input):
        if "how are you" in user_input:
            return random.choice(["I'm doing well, thanks!", "I'm good, how about you?", "I'm a bot, but I'm functioning well!"])
        elif "your name" in user_input:
            return "I'm just a Bot. You can call me Bot."
        elif "what do you do" in user_input:
            return "I'm here to chat and assist you with basic questions."
        elif "who created you" in user_input:
            return "I was created by a developer using Python."
        elif "how old are you" in user_input:
            return "I don't have an age. I'm just an AI-assisted system."

    def farewell(self):
        return random.choice(["Goodbye!", "See you later!", "Bye!"])

    def ask_user_questions(self):
        questions = ["What's your favourite hobby?", "Do you enjoy programming?", "Have you visited me once before?"]
        for question in questions:
            user_response = input("Bot: " + question + " ")
            self.context[question] = user_response
            print("Bot: That's interesting! You said your favourite hobby is", user_response)

    def handle_input(self, user_input):
        if "bye" in user_input:
            return self.farewell()
        elif any(question_keyword in user_input for question_keyword in ["hello", "hi", "hey"]):
            return self.greeting()
        elif any(question_keyword in user_input for question_keyword in ["how are you", "your name", "what do you do", "who created you", "how old are you"]):
            return self.basic_questions(user_input)
        elif any(question_keyword in user_input for question_keyword in ["what's your favourite colour", "enjoy programming", "travelled recently"]):
            return "Bot: I remember you said your favourite colour is " + self.context["What's your favorite color?"]
        else:
            return "Bot: I'm not sure how to respond to that. Can you ask me something else?"

if __name__ == "__main__":
    chatbot = Bot()
    print("Hello! Ask me something or say goodbye to end the conversation.")

    while True:
        user_input = input("You: ").lower()
        response = chatbot.handle_input(user_input)
        print(response)

        if "bye" in user_input:
            break

    chatbot.ask_user_questions()
