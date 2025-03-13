def tisserand(a, T, i):
    """
    Gives the value of the eccentricity for a given semi-major axis and Tisserand parameter.

    parameters:
    a: semi-major axis
    T: Tisserand parameter
    i: inclination

    returns:
    eccentricity
    """
    from numpy import maximum, sqrt
    expression = 1 - 1 / (4 * a**3) * (T * a - 1)**2
    expression = maximum(expression, 0) 
    return sqrt(expression)