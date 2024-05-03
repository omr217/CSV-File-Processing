import pandas as pd
from collections import Counter
import re

class HateSpeechAnalyzer:
    def __init__(self, file_path):
        self.df = self.load_dataset(file_path)

    def load_dataset(self, file_path):
        """Load the dataset from the given file path."""
        try:
            df = pd.read_csv(file_path)
            return df
        except FileNotFoundError:
            print(f"File not found at path: {file_path}")
            return None

    def explore_data(self):
        """Explore the dataset by printing the first 10 sentences along with their labels."""
        print("Available Columns:", self.df.columns)

        if 'Content' in self.df.columns:  # Adjusted column name
            # Display the first 10 rows
            print("First 10 rows of the dataset:")
            print(self.df.head(10))

            # Find the correct label column name and use it
            label_columns = [col for col in self.df.columns if 'Label' in col]
            if label_columns:
                label_column = label_columns[0]
                unique_labels = self.df[label_column].unique()
                print("\nUnique values in the label column:", unique_labels)
            else:
                print("\nLabel column not found in the DataFrame.")
        else:
            print("Column name 'Content' not found in the DataFrame.")

    def sort_and_search(self):
        """Sort the sentences based on their length in ascending order and print the longest and shortest sentences."""
        if 'Content' in self.df.columns:  # Change to 'Content' instead of 'Text'
            self.df['sentence_length'] = self.df['Content'].apply(len)
            sorted_df = self.df.sort_values(by='sentence_length')
            shortest_sentence = sorted_df.iloc[0]['Content']
            longest_sentence = sorted_df.iloc[-1]['Content']

            print("Shortest Sentence:", shortest_sentence)
            print("Longest Sentence:", longest_sentence)
            print("\n")
        else:
            print("Column name 'Content' not found in the DataFrame.")

    def frequency_analysis(self):
        """Perform frequency analysis by counting the occurrence of each unique word in the dataset."""
        if 'Content' in self.df.columns:
            def count_unique_words(sentence):
                words = re.findall(r'\b\w+\b', sentence.lower())
                return Counter(words)

            all_words_count = Counter()
            for sentence in self.df['Content']:
                all_words_count.update(count_unique_words(sentence))

            top_10_words = all_words_count.most_common(10)
            print("Top 10 Most Frequent Words:")
            for word, count in top_10_words:
                print(f"{word}: {count}")
            print("\n")
        else:
            print("Column name 'Content' not found in the DataFrame.")

    def profanity_detection(self):
        """Implement profanity detection and print the sentences with the highest number of profanities."""
        if 'Content' in self.df.columns:
            profanity_list = ["profanity1", "profanity2", "profanity3"]  # Add actual profanities

            def count_profanities(sentence):
                return sum(word in sentence.lower() for word in profanity_list)

            self.df['profanity_count'] = self.df['Content'].apply(count_profanities)

            max_profanity_sentence = self.df.loc[self.df['profanity_count'].idxmax()]['Content']
            max_profanity_count = self.df['profanity_count'].max()

            print(f"Sentence with the highest number of profanities (Count: {max_profanity_count}):")
            print(max_profanity_sentence)
        else:
            print("Column name 'Content' not found in the DataFrame.")


def main():
    file_path = 'HateSpeechDataset.csv'
    hate_speech_analyzer = HateSpeechAnalyzer(file_path)

    if hate_speech_analyzer.df is not None:
        # 1. Data Exploration
        hate_speech_analyzer.explore_data()

        # 2. Sorting and Searching
        hate_speech_analyzer.sort_and_search()

        # 3. Frequency Analysis
        hate_speech_analyzer.frequency_analysis()

        # 4. Profanity Detection
        hate_speech_analyzer.profanity_detection()

if __name__ == "__main__":
    main()
