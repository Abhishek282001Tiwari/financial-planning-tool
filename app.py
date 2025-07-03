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

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #2c3e50;
        padding: 1rem;
        background-color: #ecf0f1;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid #e9ecef;
        margin-bottom: 1rem;
    }
    .recommendation-box {
        background-color: #e3f2fd;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #1976d2;
        margin-top: 1rem;
    }
    .warning-box {
        background-color: #fff3cd;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #ffc107;
        margin-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'calculated' not in st.session_state:
    st.session_state.calculated = False

# Constants
ASSET_CLASSES = {
    'Equity': {'color': '#3498db', 'expected_return': 0.12, 'risk': 0.20},
    'Bonds': {'color': '#2ecc71', 'expected_return': 0.06, 'risk': 0.05},
    'Real Estate': {'color': '#8b4513', 'expected_return': 0.08, 'risk': 0.15},
    'Commodities': {'color': '#f1c40f', 'expected_return': 0.07, 'risk': 0.25},
    'Crypto': {'color': '#f39c12', 'expected_return': 0.20, 'risk': 0.80},
    'Insurance': {'color': '#9b59b6', 'expected_return': 0.04, 'risk': 0.02},
    'Emergency Fund': {'color': '#95a5a6', 'expected_return': 0.03, 'risk': 0.01}
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

# Main app
st.markdown('<div class="main-header"><h1>💰 Financial Planning & Portfolio Allocation Tool</h1></div>', unsafe_allow_html=True)

# Sidebar for inputs
with st.sidebar:
    st.header("📝 Your Information")
    
    # Basic inputs
    age = st.number_input("Age", min_value=18, max_value=100, value=30, help="Your current age")
    monthly_income = st.number_input("Monthly Income ($)", min_value=0, value=5000, step=100, help="Your monthly income after taxes")
    
    st.header("💼 Current Portfolio")
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
    
    st.header("🎯 Investment Goals")
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
    
    calculate_button = st.button("📊 Calculate Results", type="primary", use_container_width=True)

# Main content area
if calculate_button or st.session_state.calculated:
    st.session_state.calculated = True
    
    # Create three columns for layout
    col1, col2, col3 = st.columns([1.5, 1.5, 1])
    
    with col1:
        st.subheader("📊 Current Portfolio Distribution")
        
        # Create pie chart for current portfolio
        if total_invested > 0:
            fig_current = go.Figure(data=[go.Pie(
                labels=list(current_portfolio.keys()),
                values=list(current_portfolio.values()),
                hole=.3,
                marker_colors=[ASSET_CLASSES[asset]['color'] for asset in current_portfolio.keys()]
            )])
            fig_current.update_layout(
                height=400,
                showlegend=True,
                margin=dict(l=0, r=0, t=30, b=0)
            )
            st.plotly_chart(fig_current, use_container_width=True)
        else:
            st.info("No current investments to display")
        
        # Calculate current portfolio percentages
        if total_invested > 0:
            current_percentages = {asset: (amount/total_invested)*100 for asset, amount in current_portfolio.items()}
        else:
            current_percentages = {asset: 0 for asset in ASSET_CLASSES.keys()}
    
    with col2:
        st.subheader("🎯 Recommended Allocation")
        
        # Get age-based recommendations
        recommended_allocation = get_age_based_allocation(age)
        
        # Create pie chart for recommended portfolio
        fig_recommended = go.Figure(data=[go.Pie(
            labels=list(recommended_allocation.keys()),
            values=list(recommended_allocation.values()),
            hole=.3,
            marker_colors=[ASSET_CLASSES[asset]['color'] for asset in recommended_allocation.keys()]
        )])
        fig_recommended.update_layout(
            height=400,
            showlegend=True,
            margin=dict(l=0, r=0, t=30, b=0)
        )
        st.plotly_chart(fig_recommended, use_container_width=True)
    
    with col3:
        st.subheader("📈 Key Metrics")
        
        # Calculate portfolio metrics
        current_return, current_risk = calculate_portfolio_metrics(current_percentages)
        recommended_return, recommended_risk = calculate_portfolio_metrics(recommended_allocation)
        
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Expected Annual Return", f"{current_return*100:.1f}%")
        st.metric("Portfolio Risk (σ)", f"{current_risk*100:.1f}%")
        st.metric("Sharpe Ratio", f"{(current_return - 0.03)/current_risk:.2f}" if current_risk > 0 else "N/A")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.markdown("**Recommended Portfolio:**")
        st.metric("Expected Return", f"{recommended_return*100:.1f}%")
        st.metric("Risk Level", f"{recommended_risk*100:.1f}%")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Comparison chart
    st.subheader("📊 Current vs Recommended Allocation")
    
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
    
    # Create grouped bar chart
    fig_comparison = go.Figure()
    fig_comparison.add_trace(go.Bar(
        name='Current',
        x=df_comparison['Asset Class'],
        y=df_comparison['Current %'],
        marker_color='lightblue'
    ))
    fig_comparison.add_trace(go.Bar(
        name='Recommended',
        x=df_comparison['Asset Class'],
        y=df_comparison['Recommended %'],
        marker_color='darkblue'
    ))
    fig_comparison.update_layout(
        barmode='group',
        height=400,
        xaxis_title="Asset Class",
        yaxis_title="Allocation %",
        legend=dict(x=0.7, y=1)
    )
    st.plotly_chart(fig_comparison, use_container_width=True)
    
    # Future projections
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("💰 Future Value Projections")
        
        # Calculate future values for different scenarios
        scenarios = [0.05, 0.10, 0.15]
        years_range = list(range(1, investment_horizon + 1))
        
        fig_projection = go.Figure()
        
        for rate in scenarios:
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
                line=dict(width=3)
            ))
        
        fig_projection.update_layout(
            height=400,
            xaxis_title="Years",
            yaxis_title="Portfolio Value ($)",
            hovermode='x unified',
            yaxis_tickformat='$,.0f'
        )
        st.plotly_chart(fig_projection, use_container_width=True)
    
    with col2:
        st.subheader("🎯 Goal Achievement")
        
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
        st.info(f"💡 Investing ${monthly_investment}/month for 10 years at 10% return = ${sip_value_10yr:,.0f}")
    
    # Rebalancing recommendations
    st.subheader("🔄 Rebalancing Recommendations")
    
    rebalancing_needed = False
    recommendations = []
    
    for asset in ASSET_CLASSES.keys():
        current_pct = current_percentages.get(asset, 0)
        recommended_pct = recommended_allocation.get(asset, 0)
        diff = recommended_pct - current_pct
        
        if abs(diff) > 5:  # If difference is more than 5%
            rebalancing_needed = True
            if diff > 0:
                recommendations.append(f"✅ Increase **{asset}** allocation by {diff:.1f}%")
            else:
                recommendations.append(f"⚠️ Reduce **{asset}** allocation by {abs(diff):.1f}%")
    
    if rebalancing_needed:
        st.markdown('<div class="warning-box">', unsafe_allow_html=True)
        st.markdown("**Your portfolio needs rebalancing:**")
        for rec in recommendations:
            st.markdown(rec)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.success("✅ Your portfolio is well-balanced!")
    
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
    st.markdown("---")
    st.markdown("💡 **Remember:** This tool provides educational guidance only. Consult a financial advisor for personalized advice.")