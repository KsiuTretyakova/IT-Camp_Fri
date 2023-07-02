import openai

openai.api_key = "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"

models = openai.Model.list()
# print(models)


def handle_input(user_input):
    copletion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )
    return copletion

