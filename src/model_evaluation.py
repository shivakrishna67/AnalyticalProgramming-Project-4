class ModelEvaluation:
    def __init__(self) -> None:
        pass

    def model_eval(self, y_test, y_pred):
        """
        Evaluates the model using confusion matrix and classification report.

        Args:
            y_pred (array-like): Predicted labels from the model.
            y_test (array-like): True labels from the test set.

        Returns:
            None
        """
        from sklearn.metrics import confusion_matrix, classification_report

        # Compute confusion matrix
        cm = confusion_matrix(y_test, y_pred)

        # Print confusion matrix
        print("Confusion Matrix:")
        print(cm)

        # Generate and print classification report
        report = classification_report(y_test, y_pred)
        print("Classification Report:")
        print(report)
