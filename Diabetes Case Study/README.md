#  Diabetes Prediction — Health Classification System

##  Overview
This project is a **Health Classification System** that predicts whether a person is likely to have diabetes based on various medical parameters.  
The system uses **Machine Learning (Logistic Regression)** to analyze data and classify patients into diabetic or non-diabetic categories.  

The goal of this project is to assist in **early detection** of diabetes and help in **preventive healthcare** decisions.

---

##  Objectives
- To develop a model that can accurately classify patients as diabetic or non-diabetic.
- To analyze health-related features that most affect diabetes prediction.
- To use data-driven insights for improving healthcare awareness.

---

##  Machine Learning Model
The project applies **Logistic Regression**, a supervised learning algorithm suitable for binary classification problems.  
The model is trained on a dataset containing features such as:
- Glucose level  
- Blood pressure  
- BMI (Body Mass Index)  
- Age  
- Insulin level  
- Skin thickness  

---

##  Technologies Used
- **Python**
- **Pandas** — Data manipulation and analysis  
- **NumPy** — Numerical operations  
- **Matplotlib / Seaborn** — Data visualization  
- **Scikit-learn** — Machine Learning model building  

---

##  Workflow
1. **Data Collection:** Load dataset (e.g., `diabetes.csv`)
2. **Data Preprocessing:** Handle missing values, normalize data
3. **Exploratory Data Analysis:** Visualize relationships and trends
4. **Model Training:** Apply Logistic Regression
5. **Model Evaluation:** Use accuracy, confusion matrix, and classification report
6. **Prediction:** Predict diabetes status based on new data

## Model Output

After training the Logistic Regression model on the **diabetes dataset**, the following results were observed:

- **Training Accuracy:** 77.03%
- **Testing Accuracy:** 74.67%



##  How to Run the Project
1. Open the project in **Jupyter Notebook** or **VS Code**  
2. Load the dataset file `diabetes.csv`  
3. Run the Python program (e.g., `DiabetesLogistic.py` or `Diabetes.ipynb`)  
4. View the output predictions and charts  

---

##  Future Scope
- Integration with real-time health data (IoT devices or apps)
- Using advanced ML models like Random Forest or Neural Networks
- Deploying the model as a web or mobile application


