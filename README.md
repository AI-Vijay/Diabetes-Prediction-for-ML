# 🏥 Diabetes Prediction System

## Overview
The Diabetes Prediction System is an AI-Powered Risk Assessment Tool built with Streamlit. It utilizes a Support Vector Machine (SVM) machine learning model to evaluate a patient's risk of having diabetes based on various medical measurements and demographic data.

## Features
* **Interactive User Interface:** A clean, easy-to-use sidebar for inputting patient information.
* **Real-Time Predictions:** Instantaneous prediction results categorizing the user as Low, Moderate, or High risk.
* **Probability Breakdown:** Visual gauge charts (powered by Plotly) displaying the exact probability metrics for being diabetic vs. non-diabetic.
* **Risk Factor Analysis:** Automatically identifies and highlights specific positive health indicators (e.g., healthy BMI, normal blood pressure) and potential risk factors (e.g., high glucose levels).
* **Actionable Recommendations:** Provides tailored health advice based on the prediction outcome.

## Technical Details
* **Model Type:** Support Vector Machine (SVM)
* **Model Accuracy:** ~78%
* **Dataset:** 768 samples (based on the Pima Indians Diabetes Database)
* **Input Features:**
  * Age
  * Pregnancies
  * Glucose (mg/dL)
  * Blood Pressure (mm Hg)
  * Skin Thickness (mm)
  * Insulin (mu U/ml)
  * BMI
  * Diabetes Pedigree Function

## Technologies Used
* **Python**
* **Streamlit:** Web application framework
* **Scikit-Learn:** Machine learning model training and inference
* **Pandas & NumPy:** Data manipulation and array handling
* **Plotly:** Interactive data visualization
* **Joblib:** Model serialization and loading
* **Matplotlib & Seaborn:** Data exploration and visualization

## Installation and Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AI-Vijay/Diabetes-Prediction-for-ML.git
   cd Diabetes-Prediction-for-ML
   ```

2. **Install the required dependencies:**
   Make sure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Generate the Model Files (if not already present):**
   Ensure that `diabetes_model.pkl` and `scaler_svm.pkl` are in your directory. If they are missing or you want to retrain the model, run the Jupyter notebook:
   ```bash
   jupyter notebook Diabetes.ipynb
   ```
   *Note: Ensure you export the trained model and scaler using `joblib` at the end of the notebook.*

4. **Run the Streamlit Application:**
   ```bash
   streamlit run app.py
   ```

## Screenshots
_Add a screenshot of the Streamlit UI (input sidebar + risk gauge)._

## ⚠️ Medical Disclaimer
This prediction application is for educational and demonstrative purposes only. It should **NOT** replace professional medical advice, diagnosis, or treatment. Always consult qualified healthcare professionals for actual medical concerns.

## Author
Vijay Nagargoje — B.Tech AI & Data Science, MIT-CSN Chhatrapati Sambhajinagar.
[LinkedIn](https://www.linkedin.com/in/vijay-nagargoje) · [GitHub](https://github.com/AI-Vijay)
