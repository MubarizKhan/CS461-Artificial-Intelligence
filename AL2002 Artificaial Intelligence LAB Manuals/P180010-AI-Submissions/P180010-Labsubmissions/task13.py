import pandas as pd
import numpy as np


    
class NN:
    def __init__(self,learning_rate=0.01, n_iters=1000):
        self.lr = learning_rate
        self.n_iters = n_iters
        self.activation = self._unit_step_function
        self.weights = None
        self.bias = None 
    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        y = np.array([1 if i > 0 else 0 for i in y])
        for iterant in range(self.n_iters):
            for idx, x_i in enumerate(X):
                linear_output = np.dot(x_i, self.weights) + self.bias
                y_predicted = self.activation(linear_output)
                #Updating perceptron
                update = self.lr * (y[idx] - y_predicted)
                self.weights += update * x_i
                self.bias = update
    
    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        y_predicted = self.activation(linear_output)
        return y_predicted
    
    def _unit_step_function(self, x):
        return np.where(x>=0, 1, 0)
    
    
df = pd.read_csv('fruit_data_with_colors _1_.csv')

#missing values
print(df.head(100))
print(df.columns)

# df.replace([np.inf, -np.inf], np.nan).dropna(axis=1)
df.replace([np.inf, -np.inf], np.nan, inplace=True)
# Dropping all the rows with nan valuess
df.dropna(inplace=True)

mean_mass = df['mass'].mean()
df['mass'].fillna(mean_mass, inplace =True)
mean_height = df['height'].mean()
df['height'].fillna(mean_height, inplace=True)
#drop columns
df.drop(['fruit_name'], axis=1, inplace=True)
df.drop(['fruit_subtype'], axis=1, inplace=True)
# make labels binary because Perceptron is Binary Classification Model
for i in range(len(df)):
  if df['fruit_label'][i] == 2:
    df['fruit_label'][i] = 1
  elif df['fruit_label'][i] == 3 or df['fruit_label'][i] == 4:
    df['fruit_label'][i] = 0
    
    
    
p = NN()
# X = features/columns , y = labels
y = df['fruit_label']
df.drop(['fruit_label'], axis=1, inplace=True)
X = np.array(df)
p.fit(X, y)
p.predict(X)  
                