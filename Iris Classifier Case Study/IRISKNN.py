import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def IrisKNNClassifier(Datapath):
   
    df = pd.read_csv(Datapath)
    print("First 5 records of dataset:\n", df.head())

    
    X = df.iloc[:, :-1].values   
    y = df.iloc[:, -1].values    

  
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=5)

    
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    model = KNeighborsClassifier(n_neighbors=7)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)

    print("\n--- Evaluation Results ---")
    print("Accuracy:", round(accuracy * 100, 2), "%")
    print("Confusion Matrix:\n", cm)
    print("\nClassification Report:\n", classification_report(y_test, y_pred))

def main():
    IrisKNNClassifier("iris.csv")

if __name__ == "__main__":
    main()
