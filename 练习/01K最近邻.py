from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


iris_data = load_iris()
# print(iris_data)
X_train, X_test, y_train, y_test = train_test_split(iris_data["data"], iris_data["target"], random_state=0)

iris_df = pd.DataFrame(X_train, columns=iris_data.feature_names)
pd.scatter_matrix(iris_df, c=y_train, figsize=(15, 15), marker='o', hist_kwds={'bins': 20}, s=60, alpha=.8)
plt.show()

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)
print(y_pred)
print(y_test)
print(y_pred == y_test)
print(np.mean(y_pred == y_test))