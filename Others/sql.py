from dotenv import load_dotenv
load_dotenv() ## load all the environemnt variables

import streamlit as st
import os
from mysql.connector import connect
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX, _mysql_prompt

import google.generativeai as genai
## Configure Genai Key

genai.configure(api_key="AIzaSyAHZMHwa61Rrqx7hOWpEFyDBDJGVEP-spo")

## Function To Load Google Gemini Model and provide queries as response

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

## Fucntion To retrieve query from the database

def read_sql_query(sql):
    cnx = connect(user='manoj', password='571422',
                  host='localhost',
                  database='classicmodels')
    cur=cnx.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    cnx.commit()
    cnx.close()
    for row in rows:
        print(row)
    return rows

## Define Your Prompt
prompt=_mysql_prompt

## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response)
    st.subheader("The Response is")
    for row in response:
        print(row)
        st.header(row)









