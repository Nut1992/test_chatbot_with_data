#import streamlit as st

#st.title("🤖🤖🤖Test Chatbot")

##ex1
## Display the user input
#if user_input := st.text_input("You: ", placeholder="Type your message here..."): 
#    st.write(f"User Input: {user_input}")


#ex2
## Keep the conversation
#if "chat_history" not in st.session_state:
#    st.session_state.chat_history = []

## Display the user input
#if user_input := st.text_input("You: ", placeholder="Type your message here..."):
#    st.session_state.chat_history.append(user_input)

## Display all messages using st.write
#for message in st.session_state.chat_history:
#    st.write(message)


#ex3
## Keep the conversation
#if "chat_history" not in st.session_state: #เช็คตัวแปร
#    st.session_state.chat_history = []

## Display all messages using
#for message in st.session_state.chat_history:
#    with st.chat_message("AI"):
#        st.markdown(message)

## Display the user input
#if prompt := st.chat_input("Type your message here ..."):
#    st.session_state.chat_history.append(prompt)
#    st.chat_message("user").markdown(prompt)



import streamlit as st
import google.generativeai as genai

st.title("🤖🤖🤖Test Chatbot")

st.subheader("Conversation")
# Capture Gemini API Key
gemini_api_key = st.text_input("Gemini API Key: ", placeholder="Type your API Key here...", type="password")
# Initialize the Gemini Model
if gemini_api_key: 
    try:
# Configure Gemini with the provided API Key
        genai.configure(api_key=gemini_api_key)
        model = genai.GenerativeModel("gemini-pro")
        st.success("Gemini API Key successfully configured.")
    except Exception as e:
        st.error(f"An error occurred while setting up the Gemini model: {e}")
# Initialize session state for storing chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [] # Initialize with an empty list
# Display previous chat history using st.chat_message (if available)
for role, message in st.session_state.chat_history:
    st.chat_message(role).markdown(message)
# Capture user input and generate bot response
if user_input := st.chat_input("Type your message here..."):
# Store and display user message
    st.session_state.chat_history.append(("user", user_input))
    st.chat_message("user").markdown(user_input)
# Use Gemini AI to generate a bot response
    if model:
        try:
            response = model.generate_content(user_input)
            bot_response = response.text
    # Store and display the bot response
            st.session_state.chat_history.append(("assistant", bot_response))
            st.chat_message("assistant").markdown(bot_response)
        except Exception as e:
            st.error(f"An error occurred while generating the response: {e}")