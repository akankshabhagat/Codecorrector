import streamlit as st
import google.generativeai as genai
import os

st.title("Code helper 🤖</>")

gemini_api_key = os.getenv("gemini_api_key")
if gemini_api_key:
    genai.configure(api_key=gemini_api_key)
else:
    st.error("API key not found. Please check your environment variables.")


if "messages" not in st.session_state:
    st.session_state.messages = []


with st.container():
    user_prompt = st.text_input("Enter your query", placeholder="Python code says hello world")
    
   
    if st.button("Search"):
        if user_prompt.strip():
            
            st.session_state.messages.append({"role": "user", "content": user_prompt})
            try:
                with st.spinner("Generating response..."):
                    
                    model = genai.GenerativeModel("gemini-1.5-flash")

                   
                    response = model.generate_content(f"what is: {user_prompt}")

                    
                    if response and hasattr(response, 'text'):
                        assistant_response = response.text
                        st.session_state.messages.append({"role": "assistant", "content": assistant_response})
                    else:
                        st.error("No response from the model.")

            except Exception as e:
                st.error(f"Error generating response: {e}")
        else:
            st.warning("Please enter a code snippet before searching.")

if st.button("Clear Chat"):
                st.session_state.messages = []
                
for message in reversed(st.session_state.messages):
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
