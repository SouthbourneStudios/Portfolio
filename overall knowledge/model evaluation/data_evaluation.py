import numpy as np
# Overfitting:
# Overfitting occurs when a model learns the training data so well,
#       that it captures random fluctuations or noise specific to that data,
#       rather than the true underlying relationship between inputs and outputs.

# The true measure of a machine learning model's success isn't how well it performs on data it has already seen,
#       but how well it performs on new, unseen data.
#       This ability to perform well on data not used during training is called generalization.

# ----------------------------------------------------------------------

# Training Set:
# The training set is like that first set of flashcards you study from.
# It's the specific portion of your overall dataset that you feed directly into your machine learning algorithm.
# Its primary purpose is to allow the model to learn.

# For a classification task (like identifying spam emails),
#       the model learns which input features (words, sender addresses, etc.)
#       are associated with which category (spam or not spam).

# For a regression task (like predicting house prices),
#       the model learns how input features (square footage, number of bedrooms, location, etc.)
#       combine to estimate a numerical value (the price).

# Generally, the training set constitutes the larger fraction of your total data (common splits are 70% or 80% for training),
# as providing the model with more examples usually helps it learn more patterns.


# Test Set:
# The primary goal of the test set is to provide an unbiased assessment of the final model's performance on unseen data.
# It's fundamentally important to treat the test set as a final, one-time checkpoint.
# Should only use the test set to evaluate your model after you have finished all training and any tuning (like selecting model parameters).

#-----------------------------------------------------------

# Train-Test Split Procedure:
# 1. Start with Your Entire Labeled Dataset
# 2. Shuffle Your Data (Usually Recommended)
# 3. Choose a Split Ratio, Perform the Split
# 4. Keep the Test Set Separate:
#       This is a fundamentally important step. Once the split is done,
#       you should treat the test set like it doesn't exist until you have a final,
#       trained model ready for evaluation.

# Our feature data (Weight, Texture)
X = np.array([[150, 0], [170, 0], [140, 1], [130, 1], [160, 0],
              [180, 0], [125, 1], [135, 1], [190, 0], [145, 1]])

# Our label data (0=Apple, 1=Orange)
y = np.array([0, 0, 1, 1, 0, 0, 1, 1, 0, 1])

X_train, y_train = X[:7], y[:7] # 80%
X_test, y_test = X[7:], y[7:] # 20%

# -----------------------------------------------------------

# Cross-Validation Concept:
# Relying on a single train-test split can sometimes give a performance estimate that's overly optimistic or pessimistic.


# Imagine you have your dataset. Instead of splitting it into just two pieces (train and test),
#       you divide it into several equal parts, often called "folds".

# 1. Fold 1 as Test: Train the model on folds 2, 3, 4, and 5.
#       Then, evaluate the trained model using fold 1 as the test set.
#       Record the performance metric (like accuracy or MSE).

# 2. Fold 2 as Test: Discard the previous model. Train a new model from scratch using folds 1, 3, 4, and 5.
#       Evaluate this model using fold 2 as the test set.
#       Record the performance.

# 3. Fold 3 as Test: Repeat the process,
#       training on folds 1, 2, 4, and 5,
#       and testing on fold 3.
#       Record the performance.

# 4. Continue...: Repeat this until each fold has served as the test set exactly once.

# 5. Average: Calculate the average of the performance metrics recorded in each step.
#       This average score is a more reliable estimate of the model's performance on unseen data,
#       than the score from a single train-test split.

# By testing the model on multiple, independent subsets of the data, cross-validation significantly reduces the chance that your evaluation results are skewed by one particularly "lucky" or "unlucky" split.

# ----------------------------------------------------------------------------------------

# Common Mistakes in Basic Evaluation:
# 1. Evaluating on Training Data: This is perhaps the most fundamental error.
#
# 2. Leaking Data During Preprocessing:
#       Data leakage occurs when information from outside the training dataset is inadvertently used to create the model.
#       A common way this happens is during data preprocessing steps like scaling (e.g., standardization or normalization) or imputation (filling missing values).
#
#       Solution: Perform the train-test split first. Then, fit your preprocessors (like scalers or imputers) only on the training data.

# 3. Choosing the Wrong Metric: Understand the implications of different types of errors for your specific problem.

# 4. Misinterpreting Metric Values.
# 5. Relying on a Single Data Split