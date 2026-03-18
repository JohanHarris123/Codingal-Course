"""
Calculate the probability of observing 12 or more days of rain in the next 30 days when we expected 10 Also, 
calculate the probability of observing between 12 and 18 days of rain.
"""

import scipy.stats as stats
prob1 = 1 - stats.poisson.cdf