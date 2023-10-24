# Frequent Pattern Mining Project

## Introduction

Welcome to the Frequent Pattern Mining Project! This project is designed to help you learn and implement the concepts of Frequent Pattern Mining using a real-time dataset. Frequent Pattern Mining is a fundamental data mining technique used to discover recurring patterns in large datasets.This project explores the theory behind frequent pattern mining and apply it to a real-world dataset to gain practical experience.

## Objective

Core concepts of Frequent Pattern Mining and guide you through the process of implementing these concepts on a real-time dataset. By the end of this project, you should be able to:

- Understand the fundamental principles of Frequent Pattern Mining.
- Implement frequent itemset mining algorithms such as Apriori or FP-growth.
- Apply these algorithms to a real dataset to discover frequent patterns.
- Gain insights from the discovered patterns and understand their practical applications.

## Getting Started

Before you begin, make sure you have the necessary tools and resources in place:

- Programming Language: You will need a programming language such as Python to implement the Frequent Pattern Mining algorithms.
- Dataset: A real-time dataset is used for this project, on which Frequent Pattern Mining is done.

## Files 

1. **exec.ipynb** : Contains the Jupyter Notebook of the project. Open the notebook in Google Colab or Jupyter Notebook. Run every cell sequentially for desired output. 
2. **exec.py** : Contains the .py file of the project. Execute the file on any IDE
3. **patterns_1.txt** : Output all the length-1 frequent categories (item sets) with their  absolute supports in the descending order of their support count.
4. **patterns_all.txt** : All the frequent category sets along with their absolute supports in the descending order of their support count, into a text file named.
5. **categories.txt** : The dataset (“categories.txt”) in this folder consists of the category lists of 77,185 places in the United States.Each line corresponds to the category list of one place, where the list consists of a number of category instances (e.g., hotels, restaurants, etc.) that are separated by semicolons.

## Implementation

To get started with the implementation, follow these steps:

1. **Data Preparation**: Load and preprocess your dataset. Ensure it is in a suitable format for analysis. Make required changes for the text dataset so that we extract the set of unique labels. Find the frequency of labels and print them on different .txt file.

2. **Algorithm Selection**:In this project we have used Apriori algorithm.

3. **Coding**: The code for Apriori algorithm is written. Two functions - generate_candidate_itemsets and prune_candidate_itemsets are used for the self join and pruning steps respectively.

4. **Mining Frequent Patterns**: Run the algorithm on the dataset to discover frequent patterns. The support we have used here is 0.01, that is 771.

5. **Conclusion**: After implementing the Apriori algorithm with a minimum support threshold of 0.01 (or 1% relative support), you were able to mine frequent category sets from the dataset of 77,185 category lists. The analysis likely resulted in a collection of category sets that occur frequently together.

Happy mining! 👷‍♂️📊🕵‍♀️