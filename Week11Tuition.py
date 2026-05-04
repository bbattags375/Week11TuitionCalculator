def calcTuition(credits):
    """Calculate tuition based on number of credits."""
    if credits >= 12:
        return 20000
    elif 1 <= credits <= 11:
        return 1200 + (1700 * credits)
    else:
        return 0

def main():
    credits = int(input("Enter the number of credits: "))

    if credits < 1:
        print("Invalid number of credits. Please enter a positive number.")
    else:
        tuition = calcTuition(credits)
        print(f"Tuition for {credits} credit(s): ${tuition:,.2f}")

main()