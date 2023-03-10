import openai

openai.api_key = key

# basic example 1
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt="who was Carl sagan?"  # query
)
print(response)  # print all response
print(response.choices[0].text)


# max_tokens
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt="who was Carl sagan?",  # query
    max_tokens=4000
)
print(response)  # print all response


# Other models
models_list = ["text-davinci-003", "text-davinci-002", "text-curie-001", "text-babbage-001", "text-ada-001"]
for models in models_list:
    response = openai.Completion.create(
        model=models,
        prompt="Who was Carl Sagan?",
        max_tokens=2000
        )
    response = response.choices[0].text.replace('\n', '') + '\n'
    print(models + ':\n' + response)

    
# More responses
response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Who was Carl Sagan?",
    max_tokens=2000,
    n=4
)
for i in range(len(response.choices)):
    print(response.choices[i].text)
