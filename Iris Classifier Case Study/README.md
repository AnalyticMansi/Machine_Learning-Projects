# Iris Flower Classification — KNN-Based Prediction System

##  Overview
This project is a Classification System designed to predict the species of Iris flowers — Setosa, Versicolor, or Virginica — based on their sepal and petal dimensions.
It uses the K-Nearest Neighbors (KNN) algorithm, a simple and powerful supervised machine learning technique for classification task

##  Objectives
- To classify Iris flower species using the K-Nearest Neighbors algorithm.
- To analyze the relationship between sepal/petal measurements and species classification.
- To evaluate model performance using accuracy, confusion matrix, and classification metrics.

##  Machine Learning Model
The project uses the K-Nearest Neighbors **(KNN)** algorithm.
It works by finding the k nearest data points (neighbors) to a given sample and assigning the class that is most frequent among them.

**Key Features Used:**
- Sepal Length
- Sepal Width
- Petal Length
- Petal Width
- 

##  Technologies Used
- **Python**
- **Pandas** — Data manipulation and analysis
- **Scikit-learn** — Model building and evaluation

---
##  Workflow

- **Data Loading:** Import the iris.csv dataset.
- **Data Preprocessing:** Split the dataset into features and target variables.
- **Data Scaling:** Normalize data using StandardScaler.
- **Model Training:** Train the KNN Classifier with optimal k value (e.g., 7).
- **Model Prediction:** Predict flower species for test data.
- **Model Evaluation:** Calculate accuracy, confusion matrix, and classification report.

--- 

## Model Details 

- Accuracy: 95.56%
- Confusion Matrix:
[[15  0  0]
 [ 0 15  1]
 [ 0  1 13]]

--- 
##  How to Run the Project
1. Open the project in **Jupyter Notebook** or **VS Code**  
2. Load the dataset file 'iris.csv'  
3. Run the Python program (e.g., `irisKNN.py`)   
---
##  Future Scope
- Experiment with different values of k to optimize accuracy.
- Compare results with other algorithms like Decision Tree or SVM.
- Visualize decision boundaries for better interpretability.
- Deploy as a web app for real-time flower classification.


