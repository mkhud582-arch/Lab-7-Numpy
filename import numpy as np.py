# Install required package


# Import libraries
import numpy as np
from ucimlrepo import fetch_ucirepo

# Fetch the Auto MPG dataset
auto_mpg = fetch_ucirepo(id=9)

# Extract input features (X) and target variable (y)
X = auto_mpg.data.features
y = auto_mpg.data.targets

# Display dataset dimensions
print("\nFeatures shape:", X.shape)
print("Target shape:", y.shape)

# Display first five records
print("\nInput Features:")
print(X.head())

print("\nTarget Variable:")
print(y.head())


# ============================================================
# Task: Missing Values Analysis (Using NumPy)
# ============================================================

# Convert features to a NumPy array
data = X.to_numpy()


# Check whether there are missing values
#add your code here
print("Are there any missing values?", np.isnan(data).any())

# Count the total number of missing values
#add your code here
print("Total number of missing values:", np.isnan(data).sum())

# Find row and column indices of missing values
#add your code here
missing_indices = np.where(np.isnan(data))
print(missing_indices)
