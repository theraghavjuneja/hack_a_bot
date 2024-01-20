import streamlit as st
import os 
from google.cloud import dialogflow_v2
st.header("Elly")
with st.expander("ℹ️ Disclaimer"):
    st.caption(
        "Elly is still under development and testing by team ELIXIR. It can make mistakes sometimes."
    )
# here i have got the credentials of my app
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\Charanjeet Juneja\OneDrive\Desktop\hack_a_bot\chatbot.json"

def send_message_to_dialogflow(project_id,session_id,message):
    session_client = dialogflow_v2.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow_v2.TextInput(text=message, language_code="en-US")
    query_input = dialogflow_v2.QueryInput(text=text_input)

    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )

    return response.query_result.fulfillment_text
project_id = "hackahon-chatbot-tx9j"
session_id = "my_id"
USER = "user"
ASSISTANT = "ai"
MESSAGES = "messages"

def initialize_session():
    if MESSAGES not in st.session_state:
        st.session_state[MESSAGES] = []

def display_messages():
    for msg in st.session_state[MESSAGES]:
        st.chat_message(msg["actor"]).write(msg["payload"])

def main():
    initialize_session()
    display_messages()

    prompt = st.chat_input("Enter a prompt here.")

    if prompt:
        user_message = {"actor": USER, "payload": prompt}
        st.session_state[MESSAGES].append(user_message)
        st.chat_message(USER).write(prompt)
        response_from_dialogflow=send_message_to_dialogflow(project_id,session_id,prompt);
        assistant_message = {"actor": ASSISTANT, "payload": response_from_dialogflow}
        st.session_state[MESSAGES].append(assistant_message)
        st.chat_message(ASSISTANT).write(response_from_dialogflow)

if __name__ == "__main__":
    main()
