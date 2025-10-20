import random
import time
import tracemalloc

# Quick Sort Implementation
def quick_sort_deterministic(A):  # Deterministic Version of Quicksort where middle element is choosen as pivot
    if len(A) <= 1:
        return A
    pivot = A[len(A) // 2]   # Picking the middle element as pivot
    left = [x for x in A if x < pivot]
    middle = [x for x in A if x == pivot]
    right = [x for x in A if x > pivot]

    return quick_sort_deterministic(left) + middle + quick_sort_deterministic(right)

def quick_sort_randomized(A):  # Randomized Version of Quciksort where pivot element is picked in random
    if len(A) <= 1:
        return A
    pivot = random.choice(A) #Picking the pivot element in random
    left = [x for x in A if x < pivot]
    middle = [x for x in A if x == pivot]
    right = [x for x in A if x > pivot]

    return quick_sort_randomized(left) + middle + quick_sort_randomized(right)

# Function to test running time 
def test_performance(data, description, func):
    tracemalloc.start()
    start = time.perf_counter()
    _ = func(data)
    end = time.perf_counter()
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    # Printing the running time of Deterministic and randomized Quicksort on different input sizes and distributions
    print(f"{func.__name__:} | {description:} | " f"Running time: {end - start:>8.6f} s")


if __name__ == "__main__":
    random.seed(42)                       
    sizes = [500, 1000, 2000]            # Various Input sizes for testing
    dists = ("Sorted", "Reverse Sorted", "Random")

    for n in sizes:
        print("="*64)
        print(f"For Input size n = {n}")
        

        sorted_data  = list(range(n))
        reverse_data = list(range(n, 0, -1))
        random_data  = random.sample(range(1, n*2), n)

        # Running the test
        test_performance(sorted_data,  "Sorted",quick_sort_deterministic)
        test_performance(reverse_data, "Reverse Sorted",quick_sort_deterministic)
        test_performance(random_data,  "Random",quick_sort_deterministic)


        test_performance(sorted_data,  "Sorted",quick_sort_randomized)
        test_performance(reverse_data, "Reverse Sorted",quick_sort_randomized)
        test_performance(random_data,  "Random",quick_sort_randomized)