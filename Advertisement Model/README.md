#  Advertisement Sales Prediction — Linear Regression Mode

##  Overview
This project is a Sales Prediction System that analyzes how different forms of media advertising — TV, Radio, and Newspaper — influence product sales.
The system uses Machine Learning (Linear Regression) to predict future sales based on advertising expenditure data.

##  Objectives
 - To build a regression model that predicts product sales based on media advertisement data.
 - To study the effect of different advertising channels on total sales.
 - To visualize relationships between input features (TV, Radio, Newspaper) and sales.
---
##  Technologies Used
- **Python**
- **Pandas** — Data cleaning and manipulation  
- **NumPy** — NNumerical calculation   
- **Scikit-learn** — Model building, evaluation, and regression analysis
- **Matplotlib / Seaborn** — Visualization and correlation heatmaps
---
##  Workflow
1. - **Data Loading:** Import Advertising.csv dataset
2  - **Data Cleaning:** Remove unnecessary columns and handle missing values
3  - **Exploratory Data Analysis (EDA):**   - Generate correlation matrix   -  Create heatmaps and pairplots for visual insights.
4. - **Model Training:** Train Linear Regression model using train_test_split()
5  - **Model Evaluation:** Compute MSE, RMSE, and R² Score
6  - **Visualization:** Plot actual vs predicted sales for performance comparison

## Model Output

**Mean Squared Error (MSE):** 3.17  
**Root Mean Squared Error (RMSE):** 1.78  
**R² Score:** 0.89

- **Model Coefficients:**
 1 TV: 0.0447
 2 Radio: 0.1892
 3 Newspaper: 0.0028
 4 Intercept: 2.979

--- 
##  How to Run the Project
1. Open the project in **Jupyter Notebook** or **VS Code**  
2. Load the dataset file Advertising.csv.csv`  
3. Run the Python program (e.g., ` AdvertisingRegressionVisualModel.py`)   
---
##  Future Scope
- Apply advanced models like Multiple Regression, Polynomial Regression, or Decision Trees.
- Add time series forecasting for monthly or seasonal ad performance.
- Deploy as a dashboard for marketing analytics and budget planning.


