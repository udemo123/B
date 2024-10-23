import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans  
from sklearn.preprocessing import StandardScaler 

data = {
    'GPA': [3.5, 3.8, 2.9, 3.2, 3.6, 3.0, 3.9, 2.7, 3.1, 3.4],
    'Study Hours': [15, 20, 5, 10, 18, 12, 25, 4, 8, 14],
    'Extracurricular Activities': [2, 3, 1, 2, 4, 1, 5, 0, 1, 3]
}
df = pd.DataFrame(data)

scaler = StandardScaler() 
scaled_data = scaler.fit_transform(df)  
k = 3

kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(scaled_data)

df['Cluster'] = kmeans.labels_
print(df)

plt.scatter(df['GPA'], df['Study Hours'], c=df['Cluster'], cmap='viridis')
plt.xlabel('GPA')
plt.ylabel('Study Hours')
plt.title('K-Means Clustering of University Students')
plt.show()
