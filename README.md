# Luxury Fashion Pricing & Demand Trends

This project explores what drives the pricing of luxury fashion products — from brand popularity to social media hype — using data from Ssense and Google Trends. It combines data cleaning, SQL analytics, machine learning, and dashboarding to uncover what makes brands like Gucci and Prada so expensive.

---

## Project Objectives

- Analyze pricing trends of luxury fashion brands
- Explore the impact of brand popularity (Google Trends) on pricing
- Predict product prices using machine learning models
- Build a Power BI dashboard for interactive insights

---

## Tools Used

| Tool            | Purpose                           |
|-----------------|------------------------------------|
| Python (Pandas) | Data cleaning & processing         |
| SQLite & SQL    | Query-based analysis               |
| Scikit-learn    | Price prediction (ML modeling)     |
| Power BI        | Interactive dashboard visualizations|
| Plotly / Seaborn| Exploratory data visualizations    |

---

## Data Sources

- **Product Pricing**: Ssense scraped data (brand, price, category, etc.)
- **Brand Popularity**: Google Trends API
- [Optional: StockX Resale or Twitter Mentions if included]

---

## Key Insights

- Gradient Boosting predicted price with **MAE: ~$628**
- Popularity and pricing show moderate correlation for brands like Gucci
- Certain categories like sneakers have more stable pricing than accessories
- Limited brand coverage from Google Trends may affect prediction scope

---

## Tableau Dashboard

This interactive Tableau dashboard visualizes pricing and popularity trends across luxury fashion brands. It includes:

- Brand popularity and pricing over time (Google Trends × Ssense)
- Price distribution by product category (e.g., bags, sneakers)
- Average price by brand
- Filters by brand, product type, and time for dynamic exploration

![Dashboard Screenshot](../tableau/exports/dashboard_screenshot.png)

> **File**: `tableau/luxury_fashion_dashboard.twb`  
---

## Machine Learning Model

- Linear Regression vs. Gradient Boosting
- Features:
  - `brand_popularity`
  - `product_type` (one-hot)
  - `brand` (one-hot)
  - `description_length`
- Best Model: **Gradient Boosting Regressor**
- Evaluation:
  - **MAE:** 627.88
  - **RMSE:** 851.07
