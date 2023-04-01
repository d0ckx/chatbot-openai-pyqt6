import openai


class Chatbot:
    def __init__(self):
        # revoked
        openai.api_key = "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"

    # this is the method that gives input to the AI and gets its response
    def get_repsonse(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.5
        ).choices[0].text
        return response


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_repsonse("Write a joke about birds")
    print(response)


