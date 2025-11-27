# Example usage
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from autohedge import AutoHedge

# Define the stocks to analyze
stocks = ["PLTR"]

# Initialize the trading system with the specified stocks
trading_system = AutoHedge(stocks)

# Define the task for the trading cycle
task = "Let's analyze palantir to see if we should buy it, we have 50k$ in allocation"

# Run the trading cycle and print the results
print(trading_system.run(task=task))
