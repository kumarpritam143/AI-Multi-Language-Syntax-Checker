import streamlit as st
from openai import OpenAI

# Load secrets
NVIDIA_API_KEY = st.secrets["NVIDIA_API_KEY"]
BASE_URL = st.secrets["BASE_URL"]
MODEL_NAME = st.secrets["MODEL_NAME"]

client = OpenAI(
    base_url=BASE_URL,
    api_key=NVIDIA_API_KEY
)

st.title("AI Multi Language Syntax Checker")

language = st.selectbox(
    "Select Programming Language",
    ["Python", "C", "C++", "Java", "JavaScript"]
)

code = st.text_area("Enter your code here", height=300)

if st.button("Check Syntax"):

    prompt = f"""
Check syntax errors in the following {language} code.
Return errors with corrected code.

Code:
{code}
"""

    completion = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are a programming syntax analyzer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.1,
        max_tokens=1000
    )

    result = completion.choices[0].message.content

    st.subheader("Analysis Result")
    st.write(result)
