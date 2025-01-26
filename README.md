# 🎯 Employee Promotion Prediction System

## 📄 **Project Overview**

This project focuses on building a **Machine Learning Model** to predict whether employees are eligible for a promotion based on their performance, achievements, and other attributes. The solution is designed to help HR departments make data-driven decisions while ensuring fairness and efficiency.

---

## 🔍 **Objectives**

- Develop a robust ML model to predict employee promotions.
- Handle class imbalance to ensure accurate predictions for underrepresented groups.
- Provide a detailed **EDA (Exploratory Data Analysis)** to understand key patterns and relationships in the data.
- Train models with optimized features for better interpretability and performance.

---

## 🛠️ **Technologies and Tools Used**

- **Programming Language**: Python 🐍
- **Libraries**: 
  - Data Processing: `pandas`, `numpy`
  - Visualization: `matplotlib`, `seaborn`
  - Machine Learning: `scikit-learn`, `xgboost`
  - Oversampling: `imbalanced-learn`
  - Model Persistence: `joblib`

---

## 📂 **Project Structure**

```
EDA-and-predictor-for-Employee-Eligible-for-Promotion/
├── data/                     # Contains datasets
│   ├── HRData.csv            # Raw dataset
│   ├── HRData_cleaned.csv    # Cleaned and preprocessed dataset
│   ├── hrdatatest.csv        # Test dataset
│   └── predictions_hrdatatest.csv # Predictions output
├── models/                   # Trained models and scalers
│   ├── xgboost_model.pkl
│   ├── xgboost_model_smote.pkl
│   └── scaler.pkl
├── scripts/                  # Scripts for each step of the pipeline
│   ├── data_preprocessing.py # Data preprocessing and cleaning
│   ├── eda.py                # Exploratory Data Analysis
│   ├── model_training.py     # Model training with SMOTE
│   ├── predict.py            # Predictions on new data
│   └── train_with_selected_features.py # Training with selected features
├── README.md                 # Project documentation
└── requirements.txt          # Python dependencies
```

---

## 🚀 **Key Features**

### 🔹 **1. Exploratory Data Analysis (EDA)**
- **Visualizations included**:
  - Distribution of promotions.
  - Correlation matrix.
  - Boxplots (e.g., age vs promotion).
  - Histograms (e.g., training scores).
  - Promotion breakdown by department.
- **Insights**:
  - `avg_training_score`, `KPIs_met >80%`, and `previous_year_rating` are highly correlated with promotions.

### 🔹 **2. Data Preprocessing**
- Handled missing values using `SimpleImputer`.
- Converted categorical variables to numerical using `LabelEncoder`.
- Standardized features using `StandardScaler`.

### 🔹 **3. Model Training**
- Used **XGBoost** for classification.
- Addressed class imbalance with **SMOTE**.
- Trained the model with the full feature set and improved its precision and recall by balancing classes using **SMOTE**:
  - **Accuracy:** 97%.
  - **Class `1` (Promoted):**
    - **Recall:** 94%.
    - **Precision:** 99%.
    - **F1-Score:** 96%.

### 🔹 **4. Predictions**
- Deployed a script to predict promotions on new datasets.
- Outputs predictions in `predictions_hrdatatest.csv`.

---

## 📊 **Model Metrics**

### **Model with Full Features**
- **Accuracy:** 94.17%
- **Class `1` (Promoted):**
  - **Recall:** 35%
  - **Precision:** 87%
  - **F1-Score:** 50%

---

## ⚙️ **How to Run the Project**

1. **Set up the environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Preprocess the data:**
   ```bash
   python scripts/data_preprocessing.py
   ```

3. **Perform EDA:**
   ```bash
   python scripts/eda.py
   ```

4. **Train the model:**
   ```bash
   python scripts/model_training.py
   ```

5. **Train with selected features:**
   ```bash
   python scripts/train_with_selected_features.py
   ```

6. **Make predictions:**
   ```bash
   python scripts/predict.py
   ```

---

## 📦 **Dependencies**

Install all required libraries with:
```bash
pip install -r requirements.txt
```

---

## 📥 **Outputs**

- Predictions are saved in the `data/predictions_hrdatatest.csv` file.
- Trained models and scalers are saved in the `models/` directory.

---

## 🤝 **Contributing**

Contributions are welcome! Feel free to submit a pull request or raise an issue. Let's make this project even better!

---

## 📧 **Contact**
For questions or feedback, please reach out to me at - [LinkedIn Profile](www.linkedin.com/in/bautista1).

---

### ✨ Thank you for exploring this project! 😊
