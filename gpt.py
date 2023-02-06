import openai
from api_k import KEY

openai.api_key = KEY
file = open('input.txt', 'r')
pt = file.read()
file.close()

response = openai.Completion.create(
    model="text-davinci-003",
    prompt=pt,
    temperature=0,
    max_tokens=60,
    top_p=1,
    frequency_penalty=0.5,
    presence_penalty=0
)

keywords = response["choices"][0]["text"]

pt2 = "classify each words in the given text and list each words' specific category: "+keywords
pt3 = "classify each words in the given text and list each words' meaning in at most 3 sentences: "+keywords

response2 = openai.Completion.create(
    model="text-davinci-003",
    prompt=pt2,
    temperature=0,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0.5,
    presence_penalty=0
)
response3 = openai.Completion.create(
    model="text-davinci-003",
    prompt=pt3,
    temperature=0,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0.5,
    presence_penalty=0
)

classes = response2["choices"][0]["text"]
meaning = response3["choices"][0]["text"]

print(meaning)

