import streamlit as st
import pickle
import numpy as np

# Load the saved Linear Regression model
with open('Obesity_Risk.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Function to predict EMISSION using the loaded model
def predict_obesity(Height, Weight, family_history_with_overweight, FCVC_minmax, Age_bin_minmax):
    features = np.array([Height, Weight, family_history_with_overweight, FCVC_minmax, Age_bin_minmax])
    features = features.reshape(1,-1)
    emission = model.predict(features)
    return emission[0]

# Streamlit UI
st.title('OBESITY LEVEL PREDICTION')
st.write("""
## Input Features
ENTER THE VALUES FOR THE INPUT FEATURES TO PREDICT OBESITY.
""")

# Input fields for user
Height = st.number_input('HEIGHT')
Weight = st.number_input('WEIGHT')
family_history_with_overweight = st.number_input('FAMILY_HISTORY_WITH_OVERWEIGHT')
FCVC_minmax = st.number_input('FCVC_MINMAX')
Age_bin_minmax = st.number_input('AGE_BIN_MINMAX')

# Prediction button
if st.button('Predict'):
    # Predict EMISSION
    obesity_prediction = predict_obesity(Height, Weight, family_history_with_overweight, FCVC_minmax, Age_bin_minmax)
    st.write(f"PREDICTED OBESITY: {obesity_prediction}")