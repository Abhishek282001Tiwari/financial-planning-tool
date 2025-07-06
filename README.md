# GitHub Repository Setup Files

## 2. README.md
```markdown
# Financial Planning Calculator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-brightgreen)](https://abhishek282001tiwari.github.io/financial-planning-tool/)

## Live Demo
**[Financial Planning Calculator](https://abhishek282001tiwari.github.io/financial-planning-tool/)** - Try it now!

## Overview

A free, open-source financial planning tool that helps users optimize their portfolio allocation based on age, risk tolerance, and financial goals. Built with modern portfolio theory principles and designed for educational purposes.

## Key Features

- Real-time Portfolio Visualization - Interactive charts showing current vs recommended allocation
- Age-based Asset Allocation - Intelligent recommendations using the Rule of 100
- Future Value Projections - Multiple CAGR scenarios (5%, 10%, 15%)
- Rebalancing Suggestions - Clear actionable advice for portfolio optimization
- Educational Insights - Learn financial concepts while planning
- Mobile Responsive - Works seamlessly on all devices
- Dark Theme - Modern, clean interface with optimal readability

## Quick Start

### Option 1: Use Online (Recommended)

Simply visit the live demo: **[Financial Planning Calculator](https://abhishek282001tiwari.github.io/financial-planning-tool/)**

### Option 2: Run Locally

```bash
# Clone the repository
git clone https://github.com/Abhishek282001Tiwari/financial-planning-tool.git
cd financial-planning-tool

# Open index.html in your browser
open index.html
```

### Option 3: Deploy to GitHub Pages

1. Fork this repository
2. Go to Settings > Pages
3. Select "Deploy from a branch"
4. Choose "main" branch
5. Your site will be available at `https://yourusername.github.io/financial-planning-tool/`

## How to Use

1. **Enter Your Information**
   - Age and monthly income
   - Current investments across 7 asset classes

2. **Set Investment Goals**
   - Monthly investment amount
   - Investment horizon

3. **Analyze Results**
   - View current vs recommended allocation
   - See future projections
   - Get rebalancing recommendations

## Financial Calculations

### Future Value Formula
```
FV = PV × (1 + r)^n
```

### SIP (Systematic Investment Plan) Formula
```
FV_SIP = P × [((1 + r)^n - 1) / r] × (1 + r)
```

### Age-based Allocation (Rule of 100)
```
Equity % = 100 - Age
Bonds % = Age
```

## Asset Classes Supported

| Asset Class | Expected Return | Risk (σ) | Color |
|------------|----------------|----------|-------|
| Equity | 12% | 20% | Blue |
| Bonds | 6% | 5% | Green |
| Real Estate | 8% | 15% | Brown |
| Commodities | 7% | 25% | Gold |
| Crypto | 20% | 80% | Orange |
| Insurance | 4% | 2% | Purple |
| Emergency Fund | 3% | 1% | Gray |

## Project Structure

```
financial-planning-tool/
├── index.html            # Main web application
├── README.md           # Project documentation
├── LICENSE             # MIT License
├── .github/workflows/  # GitHub Actions for deployment
├── docs/              # Additional documentation
│   ├── formulas.md    # Mathematical formulas
│   └── theory.md      # Portfolio theory explanation
└── images/            # Screenshots and diagrams
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Educational Resources

- [Modern Portfolio Theory](docs/theory.md)
- [Financial Formulas Explained](docs/formulas.md)
- [Markowitz Portfolio Theory](https://en.wikipedia.org/wiki/Modern_portfolio_theory)
- [Black-Litterman Model](https://en.wikipedia.org/wiki/Black%E2%80%93Litterman_model)

## Roadmap

### Version 1.0 (Current)
- ✅ Basic portfolio allocation
- ✅ Future value calculations
- ✅ Age-based recommendations
- ✅ Rebalancing suggestions
- ✅ Dark theme interface
- ✅ GitHub Pages deployment

### Version 2.0 (Planned)
- [ ] Monte Carlo simulations
- [ ] Tax optimization
- [ ] Historical backtesting
- [ ] PDF report generation
- [ ] Multi-currency support

### Version 3.0 (Future)
- [ ] Machine learning predictions
- [ ] Social benchmarking
- [ ] Advanced risk metrics
- [ ] Options strategies

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Harry Markowitz** - Modern Portfolio Theory
- **Fischer Black & Robert Litterman** - Black-Litterman Model
- **Open Source Community** - Continuous inspiration
- **Plotly.js** - Interactive charting library

## Contact

- **Author**: Abhishek Pankaj Tiwari
- **Email**: abhishekt282001@gmail.com
- **LinkedIn**: [linkedin.com/in/yourprofile](www.linkedin.com/in/abhishek282001)
- **Twitter**: [@yourhandle](https://x.com/abhishekt282001)

## Performance Metrics

- **Load Time**: < 2 seconds
- **Calculation Time**: < 100ms
- **Mobile Responsive**: Yes
- **Dark Theme**: Optimized for readability
- **No Server Required**: Pure client-side application

---

**Disclaimer**: This tool is for educational purposes only. Always consult with a qualified financial advisor before making investment decisions.

Made for the open-source community
