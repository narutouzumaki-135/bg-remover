import streamlit as st
from rembg import remove
from PIL import Image
import io

st.title("🔍 Remove Background from Images")
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_column_width=True)

    with st.spinner("Removing background..."):
        result = remove(image)
        st.image(result, caption="Image without Background", use_column_width=True)

        # Option to download
        buf = io.BytesIO()
        result.save(buf, format="PNG")
        byte_im = buf.getvalue()

        st.download_button(label="📥 Download Image",
                           data=byte_im,
                           file_name="no_bg.png",
                           mime="image/png")
