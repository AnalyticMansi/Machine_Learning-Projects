#  Titanic Prediction — Survival Classification System

##  Overview
This project is a Passenger Classification System that predicts whether a passenger survived the Titanic disaster based on various demographic and travel features.
The system uses Machine Learning (Logistic Regression) to analyze data and classify passengers into Survived or Not Survived categories.

##  Objectives
- To build a model that can accurately predict passenger survival..
- To identify the factors (like gender, class, and age) that affected survival chances.
- To visualize insights from the Titanic dataset for better understanding.

---

##  Machine Learning Model
The project uses Logistic Regression, a supervised learning algorithm ideal for binary classification problems.
The model is trained on the Titanic dataset containing features such as:
- Passenger Class (Pclass)
- Gender (Sex)
- Age
- Number of Siblings/Spouses (SibSp)
- Number of Parents/Children (Parch)
- Fare
- Embarkation Port


---

##  Technologies Used
- **Python**
- **Pandas** — Data manipulation and analysis  
- **NumPy** — Numerical operations  
- **Matplotlib / Seaborn** — Data visualization  
- **Scikit-learn** — Machine Learning model building  

---

##  Workflow
1. **Data Collection:** Load dataset (e.g., `MarvellosTitanicDataset.csv`)
2. **Data Preprocessing:** Handle missing values,encode categorical data
3. **Exploratory Data Analysis:** Visualize age, gender, class-wise survival rates
4. **Model Training:** Apply Logistic Regression
5. **Model Evaluation:** Use accuracy, confusion matrix, and classification report
6. **Prediction:** Predict survival outcome for new passenger data

## Model Output

After training the Logistic Regression model on the **Titanic dataset**, the following results were observed:

- **Model Accuracy:** 76.71%
- **Confusion Matrix:** [[174  15]
                         [ 46  27]]
  
  - This means:
  - **174** passengers were correctly predicted as Not Survived
  - **27** passengers were correctly predicted as Survived
  - **15** and **46**instances were misclassified


##  How to Run the Project
1. Open the project in **Jupyter Notebook** or **VS Code**  
2. Load the dataset file `MarvellosTitanicDataset.csv.csv`  
3. Run the Python program (e.g., `TitanicLogistic.py`)  
4. View the output predictions and survival visualizations  

---

##  Future Scope
- Experiment with advanced models like Random Forest or XGBoost
- Add feature importance visualization for better interpretability 
- Deploy as a web app where users can input passenger details to predict survival


