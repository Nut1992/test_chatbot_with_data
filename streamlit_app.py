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


##EX4
#import streamlit as st
##จำเป็นต้องทำการ pip install google.generativeai หรือลง google-generativeai ในrequirement.txt
#import google.generativeai as genai 

#st.title("🤖🤖🤖Test Chatbot")

#st.subheader("Conversation")
## Capture Gemini API Key
#gemini_api_key = st.text_input("Gemini API Key: ", placeholder="Type your API Key here...", type="password")
## Initialize the Gemini Model
#if gemini_api_key: 
#    try:
## Configure Gemini with the provided API Key
#        genai.configure(api_key=gemini_api_key)
#        model = genai.GenerativeModel("gemini-pro")
#        st.success("Gemini API Key successfully configured.")
#    except Exception as e:
#        st.error(f"An error occurred while setting up the Gemini model: {e}")
## Initialize session state for storing chat history
#if "chat_history" not in st.session_state:
#    st.session_state.chat_history = [] # Initialize with an empty list
## Display previous chat history using st.chat_message (if available)
#for role, message in st.session_state.chat_history:
#    st.chat_message(role).markdown(message)
## Capture user input and generate bot response
#if user_input := st.chat_input("Type your message here..."):
## Store and display user message
#    st.session_state.chat_history.append(("user", user_input))
#    st.chat_message("user").markdown(user_input)
## Use Gemini AI to generate a bot response
#    if model:
#        try:
#            response = model.generate_content(user_input)
#            bot_response = response.text
#    # Store and display the bot response
#            st.session_state.chat_history.append(("assistant", bot_response))
#            st.chat_message("assistant").markdown(bot_response)
#        except Exception as e:
#            st.error(f"An error occurred while generating the response: {e}")


##EX5
import streamlit as st
import pandas as pd
import google.generativeai as genai

# Set up the Streamlit app layout
st.title("🐧 My Chatbot and Data Analysis App")
st.subheader("Conversation and Data Analysis")

# Capture Gemini API Key
gemini_api_key = st.text_input("Gemini API Key: ", placeholder="Type your API Key here...", type="password")

# Initialize the Gemini Model
model = None
if gemini_api_key:
    try:
    # Configure Gemini with the provided API Key
        genai.configure(api_key=gemini_api_key)
        model = genai.GenerativeModel("gemini-pro")
        st.success("Gemini API Key successfully configured.")
    except Exception as e:
        st.error(f"An error occurred while setting up the Gemini model: {e}")

# Initialize session state for storing chat history and data
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [] # Initialize with an empty list
if "uploaded_data" not in st.session_state:
    st.session_state.uploaded_data = None # Placeholder for uploaded CSV data

# Display previous chat history using st.chat_message (if available)
for role, message in st.session_state.chat_history:
    st.chat_message(role).markdown(message)

# Add a file uploader for CSV data
st.subheader("Upload CSV for Analysis")
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
if uploaded_file is not None:
    try:
    # Load the uploaded CSV file
        st.session_state.uploaded_data = pd.read_csv(uploaded_file)
        st.success("File successfully uploaded and read.")
    # Display the content of the CSV
        st.write("### Uploaded Data Preview")
        st.dataframe(st.session_state.uploaded_data.head())
    except Exception as e:
        st.error(f"An error occurred while reading the file: {e}")
# Checkbox for indicating data analysis need
analyze_data_checkbox = st.checkbox("Analyze CSV Data with AI")

# Capture user input and generate bot response
if user_input := st.chat_input("Type your message here..."):
    # Store and display user message
    st.session_state.chat_history.append(("user", user_input))
    st.chat_message("user").markdown(user_input)

    # Determine if user input is a request for data analysis and the checkbox is selected
    if model:
        try:
            if st.session_state.uploaded_data is not None and analyze_data_checkbox:
            # Check if user requested data analysis or insights
                if "analyze" in user_input.lower() or "insight" in user_input.lower():
                    # Create a description of the data for the AI model
                    data_description = st.session_state.uploaded_data.describe().to_string()
                    prompt = f"Analyze the following dataset and provide insights {user_input} and return result only natural language. Don't send code and uses data from outside csv file :\n\n{data_description}" #เพิ่ม discrition เพื่อจูนคำตอบให้แม่นขึ้น
                    
                    # Generate AI response for the data analysis
                    response = model.generate_content(prompt)
                    bot_response = response.text
                    # Store and display the AI-generated analysis
                    st.session_state.chat_history.append(("assistant", bot_response))
                    st.chat_message("assistant").markdown(bot_response)
                else:
                    # Normal conversation with the bot
                    response = model.generate_content(user_input)
                    bot_response = response.text
                    # Store and display the bot response
                    st.session_state.chat_history.append(("assistant", bot_response))
                    st.chat_message("assistant").markdown(bot_response)
            elif not analyze_data_checkbox:
                # Respond that analysis is not enabled if the checkbox is not selected
                bot_response = "Data analysis is disabled. Please select the 'Analyze CSV Data with AI' checkbox to enable analysis."
                st.session_state.chat_history.append(("assistant", bot_response))
                st.chat_message("assistant").markdown(bot_response)
            else:
                # Respond with a message to upload a CSV file if not yet done
                bot_response = "Please upload a CSV file first, then ask me to analyze it."
                st.session_state.chat_history.append(("assistant", bot_response))
                st.chat_message("assistant").markdown(bot_response)
        except Exception as e:
            st.error(f"An error occurred while generating the response: {e}")
    else:
        st.warning("Please configure the Gemini API Key to enable chat responses.")