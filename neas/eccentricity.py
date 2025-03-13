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
    from numpy import maximum, sqrt, cos
    expression = 1 - ((T * a - 1)**2)/ ((4 * a**3)*cos(i)**2) 
    expression = maximum(expression, 0) 
    return sqrt(expression)