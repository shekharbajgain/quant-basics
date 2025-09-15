import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]
period = "3y"
num_portfolios = 4000
output_file = "efficient_frontier_plot.png"

prices = yf.download(tickers, period=period, auto_adjust=True, progress=False)

if prices.empty:
    raise ValueError("No data downloaded. Check internet connection and ticker symbols.")

if hasattr(prices.columns, "levels") and "Close" in prices.columns.get_level_values(0):
    close_prices = prices["Close"]
elif "Close" in prices.columns:
    close_prices = prices["Close"]
else:
    close_prices = prices

daily_returns = close_prices.pct_change().dropna()

if daily_returns.empty:
    raise ValueError("Not enough price data after cleaning. Try a longer period.")

mean_returns = daily_returns.mean() * 252
cov_matrix = daily_returns.cov() * 252

results = np.zeros((3, num_portfolios))
rng = np.random.default_rng(42)

for i in range(num_portfolios):
    weights = rng.random(len(tickers))
    weights /= weights.sum()

    p_return = np.sum(mean_returns * weights)

    p_std_dev = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    results[0, i] = p_return
    results[1, i] = p_std_dev
    results[2, i] = p_return / p_std_dev

plt.figure(figsize=(10, 6))
plt.scatter(results[1, :], results[0, :], c=results[2, :], cmap="viridis", s=10, alpha=0.6)
plt.colorbar(label="Sharpe Ratio")

max_sharpe_idx = np.argmax(results[2, :])
max_sharpe_return = results[0, max_sharpe_idx]
max_sharpe_std = results[1, max_sharpe_idx]

plt.scatter(max_sharpe_std, max_sharpe_return, c="red", s=100, edgecolors="black", label="Max Sharpe")

plt.title("Efficient Frontier from Real Price Data")
plt.xlabel("Expected Volatility")
plt.ylabel("Expected Return")
plt.legend()
plt.grid(True, alpha=0.3)

print(f"Tickers used: {', '.join(tickers)}")
print(f"Max Sharpe Ratio Portfolio:\nReturn: {max_sharpe_return:.2%}\nVolatility: {max_sharpe_std:.2%}")

plt.savefig(output_file, dpi=300)
print(f"Graph saved as '{output_file}'")

