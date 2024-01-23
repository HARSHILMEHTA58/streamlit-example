import streamlit as st
from PIL import Image
import numpy as np

def main1():
    # Take a picture using st.camera_input
            
    picture = st.camera_input("Take a picture")

    # Check if a picture was captured
    if picture is not None:
        # Convert the picture to a PIL Image
        pil_image = Image.open(picture)

        # Convert the PIL Image to a NumPy array
        numpy_image = np.array(pil_image)

        # Convert the NumPy array to an OpenCV image (BGR format)
        
        # Now 'opencv_image' is an OpenCV image that you can further process or display
        # For example, you can display the OpenCV image using st.image
        st.image(numpy_image, caption='Captured Image', channels='BGR')
        st.write("HEllo")
    else:
        st.write("NOT hello")
        st.warning("No picture captured.")

if __name__ == "__main__":
    st.title("Webcam Capture App")

    # Create a button to trigger image capture and display
    if st.button("Capture and Display"):
        main1()
