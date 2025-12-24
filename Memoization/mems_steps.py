import time


def time_it(func, *args):
    """
    Measure how long a function takes to run.
    """
    start = time.time()
    result = func(*args)
    end = time.time()
    print(f"Result: {result}")
    print(f"Time taken: {end - start:.6f} seconds\n")


# --------------------------------------------------
# Naive recursive version (NO memoization)
# --------------------------------------------------


def step_count(n, steps):
    """
    Count the number of ways to climb n steps
    using allowed step sizes in 'steps'.
    This is the slow, naive recursive version.
    """
    # Successful path
    if n == 0:
        return 1

    # Overshot the bottom
    if n < 0:
        return 0

    # Recursive expansion
    return sum(step_count(n - s, steps) for s in steps)


# --------------------------------------------------
# Memoized version (WITH caching)
# --------------------------------------------------


def memsteps(n, steps):
    """
    Wrapper that creates the cache and starts recursion.
    """
    cache = {}
    return memsteps_cache(n, steps, cache)


def memsteps_cache(n, steps, cache):
    """
    Recursive step counter using memoization.
    """
    # Successful path
    if n == 0:
        return 1

    # Overshot the bottom
    if n < 0:
        return 0

    # Return cached result if we have it
    if n in cache:
        return cache[n]

    # Compute, cache, and return result
    total = sum(memsteps_cache(n - s, steps, cache) for s in steps)
    cache[n] = total
    return total


# --------------------------------------------------
# Main program
# --------------------------------------------------

if __name__ == "__main__":
    steps = [1, 3, 5]

    print("Naive recursive version:")
    time_it(step_count, 10, steps)
    # WARNING: uncommenting the next line will be very slow
    # time_it(step_count, 35, steps)

    print("Memoized version:")  
    time_it(memsteps, 10, steps)
    time_it(memsteps, 35, steps)
    time_it(memsteps, 100, steps)
