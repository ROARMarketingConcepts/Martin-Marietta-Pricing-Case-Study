from imblearn.over_sampling import SMOTE
import xgboost as xgb
from preprocessing import load_and_split_data

def train_with_smote():
    X_train, X_test, y_train, y_test = load_and_split_data()
    X_res, y_res = SMOTE(random_state=42).fit_resample(X_train, y_train)

    model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss')
    model.fit(X_res, y_res)
    return model, X_test, y_test
