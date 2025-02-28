# Physics and Units Program

This project provides a command-line interface to perform and view physics formulas, as well as explore various unit conversions. The program is organized into four files for ease of maintenance and further expansion.

---

## File Structure

```
project/
├── main.py
├── physics_calculations.py
├── units.py
└── view_formulas.py
```

1. **`main.py`**:
   - Entry point for the entire program.
   - Contains the top-level menu allowing you to:
     1. View physics formulas (matplotlib)
     2. Use physics formulas (interactive calculations)
     3. View available units (Pint-based menu)
     4. Quit
   - Calls functions from the other three files.

2. **`physics_calculations.py`**:
   - Contains all the physics formulas that accept numeric input and return calculations (e.g., momentum, force, etc.).
   - Includes a sub-menu (`use_physics_formulas()`) to let the user choose which formula to run.
   - Uses a temporary non-Pint unit-conversion system.

3. **`units.py`**:
   - Contains the Pint-based system for listing and converting units.
   - Defines a sub-menu (`list_units()`) that lets users see categories of units and the specific units within each category.
   - `print_units_in_columns()` provides a neat tabular display in the terminal.

4. **`view_formulas.py`**:
   - Uses Matplotlib to display mathematical formulas visually (e.g., showing momentum with vector notation `\vec{p} = m \vec{v}`).
   - Defines the `view_physics_formulas()` sub-menu, which can grow to include more formulas in the future.

---

## Getting Started

### Prerequisites
- [Python 3.9+](https://www.python.org/)
- [Pip](https://pypi.org/project/pip/)
- Recommended: a virtual environment (e.g., `venv`)

### Python Libraries
- **pint**: For unit registry and conversions.
- **matplotlib**: For rendering math formulas with vector notation.
- **pandas**: Currently used for potential expansions, and can help with data manipulation.

Install dependencies:

```bash
pip install pint matplotlib pandas
```

---

## How to Run
1. **Clone this repository** or download the files into a directory named `project` (or a folder of your choice).
2. Navigate to that directory in your terminal:
   ```bash
   cd project
   ```
3. Run the program:
   ```bash
   python main.py
   ```
4. Follow the **on-screen menus**:
   - "View physics formulas" → Displays formulas via Matplotlib (e.g., momentum as \vec{p} = m \vec{v}).
   - "Use physics formulas" → Interactive calculations for momentum, force, kinetic energy, etc.
   - "View available units" → Explore unit categories (length, mass, speed...) and see valid Pint units.
   - "Quit" → Exit the program.

---

## Overview of Program Features

1. **Physics Formulas (Interactive)**
   - Momentum, Force, Kinetic Energy, Work, Power.
   - Prompts the user for values and units, converting them to SI before performing calculations.

2. **Physics Formulas (Visual)**
   - Displays a LaTeX-formatted formula in a Matplotlib window.
   - Currently supports momentum in vector notation, with more expansions possible.

3. **Unit Converter (Pint)**
   - Lists categories (mass, length, speed, etc.) and displays all the units recognized by Pint.
   - Demo version to show the power of Pint for unit conversion.

4. **Expandable Design**
   - Additional formulas or unit categories can be added incrementally.
   - Scripts are modular, so you can replace the temporary non-Pint conversions with purely Pint-based calculations.

---

## Future Plans
- **Full Pint Integration**: Migrate the physics calculations to use Pint only.
- **Expanded Visual Formulas**: Include more formulas with Matplotlib displays.
- **Data Logging**: Save calculation history or user inputs for further analysis.
- **GUI Interface**: Potentially build a front-end using a GUI framework (e.g., PyQt or Tkinter) if desired.

---

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT) - feel free to modify and distribute. See the [LICENSE](LICENSE) file for details.
