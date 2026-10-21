import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="ClarityVision",
    page_icon="🔍",
    layout="wide"
)

st.title("ClarityVision")
st.subheader("AI-Powered Camouflaged Object Detection")

st.write(
    "Upload an image to begin analyzing "
    "objects that blend into their surroundings."
)

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.success("Image uploaded successfully!")

    st.image(
        image,
        caption="Original Image",
        use_container_width=True
    )

    st.info(
        "Camouflage detection will be added "
        "in the next development stage."
    )