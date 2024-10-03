# import streamlit as st
# from ultralytics import YOLO
# import cv2

# st.title("Object Detection and Counting")

# st.write('Welcome!')
# model = YOLO('yolov8n.pt')
# object_names = list(model.names.values())

# with st.form("my_form"):
#     uploaded_file = st.file_uploader("Upload video", type=['mp4'])
#     selected_objects = st.multiselect('Choose objects to detect', object_names, default=['person']) 
#     min_confidence = st.slider('Confidence score', 0.0, 1.0)
#     st.form_submit_button(label='Submit')
        
# if uploaded_file is not None: 
#     input_path = uploaded_file.name
#     file_binary = uploaded_file.read()
#     with open(input_path, "wb") as temp_file:
#         temp_file.write(file_binary)
#     video_stream = cv2.VideoCapture('video.mp4')
#     width = int(video_stream.get(cv2.CAP_PROP_FRAME_WIDTH)) 
#     height = int(video_stream.get(cv2.CAP_PROP_FRAME_HEIGHT)) 
#     fourcc = cv2.VideoWriter_fourcc(*'h264') 
#     fps = int(video_stream.get(cv2.CAP_PROP_FPS)) 
#     output_path = input_path.split('.')[0] + '_output.mp4' 

#     with st.spinner('Processing video...'): 
#         while True:
#             ret, frame = video_stream.read()
#             if not ret:
#                 break
#             results = model(source, stream=True)
#         video_stream.release()
#     st.video(output_path)

import streamlit as st
import cv2
from ultralytics import YOLO
import tempfile
import shutil
import os

# Load a pretrained YOLOv8n model
model = YOLO("yolov8n.pt")

st.title("YOLO Object Detection in Video")

# Upload video file
uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "mov"])

if uploaded_file is not None:
    # Create a temporary file to save the uploaded video
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
        temp_file.write(uploaded_file.read())
        temp_file_path = temp_file.name

    # Create a VideoCapture object from the temporary video file
    cap = cv2.VideoCapture(temp_file_path)

    stframe = st.empty()  # Placeholder for the video frame

    # Process video stream
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Perform detection
        results = model(frame, stream=True)

        for result in results:
            # Draw bounding boxes on the frame
            annotated_frame = result.plot()
            # Convert the frame to RGB format for Streamlit
            rgb_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)

            # Display the frame
            stframe.image(rgb_frame, channels="RGB", use_column_width=True)

    cap.release()
    
    # Remove the temporary file
    os.remove(temp_file_path)
