import openai

openai.api_key = key

# basic example 1
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt="who was Carl sagan?"  # query
)
print(response)  # print all response
print(response.choices[0].text)
