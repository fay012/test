import numpy as np
def mean(X):
    result = np.mean(X)
    return round(result,3)

def median(X):
    result = np.median(X)
    return round(result,3)

def std(X):
    return round(np.std(X),3)

def Max(X):
    return round(np.max(X),3)

def Min(X):
    return round(np.min(X),3)

def quartile(X):
    return round(np.percentile(X,25),3),round(np.percentile(X,50),3),round(np.percentile(X,75),3)


