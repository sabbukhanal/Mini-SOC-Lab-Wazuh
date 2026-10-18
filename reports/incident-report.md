# Mini SOC Lab — SSH Brute-Force Incident Report

## 1. Incident Overview

Incident Type: Controlled SSH Brute-Force Simulation

Date: October 18, 2026

Affected Host: sabhyata-VirtualBox

Operating System: Ubuntu Linux

Monitoring Platform: Wazuh

Source IP: 127.0.0.1

Attempted Username: fakeuser

Severity: High (Level 10)

Detection Rule: 100100

MITRE ATT&CK: T1110 — Brute Force

## 2. Incident Summary

A controlled SSH authentication attack simulation was conducted
against an Ubuntu VirtualBox machine.

Multiple invalid SSH login attempts were generated using the
username "fakeuser" from the local IP address 127.0.0.1.

Wazuh monitored authentication logs from /var/log/auth.log.

The built-in SSH detection rule 5710 identified invalid username
attempts.

A custom correlation rule, 100100, was configured to detect
repeated invalid SSH login attempts originating from the same
IP address within 60 seconds.

The custom rule successfully generated Level 10 security alerts.

## 3. Detection Timeline

October 18, 2026

23:04:38 - Custom detection alert generated.

23:04:49 - Additional custom alert generated.

23:05:01 - Additional custom alert generated.

23:05:08 - Additional custom alert generated.

23:06:48 - Additional custom alert generated.

23:06:56 - Additional custom alert generated.

23:07:11 - Additional custom alert generated.

23:07:23 - Additional custom alert generated.

All times are Nepal Standard Time (UTC+05:45).

## 4. Detection Rule

Rule ID: 100100

Severity: 10

Frequency: 5

Timeframe: 60 seconds

Parent Rule: 5710

Correlation: Same source IP address

MITRE ATT&CK: T1110 — Brute Force

## 5. Evidence

- SSH authentication logs
- Wazuh built-in detection alerts
- Custom rule configuration
- Wazuh Logtest results
- Live custom rule alerts
- Wazuh Dashboard screenshots

## 6. Detection Limitations

1. The custom rule primarily detects invalid usernames.
2. Attempts targeting existing usernames may not match rule 5710.
3. Distributed attacks from multiple source IPs may bypass
   the same-source-IP condition.
4. Attempts occurring outside the 60-second correlation window
   may not trigger the rule.
5. The rule generates alerts but does not automatically block IPs.
6. Missing or delayed authentication logs can prevent detection.

## 7. Incident Response

The source IP was identified as 127.0.0.1.

The authentication attempts were confirmed to be part of an
authorized local security test.

No successful unauthorized login was established.

The detection alerts were reviewed using Wazuh Dashboard.

## 8. Conclusion

The Mini SOC Lab successfully detected repeated SSH
authentication failures using Wazuh.

Custom rule 100100 generated Level 10 alerts during
the controlled simulation.

The project demonstrates basic security monitoring,
event correlation, custom rule development, and
incident reporting.

