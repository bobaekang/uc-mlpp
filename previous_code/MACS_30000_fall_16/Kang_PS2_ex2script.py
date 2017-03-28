'''
------------------------------------------------------------------------
This is Bobae's PS2:
The current script runs the codes only for exercises 2,
using the functions in written another script, ex2module.py.
------------------------------------------------------------------------
'''
import numpy as np
import ex2module as ex2m
# Declare your parameters
mean = np.log(70)
sd = 0.2

seed = 300
np.random.seed(seed)
# Then add your code generating 10,000 draws here.
scores = np.random.lognormal(mean, sd, 10000)


# Then run the scores through the function that performs
# three waves of eliminating outliers that are 3 standard
# deviations away from the mean.
scrubbed_scores = ex2m.threescrubs(scores)
print('The number of elements after applying threescrubs() is', scrubbed_scores.shape[0])
print('The mean of scrubbed_scores is', scrubbed_scores.mean())
print('The standard deviation of scrubbed_scores is', scrubbed_scores.std())
