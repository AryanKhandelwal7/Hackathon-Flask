import openai

openai.api_key = "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"

messages = []
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready!")
while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")