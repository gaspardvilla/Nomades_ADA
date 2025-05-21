# Enable ipympl backend
# %matplotlib widget

from sklearn.decomposition import PCA
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
import numpy as np

# Load the digits dataset
digits = load_digits()
print(f"Data shape: {digits.data.shape}")  # Debug info

# Perform PCA
pca = PCA(n_components=3)
pca_digits = pca.fit_transform(digits.data)
print("PCA transformation complete")  # Debug info

# Create 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Create the scatter plot
scatter = ax.scatter(
    pca_digits[:, 0], 
    pca_digits[:, 1], 
    pca_digits[:, 2], 
    c=digits.target, 
    cmap='tab10',
    edgecolor='k',
    alpha=0.7,
    s=40
)

# Add labels and title
ax.set_title("Interactive 3D PCA of Digits Dataset", pad=15)
ax.set_xlabel("1st Principal Component")
ax.set_ylabel("2nd Principal Component")
ax.set_zlabel("3rd Principal Component")

# Add colorbar
cbar = plt.colorbar(scatter, ax=ax, pad=0.1)
cbar.set_ticks(np.arange(10))
cbar.set_ticklabels([str(i) for i in range(10)])
cbar.set_label('Digit Class')

# Add grid
ax.grid(True, alpha=0.5)

plt.tight_layout()
plt.show()