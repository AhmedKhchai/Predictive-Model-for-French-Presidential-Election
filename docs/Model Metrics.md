### Metrics in Classification Report

#### 1. Precision

**Precision** answers the question, "What proportion of identified positives are actually positive?"

\[
\text{Precision} = \frac{\text{True Positive}}{\text{True Positive} + \text{False Positive}}
\]

- **True Positive (TP)**: The number of correct predictions that the instances are positive.
- **False Positive (FP)**: The number of incorrect predictions that the instances are positive.

High precision indicates that false positives are low.

#### 2. Recall (Sensitivity)

**Recall** answers the question, "What proportion of actual positives are correctly classified?"

\[
\text{Recall} = \frac{\text{True Positive}}{\text{True Positive} + \text{False Negative}}
\]

- **False Negative (FN)**: The number of incorrect predictions that the instances are negative.

High recall means most of the positive instances have been captured by the model.

#### 3. F1-Score

The **F1-Score** is the harmonic mean of precision and recall and provides a single score that balances both the
concerns of precision and recall in one number.

\[
\text{F1-Score} = 2 \times \left( \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} \right)
\]

A perfect F1-Score would be 1, and the worst would be 0. It is a good way to show that a class is well-suited for both
precision and recall.

#### 4. Support

**Support** is the number of actual occurrences of the class in the specified dataset. Imbalanced support in the
training data may indicate structural weaknesses in the reported scores of the classifier.

#### 5. Macro Avg

The **Macro Avg** takes the average of the metric (be it precision, recall, or F1-score) across all classes. It doesn't
consider class imbalance.

#### 6. Weighted Avg

The **Weighted Avg** calculates metrics for each label and finds their average weighted by the number of true instances
for each label. This alters the metric to account for label imbalance.

### Overall

- **Accuracy**: This is simply the ratio of the correctly predicted observation to the total observations.

\[
\text{Accuracy} = \frac{\text{True Positive} + \text{True Negative}}{\text{Total Observations}}
\]

While accuracy can be a useful initial glance at the quality of a model, it can be misleading if the classes are
imbalanced.

Would you like to dive deeper into any of these metrics?