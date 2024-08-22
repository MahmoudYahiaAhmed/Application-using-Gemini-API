import os 
import streamlit as st 
import google.generativeai as genai
from dotenv import load_dotenv 

# Load environment variables
load_dotenv() 
api = os.getenv("Google_api_key")

# Configure the Google Generative AI
if api:
    genai.configure(api_key=api)
else:
    st.error("Google API key not found or incorrect")

# Function to generate text using the Google API
def generate_text(text):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(text)
    return response.text

# Streamlit app title
st.title("Google API Text Generator with Chat UI")

# Initialize session state for messages if not already present
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display all stored messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input area for user's text
if user_input := st.chat_input("Please enter text"):
    # Display user's input as a chat message
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Append user's message to session state
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Generate response from the Google API
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        with st.spinner("Generating response..."):
            response_text = generate_text(user_input)
            message_placeholder.markdown(f"{response_text}")

    # Append assistant's message to session state
    st.session_state.messages.append({"role": "assistant", "content": response_text})
