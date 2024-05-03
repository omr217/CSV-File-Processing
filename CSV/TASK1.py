import numpy as np
import time

# Class for generating datasets
class DataGenerator:
    @staticmethod
    def generate_random_dataset(size):
        # Generate a randomly permuted dataset of specified size
        return np.random.permutation(np.arange(1, size + 1))

    @staticmethod
    def generate_partially_sorted_dataset(size, sorted_percentage):
        # Generate a partially sorted dataset with a given sorted percentage
        sorted_size = int(size * sorted_percentage)
        sorted_part = np.sort(np.random.choice(size, sorted_size, replace=False))
        random_part = np.setdiff1d(np.arange(size), sorted_part)
        return np.concatenate((sorted_part, random_part))

# Class for Insertion Sort algorithm
class InsertionSort:
    @staticmethod
    def sort(arr):
        # Implement the Insertion Sort algorithm
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

# Class for Merge Sort algorithm
class MergeSort:
    @staticmethod
    def sort(arr):
        # Implement the Merge Sort algorithm
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            MergeSort.sort(left_half)
            MergeSort.sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

# Class for measuring runtime performance
class PerformanceAnalyzer:
    @staticmethod
    def measure_runtime(sorting_algorithm, dataset):
        # Measure the runtime of a sorting algorithm on a dataset
        start_time = time.time()
        sorting_algorithm.sort(dataset.copy())
        return time.time() - start_time

# Data Generation
dataset_random = DataGenerator.generate_random_dataset(10000)
dataset_partially_sorted = DataGenerator.generate_partially_sorted_dataset(10000, 0.8)
dataset_nearly_sorted = DataGenerator.generate_partially_sorted_dataset(10000, 0.95)

# Insertion Sort
insertion_sort = InsertionSort()
insertion_sort.sort(dataset_random.copy())
insertion_sort.sort(dataset_partially_sorted.copy())
insertion_sort.sort(dataset_nearly_sorted.copy())

# Merge Sort
merge_sort = MergeSort()
merge_sort.sort(dataset_random.copy())
merge_sort.sort(dataset_partially_sorted.copy())
merge_sort.sort(dataset_nearly_sorted.copy())

# Comparative Analysis
analyzer = PerformanceAnalyzer()

# Measure runtime for Insertion Sort on different datasets
random_runtime_insertion = analyzer.measure_runtime(InsertionSort(), dataset_random)
partially_sorted_runtime_insertion = analyzer.measure_runtime(InsertionSort(), dataset_partially_sorted)
nearly_sorted_runtime_insertion = analyzer.measure_runtime(InsertionSort(), dataset_nearly_sorted)

# Measure runtime for Merge Sort on different datasets
random_runtime_merge = analyzer.measure_runtime(MergeSort(), dataset_random)
partially_sorted_runtime_merge = analyzer.measure_runtime(MergeSort(), dataset_partially_sorted)
nearly_sorted_runtime_merge = analyzer.measure_runtime(MergeSort(), dataset_nearly_sorted)

# Display results
print("Insertion Sort - Random Dataset: {:.6f} seconds".format(random_runtime_insertion))
print("Insertion Sort - Partially Sorted Dataset: {:.6f} seconds".format(partially_sorted_runtime_insertion))
print("Insertion Sort - Nearly Sorted Dataset: {:.6f} seconds".format(nearly_sorted_runtime_insertion))

print("\nMerge Sort - Random Dataset: {:.6f} seconds".format(random_runtime_merge))
print("Merge Sort - Partially Sorted Dataset: {:.6f} seconds".format(partially_sorted_runtime_merge))
print("Merge Sort - Nearly Sorted Dataset: {:.6f} seconds".format(nearly_sorted_runtime_merge))
