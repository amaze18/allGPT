from pygpt4all.models.gpt4all_j import GPT4All_J

model = "/home/user/privateGPT/models/ggml-gpt4all-j-v1.3-groovy.bin"

def new_text_callback(text):
    print(text, end="")

model = GPT4All_J(model)

ans=model.generate("What is the captial of Pakistan")
print(ans)

from gpt4all import GPT4All

path = "/home/user/privateGPT/models/ggml-gpt4all-l13b-snoozy.bin"

model = GPT4All(path)

messages = [{"role": "user", "content": "What is the national flower of Canada"}]
model.chat_completion(messages)