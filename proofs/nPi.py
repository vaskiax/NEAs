def nPi()-> None:
    """
    This function provides a latex representation of the proof of a set of specific conditions 
    to be met by minor solar system body to be categorized as a Near Earth Asteroid (NEA). 

    The set of conditions here corresponds to the relation between the interception points of the 
    semi-major axis of the orbit of the NEA and the ones of the Earth's orbit.

    
    inputs: None

    outputs: None

    """
    from IPython.display import display, Markdown
    
    full_text = r"""
                Let $Q_{NEA}$ be the afelion and $q_{NEA}$ the perihelion distances, while $Q_{E}$ and $q_{E}$ are the afelion and perihelion distances of the Earth, respectively.

                These numbers are solutions to the equation $r(n) = \frac{a(1-e^{2})}{1+e\cos(n\pi)}$, where $a$ is the semi-major axis, $e$ the eccentricity, for $n \in \{0,1\}$.

                Hence, for n = 0, the perihelion distance for $q_{NEA}$ and $q_{E}$ is $q_{NEA} = a(1-e)$ and $q_{E} = a_{E}(1-e_{E})$, where $a_{E}$ and $e_{E}$ are the semi-major axis and eccentricity of the Earth's orbit.

                Similarly, for n = 1, the afelion distance for $Q_{NEA}$ and $Q_{E}$ is $Q_{NEA} = a(1+e)$ and $Q_{E} = a_{E}(1+e_{E})$.

                Since the condition for a minor solar system body to be classified as a NEA implies that the body's orbit must have an interception point with the Earth's orbit, which necessarily means that the perihelion and afelion distances of the body serve as lower and upper bounds for the semi-major axis of the asteroid's orbit.

                So, the condition for a minor solar system body to be classified as a NEA is given by the inequality: $q_{NEA} < r_{E} < Q_{NEA}$, where $r_{E}$ is the semi-major axis of the Earth's orbit.

                However, Earth's orbit is not circular, so it has its own intrinsic bounds for the semi-major axis, which are given by the inequality: $q_{E} \leq r_{E} \leq Q_{E}$.

                Then, what is needed is that the interception between these two intervals is not empty, and such a condition is met when the inequality $\max(q_{NEA}, q_{E}) \leq \min(Q_{NEA}, Q_{E})$ is satisfied.

                Applied for the asteroid case, its afelion distance is, in general, greater than the Earth's afelion distance. Hence, for an interception to happen, the Earth's afelion distance must be greater than the asteroid's perihelion distance. Otherwise, the asteroid's greatest approach to the sun would never reach the interior of the Earth's orbit.

                Thus, the condition for a minor solar system body to be classified as a NEA is given by the inequality: $q_{NEA} < Q_{E}$.

                Similarly, for the less common case where the asteroid's afelion distance is less than the Earth's afelion distance, the inequality is reversed, leading to the condition: $Q_{NEA} > q_{E}$. Hence, arriving at the relations that must be met.
                """

    return(Markdown(full_text))