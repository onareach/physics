# view_formulas.py

import matplotlib.pyplot as plt

def display_p_equals_mv_arrows():
    """Use matplotlib to display the momentum formula with vector arrows."""
    plt.figure(figsize=(6, 2))
    # Here, we do $\\vec{p} = m \\vec{v}$ with double backslashes for LaTeX commands
    plt.text(0.5, 0.5, '$\\vec{p} = m \\vec{v}$', fontsize=24, ha='center')
    plt.axis('off')
    plt.show()

def display_conservation_of_momentum():
    """
    Display the conservation of momentum formula:
    \vec{p}_{1, initial} + \vec{p}_{2, initial} = \vec{p}_{1, final} + \vec{p}_{2, final}
    """
    plt.figure(figsize=(6, 2))
    # Use LaTeX syntax with \\text{initial} and \\text{final}
    plt.text(
        0.5,
        0.5,
        '$\\vec{p}_{1,\\text{initial}} + \\vec{p}_{2,\\text{initial}} '
        '= \\vec{p}_{1,\\text{final}} + \\vec{p}_{2,\\text{final}}$',
        fontsize=20,
        ha='center'
    )
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
        print("2. Conservation of Momentum: \\vec{p}_{1,i} + \\vec{p}_{2,i} = \\vec{p}_{1,f} + \\vec{p}_{2,f}")
        print("0. Return to Main Menu")

        choice = input("\nEnter your choice (number): ").strip()
        if choice == "0":
            break
        elif choice == "1":
            display_p_equals_mv_arrows()
        elif choice == "2":
            display_conservation_of_momentum()
        else:
            print("Invalid choice. Please select a valid number.")
