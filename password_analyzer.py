# Password Strength Analyzer
# A security tool to evaluate password strength

import re

def check_password_strength(password):
    """
    Analyzes password strength and provides feedback
    """
    score = 0
    feedback = []
    
    # Check length
    length = len(password)
    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long")
    
    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("❌ Add uppercase letters (A-Z)")
    
    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Add lowercase letters (a-z)")
    
    # Check for numbers
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌ Add numbers (0-9)")
    
    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("❌ Add special characters (!@#$%^&*)")
    
    # Check against common passwords
    common_passwords = ['password', '123456', 'qwerty', 'abc123', 'password123']
    if password.lower() in common_passwords:
        score = 0
        feedback.append("❌ This is a commonly used password! Never use it!")
    
    # Determine strength
    if score >= 6:
        strength = "💪 STRONG"
        color = "green"
    elif score >= 4:
        strength = "⚠️  MEDIUM"
        color = "yellow"
    else:
        strength = "❌ WEAK"
        color = "red"
    
    return strength, score, feedback

def main():
    print("=" * 50)
    print("🔐 PASSWORD STRENGTH ANALYZER")
    print("=" * 50)
    print()
    
    while True:
        password = input("Enter a password to analyze (or 'quit' to exit): ")
        
        if password.lower() == 'quit':
            print("\n👋 Thanks for using Password Analyzer!")
            break
        
        if not password:
            print("⚠️  Please enter a password\n")
            continue
        
        strength, score, feedback = check_password_strength(password)
        
        print("\n" + "=" * 50)
        print(f"Password Strength: {strength}")
        print(f"Score: {score}/6")
        print("=" * 50)
        
        if feedback:
            print("\n📋 Recommendations:")
            for item in feedback:
                print(f"  {item}")
        else:
            print("\n✅ Excellent! This is a strong password!")
        
        print("\n" + "=" * 50 + "\n")

if __name__ == "__main__":
    main()