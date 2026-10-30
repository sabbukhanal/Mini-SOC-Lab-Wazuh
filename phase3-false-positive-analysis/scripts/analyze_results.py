import csv
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
DATA = BASE / "datasets" / "experiment_results.csv"
REPORT = BASE / "reports" / "detection_accuracy.md"

with open(DATA, newline="") as f:
    records = list(csv.DictReader(f))

tests = [r for r in records if r["in_scope"] == "1"]

tp = fp = fn = tn = 0

for test in tests:
    actual = int(test["malicious"])
    detected = int(test["rule_100100"])

    if actual == 1 and detected == 1:
        tp += 1
    elif actual == 0 and detected == 1:
        fp += 1
    elif actual == 1 and detected == 0:
        fn += 1
    else:
        tn += 1

def percentage(numerator, denominator):
    if denominator == 0:
        return "N/A"
    return f"{numerator / denominator * 100:.2f}%"

precision = percentage(tp, tp + fp)
recall = percentage(tp, tp + fn)
fpr = percentage(fp, fp + tn)

print("\n====================================")
print(" WAZUH DETECTION ACCURACY ANALYSIS")
print("====================================")
print(f"Total experiments: {len(records)}")
print(f"In-scope experiments: {len(tests)}")
print(f"True Positives: {tp}")
print(f"False Positives: {fp}")
print(f"False Negatives: {fn}")
print(f"True Negatives: {tn}")
print("------------------------------------")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"False Positive Rate: {fpr}")
print("====================================")

report = f"""# Wazuh Detection Accuracy Report

## Detection Rule

Rule ID: 100100

Detection: Repeated invalid SSH username attempts.

MITRE ATT&CK: T1110 - Brute Force

## Experimental Results

| Metric | Result |
|---|---|
| Total experiments | {len(records)} |
| In-scope experiments | {len(tests)} |
| True Positives | {tp} |
| False Positives | {fp} |
| False Negatives | {fn} |
| True Negatives | {tn} |
| Precision | {precision} |
| Recall | {recall} |
| False Positive Rate | {fpr} |

## Coverage Gap

Password guessing against an existing SSH username
was detected by built-in Wazuh rule 5760 in the
observed test output, but custom rule 100100 was
not observed.

This scenario is excluded from the custom-rule
accuracy calculation because it is outside the
rule's intended invalid-username detection scope.

## Limitations

These results come from three in-scope synthetic
Logtest scenarios, not production authentication traffic.

They demonstrate specific detection behaviors.
The percentages are not estimates of real-world
SOC detection accuracy or false-positive prevalence.

The results depend on the manually recorded test
outcomes and scenario ground-truth labels.
"""

REPORT.write_text(report)

print(f"\nReport saved to: {REPORT}")
