import streamlit as st
import requests
import uuid

st.title("Echo Bot")


if "thread_id" not in st.session_state:
    st.session_state.thread_id = "default"

with st.sidebar:
    st.subheader("Conversations")

    threads = requests.get("http://localhost:4001/chat/threads").json()

    for thread in threads:
        if st.button(thread):
            st.session_state.thread_id = thread
            st.session_state.messages = []  


if "messages" not in st.session_state:
    try:
        message_history = requests.get(
            f"http://localhost:4001/chat/history/{st.session_state.thread_id}"
        ).json()
    except:
        message_history = []
    st.session_state.messages = message_history

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("Type your message"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = requests.post(
        f"http://localhost:4001/chat/{st.session_state.thread_id}",
        params={"message": prompt}
    ).json()["messages"][-1]["content"]

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
