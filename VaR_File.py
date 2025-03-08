import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def VaR(r, confidence, principal = 1):
    alpha = 1 - confidence
    VaRThreshold = np.percentile(r, alpha * 100)
    out = principal * abs(VaRThreshold)

    return out

# Partial demonstration
def percent_var(r, confidence):
    # This function returns the left tail value and displays a histogram
    # r = a vector of stock percent returns
    # out = positively stated value of r at the 1-alpha percentile
    

    plt.hist(r, bins=50, alpha=0.75)
    plt.show()
    alpha = 1 - confidence
    out = np.percentile(r, alpha * 100)  # Calculate the percentile
    return abs(out)  # Return the absolute value of the calculated percentile

# Example tools: percentile
returns = np.random.normal(0, 1, 10000)
print(np.percentile(returns, 97.72))

# Unit test
r = np.random.normal(0.05, 0.03, 1000000)
probability2SD = norm.cdf(2)  # Probability under normal curve within 2 standard deviations

my_confidence = probability2SD
my_percent_var = percent_var(r, my_confidence )
print(np.round(my_percent_var, 2) == 0.01)
