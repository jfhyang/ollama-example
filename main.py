import ollama

r = ollama.generate(model='llama3.1:8b-instruct-q8_0', prompt='3.9和3.11哪个大？')
print(r["response"])