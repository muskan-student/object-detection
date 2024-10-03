import streamlit as st
from ultralytics import YOLO
import cv2
from PIL import Image

st.title("Object Detection")

st.write('Welcome!')
model = YOLO('yolov8n.pt')
object_names = list(model.names.values())

with st.form("my_form"):
    uploaded_file = st.camera_input("Web cam")
    selected_objects = st.multiselect('Choose objects to detect', object_names, default=object_names) 
    min_confidence = st.slider('Confidence score', 0.0, 1.0, .5, step=.1)
    st.form_submit_button(label='Submit')
        
if uploaded_file is not None: 
    input_path = uploaded_file.name
    file_binary = uploaded_file.read()
    with open(input_path, "wb") as temp_file:
        temp_file.write(file_binary)
    frame = cv2.imread(input_path)
    width = int(frame.shape[0]) 
    height = int(frame.shape[1]) 
    output_path = input_path.split('.')[0] + '_output.jpg' 
    with st.spinner('Processing Image...'): 
        result = model(input_path)
        # Visualize the results
        for i, r in enumerate(result):
            # Plot results image
            im_bgr = r.plot()  # BGR-order numpy array
            im_rgb = Image.fromarray(im_bgr[..., ::-1])  # RGB-order PIL image
            r.save(filename=f"results{i}.jpg")
            st.image(f"results{i}.jpg")