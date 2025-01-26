import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer

def preprocess_data(input_path, output_path):
    # Load the dataset
    df = pd.read_csv(input_path)
    
    # Fill missing values (ensure the output is 1D using .ravel())
    imputer = SimpleImputer(strategy='most_frequent')
    df['education'] = imputer.fit_transform(df[['education']]).ravel()
    df['previous_year_rating'] = imputer.fit_transform(df[['previous_year_rating']]).ravel()

    # Encode categorical variables
    label_encoder = LabelEncoder()
    df['gender'] = label_encoder.fit_transform(df['gender'])
    df['department'] = label_encoder.fit_transform(df['department'])
    df['region'] = label_encoder.fit_transform(df['region'])
    df['recruitment_channel'] = label_encoder.fit_transform(df['recruitment_channel'])

    # Save the preprocessed data
    df.to_csv(output_path, index=False)
    print(f"Data preprocessing completed. Cleaned data saved to '{output_path}'.")

if __name__ == "__main__":
    preprocess_data('data/HRData.csv', 'data/HRData_cleaned.csv')
