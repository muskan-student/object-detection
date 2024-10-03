import streamlit as st
from streamlit_option_menu import option_menu
import base64

st.set_page_config(
    page_title ="object Detection",
    layout = 'wide'
)


# Title with gradient background and shadow effect
st.markdown(
    """
    <style>
    .title {
        font-size: 50px;
        font-weight: bold;
        text-align: center;
        color: white;
        padding: 20px;
        background: linear-gradient(to right, #6A1B9A, #8E24AA, #C2185B);
        border-radius: 10px;
        text-shadow: 2px 2px 4px #000000;
    }
    </style>
    <div class="title">Object Detection through YOLOv</div>
    """,
    unsafe_allow_html=True
)


#ui integration
with st.spinner ('loading dataset...'):
    st.success('Done !')
    st.snow()
    
st.markdown(
    """
    <style>
    .stApp {
        background: #C8A1E0;
    }
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
        font-family: 'Arial', sans-serif;
        padding: 10px;
}
    .sidebar .nav-link {
        font-size: 18px;
        color: #333;
}

    
    .main-header {
        font-family: 'Helvetica', sans-serif;
        font-size: 36px;
        color: #003399; /* Darker blue */
        text-align: center;
        margin-bottom: 20px;
    }

    
    .instruction-dropdown {
        background-color: #e6e6e6;
        border-radius: 8px;
        color: #333333;
        font-size: 16px;
    }
    .styled-button {
        background-color: #28a745;
        color: white;
        padding: 10px 20px;
        border-radius: 10px;
        border: none;
        font-size: 18px;
        cursor: pointer;
    
    </style>
    """,
    unsafe_allow_html=True
)

#from streamlit_option_menu import option_menu

# Sidebar with Icons for Navigation
with st.sidebar:
    selected = option_menu(
        "Navigation", 
        ["Home", "Videos", "Webcam"], 
        icons=["house", "camera-video", "camera"],
        menu_icon="cast", default_index=0,
    )


# App Title
st.markdown("<h1 class='main-header'>Object Detection Dashboard</h1>", unsafe_allow_html=True)


    # Instruction Dropdown Styling
st.selectbox("Instruction", ["Step 1: Upload Video or allow webcam", "Step 2: click submit","Step 3:Start detecting the object","Step 4: View result"], key="instruction", 
             help="Choose a step to get started", format_func=lambda x: f"🔍 {x}")

st.markdown(
    """
    <style>
    div.stButton > button {
        background-color: #4CAF50;
        color: white;
        border-radius: 12px;
        font-size: 20px;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        text-align: center;
        padding: 10px;
        font-size: 14px;
    }
    </style>
    <div class="footer">
        Created by <a href="https://github.com/muskan-student/object-detection.git" target="_blank">Muskan Bajpai</a>
    </div>
    """, unsafe_allow_html=True)


if st.button('Styled Button'):
    st.write('Button clicked!')
    

# Adding a video example to demonstrate the functionality
st.markdown("### Example of Object Detection in Action:")

# Display video example (you can use a local file or an online link)
video_file = open(r'c:\Users\PC\OneDrive\Desktop\objectvideo.mp4', 'rb')  # Local video file
video_byte = (video_file).read()  # For local video

# Display video in a frame
# Encode the video as base64
video_base64 = base64.b64encode(video_byte).decode('utf-8')

# Display video in a fixed frame
st.markdown(
    f"""
    <style>
    .video-frame {{
        width: 640px;
        height: 360px;
        overflow: hidden;
        border: 3px solid #ccc;
        margin: 0 auto;
    }}
    video {{
        width: 100%;
        height: 100%;
        object-fit: cover;
    }}
    </style>
    <div class="video-frame">
        <video controls>
            <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
    </div>
    """,
    unsafe_allow_html=True
)