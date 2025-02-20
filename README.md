# Revenue Waterfall Prediction

An interactive Python-based tool for forecasting annual revenue using a revenue waterfall model. This application allows users to adjust key parameters such as project churn, new project enrollments, average annual prices for different revenue categories, and growth assumptions to generate a customized forecast. The tool is built with [Streamlit](https://streamlit.io/) for a dynamic, user-friendly UI.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)

## Overview

This tool provides a revenue waterfall prediction model that forecasts future annual revenue by combining:
- **Active Projects:** The number of ongoing projects.
- **New Projects & Churn:** Adjustments based on new projects enrolled and projects lost.
- **Revenue Streams:** Calculations for service contracts, spare parts, and other service products.
- **Growth Assumptions:** Annual growth rates applied to spare parts purchases and other configurable parameters.

The forecast is visualized with interactive charts, allowing users to see both the total revenue trend and the breakdown by revenue category.

## Features

- **Interactive UI:** Easily adjust parameters through the sidebar.
- **Revenue Forecasting:** Calculates revenue for each forecast year based on provided inputs.
- **Dynamic Visualizations:** Line and stacked bar charts display total revenue trends and revenue breakdown.
- **Customizable Inputs:** Default values are provided, and users can fine-tune parameters such as:
  - Base year, forecast start, and end years.
  - Active projects, new projects per year, and churn projects per year.
  - Average annual prices for service contracts, spare parts, and other services.
  - Spare parts annual growth rate.


## Installation

```bash

git clone https://github.com/xinnnan/revenue-waterfall-prediction.git
cd revenue-waterfall-prediction
pip3 install -r requirements.txt
python3 -m streamlit run main.py


