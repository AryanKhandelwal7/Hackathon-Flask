import openai

# Replace this with your OpenAI API key (make sure to keep it secure)
openai.api_key = "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"

def get_gpt_response(prompt, is_basic=False):
    # Adjust the system message depending on whether it's a basic front-end question or not
    system_message = "You are a helpful assistant who only answers front-end development questions and provides code snippets when necessary and answers to any questions related to Bitloops."
    if is_basic:
        system_message = "You are a helpful assistant. Please provide a basic explanation without going too much into detail unless requested."
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt},
        ],
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.7,
    )
    
    return response['choices'][0]['message']['content'].strip()

def is_frontend_question(prompt):
    # List of common front-end development topics/keywords
    frontend_keywords = ['html', 'css', 'javascript', 'react', 'vue', 'angular', 'frontend', 'web design', 'ui', 'ux', 
                         'bootstrap', 'tailwind', 'responsive design', 'dom', 'jquery', 'typescript', 'sass', 'scss']

    # Check if any of the keywords appear in the prompt
    return any(keyword in prompt.lower() for keyword in frontend_keywords)

def is_greeting(prompt):
    # Check if the user input is a greeting
    greetings = ['hello', 'hey', 'hi', 'greetings', 'hola']
    return any(greet in prompt.lower() for greet in greetings)

def is_bitloops_question(prompt):
    # Check if the question is related to Bitloops
    return 'bitloops' in prompt.lower()

if __name__ == "__main__":
    while True:
        prompt = input("User Prompt: ")
        if prompt.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break  # Exit the loop if the user types 'exit'

        # Handle greetings
        if is_greeting(prompt):
            print("GPT Response : Hey! How's it going?")
            continue  # Go back to the start of the loop

        # Handle Bitloops-related questions
        if is_bitloops_question(prompt):
            response = get_gpt_response(prompt)
            print("GPT Response:", response)
            continue

        # Handle front-end development questions (basic and non-basic)
        if is_frontend_question(prompt):
            # For basic front-end questions, provide simpler answers
            response = get_gpt_response(prompt, is_basic=True)
            print("GPT Response:", response)
        else:
            print("GPT Response : That’s an interesting question! However, I can only answer front-end development or Bitloops-related queries. Let me know if you have any!")

