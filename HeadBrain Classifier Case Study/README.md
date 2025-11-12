# Head & Brain Analysis — Linear Regression Model

##  Overview
This project is a Linear Regression Analysis that examines the relationship between head size and brain weight using a biological dataset.
It predicts Brain Weight (grams) from Head Size (cm³) using regression modeling.

The main goal of this study is to demonstrate how simple linear regression can help understand and visualize correlations between two biological measurements.

##  Objectives
- To analyze the correlation between head size and brain weight.
- To build a linear regression model that predicts brain weight based on head size.
- To evaluate the model’s performance using MSE, RMSE, and R² metrics.
- To visualize the regression line representing the relationship.

##  Machine Learning Algorithm Used
The project uses Linear Regression, a supervised learning algorithm that establishes a linear relationship between the dependent and independent variables.
**Formula:**
𝑌= 𝑚𝑋 + 𝑐
Where:
Y → Predicted Brain Weight
X → Head Size
m → Slope (Coefficient)
c → Intercept


##  Technologies Used
- **Python**
- **Pandas** — Data manipulation and exploration 
- **NumPy** — NNumerical calculation
- **Matplotlib** — Data visualization
- **Scikit-learn** — Regression modeling and evaluation metrics

---
##  Workflow

- **Data Loading:** Import the MarvellousHeadBrain.csv dataset.
- **Data Exploration:** View first few records and summary statistics.
- **Feature Selection:** Independent Variable → Head Size(cm^3)
                         Dependent Variable → Brain Weight(grams)
- **Data Splitting:** Divide the dataset into training and testing sets (80:20).
- **Model Training:** Fit a Linear Regression model on training data.
- **Model Evaluation:** Calculate MSE, RMSE, and R² Score.
- **Visualization:** Plot regression line between Head Size and Brain Weight.

--- 

## Model Details 

- Independent Variable: Head Size
- Dependent Variable: Brain Weight

- Total Records in Dataset: (237, 1)
- Training Dataset Dimensions: (189, 1)
- Testing Dataset Dimensions: (48, 1)

## Results of Case Study

- Slope of line (m): 0.26188776
- Intercept (c): 328.60141186

- Mean Squared Error (MSE): 4672.0435
- Root Mean Squared Error (RMSE): 68.3523
- R² Score: 0.7149


--- 
##  How to Run the Project
1. Open the project in **Jupyter Notebook** or **VS Code**  
2. Load the dataset file MarvellousHeadBrain.csv'  
3. Run the Python program (e.g., ` HeadBrainLinerVisualResult.py`)   
---
##  Future Scope
- Include gender and age as additional features for multi-variable regression.
- Compare with Polynomial Regression for improved curve fitting.
- Develop a simple web app for interactive predictions.


