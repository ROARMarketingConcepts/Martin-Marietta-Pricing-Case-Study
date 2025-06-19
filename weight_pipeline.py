import xgboost as xgb
from preprocessing import load_and_split_data

def train_with_weight():
    X_train, X_test, y_train, y_test = load_and_split_data()
    scale = (y_train == 0).sum() / (y_train == 1).sum()

    model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss', scale_pos_weight=scale)
    model.fit(X_train, y_train)
    return model, X_test, y_test
