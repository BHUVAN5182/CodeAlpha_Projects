# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "AMZN": 190,
    "MSFT": 420
}

total_investment = 0

print("===== Stock Portfolio Tracker =====")
print("Available stocks:", ", ".join(stock_prices.keys()))

# Number of different stocks
n = int(input("How many stocks do you want to buy? "))

portfolio = []

for i in range(n):
    stock = input("\nEnter stock name: ").upper()

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))

        price = stock_prices[stock]
        investment = price * quantity
        total_investment += investment

        portfolio.append((stock, quantity, price, investment))

        print(f"{stock}: {quantity} × ${price} = ${investment}")
    else:
        print("Stock not available.")

# Display portfolio
print("\n===== Portfolio Summary =====")

for stock, quantity, price, investment in portfolio:
    print(f"{stock} | Quantity: {quantity} | Price: ${price} | Value: ${investment}")

print("--------------------------------")
print(f"Total Investment: ${total_investment}")

# Optional: Save result to a text file
save = input("\nDo you want to save the result to a file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("-----------------------\n")

        for stock, quantity, price, investment in portfolio:
            file.write(
                f"{stock} | Quantity: {quantity} | "
                f"Price: ${price} | Value: ${investment}\n"
            )

        file.write("-----------------------\n")
        file.write(f"Total Investment: ${total_investment}\n")

    print("Portfolio saved to portfolio.txt")
