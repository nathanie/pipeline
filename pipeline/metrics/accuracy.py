from .base import MetricsCalculatorBase

from sklearn.metrics import accuracy_score

import numpy as np


class MetricsCalculatorAccuracy(MetricsCalculatorBase):
    def __init__(self, border=0.5):
        super().__init__()
        self.zero_cache()
        self._border = border

    def zero_cache(self):
        self._predictions = []
        self._true_labels = []

    def add(self, y_predicted, y_true):
        self._predictions.append(y_predicted.cpu().data.numpy())
        self._true_labels.append(y_true.cpu().data.numpy())

    def calculate(self):
        y_pred = np.concatenate(self._predictions)
        y_true = np.concatenate(self._true_labels)

        y_pred = (y_pred >= self._border).astype("int")

        result = accuracy_score(y_true, y_pred)
        return {"accuracy": result}
