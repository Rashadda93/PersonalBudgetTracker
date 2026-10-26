
import json
from pathlib import Path
from decimal import Decimal, InvalidOperation

DATA_FILE = Path(__file__).with_name("budget_data.json")


def load_data():
    if DATA_FILE.exists():
        try:
            with DATA_FILE.open("r") as file:
                return json.load(file)
        except (OSError, json.JSONDecodeError):
            print("Could not load saved data.")

    return {"budget": "0", "transactions": []}


def save_data(tracker):
    with DATA_FILE.open("w") as file:
        json.dump(tracker, file, indent=4)
    print("Financial data saved successfully!")


def get_positive_amount(prompt):
    while True:
        try:
            amount = Decimal(input(prompt))
            if not amount.is_finite() or amount <= 0:
                print("Please enter a positive amount.")
            else:
                return amount
        except InvalidOperation:
            print("Invalid amount. Enter a number.")


def add_income(tracker):
    category = input("Enter income source: ")
    amount = get_positive_amount("Enter income amount: $")

    tracker["transactions"].append({
        "type": "Income",
        "category": category,
        "amount": str(amount)
    })

    save_data(tracker)
    print("Income added successfully!")


def add_expense(tracker):
    category = input("Enter expense category: ")
    amount = get_positive_amount("Enter expense amount: $")

    tracker["transactions"].append({
        "type": "Expense",
        "category": category,
        "amount": str(amount)
    })

    save_data(tracker)
    print("Expense added successfully!")


def set_budget(tracker):
    amount = get_positive_amount("Enter monthly budget: $")
    tracker["budget"] = str(amount)
    save_data(tracker)
    print("Monthly budget updated!")


def view_summary(tracker):
    income = Decimal("0")
    expenses = Decimal("0")

    for transaction in tracker["transactions"]:
        amount = Decimal(transaction["amount"])

        if transaction["type"] == "Income":
            income += amount
        else:
            expenses += amount

    budget = Decimal(tracker["budget"])
    balance = income - expenses
    remaining = budget - expenses

    print("\n--- BUDGET SUMMARY ---")
    print(f"Total Income: ${income:.2f}")
    print(f"Total Expenses: ${expenses:.2f}")
    print(f"Remaining Balance: ${balance:.2f}")
    print(f"Monthly Budget: ${budget:.2f}")
    print(f"Budget Remaining: ${remaining:.2f}")

    if expenses > budget:
        print("Status: Over Budget")
    else:
        print("Status: Within Budget")


def view_transactions(tracker):
    print("\n--- TRANSACTION HISTORY ---")

    if not tracker["transactions"]:
        print("No transactions recorded.")
        return

    for transaction in tracker["transactions"]:
        print(
            f'{transaction["type"]}: '
            f'{transaction["category"]} - '
            f'${Decimal(transaction["amount"]):.2f}'
        )


def main():
    tracker = load_data()

    while True:
        print("\n===== PERSONAL BUDGET TRACKER =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Set Monthly Budget")
        print("4. View Budget Summary")
        print("5. View Transactions")
        print("6. Save Financial Data")
        print("7. Exit Program")

        choice = input("Choose an option (1-7): ")

        if choice == "1":
            add_income(tracker)
        elif choice == "2":
            add_expense(tracker)
        elif choice == "3":
            set_budget(tracker)
        elif choice == "4":
            view_summary(tracker)
        elif choice == "5":
            view_transactions(tracker)
        elif choice == "6":
            save_data(tracker)
        elif choice == "7":
            save_data(tracker)
            print("Thank you for using Budget Tracker!")
            break
        else:
            print("Invalid selection. Try again.")


if __name__ == "__main__":
    main()
