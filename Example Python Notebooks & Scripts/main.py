from smote_pipeline import train_with_smote
from weight_pipeline import train_with_weight
from evaluate import evaluate

model_smote, X_test, y_test = train_with_smote()
evaluate(model_smote, X_test, y_test, "SMOTE")

model_weight, X_test, y_test = train_with_weight()
evaluate(model_weight, X_test, y_test, "scale_pos_weight")
