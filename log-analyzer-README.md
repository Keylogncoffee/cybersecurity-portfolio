# 🔒 Security Log Analyzer

A Python tool for analyzing security logs to detect threats, suspicious patterns, and potential security incidents.

## Features

- **Failed Login Detection**: Identifies authentication failures and tracks sources
- **Port Scan Detection**: Flags network reconnaissance attempts
- **Suspicious IP Tracking**: Identifies IPs with multiple failed attempts
- **Error Analysis**: Summarizes system errors and warnings
- **Risk Assessment**: Calculates overall security risk score (0-100)
- **Actionable Recommendations**: Provides security remediation steps

## How It Works

The analyzer uses pattern matching and statistical analysis to:

1. Parse security log files line by line
2. Extract IP addresses using regex
3. Identify security-relevant events (failed logins, scans, errors)
4. Count and correlate suspicious activity
5. Generate risk scores based on threat indicators
6. Provide prioritized security recommendations

## Usage
```bash
python log_analyzer.py
```

Enter the log file name when prompted (e.g., `sample_security.log`)

## Example Output
```
🔒 SECURITY LOG ANALYSIS REPORT
======================================================================
Log File: sample_security.log
Total Log Entries: 15
Analysis Time: 2025-12-07 12:38:08

📊 FAILED LOGIN ATTEMPTS
Total Failed Logins: 7

🚨 SUSPICIOUS IP ADDRESSES
  🔴 203.0.113.42: 4 failed attempts

🎯 RISK ASSESSMENT
Risk Score: 94/100
Risk Level: 🔴 CRITICAL

⚠️  IMMEDIATE ACTION REQUIRED:
  • Block suspicious IP addresses
  • Review authentication logs
  • Enable rate limiting
```

## Technical Details

- **Language**: Python 3.x
- **Libraries**: `collections.Counter`, `re` (regex), `datetime`
- **Analysis Methods**: Pattern matching, statistical correlation, risk scoring
- **Log Format**: Standard security log format (timestamp, level, message)

## What I Learned

- Log file parsing and analysis techniques
- Regular expressions for IP address extraction
- Security incident detection methodologies
- Risk scoring algorithms
- Threat pattern recognition
- Building defensive security tools

## Risk Scoring Algorithm
```python
Risk Score Calculation:
- Failed Login: +5 points each
- Port Scan: +15 points each
- Suspicious IP (3+ attempts): +20 points each
- Error: +3 points each
- Maximum: 100 points

Risk Levels:
- 0-19: LOW (✅)
- 20-39: MODERATE (🟢)
- 40-69: ELEVATED (🟡)
- 70-100: CRITICAL (🔴)
```

## Use Cases

**Security Operations Centers (SOC):**
- First-level log analysis
- Incident detection
- Threat triage

**System Administrators:**
- Daily security monitoring
- Anomaly detection
- Compliance reporting

**Security Researchers:**
- Attack pattern analysis
- Threat intelligence gathering
- Security testing validation

## Sample Log File Included

The repository includes `sample_security.log` with realistic security events:
- Multiple failed login attempts
- Port scan activity
- Authentication errors
- Normal system events

Perfect for testing and demonstration.

## Future Improvements

- [ ] Support for multiple log formats (Apache, Nginx, Windows Event Logs)
- [ ] Real-time log monitoring
- [ ] Integration with SIEM platforms
- [ ] Geolocation lookup for suspicious IPs
- [ ] Email/Slack alerts for critical events
- [ ] Machine learning for anomaly detection
- [ ] Export reports to PDF/JSON
- [ ] Database storage for historical analysis

## Real-World Application

This tool demonstrates core SOC analyst skills:
- Log analysis and correlation
- Threat detection and classification
- Risk assessment and prioritization
- Security incident reporting

These are essential skills for:
- SOC Analyst roles
- Security Operations Engineer
- Incident Response Analyst
- Security Monitoring Specialist
