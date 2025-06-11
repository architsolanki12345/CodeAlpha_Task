def stock_portfolio():
    prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "AMZN": 130
    }

    portfolio = {}
    print("📈 Stock Portfolio Tracker")

    while True:
        stock = input("Enter stock symbol (or type 'done'): ").upper()
        if stock == 'DONE':
            break
        if stock not in prices:
            print("⚠️ Invalid stock symbol.")
            continue
        qty = input(f"Enter quantity of {stock}: ")
        if not qty.isdigit():
            print("⚠️ Invalid quantity.")
            continue
        portfolio[stock] = portfolio.get(stock, 0) + int(qty)

    total_value = sum(prices[symbol] * qty for symbol, qty in portfolio.items())
    print("\n🧾 Portfolio Summary:")
    for symbol, qty in portfolio.items():
        print(f"{symbol}: {qty} shares @ ₹{prices[symbol]} each")

    print("💰 Total Investment Value: ₹", total_value)

    
    with open("portfolio_summary.txt", "w") as f:
        f.write("Stock Portfolio Summary\n")
        for symbol, qty in portfolio.items():
            f.write(f"{symbol}: {qty} shares @ ₹{prices[symbol]}\n")
        f.write(f"\nTotal Investment: ₹{total_value}")

    print("📁 Saved to portfolio_summary.txt")

stock_portfolio()
