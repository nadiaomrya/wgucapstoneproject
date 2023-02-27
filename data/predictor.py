from .forms import *
from .models import *
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from .views import *


def make_prediction(file, answers):
# Load the data from the CSV file
        df = pd.read_csv(file)
        print(df.columns.tolist())
# Split the data into a training set and a test set
        X = df.drop("Class ", axis=1)
        y = df["Class "]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train the model using a random forest classifier
        model = RandomForestClassifier()
        model.fit(X_train, y_train)

# Evaluate the model on the test set
        accuracy = model.score(X_test, y_test)
        print("Test set accuracy: {:.2f}".format(accuracy))

# Use the model to make predictions on new data
        new_data = pd.DataFrame({
            "var1": [1, 0, 1],
            "var2": [1, 0, 1],
            "var3": [1, 0, 1],
            "var4": [1, 0, 1],
            "var5": [1, 0, 1],
            "var6": [1, 0, 1],
            "var7": [1, 0, 1],
            "var8": [1, 0, 1],
            "var9": [1, 0, 1],
            "var10": [1, 0, 1]
        })

# Turn list of strings into list of ints
        values =  [int(x) for x in answers]

# Create a DataFrame from the list of values
        new_data = pd.DataFrame([values])

# Print the resulting DataFrame
        print(new_data)

        predictions = model.predict(new_data)
        print("Predictions:", predictions)
        return predictions
