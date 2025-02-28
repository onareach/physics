# units.py
import pint

ureg = pint.UnitRegistry()

unit_categories = {
    "Length": "m",
    "Mass": "kg",
    "Time": "s",
    "Speed": "m/s",
    "Force": "N",
    "Energy": "J",
    "Power": "W",
    "Pressure": "Pa",
    "Temperature": "kelvin",
    "Volume": "liter",
}

def list_units():
    """Display a sub-menu for choosing unit categories using Pint."""
    while True:
        print("\nSelect a unit category to view available units:")
        for i, category in enumerate(unit_categories.keys(), 1):
            print(f"{i}. {category}")
        print("0. Return to main menu.")

        choice = input("\nEnter your choice (number): ").strip()
        if choice == "0":
            break

        try:
            choice_index = int(choice) - 1
            category = list(unit_categories.keys())[choice_index]
            units = get_units_for_category(category)
            print("\nAvailable Units:\n")
            print_units_in_columns(units)
        except (IndexError, ValueError):
            print("Invalid choice. Please select a valid number.")

def get_units_for_category(category):
    """Retrieve all compatible units for a selected category using Pint."""
    base_unit = unit_categories[category]
    return sorted(str(unit) for unit in ureg.get_compatible_units(base_unit))

def print_units_in_columns(units, num_columns=3):
    """Print units in a clean, multi-column format."""
    col_width = 20
    num_rows = (len(units) + num_columns - 1) // num_columns
    for row in range(num_rows):
        row_entries = []
        for col in range(num_columns):
            index = row + col * num_rows
            if index < len(units):
                row_entries.append(units[index].ljust(col_width))
        print("  ".join(row_entries))
