# 🔐 Password Strength Analyzer

A Python-based security tool that evaluates password strength and provides actionable recommendations for improvement.

## Features

- **Comprehensive Analysis**: Checks for length, uppercase, lowercase, numbers, and special characters
- **Common Password Detection**: Warns against commonly used passwords
- **Scoring System**: Provides a 0-6 strength score
- **Actionable Feedback**: Gives specific recommendations to improve weak passwords
- **Interactive CLI**: Easy-to-use command-line interface

## How It Works

The tool analyzes passwords based on multiple security criteria:

1. **Length Check**: Rewards passwords 8+ characters (12+ for bonus points)
2. **Character Variety**: Checks for uppercase, lowercase, numbers, and special characters
3. **Common Password List**: Flags commonly exploited passwords
4. **Strength Rating**: Categorizes as WEAK, MEDIUM, or STRONG

## Usage
```bash
python password_analyzer.py
```

Then enter passwords to analyze. Type `quit` to exit.

## Example Output
```
Enter a password to analyze: MyP@ssw0rd123
==================================================
Password Strength: 💪 STRONG
Score: 6/6
==================================================
✅ Excellent! This is a strong password!
```

## Technical Details

- **Language**: Python 3.x
- **Libraries**: `re` (regular expressions for pattern matching)
- **Security Concepts**: Password entropy, common password detection, multi-factor strength analysis

## What I Learned

- Regular expressions for pattern matching in Python
- Security best practices for password requirements
- User input validation and error handling
- Building interactive CLI applications
- Implementing scoring algorithms

## Future Improvements

- [ ] Add password breach checking via Have I Been Pwned API
- [ ] Implement entropy calculation for more accurate strength assessment
- [ ] Add support for password generation
- [ ] Create GUI version
- [ ] Add multi-language support

## Security Note

This tool is for educational purposes. Passwords entered are not stored or transmitted anywhere - all analysis happens locally.
