import streamlit as st
from graph import graph

st.set_page_config(page_title="Debales AI Assistant", layout="centered")

st.title("🤖 Debales AI Assistant")
st.caption("RAG + SERP + LangGraph Powered")

if "chat" not in st.session_state:
    st.session_state.chat = []

query = st.text_input("Ask something...")

if st.button("Send") and query:
    result = graph.invoke({"question": query})
    answer = result["answer"]

    st.session_state.chat.append(("You", query))
    st.session_state.chat.append(("Bot", answer))

for role, msg in st.session_state.chat:
    if role == "You":
        st.markdown(f"**🧑 {msg}**")
    else:
        st.markdown(f"**🤖 {msg}**")
