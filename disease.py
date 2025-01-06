import pandas as pd

# Load the training dataset
df = pd.read_csv('/kaggle/input/disease-prediction-using-machine-learning/Training.csv')

print(df.head(5))
  


X = df.iloc[:, :-1]  # Features (symptoms)
y = df['prognosis']   # Target variable



# Assuming 'X' contains your features
X_encoded = pd.get_dummies(X)



from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)



from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(random_state=42)



model.fit(X_train, y_train)



y_pred = model.predict(X_test)

from sklearn.metrics import accuracy_score, classification_report

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))



# Assuming 'model' is your trained Random Forest model
feature_importance = pd.DataFrame({'Feature': X_encoded.columns, 'Importance': model.feature_importances_})
feature_importance = feature_importance.sort_values(by='Importance', ascending=False)
print(feature_importance)




test_data = pd.read_csv('/kaggle/input/disease-prediction-using-machine-learning/Testing.csv')




# Assuming 'model' is your trained Random Forest model
test_data_encoded = pd.get_dummies(test_data)  # Encode if needed
test_predictions = model.predict(test_data_encoded)

print("Predictions for testing data:")
print(test_predictions)





testing_data = pd.read_csv('/kaggle/input/disease-prediction-using-machine-learning/Testing.csv')

# Extract true labels from the testing dataset
true_labels = testing_data['prognosis']

# Calculate accuracy and print the classification report
accuracy_test = accuracy_score(true_labels, test_predictions)
print("Accuracy on testing data:", accuracy_test)

print("\nClassification Report:")
print(classification_report(true_labels, test_predictions))







import pandas as pd
from ipywidgets import interact_manual, Dropdown

# Load the training dataset
df = pd.read_csv('/kaggle/input/disease-prediction-using-machine-learning/Training.csv')

# Exclude 'prognosis' from the symptom list
symptoms = df.columns[:-1].tolist()

# Create a function to make predictions based on selected symptoms
def predict_disease(**selected_symptoms):
    # Ensure the input data structure is consistent with the training data
    input_data = pd.DataFrame({symptom: [0] for symptom in symptoms})
    for symptom, value in selected_symptoms.items():
        if symptom != 'prognosis':
            input_data[symptom] = int(value)

    # Assuming 'model' is your trained RandomForestClassifier model
    # Preprocess the input and make predictions
    input_encoded = pd.get_dummies(input_data)

    # Ensure that the input data columns match the feature names used during training
    input_encoded = input_encoded.reindex(columns=model.feature_names_in_, fill_value=0)

    prediction = model.predict(input_encoded)[0]

    return f"The predicted disease based on symptoms is: {prediction}"

# Create an interactive dropdown for each symptom excluding 'prognosis'
interact_manual(predict_disease, **{symptom: Dropdown(options=[0, 1], description=symptom) for symptom in symptoms if symptom != 'prognosis'})




















































































































































































