# Import the Streamlit library to build interactive web apps in Python
import streamlit as st 

import  mychatbot_backend as demo

# Set Title for Chatbot
st.title("Hi, This is Chatbot PavanUppuluri :sunglasses:") # **Modify this based on the title you want in want

# Check if the 'memory' object is not already stored in the Streamlit session state.
# If not, initialize it using the demo_memory() function (from the demo module),
# which creates a ConversationSummaryBufferMemory instance for maintaining chat context.

if 'memory' not in st.session_state: 
    st.session_state.memory = demo.demo_memory()

# Add the UI chat history to the session cache - Session State
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history: 
    with st.chat_message(message["role"]): 
        st.markdown(message["text"]) 

# Reneder a chatbot input box to nter the details
     
input_text = st.chat_input("Chat with Pavan's Bot here") 
if input_text: 
    
    with st.chat_message("user"): 
        st.markdown(input_text) 
    
    st.session_state.chat_history.append({"role":"user", "text":input_text}) 

    chat_response = demo.demo_conversation(input_text=input_text, memory=st.session_state.memory)
    
    with st.chat_message("assistant"): 
        st.markdown(chat_response) 
    
    st.session_state.chat_history.append({"role":"assistant", "text":chat_response}) 