# ✍️ Handwritten Digit Recognizer Using AI

This is a simple and interactive web app that allows users to draw digits (0–9) on a canvas and predicts the digit using a trained neural network model. The app is built using **Streamlit** and **TensorFlow**.

---

## 🚀 Features

- Draw digits with your mouse or touch input.
- Predicts the digit using a deep learning model.
- Clean, responsive UI with canvas and output side-by-side.
- Confidence score for predictions.

---

## 🧠 Model

The model is a convolutional neural network (CNN) trained on the **MNIST** dataset. It is saved in the file `digit_model.keras` and expects grayscale 28x28 pixel images.

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/digit-recognizer.git
cd digit-recognizer
```

### 2. Create a Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install streamlit tensorflow pillow streamlit-drawable-canvas numpy
```

---

## ▶️ How to Run the App

```bash
streamlit run app.py
```

Then open the link in your browser (usually http://localhost:8501).

---

## 📁 Project Structure

```
digit-recognizer/
│
├── app.py                # Main Streamlit app
├── digit_model.keras     # Trained TensorFlow model
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## 📝 Notes

- The canvas is black with white strokes to match the input format expected by the MNIST-trained model.
- Prediction only occurs after clicking the **"Predict Digit"** button.
- You may improve accuracy by retraining the model or applying better preprocessing techniques.

---

## ✅ Conclusion

The Handwritten Digit Recognizer project successfully demonstrates the power of deep learning and computer vision through a simple, interactive web application. By combining a Convolutional Neural Network (CNN) trained on the MNIST dataset with a user-friendly interface built using Streamlit, this project allows users to draw digits and instantly receive accurate predictions.

This application bridges the gap between machine learning models and real-world usability by offering an engaging interface for inference. It also lays the foundation for more advanced digit or character recognition systems, including OCR and handwriting analysis tools.

Overall, the project not only showcases the practical application of neural networks but also highlights how modern tools like Streamlit make it easier to deploy and share AI models with a broader audience.




