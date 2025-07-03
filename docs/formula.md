```markdown
# Financial Formulas Documentation

## Core Mathematical Formulas

### 1. Future Value (FV) with Compound Interest

**Formula:**
FV = PV × (1 + r)^n

**Where:**
- `FV` = Future Value
- `PV` = Present Value (initial investment)
- `r` = Annual interest rate (as decimal)
- `n` = Number of years

**Example:**
```python
# $10,000 invested at 8% for 10 years
PV = 10000
r = 0.08
n = 10
FV = 10000 * (1 + 0.08)^10 = $21,589.25
2. Systematic Investment Plan (SIP) Future Value
Formula:
FV_SIP = P × [((1 + r)^n - 1) / r] × (1 + r)
Where:

P = Periodic payment amount
r = Periodic interest rate
n = Number of periods

Monthly SIP Formula:
pythonmonthly_rate = annual_rate / 12
months = years * 12
FV = monthly_payment * (((1 + monthly_rate)^months - 1) / monthly_rate) * (1 + monthly_rate)
3. Portfolio Expected Return
Formula:
E(Rp) = Σ(wi × E(Ri))
Where:

E(Rp) = Expected portfolio return
wi = Weight of asset i in portfolio
E(Ri) = Expected return of asset i

4. Portfolio Risk (Standard Deviation)
Simplified Formula (assuming no correlation):
σp = √(Σ(wi² × σi²))
Complete Formula (with correlation):
σp = √(Σ(wi² × σi²) + ΣΣ(wi × wj × σi × σj × ρij))
Where:

σp = Portfolio standard deviation
σi = Standard deviation of asset i
ρij = Correlation between assets i and j

5. Sharpe Ratio
Formula:
Sharpe = (Rp - Rf) / σp
Where:

Rp = Portfolio return
Rf = Risk-free rate (typically 3%)
σp = Portfolio standard deviation

6. Age-Based Allocation Rules
Rule of 100:
Equity % = 100 - Age
Bond % = Age
Modified Rule (Used in our tool):
pythonequity_pct = max(100 - age, 20)  # Minimum 20% equity
bond_pct = min(age, 60)  # Maximum 60% bonds
other_assets = 100 - equity_pct - bond_pct
Implementation Examples
Future Value Calculation
pythondef calculate_future_value(present_value, rate, years):
    return present_value * (1 + rate) ** years

SIP Calculation
pythondef calculate_sip_future_value(monthly_investment, annual_rate, years):
    monthly_rate = annual_rate / 12
    months = years * 12
    if monthly_rate == 0:
        return monthly_investment * months
    return monthly_investment * (((1 + monthly_rate) ** months - 1) / monthly_rate) * (1 + monthly_rate)
    
References

Bodie, Z., Kane, A., & Marcus, A. J. (2018). Investments (11th ed.). McGraw-Hill.
Markowitz, H. (1952). Portfolio Selection. The Journal of Finance, 7(1), 77-91.
Sharpe, W. F. (1966). Mutual Fund Performance. The Journal of Business, 39(1), 119-138.

