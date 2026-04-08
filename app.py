print("Mental Health Risk Detection System")

mood = int(input("Enter your mood level (1-10): "))
stress = int(input("Enter your stress level (1-10): "))
sleep = int(input("Enter your sleep hours (1-10): "))

if mood <= 3 and stress >= 7:
    print("Risk Level: HIGH")
    print("Suggestion: Please consider talking to a counselor or a trusted person.")
elif mood <= 5:
    print("Risk Level: MEDIUM")
    print("Suggestion: Try relaxation techniques like meditation or journaling.")
else:
    print("Risk Level: LOW")
    print("Suggestion: Keep maintaining a healthy routine!")
