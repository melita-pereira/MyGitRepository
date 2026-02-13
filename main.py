from calculator import add, subtract, multiply, divide
from grade_analyzer import analyze_course

def show_menu():
    print("\n===Student Utility Toolkit: ===")
    print("1. Analyze a course")
    print("2. Calculator")
    print("3. Exit")

def calculator_menu():
    print("\n--- Calculator ---")
    print("Available operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Back to main menu")

    choice = input("Select an operation (1-5): ")

    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == '1':
            print(f"Result: {add(a,b)}")
        elif choice == '2':
            print(f"Result: {subtract(a,b)}")
        elif choice == '3':
            print(f"Result: {multiply(a,b)}")
        elif choice == '4':
            print(f"Result: {divide(a,b)}")
    except ValueError:
        print("Error: Please enter valid numbers.")

def main():
    while True:
        show_menu()
        choice = input("Select an option (1-3): ")

        if choice == '1':
            print("\n--- Course Grade Analyzer ---")
            analyze_course()
        elif choice == '2':
            calculator_menu()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
if __name__ == "__main__":    main()