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

# Ultra-clean, modern minimalist CSS
st.markdown("""
<style>
    /* Import Inter font - modern design's choice */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* modern design-exact color palette */
    :root {
        --bg-primary: #FFFFFF;
        --bg-accent: #ECEEF3;
        --bg-sidebar: #F9FAFB;
        --bg-footer: #F1F5F9;
        --text-primary: #1A1A1A;
        --text-secondary: #6B7280;
        --text-light: #9CA3AF;
        --link-color: #3B82F6;
        --button-soft-blue: #3B82F6;
        --button-soft-red: #EF4444;
        --border-subtle: #E5E7EB;
        --border-light: #F3F4F6;
    }
    
    /* Global reset and base styles */
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        scroll-behavior: smooth;
    }
    
    /* Override Streamlit defaults completely */
    .main {
        background-color: var(--bg-primary);
        color: var(--text-primary);
        padding: 0;
    }
    
    .block-container {
        padding: 0;
        max-width: none;
    }
    
    /* modern sticky header */
    .claude-header {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 1000;
        background: var(--bg-primary);
        border-bottom: 1px solid var(--border-subtle);
        padding: 1rem 2rem;
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
    }
    
    .header-content {
        max-width: 1200px;
        margin: 0 auto;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .logo {
        font-size: 1.5rem;
        font-weight: 600;
        color: var(--text-primary);
        text-decoration: none;
    }
    
    /* Main content with proper spacing */
    .main-content {
        margin-top: 80px;
        max-width: 1200px;
        margin-left: auto;
        margin-right: auto;
        padding: 3rem 2rem;
        animation: fadeIn 0.6s ease-out;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* modern typography hierarchy */
    .hero-title {
        font-size: 3rem;
        font-weight: 600;
        color: var(--text-primary);
        line-height: 1.1;
        letter-spacing: -0.02em;
        margin-bottom: 1rem;
    }
    
    .hero-subtitle {
        font-size: 1.25rem;
        color: var(--text-secondary);
        line-height: 1.6;
        margin-bottom: 3rem;
        max-width: 600px;
    }
    
    .section-title {
        font-size: 2rem;
        font-weight: 600;
        color: var(--text-primary);
        margin: 3rem 0 1.5rem 0;
        letter-spacing: -0.015em;
    }
    
    .subsection-title {
        font-size: 1.25rem;
        font-weight: 500;
        color: var(--text-primary);
        margin-bottom: 1rem;
    }
    
    /* Clean sidebar styling */
    .sidebar .sidebar-content {
        background: var(--bg-sidebar);
        border-right: 1px solid var(--border-subtle);
        padding: 2rem 1.5rem;
    }
    
    /* Soft, rounded input elements */
    .stNumberInput > div > div > input,
    .stSlider > div > div > div > div,
    .stSelectbox > div > div {
        border-radius: 12px;
        border: 1px solid var(--border-subtle);
        background: var(--bg-primary);
        transition: all 0.2s ease;
    }
    
    .stNumberInput > div > div > input:focus,
    .stSelectbox > div > div:focus {
        border-color: var(--link-color);
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
        outline: none;
    }
    
    /* Clean button styling */
    .stButton > button {
        background: var(--button-soft-blue);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 2rem;
        font-weight: 500;
        transition: all 0.2s ease;
        box-shadow: none;
    }
    
    .stButton > button:hover {
        background: #2563EB;
        transform: translateY(-1px);
    }
    
    /* Soft card design */
    .metric-card {
        background: var(--bg-primary);
        border: 1px solid var(--border-light);
        border-radius: 15px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        border-color: var(--border-subtle);
        transform: translateY(-2px);
    }
    
    /* Status indicators - soft colors */
    .info-box {
        background: #F0F9FF;
        border: 1px solid #BAE6FD;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1.5rem 0;
    }
    
    .warning-box {
        background: #FFFBEB;
        border: 1px solid #FDE68A;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1.5rem 0;
    }
    
    .success-box {
        background: #F0FDF4;
        border: 1px solid #BBF7D0;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1.5rem 0;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background: var(--bg-primary);
        border: 1px solid var(--border-light);
        border-radius: 12px;
        font-weight: 500;
    }
    
    /* Chart containers */
    .chart-container {
        background: var(--bg-primary);
        border: 1px solid var(--border-light);
        border-radius: 15px;
        padding: 1.5rem;
        margin-bottom: 2rem;
    }
    
    /* modern footer */
    .claude-footer {
        background: var(--bg-footer);
        border-top: 1px solid var(--border-subtle);
        margin-top: 5rem;
        padding: 3rem 0;
    }
    
    .footer-content {
        max-width: 1200px;
        margin: 0 auto;
        text-align: center;
        padding: 0 2rem;
    }
    
    .footer-links {
        display: flex;
        justify-content: center;
        gap: 3rem;
        margin-bottom: 2rem;
        flex-wrap: wrap;
    }
    
    .footer-links a {
        color: var(--text-secondary);
        text-decoration: none;
        font-weight: 500;
        transition: all 0.2s ease;
        position: relative;
    }
    
    .footer-links a:hover {
        color: var(--text-primary);
    }
    
    .footer-links a:hover::after {
        content: '';
        position: absolute;
        bottom: -4px;
        left: 0;
        right: 0;
        height: 1px;
        background: var(--text-primary);
    }
    
    .footer-copyright {
        color: var(--text-light);
        font-size: 0.875rem;
        padding-top: 2rem;
        border-top: 1px solid var(--border-subtle);
    }
    
    /* Mobile responsiveness */
    @media (max-width: 768px) {
        .claude-header {
            padding: 1rem;
        }
        
        .main-content {
            padding: 2rem 1rem;
        }
        
        .hero-title {
            font-size: 2rem;
        }
        
        .footer-links {
            gap: 2rem;
        }
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    .stDeployButton {display: none;}
    footer {visibility: hidden;}
    .stApp > header {visibility: hidden;}
    
    /* Smooth scrolling for the entire page */
    html {
        scroll-behavior: smooth;
    }
    
    /* Chart styling to match modern design aesthetic */
    .plotly-graph-div {
        border-radius: 15px;
        overflow: hidden;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'calculated' not in st.session_state:
    st.session_state.calculated = False

# Constants with soft, modern color palette
ASSET_CLASSES = {
    'Equity': {'color': '#3B82F6', 'expected_return': 0.12, 'risk': 0.20},
    'Bonds': {'color': '#8B5CF6', 'expected_return': 0.06, 'risk': 0.05},
    'Real Estate': {'color': '#06B6D4', 'expected_return': 0.08, 'risk': 0.15},
    'Commodities': {'color': '#84CC16', 'expected_return': 0.07, 'risk': 0.25},
    'Crypto': {'color': '#F59E0B', 'expected_return': 0.20, 'risk': 0.80},
    'Insurance': {'color': '#EF4444', 'expected_return': 0.04, 'risk': 0.02},
    'Emergency Fund': {'color': '#6B7280', 'expected_return': 0.03, 'risk': 0.01}
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

# modern sticky header
st.markdown("""
<div class="claude-header">
    <div class="header-content">
        <div class="logo">WealthWise</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Main content wrapper with hero section
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Hero section - modern design style
st.markdown('<h1 class="hero-title">Smart Financial Planning</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">Plan your investments and track your financial goals with data-driven insights. Get personalized recommendations based on your age and risk profile.</p>', unsafe_allow_html=True)

# Clean sidebar with soft styling
with st.sidebar:
    st.markdown("### Input Parameters")
    
    # Personal Information
    with st.expander("👤 Personal Information", expanded=True):
        age = st.number_input("Age", min_value=18, max_value=100, value=30, help="Your current age")
        monthly_income = st.number_input("Monthly Income ($)", min_value=0, value=5000, step=100, help="Your monthly income after taxes")
    
    # Current Portfolio
    with st.expander("💼 Current Portfolio", expanded=True):
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
    with st.expander("🎯 Investment Goals", expanded=True):
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
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.markdown('<h3 class="subsection-title">Current Portfolio Distribution</h3>', unsafe_allow_html=True)
        
        # Create soft, modern pie chart
        if total_invested > 0:
            fig_current = go.Figure(data=[go.Pie(
                labels=list(current_portfolio.keys()),
                values=list(current_portfolio.values()),
                hole=.4,
                marker_colors=[ASSET_CLASSES[asset]['color'] for asset in current_portfolio.keys()],
                textinfo='label+percent',
                textfont_size=11,
                marker=dict(line=dict(color='#FFFFFF', width=2))
            )])
            fig_current.update_layout(
                height=400,
                showlegend=True,
                margin=dict(l=0, r=0, t=0, b=0),
                font=dict(family="Inter, sans-serif", size=12, color='#1A1A1A'),
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
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.markdown('<h3 class="subsection-title">Recommended Allocation</h3>', unsafe_allow_html=True)
        
        # Get age-based recommendations
        recommended_allocation = get_age_based_allocation(age)
        
        # Create soft, modern pie chart
        fig_recommended = go.Figure(data=[go.Pie(
            labels=list(recommended_allocation.keys()),
            values=list(recommended_allocation.values()),
            hole=.4,
            marker_colors=[ASSET_CLASSES[asset]['color'] for asset in recommended_allocation.keys()],
            textinfo='label+percent',
            textfont_size=11,
            marker=dict(line=dict(color='#FFFFFF', width=2))
        )])
        fig_recommended.update_layout(
            height=400,
            showlegend=True,
            margin=dict(l=0, r=0, t=0, b=0),
            font=dict(family="Inter, sans-serif", size=12, color='#1A1A1A'),
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
    
    # Soft comparison chart
    st.markdown('<h2 class="section-title">Portfolio Comparison</h2>', unsafe_allow_html=True)
    
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
    
    # Create soft, modern grouped bar chart
    fig_comparison = go.Figure()
    fig_comparison.add_trace(go.Bar(
        name='Current Portfolio',
        x=df_comparison['Asset Class'],
        y=df_comparison['Current %'],
        marker_color='#3B82F6',
        marker_line_width=0,
        opacity=0.8
    ))
    fig_comparison.add_trace(go.Bar(
        name='Recommended Portfolio',
        x=df_comparison['Asset Class'],
        y=df_comparison['Recommended %'],
        marker_color='#6B7280',
        marker_line_width=0,
        opacity=0.8
    ))
    fig_comparison.update_layout(
        barmode='group',
        height=400,
        xaxis_title="Asset Class",
        yaxis_title="Allocation %",
        font=dict(family="Inter, sans-serif", size=12, color='#1A1A1A'),
        legend=dict(x=0.7, y=1, bgcolor='rgba(255,255,255,0.9)'),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False, linecolor='#E5E7EB'),
        yaxis=dict(showgrid=True, gridcolor='#F3F4F6', linecolor='#E5E7EB')
    )
    st.plotly_chart(fig_comparison, use_container_width=True)
    
    # Soft future projections
    st.markdown('<h2 class="section-title">Growth Projections</h2>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.markdown('<h3 class="subsection-title">Growth Scenarios</h3>', unsafe_allow_html=True)
        
        # Calculate future values for different scenarios
        scenarios = [0.05, 0.10, 0.15]
        scenario_colors = ['#3B82F6', '#8B5CF6', '#06B6D4']
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
                line=dict(width=3, color=scenario_colors[i]),
                opacity=0.8
            ))
        
        fig_projection.update_layout(
            height=400,
            xaxis_title="Years",
            yaxis_title="Portfolio Value ($)",
            hovermode='x unified',
            yaxis_tickformat='$,.0f',
            font=dict(family="Inter, sans-serif", size=12, color='#1A1A1A'),
            legend=dict(x=0.02, y=0.98, bgcolor='rgba(255,255,255,0.9)'),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(showgrid=False, linecolor='#E5E7EB'),
            yaxis=dict(showgrid=True, gridcolor='#F3F4F6', linecolor='#E5E7EB')
        )
        st.plotly_chart(fig_projection, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
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

# modern footer
st.markdown("""
<div class="claude-footer">
    <div class="footer-content">
        <div class="footer-links">
            <a href="https://www.linkedin.com/in/abhishek282001tiwari/" target="_blank">LinkedIn</a>
            <a href="https://twitter.com/yourhandle" target="_blank">Twitter</a>
            <a href="https://github.com/Abhishek282001Tiwari" target="_blank">GitHub</a>
            <a href="mailto:youremail@example.com" target="_blank">Contact</a>
        </div>
        <div class="footer-copyright">
            © 2024 WealthWise. This tool provides educational guidance only.
        </div>
    </div>
</div>
""", unsafe_allow_html=True)