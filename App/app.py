import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load the model and scaler
model = joblib.load('models/xgboost_model_smote.pkl')
scaler = joblib.load('models/scaler.pkl')

# Function to preprocess input data
def preprocess_data(input_data):
    # Convert categorical variables to numeric
    label_encoder = LabelEncoder()
    for column in input_data.select_dtypes(include=['object']).columns:
        input_data[column] = label_encoder.fit_transform(input_data[column])

    # Standardize the dataset
    input_data_scaled = scaler.transform(input_data)
    return input_data_scaled

# Streamlit app
st.title("🎯 Employee Promotion Prediction System")
st.write("Upload employee data to predict their eligibility for promotion.")

# File upload
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
    # Read the file
    input_data = pd.read_csv(uploaded_file)
    st.write("### Input Data Preview:")
    st.dataframe(input_data)

    # Drop irrelevant columns (if any)
    if 'employee_id' in input_data.columns:
        input_data = input_data.drop(columns=['employee_id'])

    # Preprocess the data
    try:
        processed_data = preprocess_data(input_data)

        # Predict
        predictions = model.predict(processed_data)
        input_data['is_promoted'] = predictions

        st.write("### Predictions:")
        st.dataframe(input_data)

        # Download results
        csv = input_data.to_csv(index=False)
        st.download_button(
            label="📥 Download Predictions as CSV",
            data=csv,
            file_name="predictions.csv",
            mime="text/csv"
        )
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")

st.write("Developed by your friendly AI assistant! 😊")
