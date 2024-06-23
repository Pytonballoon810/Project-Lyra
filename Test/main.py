from os import getenv, path
from dotenv import load_dotenv
# from gpt4all import GPT4All

from openai import OpenAI

load_dotenv()

# OpenAI Test
# client = OpenAI(api_key=getenv('OPENAI_API_KEY'))
# completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "What is human life expectancy in the United States?"},
#     ]
# )

# print(completion.choices[0].message)


# GPT4ALL Test
# MODEL = GPT4All(model_name='mistral-7b-instruct-v0.1.Q4_0',
#                 model_path=getenv('MODEL_PATH'),
#                 device=getenv('DEVICE'))

# BASEPATH = path.dirname(__file__)
# system_prompt_path = path.abspath(path.join(BASEPATH, 'system-prompt.md'))

# with open(system_prompt_path, 'r', encoding="utf-8") as file:
#     FIRST_INPUT = file.read()
# with MODEL.chat_session(system_prompt="") as lyra:
#     response = lyra.generate(FIRST_INPUT)
#     print(response)
#     while True:
#         response = print(lyra.generate(input("Enter your response: ")))
        