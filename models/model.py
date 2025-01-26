import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from imblearn.over_sampling import SMOTE
import joblib

def train_model():
    # Load the preprocessed data
    data_path = 'data/HRData_cleaned.csv'  # Path to the cleaned dataset
    df = pd.read_csv(data_path)

    # Convert categorical variables to numeric
    label_encoder = LabelEncoder()
    for column in df.select_dtypes(include=['object']).columns:
        df[column] = label_encoder.fit_transform(df[column])

    # Separate features (X) and target (y)
    X = df.drop(columns=['employee_id', 'is_promoted'])
    y = df['is_promoted']

    # Standardize the dataset (scaling)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Apply SMOTE to balance the classes
    smote = SMOTE(random_state=42)
    X_resampled, y_resampled = smote.fit_resample(X_scaled, y)

    print("Before SMOTE:", pd.Series(y).value_counts())
    print("After SMOTE:", pd.Series(y_resampled).value_counts())

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)

    # Initialize and train the XGBoost model
    model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss')
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate the model
    print("Model Accuracy: ", accuracy_score(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))

    # Save the trained model and scaler
    joblib.dump(model, 'models/xgboost_model_smote.pkl')
    joblib.dump(scaler, 'models/scaler.pkl')
    print("Model and scaler saved in 'models/' directory.")

if __name__ == "__main__":
    train_model()
