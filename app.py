import streamlit as st
import requests
from PIL import Image

# Main Streamlit app
def main():
    st.title("Vision and Language Transformer (ViLT)")
    uploaded_image = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])
    
    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        query = st.text_input("Enter your question", "")
        if st.button("Enter📤"):
            with st.spinner('Predicting...'):
                # Prepare data
                files = {"image": uploaded_image.getvalue()}
                data = {"query": query}
                # Send request to server
                response = requests.post("http://127.0.0.1:8000/predict", files=files, data=data)
                if response.status_code == 200:
                    result = response.json()["result"]
                    st.success(f"Predicted Answer: {result}")
                else:
                    st.error("Failed to get prediction. Please try again.")

if __name__ == "__main__":
    main()
