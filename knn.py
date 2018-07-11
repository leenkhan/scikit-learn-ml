from sklearn.datasets.samples_generator import make_blobs
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import matplotlib.pyplot as plt

centers=[[-2,2],[2,2],[0,4]]

X,y = make_blobs(n_samples=60, centers=centers,
                 random_state=0, cluster_std=0.60)
print(X)
print("y: \n")
print(y)

plt.figure(figsize=(16, 10), dpi=72)
c = np.array(centers)
plt.scatter(X[:, 0], X[:, 1], c=y, s=100, cmap='cool')
plt.scatter(c[:, 0], c[:, 1], s=100, marker='^', c='r')
plt.show()

k = 5
clf = KNeighborsClassifier(n_neighbors=k)
clf.fit(X, y)
X_sample = np.array([0, 2])
y_sample = clf.predict(X_sample)
neighbors = clf.kneighbors(X_sample, return_distance=False)

print("neighbors: \n")
print(neighbors)