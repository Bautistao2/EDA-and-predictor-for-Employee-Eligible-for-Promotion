import pandas as pd
import joblib

def make_predictions(input_data_path, output_data_path):
    # Load the trained model and scaler
    model = joblib.load('models/xgboost_model_smote.pkl')
    scaler = joblib.load('models/scaler.pkl')

    # Load new input data
    input_data = pd.read_csv(input_data_path)

    # Remove irrelevant columns (e.g., employee_id)
    if 'employee_id' in input_data.columns:
        input_data = input_data.drop(columns=['employee_id'])

    # Convert categorical variables to numeric if they exist
    from sklearn.preprocessing import LabelEncoder
    label_encoder = LabelEncoder()
    for column in input_data.select_dtypes(include=['object']).columns:
        input_data[column] = label_encoder.fit_transform(input_data[column])

    # Standardize the input data
    input_data_scaled = scaler.transform(input_data)

    # Make predictions
    predictions = model.predict(input_data_scaled)

    # Add predictions to the input data
    input_data['is_promoted'] = predictions

    # Save the predictions to a new file
    input_data.to_csv(output_data_path, index=False)
    print(f"Predictions saved to {output_data_path}")

if __name__ == "__main__":
    # Using 'hrdatatest.csv' as the input file
    make_predictions('data/hrdatatest.csv', 'data/predictions_hrdatatest.csv')
