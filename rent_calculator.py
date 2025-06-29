import json
import os
import matplotlib.pyplot as plt
import sys

def get_positive_float(prompt, default=0.0):
    """Get a positive float from user input."""
    try:
        value = float(input(prompt))
        if value < 0:
            print("Value cannot be negative. Try again.")
            return get_positive_float(prompt, default)
        return value
    except (ValueError, EOFError, KeyboardInterrupt):
        print(f"Invalid input or input stream closed. Using default value {default}.")
        return default

def get_expenses():
    """Collect all expense inputs interactively."""
    return {
        "rent": get_positive_float("Enter the rent: "),
        "electricity": get_positive_float("Enter the electricity bill: "),
        "gas": get_positive_float("Enter the gas bill: "),
        "maid": get_positive_float("Enter the housemaid charge: "),
        "wifi": get_positive_float("Enter the amount of Wi-Fi bill: ")
    }

def get_split_type():
    """Ask user for equal or unequal splitting."""
    try:
        choice = input("Split equally (E) or unequally (U)? ").strip().upper()
        if choice in ["E", "U"]:
            return choice
        print("Invalid choice. Enter 'E' or 'U'.")
        return get_split_type()
    except (EOFError, KeyboardInterrupt):
        print("Input stream closed. Defaulting to equal split.")
        return "E"

def get_unequal_contributions(total_members, total_cost):
    """Collect contributions for unequal splitting."""
    contributions = []
    print(f"Total cost to split: {total_cost:.2f}")
    for i in range(int(total_members)):
        try:
            amount = float(input(f"Enter contribution for member {i+1}: "))
            if amount < 0:
                print("Contribution cannot be negative.")
                continue
            contributions.append(amount)
        except (ValueError, EOFError, KeyboardInterrupt):
            print("Invalid input or input stream closed. Using default value 0.")
            contributions.append(0.0)
    if abs(sum(contributions) - total_cost) > 0.01:  # Allow small float errors
        print("Warning: Contributions do not match total cost!")
    return contributions

def calculate_per_person(expenses, total_members):
    """Calculate cost per person for equal splitting."""
    if total_members == 0:
        return None
    return sum(expenses.values()) / total_members

def save_data(expenses, total_members, filename="expenses.json"):
    """Save expenses and member count to a JSON file."""
    data = {"expenses": expenses, "total_members": total_members}
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"Error saving data: {e}")

def load_data(filename="expenses.json"):
    """Load expenses and member count from a JSON file."""
    if os.path.exists(filename):
        try:
            with open(filename, "r") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading data: {e}")
    return None

def plot_expenses(expenses, filename="expense_breakdown.png"):
    """Generate and save a pie chart of expenses."""
    labels = [key.capitalize() for key in expenses.keys()]
    values = expenses.values()
    plt.figure(figsize=(8, 6))
    plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=140, colors=plt.cm.Paired.colors)
    plt.title("Expense Breakdown")
    try:
        plt.savefig(filename)
        print(f"Pie chart saved as '{filename}'")
    except Exception as e:
        print(f"Error saving pie chart: {e}")
    plt.close()

def main():
    """Main program function."""
    print("Welcome to the Rent Calculator!")
    
    # Load previous data if available
    data = load_data()
    if data:
        try:
            choice = input("Load previous data? (Y/N): ").strip().upper()
            if choice == "Y":
                expenses = data["expenses"]
                total_members = data["total_members"]
                print("Loaded previous data.")
            else:
                expenses = get_expenses()
                total_members = get_positive_float("Enter the number of flat members: ", default=1)
        except (EOFError, KeyboardInterrupt):
            print("Input stream closed. Using default values.")
            expenses = get_expenses()
            total_members = 1
    else:
        expenses = get_expenses()
        total_members = get_positive_float("Enter the number of flat members: ", default=1)

    # Validate total members
    if total_members < 1:
        total_members = 1
        print("Number of members set to 1 to avoid division by zero.")

    # Calculate total cost
    total_cost = sum(expenses.values())
    
    # Display expense breakdown
    print("\nExpense Breakdown:")
    for expense, amount in expenses.items():
        print(f"{expense.capitalize():12}: {amount:.2f}")
    print(f"{'Total Cost':12}: {total_cost:.2f}")

    # Handle splitting
    split_type = get_split_type()
    if split_type == "E":
        per_person_cost = calculate_per_person(expenses, total_members)
        if per_person_cost is not None:
            print(f"{'Per Person':12}: {per_person_cost:.2f}")
    else:
        contributions = get_unequal_contributions(total_members, total_cost)
        print("\nContributions:")
        for i, amount in enumerate(contributions, 1):
            print(f"{'Member ' + str(i):12}: {amount:.2f}")

    # Generate pie chart
    try:
        if input("\nGenerate expense pie chart? (Y/N): ").strip().upper() == "Y":
            plot_expenses(expenses)
    except (EOFError, KeyboardInterrupt):
        print("Input stream closed. Skipping pie chart generation.")

    # Save data
    try:
        if input("Save data? (Y/N): ").strip().upper() == "Y":
            save_data(expenses, total_members)
    except (EOFError, KeyboardInterrupt):
        print("Input stream closed. Data not saved.")

if __name__ == "__main__":
    main()

#thankyouforreading