import streamlit as st

st.title("🤖🤖🤖Test Chatbot")

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
if "chat_history" not in st.session_state: #เช็คตัวแปร
    st.session_state.chat_history = []

## Display all messages using
for message in st.session_state.chat_history:
    with st.chat_message("AI"):
        st.markdown(message)

## Display the user input
if prompt := st.chat_input("Type your message here ..."):
    st.session_state.chat_history.append(prompt)
    st.chat_message("user").markdown(prompt)
