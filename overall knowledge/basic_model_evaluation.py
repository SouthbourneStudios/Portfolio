import numpy as np
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

# -______________________________________________________________________________________

# METRICS FOR CLASSIFICATION:
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

# Recall:
# also known as Sensitivity or the True Positive Rate (TPR), addresses how completely a model identifies positive instances.

_Recall = _TP_count / (_TP_count + _TN_count)

# Prioritizing Recall is significant in situations where failing to identify a positive case (a False Negative) has serious consequences.
# It's important to understand that Recall focuses on finding all the actual positives,
#       whereas Precision focuses on ensuring that the instances the model predicts as positive are indeed positive.

# F1-SCORE:
# The F1-score is a way to combine precision and recall into a single metric.
# It's calculated as the harmonic mean of precision and recall.

_F1_Score = (2 * _Precision * _Recall) / (_Precision + _Recall)

# Like precision and recall, the F1-score ranges from 0 to 1.
# An F1-score of 1 represents perfect precision and recall.
# An F1-score of 0 means either precision or recall (or both) is zero.

# A higher F1-score indicates a better balance between precision and recall.

# -______________________________________________________________________________________

# METRICS FOR REGRESSION:
# Mean Absolute Error (MAE): Measures the average magnitude of the errors in a set of predictions, without considering their direction.
# Mean Squared Error (MSE): Measures the average of the squares of the errors. It gives higher weight to larger errors.
# Root Mean Squared Error (RMSE): The square root of the MSE, providing an error metric in the same units as the target variable.
# Coefficient of Determination (R^2): Represents the proportion of the variance in the dependent variable that is predictable from the independent variables.


# Prediction Error:
# This difference between the actual value and the predicted value is called the error or sometimes the residual.
_actual_value = 0
_predicted_value = 0
_Error =  _actual_value - _predicted_value

# A positive error means the model's prediction was too low. A negative error means the prediction was too high.
# An error of zero means the prediction was perfect for that specific instance.

# Mean Absolute Error (MAE):
# MAE tells you, on average, how far your predictions are from the true values,
# regardless of whether the prediction was too high or too low
def calculate_mae(y_true, y_pred):
    # Calculate the absolute differences between true and predicted values
    absolute_errors = np.abs(y_true - y_pred)
    # Calculate the mean of these absolute differences
    mae_value = np.mean(absolute_errors)
    return mae_value

# Actual (true) values
_y_true = np.array([3, -0.5, 2, 7])
# Predicted values
_y_pred = np.array([2.5, 0.0, 2, 8])

# Calculate MAE
mae = calculate_mae(_y_true, _y_pred)

# Lower is Better: A lower MAE generally indicates a better-fitting model,
# as predictions are, on average, closer to the actual values.
# An MAE of 0 would mean perfect predictions.

# Overall, MAE provides a clear, interpretable measure of average prediction error,
#       making it a valuable tool for understanding regression model performance,
#       especially when you prefer a metric less sensitive to outlier predictions or
#       when direct interpretability of the average error magnitude is most important.

# -______________________________________________________________________________________
# Mean Squared Error (MSE):
# Mean Squared Error calculates the average of the squared differences between the actual values and the predicted values.
# Eliminates Negative Values: Squaring ensures that all error contributions are positive.
# Penalizes Large Errors More: This is the most distinctive feature of MSE. Squaring gives disproportionately more weight to larger errors.

# MSE is useful when large errors are particularly undesirable.

# 1. Calculate the error for each prediction: y_true[x] - y_pred[x]
# 2. Square each error: list.append(error = (y_true[x] - y_pred[x])**2)
# 3. Sum up all the squared errors: sum(errors_list)
# 4. Divide by the number of predictions: sum_error / y_true.count()

# Calculate the squared differences, then the mean
_mse_value = np.mean((_y_true - _y_pred)**2)

# Sensitivity to Outliers: Due to the squaring, MSE is highly sensitive to outliers. A single prediction that is extremely far off the actual value can drastically inflate the MSE.

# Root Mean Squared Error (RMSE):
# It's simply the square root of the Mean Squared Error.

_rmse_value = np.sqrt(_mse_value)

# Like MSE, RMSE gives disproportionately high weight to large errors because the errors are squared before being averaged.
# A model that produces even a few predictions with very large errors
#       will have a significantly higher RMSE than a model with similar average error magnitude
#       but fewer extreme errors.
#
# Lower values of RMSE indicate a better fit of the model to the data.
# An RMSE of 0 means the model made perfect predictions for every observation in the dataset.

