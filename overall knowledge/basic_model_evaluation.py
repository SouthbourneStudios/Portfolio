# The primary goal of evaluation metrics is to quantify model performance:
#  1. Objectivity: Metrics provide an unbiased assessment.
#  2. Comparison: Once we have numerical scores, we can directly compare different models.
#  3. Optimization: Metrics guide the model development process.
#       Low scores on certain metrics might indicate problems like underfitting (the model is too simple),
#       or overfitting (the model learned the training data too specifically and doesn't generalize).

#  4. Communication: Metrics provide a standard language for discussing model performance.

# TYPES:
# It's important to understand that different types of problems (like classification vs. regression) require different types of metrics.

# The goal of a classification model is to learn a mapping from input features (characteristics of the data) to specific output labels,
#   often called classes. These labels represent discrete, distinct categories.

#   1. Image Recognition: A model analyzes an image and classifies it based on its content,
#       such as identifying whether a picture contains a cat, a dog, or a bird.

#   2. Sentiment Analysis: Analyzing a piece of text (like a product review)
#       to classify the sentiment expressed as positive, negative, or neutral.


# Regression predicts a continuous numerical value.
# Think of it as predicting "how much" or "how many" rather than "what kind".

# This difference means we need entirely different ways to measure how well our regression models are performing compared to classification models.

# Ground Truth vs prediction:
#   The core idea of evaluation is to compare the model's final predictions against the actual,
#   known labels, often called the ground truth.


# Accuracy: A Simple First Metric:
#   Accuracy measures the overall correctness of the model.
#   It tells us the proportion of predictions that the model classified correctly out of the total number of predictions made.

_Total_Predictions = 10
_Correct_Predictions = 5
_Accuracy = _Correct_Predictions / _Total_Predictions

# Accuracy scores range from 0 (meaning the model got every prediction wrong) to 1 (meaning the model got every prediction right).
#   1. While accuracy gives us a quick summary of overall correctness,
#       it can sometimes paint an overly optimistic or even misleading picture of a model's performance.
#   2. This often happens when dealing with imbalanced datasets.


# An Imbalanced Dataset
# 1. An imbalanced dataset is one where the number of observations belonging to one class is significantly lower than those belonging to the other classes.
# 2. In these situations, one class (the "majority" class, like healthy patients or legitimate transactions)
#       greatly outnumbers the other (the "minority" class, like sick patients or fraudulent transactions).

# TP, FP, TN, FN:
#   True Positives (TP), These are the cases where the model correctly predicts the positive class.
#       Actual: Positive
#       Predicted: Positive
#       Example: An email that is spam is correctly identified as spam by the filter.

# False Positives (FP), These are the cases where the model incorrectly predicts the positive class when the actual class is negative.
#                       This is sometimes called a "Type I Error".
#       Actual: Negative
#       Predicted: Positive
#       Example: An important email that is not spam is incorrectly identified as spam and perhaps sent to the junk folder.

# True Negatives (TN), These are the cases where the model correctly predicts the negative class.
#       Actual: Negative
#       Predicted: Negative
#       Example: An email that is not spam is correctly identified as not spam.

# False Negatives (FN), These are the cases where the model incorrectly predicts the negative class when the actual class is positive.
#                      This is sometimes called a "Type II Error".
#       Actual: Positive
#       Predicted: Negative
#       Example: An email that is spam is incorrectly identified as not spam and lands in the inbox.
#       Understanding the Outcomes

_TP_count = 0
_FP_count = 0
_TN_count = 0
_FN_count = 0

_Accuracy = (_TP_count + _TN_count) / (_TP_count + _FP_count + _TN_count + _FN_count)

# Precision metric:
# Precision answers the question: Out of all the instances the model predicted to be positive,
#   what fraction were actually positive?

_Precision = _TP_count / (_TP_count + _FP_count)

# High precision is particularly desirable when the cost of a False Positive is high.

