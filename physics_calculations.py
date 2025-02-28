# physics_calculations.py
import math

# This section is for the "temporary" non-Pint conversions.
def get_unit_conversion(unit_type):
    """Return a dictionary of unit conversion factors (temporary system)."""
    unit_conversions = {
        "mass": {"kg": 1, "g": 0.001, "lb": 0.453592},
        "velocity": {"m/s": 1, "km/h": 0.277778, "mph": 0.44704},
        "force": {"N": 1, "lbf": 4.44822},
        "distance": {"m": 1, "cm": 0.01, "km": 1000, "mi": 1609.34},
        "time": {"s": 1, "min": 60, "hr": 3600},
        "energy": {"J": 1, "cal": 4.184, "kWh": 3600000},
    }
    return unit_conversions.get(unit_type, {})

def get_numeric_input(prompt, unit_type):
    """
    Prompts user for a numeric value and unit.
    Converts it to SI units (temporary approach until fully moved to Pint).
    Returns a tuple: (value_in_SI, original_unit).
    """
    conversions = get_unit_conversion(unit_type)
    print(f"Available units for {unit_type}: {', '.join(conversions.keys())}")
    unit = input("Enter unit: ").strip()
    if unit not in conversions:
        print("Invalid unit. Using SI unit by default.")
        unit = list(conversions.keys())[0]
    value = float(input(f"Enter value in {unit}: "))
    return value * conversions[unit], unit

# Individual physics formulas
def momentum():
    mass, mass_unit = get_numeric_input("Enter mass", "mass")
    velocity, velocity_unit = get_numeric_input("Enter velocity", "velocity")
    momentum_value = mass * velocity
    momentum_unit = f"{mass_unit}*{velocity_unit}"
    print(f"Momentum = {momentum_value} {momentum_unit}")

def force():
    m = get_numeric_input("Enter mass", "mass")[0]
    a = get_numeric_input("Enter acceleration", "velocity")[0]
    print(f"Force = {m * a} N")

def kinetic_energy():
    m = get_numeric_input("Enter mass", "mass")[0]
    v = get_numeric_input("Enter velocity", "velocity")[0]
    print(f"Kinetic Energy = {0.5 * m * v ** 2} J")

def work_done():
    f = get_numeric_input("Enter force", "force")[0]
    d = get_numeric_input("Enter distance", "distance")[0]
    print(f"Work Done = {f * d} J")

def power():
    w = get_numeric_input("Enter work", "energy")[0]
    t = get_numeric_input("Enter time", "time")[0]
    print(f"Power = {w / t} W")

def list_formulas():
    """Return a dictionary mapping formula names to their functions."""
    return {
        "momentum": momentum,
        "force": force,
        "kinetic_energy": kinetic_energy,
        "work_done": work_done,
        "power": power,
    }

def use_physics_formulas():
    """
    Presents a sub-menu for physics formulas.
    Lets the user pick one of the formulas to run or exit to main menu.
    """
    while True:
        formulas = list_formulas()
        formula_names = list(formulas.keys())
        print("\nPhysics Formulas:")
        for i, name in enumerate(formula_names, 1):
            print(f"{i}. {name}")
        print("0. Return to main menu.")

        choice = input("\nEnter the number of the formula you want to use: ").strip()
        if choice == "0":
            break

        try:
            formula_index = int(choice) - 1
            selected_formula = formula_names[formula_index]
            formulas[selected_formula]()  # Call the selected formula function
        except (IndexError, ValueError):
            print("Invalid selection. Please try again.")
