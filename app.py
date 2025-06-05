import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
from streamlit_drawable_canvas import st_canvas

st.set_page_config(page_title="Digit Recognizer", layout="centered")

st.title("✍️ Handwritten Digit Recognizer")
st.write("Draw a digit (0–9) and click the button to predict.")

# Load model
model = tf.keras.models.load_model('digit_model.keras')

# Layout: Canvas on the left, output on the right
col1, col2 = st.columns([1, 1])

with col1:
    canvas_result = st_canvas(
        fill_color="#000000",
        stroke_width=10,
        stroke_color="#FFFFFF",
        background_color="#000000",
        width=280,
        height=280,
        drawing_mode="freedraw",
        key="canvas"
    )

# Button appears below both columns
predict_clicked = st.button("Predict Digit")

with col2:
    if predict_clicked and canvas_result.image_data is not None:
        # Process the image
        image = Image.fromarray((canvas_result.image_data[:, :, 0]).astype(np.uint8))
        image = image.resize((28, 28)).convert("L")

        img_array = np.array(image) / 255.0
        img_array = img_array.reshape(1, 28, 28)

        prediction = model.predict(img_array)
        predicted_digit = np.argmax(prediction)
        confidence = np.max(prediction) * 100

        st.image(image, caption="Processed Image", width=150)
        st.subheader(f"Predicted Digit: {predicted_digit}")
        st.write(f"Confidence: {confidence:.2f}%")

        if confidence < 70:
            st.info("⚠️ Low confidence — try drawing more clearly.")
