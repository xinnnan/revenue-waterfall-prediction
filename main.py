import streamlit as st
import pandas as pd
import plotly.express as px

def forecast_revenue(
    base_year,
    forecast_start,
    forecast_end,
    base_active_projects,
    avg_service_contract,
    avg_spare_parts,
    avg_other_service,
    new_projects_per_year,
    churn_projects_per_year,
    spare_parts_growth_rate
):
    """
    Forecast revenue from the base year using a waterfall approach.
    
    For each forecast year:
      - Update the active projects count: subtract churn and add new projects.
      - Service Contract Revenue = Active Projects * Average Service Contract Price.
      - Spare Parts Revenue = Active Projects * (Average Spare Parts Purchase * (1 + growth_rate)^(year - base_year)).
      - Other Service Revenue = Active Projects * Average Other Service Price.
      - Total Revenue = Sum of the above.
    """
    forecast_data = []
    active_projects = base_active_projects

    # Forecast year by year from forecast_start to forecast_end
    for year in range(forecast_start, forecast_end + 1):
        # Update active projects: apply churn then add new projects
        active_projects = active_projects - churn_projects_per_year + new_projects_per_year
        
        # Compute each revenue component
        service_revenue = active_projects * avg_service_contract
        
        # Assume spare parts revenue per project grows each year
        effective_avg_spare_parts = avg_spare_parts * ((1 + spare_parts_growth_rate) ** (year - base_year))
        spare_parts_revenue = active_projects * effective_avg_spare_parts
        
        other_service_revenue = active_projects * avg_other_service
        
        total_revenue = service_revenue + spare_parts_revenue + other_service_revenue
        
        forecast_data.append({
            'Year': year,
            'Active Projects': active_projects,
            'Service Contract Revenue': service_revenue,
            'Spare Parts Revenue': spare_parts_revenue,
            'Other Service Revenue': other_service_revenue,
            'Total Revenue': total_revenue
        })
    
    df_forecast = pd.DataFrame(forecast_data)
    return df_forecast

def main():
    st.title("Annual Revenue Waterfall Prediction Model")
    st.write("Customize parameters below to forecast future revenue growth based on your project pipeline data.")
    
    st.sidebar.header("Forecast Timeframe")
    base_year = st.sidebar.number_input("Base Year", value=2024, step=1)
    forecast_start = st.sidebar.number_input("Forecast Start Year", value=2025, step=1)
    forecast_end = st.sidebar.number_input("Forecast End Year", value=2030, step=1)
    
    st.sidebar.header("Project Numbers")
    base_active_projects = st.sidebar.number_input("Active Projects in Base Year", value=25, step=1)
    new_projects_per_year = st.sidebar.number_input("New Projects per Year", value=8, step=1)
    churn_projects_per_year = st.sidebar.number_input("Churn Projects per Year", value=5, step=1)
    
    st.sidebar.header("Average Annual Prices (per Project)")
    avg_service_contract = st.sidebar.number_input("Avg Service Contract Price", value=40000.0, step=1000.0, format="%.2f")
    avg_spare_parts = st.sidebar.number_input("Avg Spare Parts Purchase", value=60000.0, step=1000.0, format="%.2f")
    avg_other_service = st.sidebar.number_input("Avg Other Service Price", value=30000.0, step=1000.0, format="%.2f")
    
    st.sidebar.header("Growth Assumptions")
    spare_parts_growth_rate = st.sidebar.slider("Spare Parts Growth Rate (annual)", 0.0, 0.5, 0.05, 0.01)
    
    run_forecast = st.sidebar.button("Run Forecast")
    
    if run_forecast:
        df_forecast = forecast_revenue(
            base_year=base_year,
            forecast_start=forecast_start,
            forecast_end=forecast_end,
            base_active_projects=base_active_projects,
            avg_service_contract=avg_service_contract,
            avg_spare_parts=avg_spare_parts,
            avg_other_service=avg_other_service,
            new_projects_per_year=new_projects_per_year,
            churn_projects_per_year=churn_projects_per_year,
            spare_parts_growth_rate=spare_parts_growth_rate
        )
        
        st.subheader("Forecast Results")
        st.dataframe(df_forecast)
        
        # Plot total revenue over forecast years
        fig = px.line(df_forecast, x="Year", y="Total Revenue", title="Total Revenue Forecast")
        st.plotly_chart(fig)
        
        # Plot revenue breakdown by category as a stacked bar chart
        fig2 = px.bar(
            df_forecast,
            x="Year",
            y=["Service Contract Revenue", "Spare Parts Revenue", "Other Service Revenue"],
            title="Revenue Breakdown by Category",
            barmode='stack'
        )
        st.plotly_chart(fig2)

if __name__ == "__main__":
    main()
