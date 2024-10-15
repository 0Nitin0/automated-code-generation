import os
import re
import openai

# Set your OpenAI API key (make sure to keep this secure and private)
openai.api_key = 'Enter your apen ai key here'

def search_code_in_folder(folder_path, query):
    """
    Search for code snippets in files within the folder that match the query.
    """
    matched_snippets = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):  # Search only in Python files
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    # Check if the file contains code that matches the query (simple keyword matching for demo)
                    if re.search(query, content, re.IGNORECASE):
                        matched_snippets.append(content)
    return matched_snippets

def generate_code(query, matched_snippets):
    """
    Use OpenAI API to generate code based on the query and matched code snippets.
    """
    if matched_snippets:
        # Combine matched snippets and user query for context
        input_text = f"User's query: '{query}', and these code snippets:\n"
        input_text += "\n".join(matched_snippets[:3])  # Limit to first 3 snippets for context
    else:
        input_text = f"User's query: '{query}' - No relevant code snippets found."
    
    # Call OpenAI API to generate the code
    # Changed the engine to 'gpt-3.5-turbo' because 'text-davinci-003' is deprecated.
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates Python code."},
            {"role": "user", "content": input_text + "\nGenerate Python code based on the above query and snippets."},
        ],
        max_tokens=200,
        temperature=0.7,
    )
    
    # Return the generated code
    # Accessing the content from the response for gpt-3.5-turbo
    return response['choices'][0]['message']['content'].strip()

def main():
    # Ask the user what they want to do
    user_query = input("What do you want to do? ")
    
    # Folder containing the Python code files
    folder_path = 'D:/automated code generation/Python-master'  # Modify this to your folder path
    
    # Step 1: Search for code snippets in the folder based on the user query
    matched_snippets = search_code_in_folder(folder_path, user_query)
    
    # Step 2: Generate new code based on the found snippets and user query
    generated_code = generate_code(user_query, matched_snippets)
    
    # Output the generated code
    print("Generated Code:")
    print(generated_code)

if __name__ == "__main__":
    main()
