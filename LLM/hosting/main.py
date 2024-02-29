from dotenv import load_dotenv
from gpt4all import GPT4All
from os import getenv, path

load_dotenv()
MODEL = GPT4All(model_name='mistral-7b-instruct-v0.1.Q4_0', model_path=getenv('MODEL_PATH'))
BASEPATH = path.dirname(__file__)
system_prompt_path = path.abspath(path.join(BASEPATH, '..', 'system-prompt.md'))
with open(system_prompt_path, 'r', encoding="utf-8") as file:
    FIRST_INPUT = file.read()
with MODEL.chat_session(system_prompt="", prompt_template="[INST] %1 [/INST]") as lyra:
    respone = lyra.generate(FIRST_INPUT)
    print(respone)
    print(lyra.generate(input("Enter your response: ")))