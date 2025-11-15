# Quantitative Finance Projects

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C)
![Yahoo Finance](https://img.shields.io/badge/Data-Yahoo%20Finance-5F01D1)

I built this repo to move beyond formulas and study how markets behave in practice.
Using real stock data, I created three focused mini-projects to test ideas step by step.
Together, they show how I think about portfolio construction, risk, and momentum through hands-on analysis.

## ✨ Highlights

- 📊 Real market data pipeline using Yahoo Finance
- 🧮 Practical use of portfolio theory, simulation, and derivatives
- 📁 Three focused projects with clear outputs

## 📌 Project Snapshot

| Project | Focus | Output |
|---|---|---|
| 📈 [efficient_frontier](efficient_frontier/README.md) | Risk vs. return | Frontier plot + max Sharpe point |
| 🎲 [monte_carlo_sim](monte_carlo_sim/README.md) | Price uncertainty | Simulated paths + final distribution |
| 📉 [price_derivative](price_derivative/README.md) | Trend momentum | Price, velocity, acceleration chart |

## 📅 Project Completion Dates

- 📈 Efficient Frontier — September 2025
- 📉 Price Derivative Analyzer — October 2025
- 🎲 Monte Carlo Risk Simulator — November 2025

## ⚙️ Setup

```bash
pip install -r requirements.txt
```

Run any script from its folder, for example:

```bash
cd efficient_frontier
python frontier.py
```

## 🗂️ Data Source

- Yahoo Finance historical market data through `yfinance`.
- `yfinance` documentation: https://ranaroussi.github.io/yfinance/

## 📚 References

### 📈 Efficient Frontier
- [arXiv:1710.02435 — Sparse Portfolio Selection via the sorted ℓ1-Norm](https://arxiv.org/abs/1710.02435)
- [arXiv:2005.08703 — Reactive Global Minimum Variance Portfolios with k-BAHC covariance cleaning](https://arxiv.org/abs/2005.08703)
- [MIT OCW Lecture Library — 15.401 Video Lectures and Slides](https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/pages/video-lectures-and-slides/)

### 🎲 Monte Carlo Risk Simulation
- [arXiv:1504.02896 — Pricing and Risk Management with High-Dimensional Quasi Monte Carlo and Global Sensitivity Analysis](https://arxiv.org/abs/1504.02896)
- [arXiv:2209.14549 — Multilevel Monte Carlo and its Applications in Financial Engineering](https://arxiv.org/abs/2209.14549)
- [MIT OCW Lecture Library — 6.041SC Resource Index](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/pages/resource-index/)

### 📉 Price Derivative Analysis
- [arXiv:1904.04912 — Enhancing Time Series Momentum Strategies Using Deep Neural Networks](https://arxiv.org/abs/1904.04912)
- [arXiv:1702.07374 — Time series momentum and contrarian effects in the Chinese stock market](https://arxiv.org/abs/1702.07374)
- [MIT OCW Lecture Library — 18.01SC Differentiation Unit](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/pages/1.-differentiation/)
