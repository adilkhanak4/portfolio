
import yfinance as yf
import pandas as pd

class StockPortfolio:
    def _init_(self):
        self.stocks = {}
        self.filename = 'stock.csv'

    def add_stock(self, symbol, quantity):
        if symbol in self.stocks:
            self.stocks[symbol] += quantity
        else:
            self.stocks[symbol] = quantity
        self.save_data()

    def remove_stock(self, symbol, quantity):
        if symbol in self.stocks:
            self.stocks[symbol] -= quantity
            if self.stocks[symbol] <= 0:
                del self.stocks[symbol]
        self.save_data()

    def get_portfolio_value(self):
        total_value = 0
        for symbol, quantity in self.stocks.items():
            try:
                ticker = yf.Ticker(symbol)
                data = ticker.history(period='1d')
                if not data.empty:
                    total_value += data['Close'].iloc[-1] * quantity
                else:
                    print(f"No data available for {symbol}")
            except Exception as e:
                print(f"Error getting data for {symbol}: {str(e)}")
        return total_value

    def get_stock_data(self, symbol):
        try:
            ticker = yf.Ticker(symbol)
            data = ticker.history(period='1d')
            return data
        except Exception as e:
            print(f"Error getting data for {symbol}: {str(e)}")
            return None

    def save_data(self):
        with open(self.filename, 'w') as file:
            for symbol, quantity in self.stocks.items():
                file.write(f'{symbol}: {quantity}\n')

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                for line in file.readlines():
                    symbol, quantity = line.strip().split(': ')
                    self.stocks[symbol] = int(quantity)
        except FileNotFoundError:
            pass

    def display_stocks(self):
        print('Stock Portfolio:')
        for symbol, quantity in self.stocks.items():
            print(f'{symbol}: {quantity}')

    def track_performance(self):
        print('Stock Performance:')
        for symbol, quantity in self.stocks.items():
            try:
                ticker = yf.Ticker(symbol)
                data = ticker.history(period='1y')
                if not data.empty:
                    print(f'{symbol}:')
                    print(f'  - Current Price: {data["Close"].iloc[-1]}')
                    print(f'  - 1-Year High: {data["High"].max()}')
                    print(f'  - 1-Year Low: {data["Low"].min()}')
                    print(f'  - 1-Year Return: {(data["Close"].iloc[-1] / data["Close"].iloc[0]) - 1:.2%}')
                else:
                    print(f"No data available for {symbol}")
            except Exception as e:
                print(f"Error getting data for {symbol}: {str(e)}")

def main():
    portfolio = StockPortfolio()
    portfolio.load_data()
    while True:
        print('1. Add Stock')
        print('2. Remove Stock')
        print('3. Get Portfolio Value')
        print('4. Get Stock Data')
        print('5. Display Stocks')
        print('6. Track Performance')
        print('7. Exit')
        choice = input('Enter your choice: ')
        if choice == '1':
            symbol = input('Enter stock symbol: ')
            quantity = int(input('Enter quantity: '))
            portfolio.add_stock(symbol, quantity)
        elif choice == '2':
            symbol = input('Enter stock symbol: ')
            quantity = int(input('Enter quantity: '))
            portfolio.remove_stock(symbol, quantity)
        elif choice == '3':
            print('Portfolio Value: ', portfolio.get_portfolio_value())
        elif choice == '4':
            symbol = input('Enter stock symbol: ')
            data = portfolio.get_stock_data(symbol)
            if data is not None:
                print(data)
        elif choice == '5':
            portfolio.display_stocks()
        elif choice == '6':
            portfolio.track_performance()
        elif choice == '7':
            break
        else:
            print('Invalid choice. Please try again.')

if _name_ == "_main_":
    main()
