print("Mental Health Risk Detection System")

while True:
    try:
        stress = int(input("Enter stress level (1-10): "))
        sleep = int(input("Enter sleep hours: "))
        mood = int(input("Enter mood level (1-10): "))

        # Input validation
        if stress < 1 or stress > 10 or mood < 1 or mood > 10:
            print("Invalid input! Values should be between 1 and 10.\n")
            continue

        # Scoring system
        score = 0
        score += stress
        score += (10 - mood)
        score += (8 - sleep)

        # Risk classification
        if score >= 20:
            risk = "High Risk"
        elif score >= 12:
            risk = "Moderate Risk"
        else:
            risk = "Low Risk"

        # Structured output
        print("\n----- RESULT -----")
        print("Stress Level:", stress)
        print("Sleep Hours:", sleep)
        print("Mood Level:", mood)
        print("Mental Health Status:", risk)
        print("------------------\n")

        # Save to file
        file = open("results.txt", "a")
        file.write(f"Stress: {stress}, Sleep: {sleep}, Mood: {mood}, Risk: {risk}\n")
        file.close()

    except:
        print("Invalid input! Please enter numbers only.\n")

    # Repeat option
    again = input("Do you want to check again? (yes/no): ")

    if again.lower() != "yes":
        print("Thank you for using the system")
        break
