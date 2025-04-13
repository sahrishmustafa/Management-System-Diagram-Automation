import streamlit as st
import requests
import time

# Configuration
BACKEND_URL = "http://localhost:8000"  # Update if hosted elsewhere

st.title("UML Diagram Generator")
st.markdown("Describe your system in natural language to generate a PlantUML diagram")

# Chat-like interface
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Describe your system..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("Generating diagram..."):
            try:
                response = requests.post(
                    f"{BACKEND_URL}/generate-uml",
                    json={"system_description": prompt}
                )
                response.raise_for_status()
                result = response.json()
                
                st.markdown("**PlantUML Code:**")
                st.code(result["plantuml_code"], language="plantuml")
                
                st.markdown("**Diagram Preview:**")
                st.image(result["diagram_url"])
                
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": f"Diagram generated! [View full size]({result['diagram_url']})"
                })
            except Exception as e:
                st.error(f"Error generating diagram: {str(e)}")