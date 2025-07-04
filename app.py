"""
Financial Planning Tool - Main Application
MVP Version
"""
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Financial Planning Tool",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Clean, minimalist CSS inspired by modern design's design
st.markdown("""
<style>
    /* Import Inter font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* modern minimalist theme variables */
    :root {
        --primary-accent: #059669;
        --text-primary: #111827;
        --text-secondary: #6B7280;
        --text-tertiary: #9CA3AF;
        --border-light: #E5E7EB;
        --border-medium: #D1D5DB;
        --bg-white: #FFFFFF;
        --bg-gray-50: #F9FAFB;
        --bg-gray-100: #F3F4F6;
        --bg-dark: #1F2937;
        --text-dark-primary: #F9FAFB;
        --text-dark-secondary: #E5E7EB;
    }
    
    /* Global styles */
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
    }
    
    /* Override Streamlit defaults */
    .main {
        background-color: var(--bg-white);
        color: var(--text-primary);
        padding: 0;
    }
    
    /* Header */
    .app-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 2rem;
        border-bottom: 1px solid var(--border-light);
        background-color: var(--bg-white);
        position: sticky;
        top: 0;
        z-index: 100;
    }
    
    .app-logo {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        font-size: 1.5rem;
        font-weight: 600;
        color: var(--text-primary);
    }
    
    .theme-toggle {
        padding: 0.5rem;
        border: 1px solid var(--border-medium);
        border-radius: 6px;
        background: var(--bg-white);
        color: var(--text-secondary);
        cursor: pointer;
        transition: all 0.2s ease;
    }
    
    .theme-toggle:hover {
        background: var(--bg-gray-50);
        border-color: var(--primary-accent);
    }
    
    /* Main content */
    .main-content {
        max-width: 1200px;
        margin: 0 auto;
        padding: 2rem;
    }
    
    /* Typography */
    .section-title {
        font-size: 1.875rem;
        font-weight: 600;
        color: var(--text-primary);
        margin-bottom: 0.5rem;
        letter-spacing: -0.025em;
    }
    
    .section-subtitle {
        font-size: 1.125rem;
        color: var(--text-secondary);
        margin-bottom: 2rem;
    }
    
    .subsection-title {
        font-size: 1.25rem;
        font-weight: 500;
        color: var(--text-primary);
        margin-bottom: 1rem;
    }
    
    /* Cards */
    .card {
        background: var(--bg-white);
        border: 1px solid var(--border-light);
        border-radius: 8px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
    }
    
    .metric-card {
        background: var(--bg-white);
        border: 1px solid var(--border-light);
        border-radius: 8px;
        padding: 1.5rem;
        margin-bottom: 1rem;
    }
    
    .metric-value {
        font-size: 1.5rem;
        font-weight: 600;
        color: var(--text-primary);
        margin-bottom: 0.25rem;
    }
    
    .metric-label {
        font-size: 0.875rem;
        color: var(--text-secondary);
        font-weight: 500;
    }
    
    /* Status boxes */
    .info-box {
        background: var(--bg-gray-50);
        border: 1px solid var(--border-light);
        border-left: 4px solid var(--primary-accent);
        border-radius: 6px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    .warning-box {
        background: #FEF3C7;
        border: 1px solid #F59E0B;
        border-left: 4px solid #F59E0B;
        border-radius: 6px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    .success-box {
        background: #ECFDF5;
        border: 1px solid var(--primary-accent);
        border-left: 4px solid var(--primary-accent);
        border-radius: 6px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    /* Sidebar styling */
    .sidebar .stExpander {
        border: 1px solid var(--border-light);
        border-radius: 6px;
        margin-bottom: 1rem;
    }
    
    /* Footer */
    .footer {
        background: var(--bg-gray-100);
        border-top: 1px solid var(--border-light);
        padding: 3rem 2rem;
        margin-top: 4rem;
    }
    
    .footer-content {
        max-width: 1200px;
        margin: 0 auto;
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 2rem;
    }
    
    .footer-brand {
        font-weight: 600;
        color: var(--text-primary);
    }
    
    .footer-links {
        display: flex;
        gap: 2rem;
        flex-wrap: wrap;
    }
    
    .footer-links a {
        color: var(--text-secondary);
        text-decoration: none;
        font-weight: 500;
        transition: color 0.2s ease;
    }
    
    .footer-links a:hover {
        color: var(--primary-accent);
    }
    
    .copyright {
        width: 100%;
        text-align: center;
        font-size: 0.875rem;
        color: var(--text-tertiary);
        margin-top: 2rem;
        padding-top: 2rem;
        border-top: 1px solid var(--border-light);
    }
    
    /* Dark mode styles */
    [data-theme="dark"] {
        --text-primary: var(--text-dark-primary);
        --text-secondary: var(--text-dark-secondary);
        --text-tertiary: #9CA3AF;
        --bg-white: var(--bg-dark);
        --bg-gray-50: #374151;
        --bg-gray-100: #374151;
        --border-light: #4B5563;
        --border-medium: #6B7280;
    }
    
    /* Mobile responsive */
    @media (max-width: 768px) {
        .app-header {
            padding: 1rem;
        }
        
        .main-content {
            padding: 1rem;
        }
        
        .footer-content {
            flex-direction: column;
            text-align: center;
        }
        
        .footer-links {
            justify-content: center;
        }
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    .stDeployButton {display: none;}
    footer {visibility: hidden;}
    .stApp > header {visibility: hidden;}
    
    /* Charts */
    .plotly-graph-div {
        border: 1px solid var(--border-light);
        border-radius: 6px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'calculated' not in st.session_state:
    st.session_state.calculated = False
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

# Constants with clean grayscale + accent color scheme
ASSET_CLASSES = {
    'Equity': {'color': '#059669', 'expected_return': 0.12, 'risk': 0.20},
    'Bonds': {'color': '#6B7280', 'expected_return': 0.06, 'risk': 0.05},
    'Real Estate': {'color': '#9CA3AF', 'expected_return': 0.08, 'risk': 0.15},
    'Commodities': {'color': '#D1D5DB', 'expected_return': 0.07, 'risk': 0.25},
    'Crypto': {'color': '#4B5563', 'expected_return': 0.20, 'risk': 0.80},
    'Insurance': {'color': '#374151', 'expected_return': 0.04, 'risk': 0.02},
    'Emergency Fund': {'color': '#111827', 'expected_return': 0.03, 'risk': 0.01}
}

# Helper functions
def calculate_future_value(present_value, rate, years):
    """Calculate future value with compound interest"""
    return present_value * (1 + rate) ** years

def calculate_sip_future_value(monthly_investment, annual_rate, years):
    """Calculate future value of Systematic Investment Plan"""
    monthly_rate = annual_rate / 12
    months = years * 12
    if monthly_rate == 0:
        return monthly_investment * months
    return monthly_investment * (((1 + monthly_rate) ** months - 1) / monthly_rate) * (1 + monthly_rate)

def get_age_based_allocation(age):
    """Calculate recommended allocation based on age (Rule of 100)"""
    equity_percentage = max(100 - age, 20)  # Minimum 20% equity
    bond_percentage = min(age, 60)  # Maximum 60% bonds
    other_percentage = 100 - equity_percentage - bond_percentage
    
    return {
        'Equity': equity_percentage,
        'Bonds': bond_percentage,
        'Real Estate': other_percentage * 0.4,
        'Commodities': other_percentage * 0.2,
        'Crypto': max(0, min(5, 50 - age)),  # Younger people can have more crypto
        'Insurance': 5,
        'Emergency Fund': other_percentage * 0.4 - 5
    }

def calculate_portfolio_metrics(allocations):
    """Calculate expected return and risk for portfolio"""
    total_return = 0
    total_risk = 0
    
    for asset, percentage in allocations.items():
        if asset in ASSET_CLASSES:
            weight = percentage / 100
            total_return += weight * ASSET_CLASSES[asset]['expected_return']
            total_risk += (weight ** 2) * (ASSET_CLASSES[asset]['risk'] ** 2)
    
    total_risk = np.sqrt(total_risk)
    return total_return, total_risk

# Clean header with logo and theme toggle
header_col1, header_col2 = st.columns([3, 1])
with header_col1:
    st.markdown("""
    <div class="app-header">
        <div class="app-logo">
            <span>📊</span>
            <span>WealthWise</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with header_col2:
    if st.button("🌙" if not st.session_state.dark_mode else "☀️", 
                 key="theme_toggle",
                 help="Toggle dark/light mode"):
        st.session_state.dark_mode = not st.session_state.dark_mode
        st.rerun()

# Apply dark mode if enabled
if st.session_state.dark_mode:
    st.markdown("""
    <script>
        document.documentElement.setAttribute('data-theme', 'dark');
    </script>
    """, unsafe_allow_html=True)

# Main content wrapper
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Page title and description
st.markdown('<h1 class="section-title">Financial Planning Tool</h1>', unsafe_allow_html=True)
st.markdown('<p class="section-subtitle">Plan your investments and track your financial goals with data-driven insights.</p>', unsafe_allow_html=True)

# Clean sidebar
with st.sidebar:
    st.markdown("### Controls")
    
    # Personal Information
    with st.expander("Personal Information", expanded=True):
        age = st.number_input("Age", min_value=18, max_value=100, value=30, help="Your current age")
        monthly_income = st.number_input("Monthly Income ($)", min_value=0, value=5000, step=100, help="Your monthly income after taxes")
    
    # Current Portfolio
    with st.expander("Current Portfolio", expanded=True):
        st.info("Enter your current investments in each asset class")
        
        current_portfolio = {}
        total_invested = 0
        
        for asset in ASSET_CLASSES.keys():
            amount = st.number_input(
                f"{asset} ($)", 
                min_value=0.0, 
                value=0.0, 
                step=100.0,
                key=f"current_{asset}"
            )
            current_portfolio[asset] = amount
            total_invested += amount
        
        st.metric("Total Invested", f"${total_invested:,.2f}")
    
    # Investment Goals
    with st.expander("Investment Goals", expanded=True):
        monthly_investment = st.slider(
            "Monthly Investment ($)", 
            min_value=0, 
            max_value=int(monthly_income * 0.5), 
            value=int(monthly_income * 0.2),
            help="How much you plan to invest monthly"
        )
        
        investment_horizon = st.slider(
            "Investment Horizon (years)", 
            min_value=1, 
            max_value=40, 
            value=10,
            help="How long you plan to invest"
        )
    
    # Calculate button
    st.markdown("<br>", unsafe_allow_html=True)
    calculate_button = st.button("Generate Analysis", type="primary", use_container_width=True)

# Main content area
if calculate_button or st.session_state.calculated:
    st.session_state.calculated = True
    
    # Create three columns for layout
    col1, col2, col3 = st.columns([1.5, 1.5, 1])
    
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<h3 class="subsection-title">Current Portfolio Distribution</h3>', unsafe_allow_html=True)
        
        # Create clean pie chart for current portfolio
        if total_invested > 0:
            fig_current = go.Figure(data=[go.Pie(
                labels=list(current_portfolio.keys()),
                values=list(current_portfolio.values()),
                hole=.3,
                marker_colors=[ASSET_CLASSES[asset]['color'] for asset in current_portfolio.keys()],
                textinfo='label+percent',
                textfont_size=11,
                marker=dict(line=dict(color='#FFFFFF', width=1))
            )])
            fig_current.update_layout(
                height=400,
                showlegend=True,
                margin=dict(l=0, r=0, t=0, b=0),
                font=dict(family="Inter, sans-serif", size=12),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                legend=dict(
                    orientation="v",
                    yanchor="middle",
                    y=0.5,
                    xanchor="left",
                    x=1.02
                )
            )
            st.plotly_chart(fig_current, use_container_width=True)
        else:
            st.info("No current investments to display")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Calculate current portfolio percentages
        if total_invested > 0:
            current_percentages = {asset: (amount/total_invested)*100 for asset, amount in current_portfolio.items()}
        else:
            current_percentages = {asset: 0 for asset in ASSET_CLASSES.keys()}
    
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<h3 class="subsection-title">Recommended Allocation</h3>', unsafe_allow_html=True)
        
        # Get age-based recommendations
        recommended_allocation = get_age_based_allocation(age)
        
        # Create clean pie chart for recommended portfolio
        fig_recommended = go.Figure(data=[go.Pie(
            labels=list(recommended_allocation.keys()),
            values=list(recommended_allocation.values()),
            hole=.3,
            marker_colors=[ASSET_CLASSES[asset]['color'] for asset in recommended_allocation.keys()],
            textinfo='label+percent',
            textfont_size=11,
            marker=dict(line=dict(color='#FFFFFF', width=1))
        )])
        fig_recommended.update_layout(
            height=400,
            showlegend=True,
            margin=dict(l=0, r=0, t=0, b=0),
            font=dict(family="Inter, sans-serif", size=12),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            legend=dict(
                orientation="v",
                yanchor="middle",
                y=0.5,
                xanchor="left",
                x=1.02
            )
        )
        st.plotly_chart(fig_recommended, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<h3 class="subsection-title">Key Metrics</h3>', unsafe_allow_html=True)
        
        # Calculate portfolio metrics
        current_return, current_risk = calculate_portfolio_metrics(current_percentages)
        recommended_return, recommended_risk = calculate_portfolio_metrics(recommended_allocation)
        
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.markdown("**Current Portfolio**")
        st.metric("Expected Annual Return", f"{current_return*100:.1f}%")
        st.metric("Portfolio Risk (σ)", f"{current_risk*100:.1f}%")
        st.metric("Sharpe Ratio", f"{(current_return - 0.03)/current_risk:.2f}" if current_risk > 0 else "N/A")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.markdown("**Recommended Portfolio**")
        st.metric("Expected Return", f"{recommended_return*100:.1f}%")
        st.metric("Risk Level", f"{recommended_risk*100:.1f}%")
        st.metric("Sharpe Ratio", f"{(recommended_return - 0.03)/recommended_risk:.2f}" if recommended_risk > 0 else "N/A")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Clean comparison chart
    st.markdown('<h2 class="section-title">Allocation Comparison</h2>', unsafe_allow_html=True)
    
    # Create comparison dataframe
    comparison_data = []
    for asset in ASSET_CLASSES.keys():
        comparison_data.append({
            'Asset Class': asset,
            'Current %': current_percentages.get(asset, 0),
            'Recommended %': recommended_allocation.get(asset, 0),
            'Difference': recommended_allocation.get(asset, 0) - current_percentages.get(asset, 0)
        })
    
    df_comparison = pd.DataFrame(comparison_data)
    
    # Create clean grouped bar chart
    fig_comparison = go.Figure()
    fig_comparison.add_trace(go.Bar(
        name='Current Portfolio',
        x=df_comparison['Asset Class'],
        y=df_comparison['Current %'],
        marker_color='#059669',
        marker_line_width=0
    ))
    fig_comparison.add_trace(go.Bar(
        name='Recommended Portfolio',
        x=df_comparison['Asset Class'],
        y=df_comparison['Recommended %'],
        marker_color='#6B7280',
        marker_line_width=0
    ))
    fig_comparison.update_layout(
        barmode='group',
        height=400,
        xaxis_title="Asset Class",
        yaxis_title="Allocation %",
        font=dict(family="Inter, sans-serif", size=12),
        legend=dict(x=0.7, y=1),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='#E5E7EB')
    )
    st.plotly_chart(fig_comparison, use_container_width=True)
    
    # Clean future projections
    st.markdown('<h2 class="section-title">Future Value Projections</h2>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<h3 class="subsection-title">Growth Scenarios</h3>', unsafe_allow_html=True)
        
        # Calculate future values for different scenarios
        scenarios = [0.05, 0.10, 0.15]
        scenario_colors = ['#059669', '#6B7280', '#9CA3AF']
        years_range = list(range(1, investment_horizon + 1))
        
        fig_projection = go.Figure()
        
        for i, rate in enumerate(scenarios):
            future_values = []
            for year in years_range:
                fv_current = calculate_future_value(total_invested, rate, year)
                fv_sip = calculate_sip_future_value(monthly_investment, rate, year)
                future_values.append(fv_current + fv_sip)
            
            fig_projection.add_trace(go.Scatter(
                x=years_range,
                y=future_values,
                mode='lines',
                name=f'{int(rate*100)}% CAGR',
                line=dict(width=3, color=scenario_colors[i])
            ))
        
        fig_projection.update_layout(
            height=400,
            xaxis_title="Years",
            yaxis_title="Portfolio Value ($)",
            hovermode='x unified',
            yaxis_tickformat='$,.0f',
            font=dict(family="Inter, sans-serif", size=12),
            legend=dict(x=0.02, y=0.98),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=True, gridcolor='#E5E7EB')
        )
        st.plotly_chart(fig_projection, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<h3 class="subsection-title">Goal Achievement</h3>', unsafe_allow_html=True)
        
        # Calculate final values
        conservative_fv = calculate_future_value(total_invested, 0.05, investment_horizon) + \
                         calculate_sip_future_value(monthly_investment, 0.05, investment_horizon)
        moderate_fv = calculate_future_value(total_invested, 0.10, investment_horizon) + \
                     calculate_sip_future_value(monthly_investment, 0.10, investment_horizon)
        aggressive_fv = calculate_future_value(total_invested, 0.15, investment_horizon) + \
                       calculate_sip_future_value(monthly_investment, 0.15, investment_horizon)
        
        st.markdown(f"**In {investment_horizon} years, your portfolio could be worth:**")
        
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            st.metric("Conservative", f"${conservative_fv:,.0f}", f"+${conservative_fv-total_invested:,.0f}")
        with col_b:
            st.metric("Moderate", f"${moderate_fv:,.0f}", f"+${moderate_fv-total_invested:,.0f}")
        with col_c:
            st.metric("Aggressive", f"${aggressive_fv:,.0f}", f"+${aggressive_fv-total_invested:,.0f}")
        
        # Monthly SIP impact
        st.markdown(f"**Impact of ${monthly_investment} monthly investment:**")
        sip_value_10yr = calculate_sip_future_value(monthly_investment, 0.10, 10)
        st.info(f"Investing ${monthly_investment}/month for 10 years at 10% return = ${sip_value_10yr:,.0f}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Clean rebalancing recommendations
    st.markdown('<h2 class="section-title">Rebalancing Recommendations</h2>', unsafe_allow_html=True)
    
    rebalancing_needed = False
    recommendations = []
    
    for asset in ASSET_CLASSES.keys():
        current_pct = current_percentages.get(asset, 0)
        recommended_pct = recommended_allocation.get(asset, 0)
        diff = recommended_pct - current_pct
        
        if abs(diff) > 5:  # If difference is more than 5%
            rebalancing_needed = True
            if diff > 0:
                recommendations.append(f"• Increase **{asset}** allocation by {diff:.1f}%")
            else:
                recommendations.append(f"• Reduce **{asset}** allocation by {abs(diff):.1f}%")
    
    if rebalancing_needed:
        st.markdown('<div class="warning-box">', unsafe_allow_html=True)
        st.markdown("**Portfolio Rebalancing Required**")
        st.markdown("Your portfolio needs the following adjustments:")
        for rec in recommendations:
            st.markdown(rec)
        st.markdown("*Tip: Rebalance quarterly or when allocation drifts >5% from target*")
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="success-box">', unsafe_allow_html=True)
        st.markdown("**Portfolio Status: Well-Balanced**")
        st.markdown("Your current allocation aligns well with the recommended strategy for your age group.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Clean educational insights
    st.markdown('<h2 class="section-title">Educational Insights</h2>', unsafe_allow_html=True)
    st.markdown('<div class="info-box">', unsafe_allow_html=True)
    
    if age < 30:
        st.markdown("• At your age, you can afford to take more risk for higher returns")
        st.markdown("• Consider maximizing equity allocation for long-term growth")
        st.markdown("• Time is your biggest asset - start investing early")
    elif age < 50:
        st.markdown("• Balance growth with stability as you approach middle age")
        st.markdown("• Diversification becomes increasingly important")
        st.markdown("• Consider increasing bond allocation gradually")
    else:
        st.markdown("• Focus on capital preservation as you near retirement")
        st.markdown("• Reduce exposure to volatile assets like crypto")
        st.markdown("• Ensure adequate emergency fund and insurance coverage")
    
    st.markdown('</div>', unsafe_allow_html=True)

else:
    # Clean welcome screen
    st.info("Enter your information in the sidebar and click 'Generate Analysis' to get started!")
    
    # Educational content
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### How it Works")
        st.markdown("""
        1. Enter your age and income
        2. Input current investments
        3. Set investment goals
        4. Get personalized recommendations
        """)
    
    with col2:
        st.markdown("### Features")
        st.markdown("""
        - Age-based allocation
        - Future value projections
        - Risk assessment
        - Rebalancing advice
        """)
    
    with col3:
        st.markdown("### Tips")
        st.markdown("""
        - Start investing early
        - Diversify your portfolio
        - Review quarterly
        - Stay disciplined
        """)

# Close main content wrapper
st.markdown('</div>', unsafe_allow_html=True)

# Clean footer with real URLs
st.markdown("""
<div class="footer">
    <div class="footer-content">
        <div class="footer-brand">
            WealthWise
        </div>
        <div class="footer-links">
            <a href="https://www.linkedin.com/in/abhishek-tiwari-282001/" target="_blank">LinkedIn</a>
            <a href="https://twitter.com/abhishek282001" target="_blank">Twitter</a>
            <a href="mailto:abhishek282001@gmail.com" target="_blank">Contact</a>
            <a href="https://github.com/Abhishek282001Tiwari" target="_blank">GitHub</a>
        </div>
    </div>
    <div class="copyright">
        © 2024 WealthWise Financial Planning Tool. All rights reserved.<br>
        This tool provides educational guidance only. Consult a financial advisor for personalized advice.
    </div>
</div>
""", unsafe_allow_html=True)