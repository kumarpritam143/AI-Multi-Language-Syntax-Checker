import streamlit as st
from openai import OpenAI
from config import NVIDIA_API_KEY, MODEL_NAME, BASE_URL

# NVIDIA OpenAI-compatible client
client = OpenAI(
    base_url=BASE_URL,
    api_key=NVIDIA_API_KEY
)

st.title("AI Multi-Language Syntax Checker")

language = st.selectbox(
    "Select Programming Language",
    ["Python", "C", "C++", "Java", "JavaScript", "Go", "Rust"]
)

code = st.text_area("Enter your code here", height=300)

if st.button("Check Syntax"):

    prompt = f"""
You are a strict syntax checking engine.

Analyze the following {language} code and return:

1. Syntax errors
2. Line numbers
3. Corrected version of the code

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

    result = completion.choices[0].message.content.strip()

    st.subheader("Analysis Result")
    st.write(result)