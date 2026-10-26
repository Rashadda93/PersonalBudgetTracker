# Personal Budget Tracker

#### Video Demo: https://youtu.be/qRiZRA_Mq6Y
#### Description:

The Personal Budget Tracker is a Python command-line application that helps users to organize their income, expenses, and monthly spending goals. I created this so that I can apply the concepts that I have learned in my Programming in Python course to a practical problem, which is understanding where money comes from, where it goes, and how much is available. Instead of manually calculating every purchase, a user can enter transactions and receive a simple summary. This application is designed for someone who wants a straightforward way to monitor spending without having to learn complicated financial software.
## What the Program Does

At the start of the program, it will display a numbered menu that has seven options. The user will have the choice to choose to add income, add, an expense, set a monthly budget, view a budget summary, view transaction history, save financial data, or exit. The menu will repeat until the user chooses the exit option, which makes it possible to complete multiple tasks during one session.

**Add Income:** Users will enter the source of income, a job, freelance work, or any other payment, along with the amount that they make. The application saves the entry with its date and time.

**Add Expenses:** Users are able to enter spending categories such as rent, utilities, groceries, transportation, and entertainment. Every expense includes its category, amount, and the date and time that it was recorded.

**Set Monthly Budget:** Users will enter a positive amount that represents their monthly spending limit. This limit will be saved and used when calculating if expenses are within budget. The program will store one spending-limit setting that will continue to apply until the user changes it; it will not maintain a separate budget limit for different months.

**View Budget Summary:** This program will calculate the income and expenses that were recorded during the current calendar month. It will display total income, total expenses, the remaining balance (income minus expenses), the monthly budget, and the budget remaining (budget minus expenses). A status message will tell the user if they are staying within budget, exactly at the limit, over budget, or have not set a budget.

**View Transactions:** This program displays all saved income and expense entries, that includes transactions from previous months. Each entry shows its date, type, category, and amount.

**Save Financial Data:** The application will automatically save changes when income, expenses, or the budget are updated. A separate menu option will also let the user manually save. Information is stored in a JSON file so that it can be loaded again the next time the program runs.

**Exit Program:** Users will be able to select the exit option to close the application. Because changes will be saved as they happen, the program won't rely on the user remembering to save at the end.

## Project Files

**`TermProject.py`** is the main Python source file. It contains the `BudgetTracker` class, the `main()` function, and other functions that are responsible for collecting input, recording transactions, displaying summaries, and handling the menu.
**`requirements.txt`** lists the external Python packages that are needed by a project. This application only uses Python's standard library, so no third-party packages will need to be installed. 
**`budget_data.json`** is created automatically when financial data is first saved. It stores the budget and transaction history between program sessions. This is a generated data file instead of a file users need to manually create.
**`README.md`** is this documentation file. It explains the purpose of the application, its features, the decisions made during development, and how to run it.

## Key Design Decisions

I chose a text-based menu because it is easier for me to understand, works in a normal terminal, and lets me focus on writing reliable Python logic instead of designing a graphical interface. The menu uses a `while` loop to remain available and `if`, `elif`, and `else` statements to direct each choice to the appropriate function.

I organized the program around a `BudgetTracker` class to demonstrate object-oriented programming. This class stores transactions and the budget together and provides methods for loading data, saving data, recording transactions, and selecting transactions from the current month. Keeping related information and behavior in one class makes the code easier to maintain and extend.

I also created **separate top-level functions** such as `add_income()`, `add_expense()`, `set_budget()`, `view_summary()`, and `view_transactions()`. Each function has a clear responsibility. This organization meets the assignment requirement for `main()` and contains at least three additional functions at the same indentation level, while making the program easier to read, test, and troubleshoot.

I selected **JSON for file storage** because it is readable, supported by Python's built-in `json` module, and suitable for a small personal application. I used the built-in `datetime` module to record transaction timestamps. For money, I used `Decimal` instead of floating-point values to avoid common rounding issues when working with currency. Amounts are stored as strings in the JSON file so their decimal values can be accurately reconstructed.

Finally, I included **input validation and exception handling**. This program rejects empty categories and asks users to correct invalid or nonpositive monetary amounts. Also, it handles certain problems when loading or saving data, such as a unreadable or incorrectly formatted JSON file. These checks support defensive programming and help the application recover more gracefully from common mistakes.

## How to Run the Project

1. Install Python 3 if it is not already installed.
2. Place `TermProject.py` and `requirements.txt` in the same project folder.
3. Open a terminal or command prompt in that folder.
4. Run the command:

   python TermProject.py

5. Enter a menu number from 1 through 7 and follow the prompts. On some computers, the command may be `python3 TermProject.py` instead.

## Example Use

A user might enter **$2,500** in job income, **$125.50** in grocery expenses, and an **$800** monthly spending limit. If those are the only transactions recorded during the current month, the program reports a remaining balance of **$2,374.50** and a remaining budget of **$674.50**. It also reports that the user is within the budget. These values update as more transactions are added.

## Future Improvements

If I continue developing this project, I would like to add separate budgets for each month, expenses that are totaled by category, the ability to edit or delete incorrect transactions, charts that show spending patterns, and a graphical interface. These features would make the tracker more flexible while building on the Python fundamentals demonstrated in this version.

## Video Demonstration

The video demonstration will introduce the project and show the menu, adding income and expenses, setting a budget, viewing summaries and transactions, and saving information. It will also explain how the functions, class, conditional statements, loops, error handling, and file handling work together. 
