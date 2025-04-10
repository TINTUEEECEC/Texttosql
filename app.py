from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(question,prompt):
    model=genai.GenerativeModel("models/gemini-1.5-pro")
    response = model.generate_content([prompt[0],question])
    return response.text

def read_sqlquery(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

prompt=[
    """
    you are an expert in converting English to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS,
    SECTION and MARKS\n\n For example, \nExample 1 - How much entries of record are present?,
    the SQL command will be like SELECT COUNT(*) FROM STUDENT;
    \n Example 2- Tell me all the students studying in Data Science class?,
    the SQL command will be SELECT * FROM STUDENT WHERE CLASS ="Data_science";
    also the sql code should not have ''' at the beginning or at the end and shouldnot have sql word in the output 
"""
]

st.set_page_config(page_title="I can Retrieve Any SQL Query", layout="wide")
st.header("Chat with SQL DB using Gemini")
    
user_question = st.text_input("Input: ", key="input")

submit=st.button("Ask the question")

if submit:
    response=get_gemini_response(user_question,prompt)
    print(response)
    data=read_sqlquery(response,"student.db")
    st.subheader("The Response is")
    print("The retrieved data is ",data)
    for row in data:
        # print(row)
        st.header(row)
