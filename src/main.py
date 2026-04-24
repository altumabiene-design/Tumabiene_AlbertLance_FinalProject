from tracker import ExpenseTracker


def main():
    tracker = ExpenseTracker()

    while True:
        print("\n==============================")
        print("      EXPENSE TRACKER")
        print("==============================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expense")
        print("4. Delete Expense (by ID)")
        print("5. Sort Expenses")
        print("6. Total Expenses")
        print("7. Category Summary")
        print("8. Save Data")
        print("9. Exit")
        print("==============================")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter title: ")
            category = input("Enter category: ")

            try:
                amount = float(input("Enter amount: "))
                tracker.add_expenses(title, amount, category)
            except ValueError:
                print("Invalid amount.")

        elif choice == "2":
            tracker.view_expenses()

        elif choice == "3":
            keyword = input("Search keyword: ")
            tracker.search_expense(keyword)

        elif choice == "4":
            try:
                expense_id = int(input("Enter Expense ID to delete: "))
                tracker.delete_expense(expense_id)
            except ValueError:
                print("Invalid ID. Please enter a number.")

        elif choice == "5":
            tracker.sort_expenses()

        elif choice == "6":
            tracker.total_expense()

        elif choice == "7":
            tracker.category_summary()

        elif choice == "8":
            tracker.save_data()

        elif choice == "9":
            tracker.save_data()
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
