print("Mental Health Risk Detection System")

mood = int(input("Enter your mood level (1-10): "))
stress = int(input("Enter your stress level (1-10): "))
sleep = int(input("Enter your sleep quality (1-10): "))
social = int(input("How socially active are you (1-10): "))

if mood <= 3 and stress >= 7 and social <= 4:
    print("Risk Level: HIGH")
    print("Suggestion: Please talk to a counselor or a trusted person immediately.")
elif mood <= 5 or stress >= 6:
    print("Risk Level: MEDIUM")
    print("Suggestion: Try meditation, journaling, or talking to friends.")
else:
    print("Risk Level: LOW")
    print("Suggestion: Keep maintaining a healthy routine!")
