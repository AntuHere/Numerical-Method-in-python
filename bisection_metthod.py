def bisection_method(f, a, b, tolerance=1e-6, max_iterations=100):
    """
    Implements the Bisection Method to find the root of a continuous function.

    Parameters:
    - f: The function for which the root is to be found.
    - a: The starting point of the interval (lower bound).
    - b: The ending point of the interval (upper bound).
    - tolerance: The acceptable error (default: 1e-6).
    - max_iterations: The maximum number of iterations (default: 100).

    Returns:
    - The approximate root of the function.
    """
    # Check if the function has opposite signs at the endpoints of the interval
    # This ensures that a root exists within the interval by the Intermediate Value Theorem
    if f(a) * f(b) > 0:
        raise ValueError("The function must have opposite signs at a and b (f(a) * f(b) < 0).")

    # Iterate up to the maximum number of iterations or until the tolerance is met
    for i in range(max_iterations):
        # Calculate the midpoint of the current interval
        c = (a + b) / 2

        # Check if the midpoint is a root or if the interval is sufficiently small
        # If f(c) == 0, we found the root exactly; if (b - a) / 2 < tolerance, stop iterating
        if f(c) == 0 or (b - a) / 2 < tolerance:
            return c  # Return the root

        # Determine which subinterval contains the root
        # If f(c) has the same sign as f(a), update the lower bound to c
        elif f(c) < 0:
            a = c  # Root lies in the interval [c, b]
        else:
            b = c  # Root lies in the interval [a, c]

    # If the method does not converge within max_iterations, return the midpoint
    # This is the best approximation we have
    return (a + b) / 2

# Example usage of the bisection method
if __name__ == "__main__":
    # Define the function to find the root of
    f = lambda x: x**3 - 4*x - 9  # Example function: x^3 - 4x - 9

    # Define the interval where the root is expected
    a, b = 2, 3

    # Call the bisection method and compute the root
    root = bisection_method(f, a, b)

    # Print the result
    # Display the approximate root found by the method
    print(f"The root is approximately: {root:.6f}")


    