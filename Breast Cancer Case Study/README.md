#  Breast Cancer Detection — Tumor Classification System

##  Overview
his project is a Tumor Classification System that predicts whether a breast tumor is malignant or benign based on several medical features.
The system uses Machine Learning algorithms (Support Vector Machine and Logistic Regression) to analyze medical data and classify tumors effectively.

##  Objectives
 - To build a classification model for detecting breast cancer.
 - To differentiate between malignant (cancerous) and benign (non-cancerous) tumors.
 - To apply and compare the performance of SVM and Logistic Regression.
---
##  Technologies Used
- **Python**
- **Pandas** — Data manipulation and analysis  
- **NumPy** — Numerical operations    
- **Scikit-learn** — Machine Learning model building
- **StandardScaler** — Feature scaling  
---
##  Workflow
1. - **Data Loading:** Load the Breast Cancer dataset using load_breast_cancer() from scikit-learn.
2. - **Data Preprocessing:** Apply feature scaling using StandardScaler().
3. - **Train-Test Split:** Divide the data into 80% training and 20% testing.
4. - **Model Training:** Train an SVM model with a linear kernel.
5. - **Prediction:** Predict tumor type (malignant or benign).
6. - **Evaluation:** Measure accuracy and display confusion matrix.

## Model Output
After training the Logistic Regression model on the **Breast Cancer dataset**, the following results were observed:
- **Model Accuracy:** 0.9561 (≈ 95.6%)
- **Confusion Matrix:** [[41, 2], [3, 68]]  
--- 
##  How to Run the Project
1. Open the project in **Jupyter Notebook** or **VS Code**  
2. Load the dataset file `BreastCancerDataset.csv`  
3. Run the Python program (e.g., `SVMBreast.py`)   
---
##  Future Scope
- Implement additional models like Random Forest and K-Nearest Neighbors (KNN).
- Create a web interface for cancer detection predictions.
- Use real-world patient datasets for improved clinical validation.


