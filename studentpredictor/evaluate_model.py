import json
import pickle

import pandas as pd
from sklearn.metrics import mean_squared_error

from config import Config

X_test = pd.read_csv(str(Config.FEATURES_PATH / "test_features.csv"))
y_test = pd.read_csv(str(Config.FEATURES_PATH / "test_labels.csv"))

with open(str(Config.MODELS_PATH / "model.pickle"), "rb") as f:
    model = pickle.load(f)

r_squared = model.score(X_test, y_test)

y_pred = model.predict(X_test)
rmse = mean_squared_error(y_test, y_pred)

with open(str(Config.METRICS_FILE_PATH), "w") as outfile:
    json.dump(dict(r_squared=r_squared, rmse=rmse), outfile)
