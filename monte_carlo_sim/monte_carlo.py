import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

ticker = "AAPL"
period = "5y"
simulations = 1000
N = 252
paths_output = "monte_carlo_paths.png"
dist_output = "monte_carlo_dist.png"

history = yf.download(ticker, period=period, auto_adjust=True, progress=False)

if history.empty:
    raise ValueError("No data downloaded. Check internet connection and ticker symbol.")

if isinstance(history.columns, pd.MultiIndex):
    if "Close" in history.columns.get_level_values(0):
        close_series = history["Close"].iloc[:, 0]
    else:
        close_series = history.iloc[:, 0]
else:
    if "Close" in history.columns:
        close_series = history["Close"]
    else:
        close_series = history.iloc[:, 0]

close_series = pd.Series(close_series).dropna()

log_returns = np.log(close_series / close_series.shift(1)).dropna()

if len(log_returns) < 30:
    raise ValueError("Not enough historical return data. Try a longer period.")

S0 = float(close_series.iloc[-1])
mu = float(log_returns.mean() * 252)
sigma = float(log_returns.std() * np.sqrt(252))
dt = 1 / 252

rng = np.random.default_rng(42)
price_paths = np.zeros((N + 1, simulations))
price_paths[0] = S0

for t in range(1, N + 1):
    Z = rng.standard_normal(simulations)
    drift = (mu - 0.5 * sigma**2) * dt
    diffusion = sigma * np.sqrt(dt) * Z
    price_paths[t] = price_paths[t - 1] * np.exp(drift + diffusion)

final_prices = price_paths[-1]
mean_final_price = np.mean(final_prices)
var_95 = np.percentile(final_prices, 5)

print(f"Simulation Results ({simulations} paths):")
print(f"Ticker: {ticker}")
print(f"Start Price: ${S0}")
print(f"Estimated annual return (mu): {mu:.2%}")
print(f"Estimated annual volatility (sigma): {sigma:.2%}")
print(f"Expected Mean Final Price: ${mean_final_price:.2f}")
print(f"95% Worst Case (VaR): ${var_95:.2f}")

plt.figure(figsize=(12, 6))

plt.plot(price_paths[:, :50], alpha=0.4, linewidth=1)

plt.plot(np.mean(price_paths, axis=1), color="black", linewidth=3, linestyle="--", label="Mean Path")

plt.title(f"Monte Carlo Simulation for {ticker} ({simulations} paths)")
plt.xlabel("Trading Days")
plt.ylabel("Price ($)")
plt.legend()
plt.grid(True, alpha=0.3)

plt.savefig(paths_output, dpi=300)
print(f"Paths graph saved as '{paths_output}'")

plt.figure(figsize=(10, 5))
plt.hist(final_prices, bins=50, color="skyblue", edgecolor="black")
plt.axvline(mean_final_price, color="red", linestyle="dashed", linewidth=2, label=f"Mean: ${mean_final_price:.2f}")
plt.axvline(var_95, color="orange", linestyle="dashed", linewidth=2, label=f"5% VaR: ${var_95:.2f}")
plt.title("Distribution of Final Prices")
plt.xlabel("Price ($)")
plt.ylabel("Frequency")
plt.legend()
plt.savefig(dist_output, dpi=300)
print(f"Distribution graph saved as '{dist_output}'")

