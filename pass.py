import re

def check_password_strength(password):

    score = 0
    feedback = []


    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r'[A-Z]',password):
        score += 1
    else:
        feedback.append("Password should include at least one uppercase letter (A-Z).")


    
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should include at least one lowercase letter (a-z).")


    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Password should include at least one digit (0-9).")


    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Password should include at least one special character (e.g., !@#$).")

    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"


    if feedback:
        feedback_str = "\n".join(feedback)
        return f"Strength: {strength}\nSuggestions to improve:\n{feedback_str}"
    else:
        return f"Strength: {strength}\nGreat! This password meets all criteria."


if __name__ == "__main__":
    print("Welcome to the Password Strength Checker!")
    
    while True:
        password = input("Enter a password to check (or 'quit' to exit): ")
        if password.lower() == 'quit':
            print("You have exited the checker.")
            break
        result = check_password_strength(password)
        print(result)
        print("\n")

