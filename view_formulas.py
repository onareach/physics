# view_formulas.py
import matplotlib.pyplot as plt

def display_p_equals_mv_arrows():
    """Use matplotlib to display the momentum formula with vector arrows."""
    # Using a normal string with double backslashes for LaTeX commands
    plt.figure(figsize=(6, 2))
    plt.text(0.5, 0.5, '$\\vec{p} = m \\vec{v}$', fontsize=24, ha='center')
    plt.axis('off')
    plt.show()

def view_physics_formulas():
    """
    Sub-menu for viewing formulas as graphical/mathematical representations.
    Additional formulas can be added in the future.
    """
    while True:
        print("\nView Physics Formulas:")
        print("1. Momentum: \\vec{p} = m \\vec{v}")
        print("0. Return to Main Menu")
        choice = input("\nEnter your choice (number): ").strip()

        if choice == "0":
            break
        elif choice == "1":
            display_p_equals_mv_arrows()
        else:
            print("Invalid choice. Please select a valid number.")
