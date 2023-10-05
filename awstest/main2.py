api_key = "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"

import openai

# Set your OpenAI API key here
# api_key = "YOUR_API_KEY"

# Initialize the OpenAI API client
openai.api_key = api_key

def response1():
    # Define the prompt or message
    # prompt = "Translate the following English text to Maranao: 'Hello, how are you?'"

    # prompt = "what is machine learning all about?"
    prompt = "explain in not more than 500 words what is machine learning all about"
    # Make an API request to generate text
    response = openai.Completion.create(
        engine="text-davinci-003",
        # "text-davinci-002",  # Use the desired engine
        prompt=prompt,
        max_tokens=500,  # Adjust as needed
        temperature=0.1,  # Adjust as needed (higher values make output more random) originally = 0.7
        n=2,  # Number of responses to generate originally = 1
        stop=None  # You can specify a stopping condition if needed
    )

    # Extract and print the response
    print(response.choices[0].text.strip())
    print("\n=================================")
    print(response.choices[1].text.strip())


def response2():
    print("\n=================================")
    # Define the user's message or prompt
    user_prompt = "Translate the following English text to French: 'Hello, how are you?'"

    # Make an API request to ChatGPT
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=user_prompt,
        max_tokens=50,
    )

    # Extract the generated text from the response
    generated_text = response.choices[0].text.strip()
    # Check for errors
    if 'error' in response:
        error_message = response['error']['message']
        print(f"Error: {error_message}")
    else:
        # Process the generated text
        print("Generated Text:")
        print(generated_text)
        # Additional processing or usage as needed

response1()
# response2()