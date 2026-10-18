# 🛡️ Mini SOC Lab Using Wazuh

## Project Overview

This project demonstrates the implementation of a Mini Security
Operations Center (SOC) using Wazuh on Ubuntu Linux.

The lab focuses on monitoring SSH authentication events, detecting
failed login attempts, creating custom security detection rules,
and analyzing alerts through the Wazuh Dashboard.

The project was developed in an authorized VirtualBox lab environment.

## Objectives

- Install and configure Wazuh SIEM.
- Monitor Ubuntu SSH authentication logs.
- Simulate controlled SSH login failures.
- Detect suspicious authentication attempts.
- Develop a custom SSH brute-force detection rule.
- Analyze security alerts in Wazuh Dashboard.
- Document an incident and detection limitations.

## Tools and Technologies

| Technology | Purpose |
|------------|---------|
| Ubuntu Linux | Lab operating system |
| Oracle VirtualBox | Virtualization |
| Wazuh Manager 4.14.9 | Security event analysis |
| Wazuh Dashboard | Security alert visualization |
| Wazuh Indexer | Security data indexing |
| OpenSSH | SSH authentication testing |
| Linux Terminal | Configuration and testing |
| GitHub | Project documentation |

## Lab Architecture

```text
             Ubuntu VirtualBox
                    |
             Wazuh Manager
                    |
          Local Monitoring (000)
                    |
             SSH Server
                    |
           /var/log/auth.log
                    |
             Wazuh Analysis
                    |
          Built-in Rule 5710
                    |
          Custom Rule 100100
                    |
            Security Alerts
                    |
             Wazuh Dashboard
```

This implementation uses Wazuh Manager's local monitoring
capability rather than a separately deployed endpoint agent.

## SSH Log Monitoring

The Wazuh Manager was configured to monitor Ubuntu authentication
logs using the following configuration:

```xml
<localfile>
  <log_format>syslog</log_format>
  <location>/var/log/auth.log</location>
</localfile>
```

Configuration file:

`/var/ossec/etc/ossec.conf`

## SSH Authentication Test

Controlled authentication failures were generated against the
local Ubuntu SSH server.

Test command:

```bash
ssh -o PubkeyAuthentication=no \
    -o PreferredAuthentications=password \
    -o NumberOfPasswordPrompts=1 \
    fakeuser@127.0.0.1
```

An incorrect test password was entered when prompted.

The SSH server rejected the login attempts.

## Built-in SSH Detection

Wazuh successfully identified invalid SSH usernames.

Rule ID: 5710

Severity: Level 5

Description:

sshd: Attempt to login using a non-existent user

## Custom SSH Detection Rule

A custom rule was developed to identify repeated invalid SSH
login attempts originating from the same IP address.

Rule ID: 100100

Severity: Level 10

Frequency: 5

Timeframe: 60 seconds

MITRE ATT&CK: T1110 — Brute Force

Rule file:

[rules/custom_ssh_rules.xml](rules/custom_ssh_rules.xml)

## Detection Results

The custom detection rule was successfully tested using
Wazuh Logtest.

The rule also generated real security alerts during a controlled
SSH authentication test.

Verified results:

| Date | Time (Nepal) | Rule ID | Severity |
|------|--------------|---------|----------|
| 2026-10-18 | 23:04:38 | 100100 | 10 |
| 2026-10-18 | 23:04:49 | 100100 | 10 |
| 2026-10-18 | 23:05:01 | 100100 | 10 |
| 2026-10-18 | 23:05:08 | 100100 | 10 |
| 2026-10-18 | 23:06:48 | 100100 | 10 |
| 2026-10-18 | 23:06:56 | 100100 | 10 |
| 2026-10-18 | 23:07:11 | 100100 | 10 |
| 2026-10-18 | 23:07:23 | 100100 | 10 |

The source IP was 127.0.0.1.

These were authorized local test events, not evidence of an
external attack.

## Detection Limitations

1. The rule depends on built-in rule 5710.
2. Password guessing against valid usernames may not trigger it.
3. Attacks distributed across multiple IP addresses may evade
   the same-source-IP condition.
4. Attempts outside the correlation window may go undetected.
5. The rule generates alerts but does not automatically block IPs.
6. Missing authentication logs may prevent detection.

## Incident Report

See the full incident report:

[SSH Brute-Force Incident Report](reports/incident-report.md)

## Evidence and Screenshots

Screenshots are stored in the `screenshots/` directory.

The evidence includes:

- Wazuh Dashboard
- Wazuh service status
- SSH authentication logs
- Built-in SSH detection
- Custom rule configuration
- Custom rule test
- Live Wazuh security alerts

## Conclusion

The Mini SOC Lab successfully demonstrated SSH authentication
monitoring and custom security event correlation using Wazuh.

A custom Level 10 detection rule was developed, tested, and
verified against live authentication events.

The project demonstrates foundational SOC skills in log
collection, SIEM configuration, detection engineering, event
analysis, and incident documentation.
