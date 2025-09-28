# Multi-Class Evaluation Metrics

**Name:** Deepthi Nalla  
**ID:** 700779838

This project demonstrates how to compute **precision** and **recall** metrics
for each class in a multi-class classification problem and how to calculate
macro-averaged and micro-averaged scores.

## Files
* `multi_class_metrics.py` – Python script that computes:
  - Per-class precision and recall
  - Macro-averaged precision and recall
  - Micro-averaged precision and recall

## Problem Setup
We have a 3-class classification (Cat, Dog, Rabbit) where the confusion matrix is:

| System \ Gold | Cat | Dog | Rabbit |
|---------------|-----|-----|--------|
| Cat           |  5  | 10  |   5    |
| Dog           | 15  | 20  |  10    |
| Rabbit        |  0  | 15  |  10    |

- Rows represent the **predicted** labels by the system.
- Columns represent the **true (gold)** labels.

Total samples = 90.

## How to Run
1. Make sure you have Python 3 installed.
2. Save this file or the code section below as `multi_class_metrics.py`.
3. In a terminal or command prompt, run:

   ```bash
   python multi_class_metrics.py
   ```

4. The script will print:
   - Precision and recall for each class (Cat, Dog, Rabbit)
   - Macro-averaged precision and recall
   - Micro-averaged precision and recall
   - A short explanation of macro vs. micro averaging

## Python Code
```python
import numpy as np

# Confusion matrix as a 2D NumPy array
# Rows = system predictions, Columns = gold/true labels
cm = np.array([
    [5, 10, 5],
    [15, 20, 10],
    [0, 15, 10]
])

classes = ["Cat", "Dog", "Rabbit"]

def precision_recall(cm):
    precisions, recalls = [], []
    for i in range(len(classes)):
        tp = cm[i, i]
        fp = cm[i, :].sum() - tp
        fn = cm[:, i].sum() - tp
        prec = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        rec = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        precisions.append(prec)
        recalls.append(rec)
    return np.array(precisions), np.array(recalls)

per_class_precision, per_class_recall = precision_recall(cm)

# Macro averages
macro_precision = per_class_precision.mean()
macro_recall = per_class_recall.mean()

# Micro averages
tp_total = np.trace(cm)
fp_total = cm.sum() - tp_total
fn_total = cm.sum() - tp_total
micro_precision = tp_total / (tp_total + fp_total)
micro_recall = tp_total / (tp_total + fn_total)

print("Per-Class Precision and Recall:")
for c, p, r in zip(classes, per_class_precision, per_class_recall):
    print(f"  {c}: precision={p:.3f}, recall={r:.3f}")

print("\nMacro-averaged:")
print(f"  Precision={macro_precision:.3f}, Recall={macro_recall:.3f}")

print("\nMicro-averaged:")
print(f"  Precision={micro_precision:.3f}, Recall={micro_recall:.3f}")

print("\nInterpretation:")
print("  - Macro average gives equal weight to each class regardless of support.")
print("  - Micro average aggregates over all decisions, weighting by class frequency.")
```

## Key Concepts
* **Precision** for class X: TP / (TP + FP)
* **Recall** for class X: TP / (TP + FN)
* **Macro average**: Unweighted mean across classes (treats all classes equally).
* **Micro average**: Aggregates total TP, FP, FN across classes (weights by class frequency).

This example illustrates how macro scores highlight per-class performance,
while micro scores reflect overall system accuracy weighted by class size.
