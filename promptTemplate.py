from langchain_openai import OpenAI
from langchain import PromptTemplate

import os
from dotenv import load_dotenv
load_dotenv()


# 'text-davinci-003' model is depreciated now, so we are using the openai's recommended model https://platform.openai.com/docs/deprecations
llm = OpenAI(model_name="gpt-3.5-turbo-instruct")

our_prompt = """
I love trips, and I have been to 6 countries. 
I plan to visit few more soon.

Can you create a post for tweet in 10 words for the above?
"""

print(our_prompt)

#Last week langchain has recommended to use invoke function for the below please.
llm.invoke(our_prompt)
print(llm.invoke(our_prompt))

# Prompt Template

#As Langchain team has been working aggresively on improving the tool, we can see a lot of changes happening every weeek,
#As a part of it, the below import has been depreciated
#from langchain.llms import OpenAI

#First we'll need to import the below LangChain x OpenAI integration package and then import it please, if not installed already

#!pip install langchain-openai==0.1.0

from langchain_openai import OpenAI

from langchain import PromptTemplate

llm = OpenAI(api_key=my_OPENAI_API_KEY, model_name="gpt-3.5-turbo-instruct")

# Using F-String

# F-String is a Python feature that allows easy string formatting by placing variables inside curly braces within a string, making code more readable and efficient.
# __Code:__
# name = "Alice"
# age = 25
# message = f"My name is {name} and I am {age} years old."
# print(message)

# __Output:__
# My name is Alice and I am 25 years old.

wordsCount = 3

our_text = "I love trips, and I have been to 6 countries. I plan to visit few more soon."

our_prompt = f"""
{our_text}

Can you create a post for tweet in {wordsCount} words for the above?
"""

# print(our_prompt)

llm.invoke(our_prompt)

print(llm.invoke(our_prompt))

# Using Prompt Template - Prompt templates helps us in keeping our code neat and clean when we are building more complex.

template = """
{our_text}

Can you create a post for tweet in {wordsCount} words for the above?
"""

prompt = PromptTemplate(
    input_variables=["wordsCount","our_text"],
    template=template,
)

final_prompt = prompt.format(wordsCount='3',our_text="I love trips, and I have been to 6 countries. I plan to visit few more soon.")

print(final_prompt)

print(llm.invoke(final_prompt))