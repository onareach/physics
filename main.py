# main.py
from units import list_units
from physics_calculations import use_physics_formulas
from view_formulas import view_physics_formulas

def main():
    """
    Top-level menu providing options to:
    1. View physics formulas (matplotlib)
    2. Use physics formulas (interactive calculations)
    3. View available units (Pint-based menu)
    4. Quit
    """
    while True:
        print("\nMain Menu")
        print("1. View physics formulas")
        print("2. Use physics formulas")
        print("3. View available units")
        print("4. Quit")

        choice = input("Enter your choice (number): ").strip()
        if choice == "1":
            view_physics_formulas()
        elif choice == "2":
            use_physics_formulas()
        elif choice == "3":
            list_units()
        elif choice == "4":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid number.")

if __name__ == "__main__":
    main()
