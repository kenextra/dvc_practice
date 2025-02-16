import pickle

import pandas as pd
from sklearn.linear_model import LinearRegression
# from sklearn.ensemble import RandomForestRegressor

from config import Config

Config.MODELS_PATH.mkdir(parents=True, exist_ok=True)

X_train = pd.read_csv(str(Config.FEATURES_PATH / "train_features.csv"))
y_train = pd.read_csv(str(Config.FEATURES_PATH / "train_labels.csv"))

model = LinearRegression()
"""
model = RandomForestRegressor(
    n_estimators=150, max_depth=6, random_state=Config.RANDOM_SEED
)
"""
model = model.fit(X_train, y_train.to_numpy().ravel())

with open(str(Config.MODELS_PATH / "model.pickle"), "wb") as f:
    pickle.dump(model, f)
