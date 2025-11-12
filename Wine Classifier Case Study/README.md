# Wine Predictor — Quality Classification System

##  Overview
The Wine Predictor — Quality Classification System is a Machine Learning project that predicts the type or class of wine based on various chemical properties.
Using the K-Nearest Neighbors (KNN) algorithm, the model classifies wines into categories depending on their composition and characteristics.

##  Objectives
To develop a machine learning model that can accurately predict the wine class (quality category) using its measurable chemical features.


##  Machine Learning Algorithm Used
K-Nearest Neighbors (KNN) Classifier
The model identifies the nearest data points in the feature space to classify a new wine sample based on similarity with known labeled examples.

##  Technologies Used
- **Python**
- **Pandas** — Data cleaning and manipulation  
- **NumPy** — NNumerical calculation   
- **Scikit-learn** — Model building, evaluation, and regression analysis

---
##  Workflow
1. - **Data Loading:** Import the WinePredictor.csv dataset. ##
2  - **Data Cleaning:** Handle missing values and ensure all records are valid.##
3  - **Feature Selection:** Separate independent features (X) and the target variable (Class).##
4  - **Data Standardization:** Apply StandardScaler to normalize the feature values.##
5  - **Data Splitting:** Split the dataset into training and testing sets using train_test_split().
6  - **Model Training:** Train the K-Nearest Neighbors (KNN) model for different K values (1–20).
7  - **Model Optimization:** Identify the best K value that gives the highest accuracy.
8  - **Model Evaluation:** Evaluate the model using accuracy score and confusion matrix.
9  - **Prediction:** Predict the wine class on test data and display the final accuracy.

--- 

## Model Output

**Best value of k is :-**  12

**Final Best Accuracy is :-**  97.22%

**Confusion Matrix:**
[[14  0  0]
 [ 1 13  0]
 [ 0  0  8]]

--- 
##  How to Run the Project
1. Open the project in **Jupyter Notebook** or **VS Code**  
2. Load the dataset file WinePredictor.csv'  
3. Run the Python program (e.g., ` WinePredictor.py`)   
---
##  Future Scope
- Use other classification algorithms (e.g., Decision Tree, Random Forest, SVM)
- Apply hyperparameter tuning for better performance
- Build an interactive dashboard for real-time prediction


