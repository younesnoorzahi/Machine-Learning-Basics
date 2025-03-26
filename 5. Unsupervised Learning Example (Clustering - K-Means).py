from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Sample data
X = np.array([[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]])

# Apply K-Means (2 clusters)
kmeans = KMeans(n_clusters=2)
kmeans.fit(X)

# Get cluster labels
labels = kmeans.labels_
print("Cluster Labels:", labels)

# Visualize
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.show()
