import sys

expenses = []


def add_expense():
    expense_name = input("Expense Name: ").capitalize()

    while True:
        try:
            expense_amount = int(input("How much did it cost: "))
            break  # Valid input -> leave the loop
        except ValueError:
            print("Expense amount should be an integer!!")

    expense_category = input("Expense Category: ").capitalize()

    expenses.append({
        "name": expense_name,
        "amount": expense_amount,
        "category": expense_category
    })


def view_expense():
    if len(expenses) == 0:
        print("\nYou haven't added any expenses yet.\n")
        return

    print("\n----- EXPENSES -----\n")

    for element in expenses:
        print(
            f"Name -- {element['name']} | "
            f"Amount -- {element['amount']} | "
            f"Category -- {element['category']}"
        )

def view_summary():
    if len(expenses) == 0:
        print("\nYou haven't added any expenses yet.\n")
        return

    largest_spent = None
    total_spent = 0
    category_spending = {}

    for item in expenses:
        amount = item["amount"]
        category = item["category"]

        total_spent += amount

        if largest_spent is None or amount > largest_spent:
            largest_spent = amount

        if category in category_spending:
            category_spending[category] += amount
        else:
            category_spending[category] = amount

    average_spent = total_spent / len(expenses)

    most_expensive_category = None
    most_expensive_category_amount = 0

    print("\n----- EXPENSE SUMMARY -----\n")

    print(f"Total spent: {total_spent}")
    print(f"Highest amount of spending is: {largest_spent}")
    print(f"Average spending is: {round(average_spent, 2)}")

    print("\nSpending by category:")

    for category, amount in category_spending.items():
        percentage = (amount / total_spent) * 100

        print(f"{category}: {amount} ({round(percentage, 2)}%)")

        if amount > most_expensive_category_amount:
            most_expensive_category_amount = amount
            most_expensive_category = category

    print(f"\nMost expensive category: {most_expensive_category}\n")


def interface():
    print("""================================
       PERSONAL EXPENSE ANALYZER
================================

1. Add expense
2. View expenses
3. View summary
4. Exit
""")

    while True:
        try:
            user_input = int(input("What do you want to do (Enter numbers): "))
            break
        except ValueError:
            print("\nYou should write numbers only.\n")

    if user_input == 1:
        add_expense()

    elif user_input == 2:
        view_expense()

    elif user_input == 3:
        view_summary()

    elif user_input == 4:
        print("Goodbye!")
        sys.exit()

    else:
        print("\nInvalid option. Choose between 1 and 4.\n")

while True:
    interface()