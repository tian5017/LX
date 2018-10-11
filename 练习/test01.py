import mglearn
import matplotlib.pyplot as plt

X, y = mglearn.datasets.make_forge()
print(X)
print(y)

mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
plt.legend(["Class0", "Class1"], loc=4)
plt.xlabel("First Feature")
plt.ylabel("Second Feature")
print(X.shape)
plt.show()
