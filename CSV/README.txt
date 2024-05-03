IMPORTANT:Since csv file is 192mb I did not include it the folder to make upload easier.

TASK1:
•Row 1-2: Import necessary libraries. NumPy is used for numerical operations, and time is used to measure runtime.

•Row 4-16: Define a class DataGenerator with two static methods to generate random and partially sorted datasets.
•Row 6-9: generate_random_dataset generates a randomly permuted dataset of the specified size.
•Row 11-15: generate_partially_sorted_dataset generates a partially sorted dataset with a given sorted percentage.
 
•Row 18-26: Define a class InsertionSort with a static method sort to perform the Insertion Sort algorithm.
•Row 20-25: Implement the Insertion Sort algorithm. 

•Row 29-43: Define a class MergeSort with a static method sort to perform the Merge Sort algorithm.
•Row 31-42: Implement the Merge Sort algorithm. 

•Row 46-53: Define a class PerformanceAnalyzer with a static method measure_runtime to measure the runtime of a sorting algorithm on a dataset.
•Row 49-52: Measure the runtime by sorting a copy of the dataset and calculating the time difference. 

•Row 57-59: Generate three datasets using the DataGenerator class.

•Row 62-68: Create an instance of InsertionSort and apply it to the three datasets.

•Row 71-77: Create an instance of MergeSort and apply it to the three datasets.

•Row 80-96: Create an instance of PerformanceAnalyzer and measure the runtime of Insertion Sort and Merge Sort on different datasets.

•Row 99-108: Display the runtime results for Insertion Sort and Merge Sort on different datasets.

TASK2:
1.self.df['profanity_count'] = self.df['Content'].apply(count_profanities)
  •This line creates a new column named 'profanity_count' in the DataFrame (self.df).
  •It uses the apply method to apply the count_profanities function to each element (sentence) in the 'Content' column.
  •The result is a count of profanities for each sentence, and these counts are stored in the 'profanity_count' column.

2.max_profanity_sentence = self.df.loc[self.df['profanity_count'].idxmax()]['Content']
  •self.df['profanity_count'].idxmax() finds the index of the row with the maximum value in the 'profanity_count' column.
  •self.df.loc[...] is used to locate the row with the maximum profanity count.
  •['Content'] extracts the 'Content' column of the row with the maximum profanity count.
  •The resulting max_profanity_sentence is the sentence with the highest number of profanities.

3.max_profanity_count = self.df['profanity_count'].max()
  •self.df['profanity_count'].max() finds the maximum value in the 'profanity_count' column, which represents the highest count of profanities in any sentence.
  •This value is stored in max_profanity_count.

4.print(f"Sentence with the highest number of profanities (Count: {max_profanity_count}):")
  •This line prints a formatted string indicating that the following line will display the sentence with the highest number of profanities.
  •{max_profanity_count} is replaced with the actual count.

5.print(max_profanity_sentence)
  •This line prints the sentence with the highest number of profanities.

