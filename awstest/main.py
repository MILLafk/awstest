# import openai
# from flask import Flask, render_template, request

# # Set your OpenAI API key here
# api_key = "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"

# # Initialize the OpenAI API client
# openai.api_key = api_key

# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def home():
#     response_text = ""

#     if request.method == 'POST':
#         user_prompt = request.form['user_prompt']

#         # Make an API request to generate text
#         response = openai.Completion.create(
#             engine="text-davinci-003",
#             prompt=user_prompt,
#             max_tokens=500,
#             temperature=0.1,
#             n=2,
#             stop=None
#         )

#         # Extract the response text
#         response_text = response.choices[0].text.strip()

#     return render_template('index.html', response_text=response_text)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)

# Function to calculate the product of numbers in a list
def calculate_product(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

# Get user input for numbers separated by commas
user_input = input("Enter numbers separated by commas: ")

# Split the input string into a list of numbers
try:
    numbers = [float(num) for num in user_input.split(',')]
    
    # Check if the list is empty
    if len(numbers) == 0:
        print("No numbers entered.")
    else:
        # Calculate the product of the numbers
        result = calculate_product(numbers)
        print(f"The product of the numbers is: {result}")
except ValueError:
    print("Invalid input. Please enter numbers separated by commas.")