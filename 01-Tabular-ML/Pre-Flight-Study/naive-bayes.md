1. Naive Bayes (The Probability Shortcut)
The Core Idea: It uses pure probability (Bayes' Theorem) to answer: "Given these words, what is the probability this document belongs to Category A vs Category B?" It picks the category with the highest probability.

The "Naive" Assumption: It assumes that every word in the document is completely independent of every other word.
If the sentence is "Crypto market crashes," Naive Bayes pretends that the word "crypto" has absolutely no relationship to the word "market." We know this is linguistically false (hence "naive"), but this mathematical shortcut makes it lightning-fast and surprisingly effective for small datasets.

How it learns: It looks at every document in your training set and literally just counts how many times each word appears in each category.

Example for a Spam Filter: It learns that the word "Viagra" appears in 80% of spam emails, and 0% of non-spam emails. When a new email arrives, it multiplies all these probabilities together and spits out a final score.