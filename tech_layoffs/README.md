# Tech Layoffs Tracker
*A quiet observation of shifts in the digital landscape.*

---

## The Essence
This project serves as a basin for data regarding technology sector layoffs. It aggregates, cleans, and visualizes workforce reductions to offer a clear, unadorned view of global industry trends. The analysis currently bridges the historical data of 2024 with the unfolding patterns of 2025.

---

## The Layout
A structured approach to understanding the data.

**tech_layoffs_analysis/** ◦ *The Logic*
Python and R scripts dedicated to cleaning, aggregating, and visualizing data. Contains interactive chart generation and geospatial mapping tools.

**tech_layoffs_csv/** ◦ *The Raw Material*
The foundation of the analysis. Organized datasets tracking layoffs by company, location, and date, including recent 2025 quarterly reports.

**tech_layoffs_sql/** ◦ *The Foundation*
SQL schemas and scripts for structuring the data warehouse and facilitating queries.

**tech_layoffs_pictures/** ◦ *The Visual*
Static exports of data visualizations and map markers.

---

## Status
⚪ **Active Analysis:** Currently processing and visualizing data for Q1 & Q2 2025.
⚪ **Historical Record:** Comprehensive datasets for 2024 are finalized.

---

## Getting Started
To interact with the analysis:

1.  **The Environment** 🌿
    Ensure Python is installed with `pandas` and `plotly` for the analysis scripts. R is required for specific data cleaning tasks.

2.  **The Database** 🪵
    Initialize the database structure using `tech_layoffs_sql/setupTechLayoffs.sql`.

3.  **The Analysis** 🌊
    Run the Jupyter notebooks in `tech_layoffs_analysis/` to generate fresh insights from the `tech_layoffs_csv/` data.