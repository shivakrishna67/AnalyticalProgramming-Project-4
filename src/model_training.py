class ModelRandomForest:
    def __init__(self):
        pass

    def model_train(self, data):
        """
        Trains a Random Forest classifier on the provided data.

        Args:
            data (pandas.DataFrame): The input data containing features and the target variable.

        Returns:
            tuple: A tuple containing the true labels (y_test) and predicted labels (y_pred) on the test set.
        """
        X, y = (
            data.drop(columns=["number_of_persons_killed"]),
            data["number_of_persons_killed"],
        )
        from sklearn.preprocessing import StandardScaler

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        from sklearn.model_selection import train_test_split, cross_val_score
        from sklearn.pipeline import Pipeline
        from sklearn.impute import (
            SimpleImputer,
        )  # The primary purpose of SimpleImputer is to address missing values in your dataset
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.metrics import accuracy_score

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(
            X_scaled, y, test_size=0.2, random_state=42
        )

        print(
            """ Random Forest is often chosen for classification tasks due to its effectiveness
              in handling various challenges inherent in machine learning problems. Its ensemble
              learning approach provides robustness against overfitting, and it can capture complex
              relationships in data, making it suitable for a wide range of datasets. Additionally,
              Random Forests offer insights into feature importance, ease of use with default 
              parameters, and the ability to handle missing data."""
        )

        # Create a pipeline with imputation and RandomForestClassifier
        pipeline = Pipeline(
            [
                ("imputer", SimpleImputer(strategy="mean")),
                (
                    "classifier",
                    RandomForestClassifier(
                        n_estimators=100,
                        random_state=42,
                        criterion="gini",
                        max_depth=10,
                        max_features=10,
                    ),
                ),
            ]
        )

        # Use cross-validation to evaluate the model
        cv_scores = cross_val_score(
            pipeline, X_train, y_train, cv=5, scoring="accuracy"
        )

        # Print the cross-validation scores
        print("Cross-Validation Scores:", cv_scores)
        print("Mean CV Score:", cv_scores.mean())

        # Fit the pipeline on the training data
        pipeline.fit(X_train, y_train)

        # Make predictions on the test set
        y_pred = pipeline.predict(X_test)

        # Evaluate the model on the test set
        test_accuracy = accuracy_score(y_test, y_pred)
        print("Test Accuracy:", test_accuracy)

        return y_test, y_pred
