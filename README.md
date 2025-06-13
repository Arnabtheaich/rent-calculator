# Rent Calculator

A Python-based tool to calculate shared expenses for flatmates, including rent, utilities, and more. Supports equal and unequal splitting, data persistence, and expense visualization in an interactive interface.

## Features
- **Interactive Mode**: Input expenses and member count via prompts.
- **Equal/Unequal Splitting**: Split costs evenly or specify individual contributions.
- **Data Persistence**: Save and load expense data to/from a JSON file.
- **Visualization**: Generate] a pie chart of expense distribution using Matplotlib.
- **Error Handling**: Validates inputs to prevent crashes (e.g., non-numeric, negative values, or input stream issues).

## Installation
```bash
pip install matplotlib
```

## Usage
Run the program and follow the prompts:
```bash
python rent_calculator.py
```

### Example Output
```
Welcome to the Rent Calculator!
Enter the rent: 10000
Enter the electricity bill: 1200
Enter the gas bill: 800
Enter the housemaid charge: 500
Enter the amount of Wi-Fi bill: 600
Enter the number of flat members: 4
Split equally (E) or unequally (U)? E

Expense Breakdown:
Rent        : 10000.00
Electricity : 1200.00
Gas         : 800.00
Maid        : 500.00
Wifi        : 600.00
Total Cost  : 13100.00
Per Person  : 3275.00

Generate expense pie chart? (Y/N): Y
Pie chart saved as 'expense_breakdown.png'
Save data? (Y/N): Y
Data saved to expenses.json
```

## Screenshots
![Expense Breakdown](screenshots/breakdown.png)
![Pie Chart](screenshots/expense_breakdown.png)

## Future Improvements
- Add a web interface using Flask.
- Store expense history in SQLite for monthly tracking.
- Support multi-currency calculations.
- Send email notifications with cost details.

## License
MIT License
