import numpy as np
import pandas
import scipy
import matplotlib.pyplot as plt
import sys

def compute_r_squared(data, predictions):
    '''
    Given a list of original data points, and also a list of predicted data points,
    write a function that will compute and return the coefficient of determination (R^2)
    '''
    
    # your code here
    
    Sres = np.sum((data-predictions)**2)
    m = np.mean(data)
    Stot = np.sum((data-m)**2)
    r_squared = 1 - Sres/Stot
    return r_squared
    
def normalize_features(array):
   """
   Normalize the features in the data set.
   """
   array_normalized = (array-array.mean())/array.std()
   mu = array.mean()
   sigma = array.std()

   return array_normalized, mu, sigma

def compute_cost(features, values, theta):
    """
    Compute the cost function given a set of features / values, 
    and the values for our thetas.
    
    """
    
    m = len(values)
    sum_of_square_errors = np.square(np.dot(features, theta) - values).sum()
    cost = sum_of_square_errors / (2*m)

    return cost

def gradient_descent(features, values, theta, alpha, num_iterations):
    """
    Perform gradient descent given a data set with an arbitrary number of features.
    """

    # Write code here that performs num_iterations updates to the elements of theta.
    # times. Every time you compute the cost for a given list of thetas, append it 
    # to cost_history.
    # features = 1157 x 3, values = 1157 x 1, theta = 3 x 1
    
    m = len(values)
    cost_history = []
    sum_of_square_errors = np.square(np.dot(features, theta) - values).sum()
    
    for iIter in range(0, num_iterations):
        cost_history.append(compute_cost(features, values, theta))
        
        err = values - np.dot(features, theta) # 1157 x 1
        theta = theta + (alpha/(2*m))*np.dot(err, features)
    return theta, pandas.Series(cost_history)

def predictions(dataframe):
    '''
    Predicts rainy days using linear regression
    '''

    dummy_units = pandas.get_dummies(dataframe['UNIT'], prefix='unit')
    features = dataframe[['rain', 'Hour', 'meantempi']].join(dummy_units)
    #features = dataframe[['rain', 'precipi', 'Hour', 'meantempi']].join(dummy_units)
    values = dataframe[['ENTRIESn_hourly']]
    m = len(values)

    features, mu, sigma = normalize_features(features)

    features['ones'] = np.ones(m)
    features_array = np.array(features)
    values_array = np.array(values).flatten()

    #Set values for alpha, number of iterations.
    alpha = 0.5 # please feel free to change this value
    num_iterations = 75 # please feel free to change this value

    #Initialize theta, perform gradient descent
    theta_gradient_descent = np.zeros(len(features.columns))
    theta_gradient_descent, cost_history = gradient_descent(features_array, 
                                                            values_array, 
                                                            theta_gradient_descent, 
                                                            alpha, 
                                                            num_iterations)
    
    predictions = np.dot(features_array, theta_gradient_descent)
    print features_array
    return predictions

def plot_residuals(turnstile_weather, predictions):
    '''plot a histogram of residuals'''
    
    plt.figure()
    (turnstile_weather['ENTRIESn_hourly'] - predictions).hist(bins=70)
    return plt

turnstile_weather = pandas.read_csv('/home/khan/dev/data/turnstile_data_master_with_weather.csv')
p = predictions(turnstile_weather)
plot_residuals(turnstile_weather, p)
r = plot_residuals(turnstile_weather, p)
r.figure()
r.show()
data = turnstile_weather['ENTRIESn_hourly']
r2 = compute_r_squared(data, predictions)
print r2
