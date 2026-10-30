# Wazuh Detection Accuracy Report

## Detection Rule

Rule ID: 100100

Detection: Repeated invalid SSH username attempts.

MITRE ATT&CK: T1110 - Brute Force

## Experimental Results

| Metric | Result |
|---|---|
| Total experiments | 4 |
| In-scope experiments | 3 |
| True Positives | 1 |
| False Positives | 1 |
| False Negatives | 0 |
| True Negatives | 1 |
| Precision | 50.00% |
| Recall | 100.00% |
| False Positive Rate | 50.00% |

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
