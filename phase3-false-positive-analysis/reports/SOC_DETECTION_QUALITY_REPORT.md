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

---

# SOC Detection Quality Assessment

## 1. Project Overview

This project evaluates SSH authentication telemetry,
false positives, and detection accuracy using Wazuh SIEM.

Environment:
- Ubuntu 26.04 LTS
- Wazuh Manager 4.14.9
- Oracle VirtualBox
- Python 3
- Wazuh Logtest

## 2. SSH Telemetry Analysis

Authentication log entries:

- Invalid username: 20
- Failed password: 23
- Successful login: 1

The counts represent log entries, not necessarily
unique authentication attempts.

## 3. Historical Detection Results

Historical Wazuh alerts:

- Rule 100100: 8 alerts
- Rule 5710: 42 alerts

## 4. Controlled Experiments

T01: Repeated malicious invalid-user attempts
Result: True Positive

T02: Password guessing against an existing username
Result: Detected by built-in rule 5760.
Custom rule 100100 was not observed.
This scenario is outside the custom rule's defined scope.

T03: Repeated benign username mistakes
Result: False Positive

T04: Single benign username mistake
Result: True Negative for custom rule 100100.

## 5. Key Findings

- Custom rule 100100 detected repeated invalid SSH usernames.
- Repeated benign username mistakes also triggered the rule.
- Built-in rule 5760 detected failed-password activity.
- Custom rule 100100 has limited SSH attack coverage.
- Detection thresholds require further evaluation.

## 6. Recommendations

1. Evaluate detection thresholds using more test cases.
2. Add coverage for password guessing against valid users.
3. Investigate legitimate authentication mistakes.
4. Test slow and distributed authentication attacks.
5. Monitor false positives after rule changes.
6. Preserve labeled test results for repeatable analysis.

## 7. Project Limitations

- Small synthetic dataset.
- Only three in-scope experiments.
- Manually labeled test scenarios.
- No production false-positive measurements.
- Limited SSH attack coverage.
- No comprehensive detection-latency analysis.

## 8. Visualizations

### Detection Metrics

![Detection Metrics](detection_metrics.svg)

### Confusion Matrix

![Confusion Matrix](confusion_matrix.svg)

## 9. Conclusion

This project demonstrates practical SOC detection
testing, SSH telemetry analysis, and evaluation
of false-positive behavior.

The results highlight why detection engineering
requires continuous testing and improvement.

The reported percentages describe controlled
synthetic scenarios, not production performance.
