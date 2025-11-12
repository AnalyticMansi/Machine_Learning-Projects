Titanic Case Study Description :- 
The Titanic Case Study is a classic machine learning project that aims to predict the survival of passengers aboard the RMS 
Titanic based on various attributes such as age, gender, passenger class, fare, and family relationships. 
The dataset used for this project is derived from the Kaggle Titanic dataset, which contains detailed information about passengers.

Objective:-
The main goal of this case study is to build a classification model that can predict whether a passenger survived or not, 
based on available features.

Dataset Information :-
Total Records: 1309
Total Columns: 10
Target Variable: Survived (0 = Not Survived, 1 = Survived)

Model Used :- 
Logistic Regression was applied to predict passenger survival.

Model Evaluation :-
Accuracy: 0.7671 (≈ 76.7%)
Confusion Matrix:

[[174  15]
 [ 46  27]]

True Negatives (174): Correctly predicted non-survivors
False Positives (15): Incorrectly predicted survivors
False Negatives (46): Missed actual survivors
True Positives (27): Correctly predicted survivors

Key Insights :- 
Female passengers had a higher survival rate.
Higher-class passengers were more likely to survive.
Age and fare played significant roles in survival prediction.
