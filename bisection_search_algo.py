def bisection_search(L, t):
    low = 0  # Start index
    high = len(L) - 1  # End index
    
    while low <= high:  # Continue until low and high indices converge
        
        mid = (low + high) // 2  # Find the middle index
        
        if L[mid] == t:  # Target value found
            return mid
        elif L[mid] < t:  # Target is in the right half
            low = mid + 1

        else:  # Target is in the left half
            high = mid - 1

    # Target value not found
    return None


# Example usage
L = [1, 2, 3, 4, 5, 6]
t = 7
result = bisection_search(L, t)

if result is not None:
    print(f"Target {t} found at index {result}.")
else:
    print(f"Target {t} not found.")
