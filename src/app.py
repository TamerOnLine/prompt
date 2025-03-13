from langchain.prompts import ChatPromptTemplate

# Define a chat prompt template with English placeholder keys
chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are an intelligent assistant specializing in programming."),
    ("user", "How can I use {language} to create an API?"),
])

# Fill the template with a specific programming language
prompt_filled = chat_template.format(language="Python")

# Print the formatted prompt
print(prompt_filled)
