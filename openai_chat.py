import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# load the environment variables
load_dotenv()

# define the summary template with a simple prompt
prompt_template = """take a step back and calculate How many letters does the word {text} have?
Here are some examples for 
1. "Vamsi Krishna D" it is 15 we need to include spaces
"Vamsi" it is 5 "krishna" is 7 D is 1 and 2 spaces so toal = 5+7+1+2 = 15
2. "Vamsi !" it is 7
Just say how many letters does the word have
"""



prompt = PromptTemplate(
    input_variables=["text"],
    template=prompt_template,
)
llm = ChatOpenAI(temperature=0, model="gpt-4o")

# create a chain and will run the prompt
chain = prompt | llm

# invole the chain
response = chain.invoke(input = {"text": "hello World!"})

print(response)

