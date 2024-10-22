import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate,SystemMessagePromptTemplate,HumanMessagePromptTemplate,PromptTemplate


templates = """
 Your name is Atom. You are a master chef so first Introduce yourself as Atom The Master Chef. Youcan write any type of food recipe which can be cooked in 5 minutes. You are only allowed to answer food related queries.If You don't know the answer tellI don't know the answer.
"""

def get_recipe(ingredients_input):
    prompt_template = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(templates),
    HumanMessagePromptTemplate.from_template("{asked_recipe}")])

    formatting_template = prompt_template.format_messages(asked_recipe = ingredients_input)

    chat = ChatOllama(temperature=0.8,model="llama3.1")
    response = chat.invoke(formatting_template)
    return response.content



# Streamlit Front end 
st.title("Welcome to Atom Recipe Tool 😋")
st.write("Enter your ingredients to get recipe suggestions.")
ingredients_input = st.text_input("Ingredients (comma separated):")

if st.button("Get Recipe"):
    if ingredients_input:
        input_recipe = get_recipe(ingredients_input)

        st.balloons()
        st.write("### Suggested Recipe:")
        st.write(input_recipe)
    else:
        st.write("Please enter some ingredients.")






# print(f"Response: {response.content}")