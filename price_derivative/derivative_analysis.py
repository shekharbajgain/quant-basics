import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

ticker = "AAPL"
period = "2y"
window = 10
output_file = "derivative_analysis_plot.png"

history = yf.download(ticker, period=period, auto_adjust=True, progress=False)

if history.empty:
    raise ValueError("No data downloaded. Check internet connection and ticker symbol.")

if isinstance(history.columns, pd.MultiIndex):
    if "Close" in history.columns.get_level_values(0):
        price_series = history["Close"].iloc[:, 0]
    else:
        price_series = history.iloc[:, 0]
else:
    if "Close" in history.columns:
        price_series = history["Close"]
    else:
        price_series = history.iloc[:, 0]

price_series = pd.Series(price_series).dropna()

if len(price_series) < window + 5:
    raise ValueError("Not enough data points for this moving average window.")

df = price_series.to_frame(name="Price")
df["MA"] = df["Price"].rolling(window=window).mean()
df["Velocity"] = df["MA"].diff()
df["Acceleration"] = df["Velocity"].diff()

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12), sharex=True)

ax1.plot(df.index, df["Price"], label="Price", alpha=0.5, color="gray")
ax1.plot(df.index, df["MA"], label=f"{window}-day moving average", color="blue", linewidth=2)
ax1.set_title(f"{ticker} Price")
ax1.legend()
ax1.grid(True, alpha=0.3)

ax2.plot(df.index, df["Velocity"], color="orange", label="Velocity (1st derivative)")
ax2.axhline(0, color="black", linestyle="--", alpha=0.5)
ax2.set_title("Velocity")
ax2.set_ylabel("$ / day")
ax2.grid(True, alpha=0.3)

ax3.plot(df.index, df["Acceleration"], color="purple", label="Acceleration (2nd derivative)")
ax3.axhline(0, color="black", linestyle="--", alpha=0.5)
ax3.set_title("Acceleration")
ax3.set_ylabel("$ / day²")
ax3.grid(True, alpha=0.3)

plt.xlabel("Date")
plt.tight_layout()

print("Analysis Complete.")
print(f"Ticker used: {ticker}")
print("Watch where acceleration crosses zero while price is still rising.")

plt.savefig(output_file, dpi=300)
print(f"Graph saved as '{output_file}'")

