import os
import openai


openai.api_key="----------------------------"

def article(query):
  result = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write a New York Times article: {}".format(query),
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
  )
  print(result)
  if 'choices' in result:
    if (len(result['choices']) > 0):
      answer = result['choices'][0]['text']
      print(answer)



article("Cognitive Dissonance")
