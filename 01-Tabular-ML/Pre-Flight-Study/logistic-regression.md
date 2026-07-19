2. Logistic Regression (The Weighted Voter)
The Core Idea: Instead of counting probabilities, it asks: "What is the weighted sum of all these words, and does that sum cross a certain decision line?"

How it learns: During training, it assigns a learned weight (coefficient) to every single word in your vocabulary.

Positive words get positive weights (pushing toward Category 1).

Negative words get negative weights (pushing toward Category 0).

Neutral words get weights near zero.

It adds up all those weights based on the words in your document, and then pushes that total sum through an S-curve (the Sigmoid function). This squashes the final number into a neat probability between 0% and 100%. If the probability is over 50%, it predicts Class 1; if under, Class 0.