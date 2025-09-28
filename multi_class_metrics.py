# Evaluation Metrics from a Multi-Class Confusion Matrix
# Confusion Matrix:
#            Gold
# System |   Cat   Dog   Rabbit
#  Cat   |    5    10    5
#  Dog   |   15    20   10
# Rabbit |    0    15   10

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
    # per-class precision and recall
    precisions = []
    recalls = []
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

# Macro averages (simple mean)
macro_precision = per_class_precision.mean()
macro_recall = per_class_recall.mean()

# Micro averages (aggregate TP, FP, FN)
tp_total = np.trace(cm)
fp_total = cm.sum(axis=1).sum() - tp_total
fn_total = cm.sum(axis=0).sum() - tp_total
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
