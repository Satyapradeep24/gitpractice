


import pandas as pd

# Load the datasets
train_path = "/Users/nukalapradeep/Downloads/Cleaned_BigMart_Train.csv"
test_path = "/Users/nukalapradeep/Downloads/Cleaned_BigMart_Test.csv"

train_df = pd.read_csv(train_path)
test_df = pd.read_csv(test_path)

# Checking dataset dimensions
train_shape = train_df.shape
test_shape = test_df.shape

# Getting dataset summary
train_info = train_df.info()
test_info = test_df.info()

# Statistical summary of numerical columns
train_summary = train_df.describe()
test_summary = test_df.describe()

# Checking missing values
train_missing = train_df.isnull().sum()
test_missing = test_df.isnull().sum()

(train_shape, test_shape, train_summary, test_summary, train_missing, test_missing)

import matplotlib.pyplot as plt
import seaborn as sns

# --- Univariate Analysis ---

# Histogram for target variable (Item_Outlet_Sales in train data)
plt.figure(figsize=(8, 5))
sns.histplot(train_df['Item_Outlet_Sales'], bins=50, kde=True, color="blue")
plt.title("Distribution of Item Outlet Sales")
plt.xlabel("Item Outlet Sales")
plt.ylabel("Frequency")
plt.show()

# Boxplot to check for outliers in numerical variables
plt.figure(figsize=(10, 5))
sns.boxplot(x=train_df['Item_Outlet_Sales'], color="green")
plt.title("Boxplot of Item Outlet Sales")
plt.show()

# --- Bivariate Analysis ---

# Scatter plot between Item MRP and Outlet Sales
plt.figure(figsize=(8, 5))
sns.scatterplot(x=train_df['Item_MRP'], y=train_df['Item_Outlet_Sales'], color="red")
plt.title("Item MRP vs. Item Outlet Sales")
plt.xlabel("Item MRP")
plt.ylabel("Item Outlet Sales")
plt.show()

# Correlation heatmap to check relationships
plt.figure(figsize=(10, 6))
sns.heatmap(train_df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

# --- Handling Missing Values ---

# Filling missing values in 'Item_Weight' with mean
train_df['Item_Weight'].fillna(train_df['Item_Weight'].mean(), inplace=True)
test_df['Item_Weight'].fillna(test_df['Item_Weight'].mean(), inplace=True)

# Filling missing values in 'Outlet_Size' with mode
train_df['Outlet_Size'].fillna(train_df['Outlet_Size'].mode()[0], inplace=True)
test_df['Outlet_Size'].fillna(test_df['Outlet_Size'].mode()[0], inplace=True)

# Verifying that missing values are handled
train_missing_after = train_df.isnull().sum()
test_missing_after = test_df.isnull().sum()

# --- Feature Engineering ---

# Creating a new feature: Price per Weight
train_df['Price_per_Weight'] = train_df['Item_MRP'] / train_df['Item_Weight']
test_df['Price_per_Weight'] = test_df['Item_MRP'] / test_df['Item_Weight']

# Encoding categorical variables using one-hot encoding
train_df = pd.get_dummies(train_df, columns=['Outlet_Type', 'Item_Fat_Content'], drop_first=True)
test_df = pd.get_dummies(test_df, columns=['Outlet_Type', 'Item_Fat_Content'], drop_first=True)

# Returning updated missing value status and sample of new features
(train_missing_after, test_missing_after, train_df.head())