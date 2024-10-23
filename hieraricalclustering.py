import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster  
import matplotlib.pyplot as plt

data = np.array([[85, 90], [80, 85], [75, 80], [60, 70], [90, 95]])

linked = linkage(data, 'ward')

plt.figure(figsize=(10, 7))
dendrogram(linked)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Data Points')
plt.ylabel('Distance')
plt.show()


num_clusters = 3 
df = pd.DataFrame(data, columns=['Feature 1', 'Feature 2']) 
df['Cluster'] = fcluster(linked, num_clusters, criterion='maxclust')

print("\nData with Cluster Assignments:")
print(df.head())

plt.figure(figsize=(10, 6))
plt.scatter(df['Feature 1'], df['Feature 2'], c=df['Cluster'], cmap='viridis')
plt.title('Clusters (Hierarchical Clustering)')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.colorbar(label='Cluster')
plt.show()
