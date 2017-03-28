'''
------------------------------------------------------------------------
This is Bobae's PS2:
The current script contains the codes only for exercises 2,
which will be used in another script, ex2script.py.
------------------------------------------------------------------------
'''
import numpy as np

# write a fuction kill_outliers()
def kill_outliers(arr):
    '''
    --------------------------------------------------------------------
    This function takes an one-dimensional array and deletes elements
    that are greater than 3 standard deviations above or below the mean.
    --------------------------------------------------------------------
    INPUTS:
    arr = an one-dimensional NumPy array

    OTHER FUNCTIONS AND FILES CALLED BY THIS FUNCTION: None

    OBJECTS CREATED WITHIN THIS FUNCTION:
    outcome = an one-dimensional NumPy array that has all elements of
        the input that are within 3 standard deviations from the mean

    FILES CREATED BY THIS FUNCTION: None

    RETURNS: outcome
    --------------------------------------------------------------------
    '''
    arr_standardized = (arr - arr.mean())/arr.std()
    outcome = arr[abs(arr_standardized) <= 3]
    return(outcome)

# write a function threescrubs()
def threescrubs(arr):
    '''
    --------------------------------------------------------------------
    This function takes an one-dimensional array and deletes elements
    that are greater than 3 standard deviations above or below the mean.
    --------------------------------------------------------------------
    INPUTS:
    arr = an one-dimensional NumPy array

    OTHER FUNCTIONS AND FILES CALLED BY THIS FUNCTION: kill_outliers()

    OBJECTS CREATED WITHIN THIS FUNCTION:
    outcome = an one-dimensional NumPy array results from applying
        kill_outliers() three times to the input array, arr.

    FILES CREATED BY THIS FUNCTION: None

    RETURNS: outcome
    --------------------------------------------------------------------
    '''
    outcome = kill_outliers(kill_outliers(kill_outliers(arr)))
    return(outcome)
