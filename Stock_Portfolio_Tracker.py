"""
====================================================
              STOCK PORTFOLIO TRACKER
====================================================
A simple Python program to calculate total investment
value based on manually defined stock prices.

Concepts Used:
- Dictionary
- Input / Output
- Functions
- Basic Arithmetic
- File Handling (.txt and .csv)
====================================================
"""

import csv


# --------------------------------------------------
# Hardcoded dictionary of stock prices
# --------------------------------------------------
stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 410,
    "AMZN": 175,
    "META": 500,
    "NVDA": 1200,
    "NFLX": 620,
    "IBM": 190,
    "ORCL": 145
}


# --------------------------------------------------
# Function to display available stocks
# --------------------------------------------------
def display_stocks():
    """Display all available stock symbols and prices."""
    print("\n" + "=" * 45)
    print("          AVAILABLE STOCKS")
    print("=" * 45)

    print(f"{'Symbol':<10}{'Price ($)':>15}")
    print("-" * 25)

    for symbol, price in stocks.items():
        print(f"{symbol:<10}{price:>15}")

    print("=" * 45)
    print("Type 'done' when you finish adding stocks.\n")


# --------------------------------------------------
# Function to get user input
# --------------------------------------------------
def get_user_input():
    """
    Get stock symbol and quantity from the user.
    Returns a list containing portfolio data.
    """
    portfolio = []

    while True:

        symbol = input("Enter stock symbol: ").upper().strip()

        # Stop input
        if symbol == "DONE":
            break

        # Check if stock exists
        if symbol not in stocks:
            print("Invalid stock symbol! Please try again.\n")
            continue

        # Get quantity with validation
        while True:
            try:
                quantity = float(input("Enter quantity: "))

                if quantity <= 0:
                    print("Quantity must be greater than 0.")
                    continue

                break

            except ValueError:
                print("Please enter a valid numeric value.")

        # Calculate subtotal
        price = stocks[symbol]
        subtotal = price * quantity

        # Save data
        portfolio.append({
            "symbol": symbol,
            "price": price,
            "quantity": quantity,
            "subtotal": subtotal
        })

        # Display current entry
        print("\nStock Added Successfully!")
        print(f"Stock    : {symbol}")
        print(f"Price    : ${price}")
        print(f"Quantity : {quantity}")
        print(f"Subtotal : ${subtotal:.2f}")
        print("-" * 40)

    return portfolio


# --------------------------------------------------
# Function to calculate total investment
# --------------------------------------------------
def calculate_total(portfolio):
    """Return total investment value."""
    total = 0

    for item in portfolio:
        total += item["subtotal"]

    return total


# --------------------------------------------------
# Function to display summary table
# --------------------------------------------------
def display_summary(portfolio):
    """Display portfolio summary."""

    if len(portfolio) == 0:
        print("\nNo stocks were added.")
        return

    total = calculate_total(portfolio)

    print("\n")
    print("=" * 70)
    print("                 PORTFOLIO SUMMARY")
    print("=" * 70)

    print(
        f"{'Stock':<10}"
        f"{'Quantity':>12}"
        f"{'Price':>15}"
        f"{'Subtotal':>18}"
    )

    print("-" * 70)

    for item in portfolio:
        print(
            f"{item['symbol']:<10}"
            f"{item['quantity']:>12}"
            f"{item['price']:>15}"
            f"{item['subtotal']:>18.2f}"
        )

    print("-" * 70)
    print(f"{'TOTAL INVESTMENT':<52}${total:.2f}")
    print("=" * 70)

    return total


# --------------------------------------------------
# Function to save summary in TXT file
# --------------------------------------------------
def save_txt(portfolio, total):
    """Save portfolio summary to a text file."""

    with open("portfolio_summary.txt", "w") as file:

        file.write("=" * 70 + "\n")
        file.write("          STOCK PORTFOLIO SUMMARY\n")
        file.write("=" * 70 + "\n")

        file.write(
            f"{'Stock':<10}"
            f"{'Quantity':>12}"
            f"{'Price':>15}"
            f"{'Subtotal':>18}\n"
        )

        file.write("-" * 70 + "\n")

        for item in portfolio:
            file.write(
                f"{item['symbol']:<10}"
                f"{item['quantity']:>12}"
                f"{item['price']:>15}"
                f"{item['subtotal']:>18.2f}\n"
            )

        file.write("-" * 70 + "\n")
        file.write(f"TOTAL INVESTMENT = ${total:.2f}\n")

    print("Text file saved successfully as 'portfolio_summary.txt'")


# --------------------------------------------------
# Function to save summary in CSV file
# --------------------------------------------------
def save_csv(portfolio):
    """Save portfolio summary to a CSV file."""

    with open("portfolio_summary.csv",
              "w",
              newline="") as file:

        writer = csv.writer(file)

        writer.writerow(
            ["Stock", "Quantity", "Price", "Subtotal"]
        )

        for item in portfolio:
            writer.writerow([
                item["symbol"],
                item["quantity"],
                item["price"],
                item["subtotal"]
            ])

    print("CSV file saved successfully as 'portfolio_summary.csv'")


# --------------------------------------------------
# Main Program
# --------------------------------------------------
def main():
    """Main function."""

    print("=" * 55)
    print("         WELCOME TO STOCK TRACKER")
    print("=" * 55)

    # Display stock list
    display_stocks()

    # Get user data
    portfolio = get_user_input()

    # Display summary
    total = display_summary(portfolio)

    # Save file option
    if len(portfolio) > 0:
        choice = input(
            "\nDo you want to save the result? (yes/no): "
        ).lower()

        if choice == "yes":

            txt_choice = input(
                "Save as TXT file? (yes/no): "
            ).lower()

            if txt_choice == "yes":
                save_txt(portfolio, total)

            csv_choice = input(
                "Save as CSV file? (yes/no): "
            ).lower()

            if csv_choice == "yes":
                save_csv(portfolio)

        else:
            print("Result was not saved.")

    print("\nThank you for using Stock Portfolio Tracker!")


# --------------------------------------------------
# Program Entry Point
# --------------------------------------------------
if __name__ == "__main__":
    main()