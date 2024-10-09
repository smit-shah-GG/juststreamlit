import streamlit as st
import requests
import json

def main():
    st.title("Chatbot")

    # Input field for user messages
    user_input = st.text_input("Enter your message:")

    # Button to send the message
    if st.button("Send"):
        url = "https://aftertest-ccraggit.onrender.com/invoke_rag"

        payload = json.dumps({
        "question": user_input,
        "coursename": "maceco"
        })
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        answer = response.json()["answer"]
        context = response.json()["context"]

        # Display response with fixed width and context
        st.markdown(f"<div style='width: 500px;'>{answer}</div>", unsafe_allow_html=True)
        st.subheader("Context:")
        for item in context:
            st.markdown(f"- **{item['metadata']['title']}**: {item['context']}")

if __name__ == "__main__":
    main()