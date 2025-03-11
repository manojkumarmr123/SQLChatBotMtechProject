import streamlit as st
from langchain_helper import get_few_shot_db_chain
from PIL import Image

st.title("Analytica Chatbot: DB Insights")

# Initialize chat history
if "messages" not in st.session_state:
    # print("Creating session state")
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Fire any question?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.spinner("Generating response..."):
        with st.chat_message("assistant"):
            chain = get_few_shot_db_chain()
            response = chain.run(prompt)
            st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

# Define the path to your image file
IMAGE_PATH = 'DB Schema Diagram.png'

# Initialize session state if not already present
if 'show_image' not in st.session_state:
    st.session_state.show_image = False

# Function to toggle image visibility
def toggle_image():
    st.session_state.show_image = not st.session_state.show_image

# Create a Streamlit button to toggle the image
st.button('DB ER Diagram', on_click=toggle_image)

# Display the image based on session state
if st.session_state.show_image:
    image = Image.open(IMAGE_PATH)
    st.image(image, caption='DB ER Diagram')

