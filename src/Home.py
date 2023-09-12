import streamlit as st


#Config
st.set_page_config(layout="wide", page_icon="💬", page_title="AI | Chat-Bot 🤖")


#Contact
with st.sidebar.expander("📬 Contact"):

    st.write("**GitHub:**",
"[AI-chatbot](https://github.com/ScriptScallywag/Py-AI_ChatBot)")
    st.write("**Created by ScriptScallyweg**")


#Title
st.markdown(
    """
    <h2 style='text-align: center;'>AI, your data-aware assistant 🤖</h1>
    """,
    unsafe_allow_html=True,)

st.markdown("---")


#Description
st.markdown(
    """ 
    <h5 style='text-align:center;'>I'm AI, an intelligent chatbot created by combining 
    the strengths of Langchain and Streamlit. I use large language models to provide
    context-sensitive interactions. My goal is to help you better understand your data.
    I support PDF, TXT, CSV, Youtube transcript 🧠</h5>
    """,
    unsafe_allow_html=True)
st.markdown("---")