from sklearn.datasets.samples_generator import make_blobs
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

centers=[[-2,2],[2,2],[0,4]]

X,y = make_blobs(n_samples=60, centers=centers,
                 random_state=0, cluster_std=0.60)
print(X)
print("y:")
print(y)

k = 5
clf = KNeighborsClassifier(n_neighbors=k)
clf.fit(X, y)
X_sample = [[0,2]]
y_sample = clf.predict(X_sample)
neighbors = clf.kneighbors(X_sample, return_distance=False)

print("neighbors: \n")
print(neighbors)

for i in neighbors:
    print(y[i])