# 🧠 Data Analysis & Algorithm Performance Toolkit

This Python project is a combination of two main components:

1. **Sorting Algorithm Performance Comparison**  
2. **Hate Speech Dataset Analysis Tool**

---

## 📌 Part 1: Sorting Algorithm Performance Comparison

### ✅ Features
- Implements **Insertion Sort** and **Merge Sort**.
- Generates datasets of various types:
  - Random
  - Partially Sorted
  - Nearly Sorted
- Measures and compares the runtime of both algorithms on these datasets.

### 🧪 Dataset Generation

```python
dataset_random = DataGenerator.generate_random_dataset(10000)
dataset_partially_sorted = DataGenerator.generate_partially_sorted_dataset(10000, 0.8)
dataset_nearly_sorted = DataGenerator.generate_partially_sorted_dataset(10000, 0.95) 
```

#### 📌 Part 2: Hate Speech Dataset Analysis
This part focuses on analyzing a labeled text dataset for potential hate speech using basic natural language processing techniques.

✅ Features
Load and preview the dataset

Identify shortest and longest sentences

Perform frequency analysis of the most common words

Detect potential profanity (customizable list)

##### 📁 Expected CSV Format
Ensure your dataset (e.g., HateSpeechDataset.csv) includes a Content column with text data and a label column (e.g., Label, Category, etc.).

📊 Functional Overview
1. Data Exploration
Prints:

Available columns

First 10 rows

Unique labels (if any)

2. Sorting & Searching
Identifies:

Shortest sentence

Longest sentence

3. Frequency Analysis
Finds:

Top 10 most frequently used words (case-insensitive, tokenized)

4. Profanity Detection
Scans for specified profane words and highlights the sentence with the highest count.

###### 🧰 Project Structure
.
├── your_script.py
├── HateSpeechDataset.csv
└── README.md
