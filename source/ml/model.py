from joblib import load
import pandas as pd
import numpy as np
from source.backend.ml.transforms import make_transformer


class Model:
    def __init__(self, filename):
        self._model = load(filename)
        self._transformer = make_transformer()

    def predict(self, data: pd.DataFrame) -> np.ndarray:
        offices = ["МОСКВА Г", "САНКТ-ПЕТЕРБУРГ Г",
                   "ВОЛОГОДСКАЯ ОБЛ", "ОРЛОВСКАЯ ОБЛ",
                   "ЛИПЕЦКАЯ ОБЛ", "РОСТОВСКАЯ ОБЛ",
                   "НИЖЕГОРОДСКАЯ ОБЛ", "ПЕРМСКИЙ КРАЙ",
                   "ЕКАТЕРИНБУРГ Г", "ЧЕЛЯБИНСК Г",
                   "НОВОСИБИРСК Г", "ИРКУТСКАЯ ОБЛ"]
        data['has_close_office'] = data['region'].copy()
        data['has_close_office'] = data['has_close_office'].apply(
            lambda x: x in offices)

        self._transformer.fit(data)
        X = self._transformer.transform(data)

        return self._model.predict_proba(X)[:, 1]
