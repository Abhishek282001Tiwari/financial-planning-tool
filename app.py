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

# Modern CSS styling with premium financial dashboard theme
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Poppins:wght@300;400;500;600;700&display=swap');
    
    /* Global theme variables */
    :root {
        --primary-mint: #00D4AA;
        --primary-teal: #008B8B;
        --accent-gold: #FFD700;
        --dark-navy: #1B2951;
        --light-gray: #F8FAFC;
        --white: #FFFFFF;
        --text-dark: #2D3748;
        --text-light: #718096;
        --border-light: #E2E8F0;
        --success-green: #10B981;
        --warning-orange: #F59E0B;
        --error-red: #EF4444;
    }
    
    /* Override Streamlit defaults */
    .main {
        padding: 0;
        background: linear-gradient(135deg, #F8FAFC 0%, #E2E8F0 100%);
    }
    
    /* Sticky header */
    .sticky-header {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 1000;
        background: linear-gradient(135deg, var(--primary-mint) 0%, var(--primary-teal) 100%);
        padding: 1rem 2rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(10px);
    }
    
    .sticky-header h1 {
        color: white;
        font-family: 'Poppins', sans-serif;
        font-weight: 700;
        font-size: 2.5rem;
        margin: 0;
        text-align: center;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    .sticky-header .subtitle {
        color: rgba(255, 255, 255, 0.9);
        font-family: 'Inter', sans-serif;
        font-size: 1.1rem;
        text-align: center;
        margin-top: 0.5rem;
    }
    
    /* Main content padding to account for sticky header */
    .main-content {
        margin-top: 140px;
        padding: 2rem;
    }
    
    /* Enhanced typography */
    .section-header {
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        font-size: 1.8rem;
        color: var(--dark-navy);
        margin-bottom: 1.5rem;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid var(--primary-mint);
    }
    
    .subsection-header {
        font-family: 'Poppins', sans-serif;
        font-weight: 500;
        font-size: 1.3rem;
        color: var(--text-dark);
        margin-bottom: 1rem;
    }
    
    /* Premium metric cards */
    .metric-card {
        background: linear-gradient(135deg, var(--white) 0%, #F9FAFB 100%);
        padding: 2rem;
        border-radius: 16px;
        border: 1px solid var(--border-light);
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.1);
    }
    
    /* Recommendation boxes */
    .recommendation-box {
        background: linear-gradient(135deg, #E6FFFA 0%, #B2F5EA 100%);
        padding: 2rem;
        border-radius: 16px;
        border-left: 6px solid var(--primary-teal);
        margin-top: 1.5rem;
        box-shadow: 0 4px 20px rgba(0, 139, 139, 0.1);
    }
    
    .warning-box {
        background: linear-gradient(135deg, #FFFBEB 0%, #FEF3C7 100%);
        padding: 2rem;
        border-radius: 16px;
        border-left: 6px solid var(--warning-orange);
        margin-top: 1.5rem;
        box-shadow: 0 4px 20px rgba(245, 158, 11, 0.1);
    }
    
    .success-box {
        background: linear-gradient(135deg, #ECFDF5 0%, #D1FAE5 100%);
        padding: 2rem;
        border-radius: 16px;
        border-left: 6px solid var(--success-green);
        margin-top: 1.5rem;
        box-shadow: 0 4px 20px rgba(16, 185, 129, 0.1);
    }
    
    /* Footer styling */
    .footer {
        background: linear-gradient(135deg, var(--dark-navy) 0%, #2D3748 100%);
        color: white;
        padding: 3rem 2rem 2rem;
        margin-top: 4rem;
        border-top: 4px solid var(--primary-mint);
    }
    
    .footer-content {
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 2rem;
    }
    
    .footer-links {
        display: flex;
        gap: 2rem;
        flex-wrap: wrap;
    }
    
    .footer-links a {
        color: var(--primary-mint);
        text-decoration: none;
        font-weight: 500;
        transition: color 0.3s ease;
    }
    
    .footer-links a:hover {
        color: var(--accent-gold);
    }
    
    .copyright {
        font-size: 0.9rem;
        color: #A0AEC0;
        margin-top: 1rem;
        text-align: center;
    }
    
    /* Chart container improvements */
    .chart-container {
        background: var(--white);
        border-radius: 16px;
        padding: 1.5rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
        border: 1px solid var(--border-light);
    }
    
    /* Hide streamlit branding */
    #MainMenu {visibility: hidden;}
    .stDeployButton {display:none;}
    footer {visibility: hidden;}
    .stApp > header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'calculated' not in st.session_state:
    st.session_state.calculated = False
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

# Constants with modern color scheme
ASSET_CLASSES = {
    'Equity': {'color': '#00D4AA', 'expected_return': 0.12, 'risk': 0.20, 'icon': '📈'},
    'Bonds': {'color': '#008B8B', 'expected_return': 0.06, 'risk': 0.05, 'icon': '🏦'},
    'Real Estate': {'color': '#8B4513', 'expected_return': 0.08, 'risk': 0.15, 'icon': '🏠'},
    'Commodities': {'color': '#FFD700', 'expected_return': 0.07, 'risk': 0.25, 'icon': '🥇'},
    'Crypto': {'color': '#F59E0B', 'expected_return': 0.20, 'risk': 0.80, 'icon': '₿'},
    'Insurance': {'color': '#1B2951', 'expected_return': 0.04, 'risk': 0.02, 'icon': '🛡️'},
    'Emergency Fund': {'color': '#10B981', 'expected_return': 0.03, 'risk': 0.01, 'icon': '💰'}
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

# Sticky header
st.markdown("""
<div class="sticky-header">
    <h1>💎 WealthWise</h1>
    <div class="subtitle">Your Premium Financial Planning Dashboard</div>
</div>
""", unsafe_allow_html=True)

# Dark mode toggle
col1, col2, col3 = st.columns([1, 1, 1])
with col3:
    if st.button("🌙 Dark Mode" if not st.session_state.dark_mode else "☀️ Light Mode"):
        st.session_state.dark_mode = not st.session_state.dark_mode
        st.rerun()

# Apply dark mode styles if enabled
if st.session_state.dark_mode:
    st.markdown("""
    <style>
        .main {
            background: linear-gradient(135deg, #1A202C 0%, #2D3748 100%);
            color: white;
        }
        .metric-card {
            background: linear-gradient(135deg, #2D3748 0%, #4A5568 100%);
            color: white;
        }
        .chart-container {
            background: #2D3748;
            color: white;
        }
        .section-header {
            color: var(--primary-mint);
        }
        .subsection-header {
            color: #E2E8F0;
        }
    </style>
    """, unsafe_allow_html=True)

# Main content wrapper
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Enhanced sidebar with expanders and icons
with st.sidebar:
    st.markdown('<div class="section-header">📊 Dashboard Controls</div>', unsafe_allow_html=True)
    
    # Personal Information Expander
    with st.expander("👤 Personal Information", expanded=True):
        age = st.number_input("Age", min_value=18, max_value=100, value=30, help="Your current age")
        monthly_income = st.number_input("💰 Monthly Income ($)", min_value=0, value=5000, step=100, help="Your monthly income after taxes")
    
    # Current Portfolio Expander
    with st.expander("💼 Current Portfolio", expanded=True):
        st.info("💡 Enter your current investments in each asset class")
        
        current_portfolio = {}
        total_invested = 0
        
        for asset in ASSET_CLASSES.keys():
            icon = ASSET_CLASSES[asset]['icon']
            amount = st.number_input(
                f"{icon} {asset} ($)", 
                min_value=0.0, 
                value=0.0, 
                step=100.0,
                key=f"current_{asset}"
            )
            current_portfolio[asset] = amount
            total_invested += amount
        
        st.metric("🎯 Total Invested", f"${total_invested:,.2f}")
    
    # Investment Goals Expander
    with st.expander("🎯 Investment Goals", expanded=True):
        monthly_investment = st.slider(
            "💳 Monthly Investment ($)", 
            min_value=0, 
            max_value=int(monthly_income * 0.5), 
            value=int(monthly_income * 0.2),
            help="How much you plan to invest monthly"
        )
        
        investment_horizon = st.slider(
            "⏰ Investment Horizon (years)", 
            min_value=1, 
            max_value=40, 
            value=10,
            help="How long you plan to invest"
        )
    
    # Calculate button with enhanced styling
    st.markdown("<br>", unsafe_allow_html=True)
    calculate_button = st.button("🚀 Generate Analysis", type="primary", use_container_width=True)

# Main content area
if calculate_button or st.session_state.calculated:
    st.session_state.calculated = True
    
    # Create three columns for layout
    col1, col2, col3 = st.columns([1.5, 1.5, 1])
    
    with col1:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.markdown('<div class="subsection-header">📊 Current Portfolio Distribution</div>', unsafe_allow_html=True)
        
        # Create enhanced pie chart for current portfolio
        if total_invested > 0:
            fig_current = go.Figure(data=[go.Pie(
                labels=list(current_portfolio.keys()),
                values=list(current_portfolio.values()),
                hole=.4,
                marker_colors=[ASSET_CLASSES[asset]['color'] for asset in current_portfolio.keys()],
                textinfo='label+percent',
                textfont_size=12,
                marker=dict(line=dict(color='#FFFFFF', width=2))
            )])
            fig_current.update_layout(
                height=450,
                showlegend=True,
                margin=dict(l=0, r=0, t=30, b=0),
                font=dict(family="Inter, sans-serif", size=14),
                legend=dict(
                    orientation="v",
                    yanchor="middle",
                    y=0.5,
                    xanchor="left",
                    x=1.05
                )
            )
            st.plotly_chart(fig_current, use_container_width=True)
        else:
            st.info("💡 No current investments to display")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Calculate current portfolio percentages
        if total_invested > 0:
            current_percentages = {asset: (amount/total_invested)*100 for asset, amount in current_portfolio.items()}
        else:
            current_percentages = {asset: 0 for asset in ASSET_CLASSES.keys()}
    
    with col2:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.markdown('<div class="subsection-header">🎯 Recommended Allocation</div>', unsafe_allow_html=True)
        
        # Get age-based recommendations
        recommended_allocation = get_age_based_allocation(age)
        
        # Create enhanced pie chart for recommended portfolio
        fig_recommended = go.Figure(data=[go.Pie(
            labels=list(recommended_allocation.keys()),
            values=list(recommended_allocation.values()),
            hole=.4,
            marker_colors=[ASSET_CLASSES[asset]['color'] for asset in recommended_allocation.keys()],
            textinfo='label+percent',
            textfont_size=12,
            marker=dict(line=dict(color='#FFFFFF', width=2))
        )])
        fig_recommended.update_layout(
            height=450,
            showlegend=True,
            margin=dict(l=0, r=0, t=30, b=0),
            font=dict(family="Inter, sans-serif", size=14),
            legend=dict(
                orientation="v",
                yanchor="middle",
                y=0.5,
                xanchor="left",
                x=1.05
            )
        )
        st.plotly_chart(fig_recommended, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="subsection-header">📈 Key Metrics</div>', unsafe_allow_html=True)
        
        # Calculate portfolio metrics
        current_return, current_risk = calculate_portfolio_metrics(current_percentages)
        recommended_return, recommended_risk = calculate_portfolio_metrics(recommended_allocation)
        
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.markdown("**📊 Current Portfolio**")
        st.metric("📈 Expected Annual Return", f"{current_return*100:.1f}%")
        st.metric("⚠️ Portfolio Risk (σ)", f"{current_risk*100:.1f}%")
        st.metric("🎯 Sharpe Ratio", f"{(current_return - 0.03)/current_risk:.2f}" if current_risk > 0 else "N/A")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.markdown("**🎯 Recommended Portfolio**")
        st.metric("📈 Expected Return", f"{recommended_return*100:.1f}%")
        st.metric("⚠️ Risk Level", f"{recommended_risk*100:.1f}%")
        st.metric("🏆 Sharpe Ratio", f"{(recommended_return - 0.03)/recommended_risk:.2f}" if recommended_risk > 0 else "N/A")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Enhanced comparison chart
    st.markdown('<div class="section-header">📊 Current vs Recommended Allocation</div>', unsafe_allow_html=True)
    
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
    
    # Create enhanced grouped bar chart
    fig_comparison = go.Figure()
    fig_comparison.add_trace(go.Bar(
        name='Current Portfolio',
        x=df_comparison['Asset Class'],
        y=df_comparison['Current %'],
        marker_color='#00D4AA',
        marker_line_color='#008B8B',
        marker_line_width=2
    ))
    fig_comparison.add_trace(go.Bar(
        name='Recommended Portfolio',
        x=df_comparison['Asset Class'],
        y=df_comparison['Recommended %'],
        marker_color='#008B8B',
        marker_line_color='#00D4AA',
        marker_line_width=2
    ))
    fig_comparison.update_layout(
        barmode='group',
        height=450,
        xaxis_title="Asset Class",
        yaxis_title="Allocation %",
        font=dict(family="Inter, sans-serif", size=14),
        legend=dict(x=0.7, y=1, bgcolor='rgba(255,255,255,0.8)'),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    st.plotly_chart(fig_comparison, use_container_width=True)
    
    # Enhanced future projections
    st.markdown('<div class="section-header">💰 Future Value Projections</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.markdown('<div class="subsection-header">📈 Growth Scenarios</div>', unsafe_allow_html=True)
        
        # Calculate future values for different scenarios
        scenarios = [0.05, 0.10, 0.15]
        scenario_colors = ['#10B981', '#00D4AA', '#FFD700']
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
                mode='lines+markers',
                name=f'{int(rate*100)}% CAGR',
                line=dict(width=4, color=scenario_colors[i]),
                marker=dict(size=6, color=scenario_colors[i])
            ))
        
        fig_projection.update_layout(
            height=450,
            xaxis_title="Years",
            yaxis_title="Portfolio Value ($)",
            hovermode='x unified',
            yaxis_tickformat='$,.0f',
            font=dict(family="Inter, sans-serif", size=14),
            legend=dict(x=0.02, y=0.98, bgcolor='rgba(255,255,255,0.8)'),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig_projection, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.markdown('<div class="subsection-header">🎯 Goal Achievement</div>', unsafe_allow_html=True)
        
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
            st.metric("🐌 Conservative", f"${conservative_fv:,.0f}", f"+${conservative_fv-total_invested:,.0f}")
        with col_b:
            st.metric("🚀 Moderate", f"${moderate_fv:,.0f}", f"+${moderate_fv-total_invested:,.0f}")
        with col_c:
            st.metric("🔥 Aggressive", f"${aggressive_fv:,.0f}", f"+${aggressive_fv-total_invested:,.0f}")
        
        # Monthly SIP impact
        st.markdown(f"**💡 Impact of ${monthly_investment} monthly investment:**")
        sip_value_10yr = calculate_sip_future_value(monthly_investment, 0.10, 10)
        st.info(f"💰 Investing ${monthly_investment}/month for 10 years at 10% return = ${sip_value_10yr:,.0f}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Enhanced rebalancing recommendations
    st.markdown('<div class="section-header">🔄 Rebalancing Recommendations</div>', unsafe_allow_html=True)
    
    rebalancing_needed = False
    recommendations = []
    
    for asset in ASSET_CLASSES.keys():
        current_pct = current_percentages.get(asset, 0)
        recommended_pct = recommended_allocation.get(asset, 0)
        diff = recommended_pct - current_pct
        
        if abs(diff) > 5:  # If difference is more than 5%
            rebalancing_needed = True
            icon = ASSET_CLASSES[asset]['icon']
            if diff > 0:
                recommendations.append(f"📈 Increase **{icon} {asset}** allocation by {diff:.1f}%")
            else:
                recommendations.append(f"📉 Reduce **{icon} {asset}** allocation by {abs(diff):.1f}%")
    
    if rebalancing_needed:
        st.markdown('<div class="warning-box">', unsafe_allow_html=True)
        st.markdown("## ⚠️ Portfolio Rebalancing Required")
        st.markdown("**Your portfolio needs the following adjustments:**")
        for rec in recommendations:
            st.markdown(rec)
        st.markdown("💡 **Tip:** Rebalance quarterly or when allocation drifts >5% from target")
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="success-box">', unsafe_allow_html=True)
        st.markdown("## ✅ Portfolio Status: Well-Balanced!")
        st.markdown("Your current allocation aligns well with the recommended strategy for your age group.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Risk assessment based on age
    st.markdown('<div class="recommendation-box">', unsafe_allow_html=True)
    st.markdown("**📚 Educational Insights:**")
    
    if age < 30:
        st.markdown("- At your age, you can afford to take more risk for higher returns")
        st.markdown("- Consider maximizing equity allocation for long-term growth")
        st.markdown("- Time is your biggest asset - start investing early!")
    elif age < 50:
        st.markdown("- Balance growth with stability as you approach middle age")
        st.markdown("- Diversification becomes increasingly important")
        st.markdown("- Consider increasing bond allocation gradually")
    else:
        st.markdown("- Focus on capital preservation as you near retirement")
        st.markdown("- Reduce exposure to volatile assets like crypto")
        st.markdown("- Ensure adequate emergency fund and insurance coverage")
    
    st.markdown('</div>', unsafe_allow_html=True)

else:
    # Welcome screen
    st.info("👈 Enter your information in the sidebar and click 'Calculate Results' to get started!")
    
    # Educational content
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 📚 How it Works")
        st.markdown("""
        1. Enter your age and income
        2. Input current investments
        3. Set investment goals
        4. Get personalized recommendations
        """)
    
    with col2:
        st.markdown("### 🎯 Features")
        st.markdown("""
        - Age-based allocation
        - Future value projections
        - Risk assessment
        - Rebalancing advice
        """)
    
    with col3:
        st.markdown("### 💡 Tips")
        st.markdown("""
        - Start investing early
        - Diversify your portfolio
        - Review quarterly
        - Stay disciplined
        """)
    
    # Footer
    # Close main content wrapper
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Premium footer
    st.markdown("""
    <div class="footer">
        <div class="footer-content">
            <div>
                <h3>💎 WealthWise</h3>
                <p>Your Premium Financial Planning Dashboard</p>
            </div>
            <div class="footer-links">
                <a href="#" target="_blank">📊 LinkedIn</a>
                <a href="#" target="_blank">🐦 Twitter</a>
                <a href="#" target="_blank">📧 Contact</a>
                <a href="#" target="_blank">📝 Blog</a>
            </div>
        </div>
        <div class="copyright">
            © 2024 WealthWise Financial Planning Tool. All rights reserved.<br>
            💡 This tool provides educational guidance only. Consult a financial advisor for personalized advice.
        </div>
    </div>
    """, unsafe_allow_html=True)