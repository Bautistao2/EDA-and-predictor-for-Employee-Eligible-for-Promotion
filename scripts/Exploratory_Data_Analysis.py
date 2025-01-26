import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler

def perform_eda():
    # Load the preprocessed data
    data_path = 'data/HRData_cleaned.csv'  # Path to the cleaned dataset
    df = pd.read_csv(data_path)

    # Create a folder to save visualizations
    output_dir = "visualizations"
    os.makedirs(output_dir, exist_ok=True)

    # Convert categorical variables to numeric
    label_encoder = LabelEncoder()
    for column in df.select_dtypes(include=['object']).columns:
        df[column] = label_encoder.fit_transform(df[column])

    # Standardize the dataset (scaling)
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df)
    scaled_df = pd.DataFrame(scaled_data, columns=df.columns)

    # 1. Distribution of promotions
    plt.figure(figsize=(8, 6))
    sns.countplot(x='is_promoted', data=df)
    plt.title('Promotion Distribution')
    plt.xlabel('Promoted (1 = Yes, 0 = No)')
    plt.ylabel('Count')
    plt.savefig(f"{output_dir}/promotion_distribution.png")
    plt.close()

    # 2. Correlation matrix (all variables)
    plt.figure(figsize=(12, 10))
    correlation_matrix = scaled_df.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix (All Variables)')
    plt.savefig(f"{output_dir}/correlation_matrix.png")
    plt.close()

    # 3. Age vs Promotion (Boxplot)
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='is_promoted', y='age', data=df)
    plt.title('Age vs Promotion')
    plt.xlabel('Promoted (1 = Yes, 0 = No)')
    plt.ylabel('Age')
    plt.savefig(f"{output_dir}/age_vs_promotion.png")
    plt.close()

    # 4. Distribution of average training score
    plt.figure(figsize=(8, 6))
    sns.histplot(df['avg_training_score'], kde=True, bins=20, color='blue')
    plt.title('Distribution of Average Training Score')
    plt.xlabel('Average Training Score')
    plt.ylabel('Frequency')
    plt.savefig(f"{output_dir}/avg_training_score_distribution.png")
    plt.close()

    # 5. Awards won vs Promotion
    plt.figure(figsize=(8, 6))
    sns.countplot(x='awards_won?', hue='is_promoted', data=df)
    plt.title('Awards Won vs Promotion')
    plt.xlabel('Awards Won (1 = Yes, 0 = No)')
    plt.ylabel('Count')
    plt.legend(title='Promoted')
    plt.savefig(f"{output_dir}/awards_vs_promotion.png")
    plt.close()

    # 6. Department-wise promotion distribution
    plt.figure(figsize=(12, 8))
    sns.countplot(x='department', hue='is_promoted', data=df, order=df['department'].value_counts().index)
    plt.title('Promotions by Department')
    plt.xlabel('Department')
    plt.ylabel('Count')
    plt.xticks(rotation=0)
    plt.legend(title='Promoted')
    plt.savefig(f"{output_dir}/department_vs_promotion.png")
    plt.close()

    print(f"EDA completed. All visualizations have been saved to the '{output_dir}' directory.")

if __name__ == "__main__":
    perform_eda()
