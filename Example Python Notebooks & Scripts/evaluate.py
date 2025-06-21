from sklearn.metrics import classification_report, confusion_matrix

def evaluate(model, X_test, y_test, label):
    y_pred = model.predict(X_test)
    print(f"\n{label} Results:\n")
    print(classification_report(y_test, y_pred, digits=4))
    confusion_matrix(y_test, y_pred)
    return
