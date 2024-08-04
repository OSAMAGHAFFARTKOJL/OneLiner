import streamlit as st
from PIL import Image
import base64
from io import BytesIO


# Function to convert image to base64
def image_to_base64(image_path):
    with Image.open(image_path) as img:
        buffer = BytesIO()
        img.save(buffer, format="JPEG")
        img_str = base64.b64encode(buffer.getvalue()).decode()
    return img_str



# Function to simulate running a new Streamlit script
def run_new_script():
    # Clear previous session state and set a flag to indicate the new script should run
    st.session_state["second_page"] = True
    st.rerun()

# Check if the button has been clicked and set the flag
if "second_page" not in st.session_state:
    st.session_state["second_page"] = False

# Main content
if st.session_state["second_page"]:
    exec(open("second_page.py").read())
else:



    # Set the page config
    st.set_page_config(page_title="OneLiner", layout="wide")

# Load custom CSS and font
    st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
    /* Add your custom CSS here */
    body {
        font-family: 'Roboto', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)
    # Load custom CSS from file
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Add custom header with HTML
    st.markdown("""
        <div class="custom-header">
            <div class="titles">ᯓ★OneLiner</div>
            <div class="right-title">VINTIQ</div>
        </div>
    """, unsafe_allow_html=True)

    # Add main content with padding to avoid overlap
    st.markdown('<div class="main-content">', unsafe_allow_html=True)

    # Load and display the first image with base64
    img_str_home = image_to_base64("Home.jpg")
    st.markdown(
        f'<div class="image-container"><img src="data:image/jpeg;base64,{img_str_home}" class="custom-image" alt="Home Image"></div>',
        unsafe_allow_html=True,
    )

    st.write(" ")
    st.write(" ")
    st.write(" ")
    # Display title and subtitle with custom styling
    st.markdown('<p class="title">How can OneLiner Help</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">OneLiner is perfect for learning quickly and efficiently making it suitable for all learners!</p>', unsafe_allow_html=True)

    st.write(" ")
    st.write(" ")
    st.write(" ")
    # Add a "Try it now" button with custom styling
    # st.markdown('<button class="button">Try it now</button>', unsafe_allow_html=True)
    # Button to run the Streamlit file
    if st.button("Try it now"):
        # Replace 'your_streamlit_file.py' with the actual file path
        run_new_script() 
    st.write(" ")
    st.write(" ")
    st.write(" ")
    # Load and display the second image with base64
    img_str_math = image_to_base64("math.jpg")

    # Create a container for the image and text
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write('')
    with col2:
        st.markdown(f'<img src="data:image/jpeg;base64,{img_str_math}" width="300" alt="Math Image">', unsafe_allow_html=True)

    # Display the "Personalized Learning" section in the first column
    with col1:
        st.markdown('<p class="section-header">Unlock your potential with OneLiner</p>', unsafe_allow_html=True)
        st.markdown('<p class="section-description">Master Coding and Math:</p>', unsafe_allow_html=True)
        st.markdown('<p class="section-description">Smart Hint: Get step-by-step hints for coding and math problems to enhance your problem-solving.</p>', unsafe_allow_html=True)

    # Load and display the third image with base64
    img_str_coding = image_to_base64("coding.jpg")

    # Create a container for the image and text
    col1, col2 = st.columns([1.5, 2])
    with col2:
        st.write('')
    with col1:
        st.markdown(f'<img src="data:image/jpeg;base64,{img_str_coding}" width="300" alt="Coding Image">', unsafe_allow_html=True)

    # Display the "Personalized Learning" section in the second column
    with col2:
        st.markdown('<p class="section-header">Personalized Learning:</p>', unsafe_allow_html=True)
        st.markdown('<p class="section-description">Adaptive Assistance:</p>', unsafe_allow_html=True)
        st.markdown('<p class="section-description">Hints are tailored to your progress, becoming more challenging as you solve.</p>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
