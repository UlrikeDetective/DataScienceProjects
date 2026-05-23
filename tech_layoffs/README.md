# > ./tech_layoffs_tracker

> **SYSTEM_STATUS**: ONLINE
> **CURRENT_TARGET**: 2026 Global Workforce Metrics

## [ ROOT_ACCESS ]

This repository acts as the central mainframe for intercepting, parsing, and visualizing layoff telemetry from the global tech sector. It leverages SQL for data structuring and Python/R kernels for high-level statistical analysis and geospatial plotting.

## [ Data Sources ]

- [Layoffs.fyi](https://layoffs.fyi/)
- [Peerlist Layoffs Tracker](https://peerlist.io/layoffs-tracker)
- [CompaniesMarketCap](https://companiesmarketcap.com/tech/largest-tech-companies-by-number-of-employees)

## [ FILESYSTEM_MAP ]

```bash
/root
├── tech_layoffs_analysis/   # [BIN] Analysis kernels (Python/R) & Plotly modules
├── tech_layoffs_csv/        # [DAT] Raw payloads (telemetry through May 2026)
├── tech_layoffs_sql/        # [SQL] Database schemas & ETL scripts
└── tech_layoffs_pictures/   # [IMG] Rendered visual artifacts
```

## [ OPERATION_LOG ]

- **[COMPLETED]** :: 2024-2025 Data Aggregation & Archival.
- **[COMPLETED]** :: May 2026 Data Ingestion (Peerlist payload integration).
- **[ACTIVE]** :: Interactive Plotly visualizations & animated geospatial mapping.

### Historical Scraping & Update Log
- **2023-12-25**: Initial web scraping of historical 2023 data.
- **2024-03-30**: Q1 2024 data ingestion.
- **2024-06-29**: Q2 2024 data ingestion (Peerlist).
- **2024-07-06**: Q2 2024 supplemental ingestion (Layoffs.fyi).
- **2024-09-28**: Q3 2024 data ingestion.
- **2026-01-01**: 2025 full-year aggregation (Peerlist).
- **2026-05-22**: 2026 Q1/Q2 data ingestion and normalization.

### Data Cleaning Protocol
- **Location Normalization**: Sanitized location strings and categorized by City, State, Country, and Continent.
- **Metric Derivation**: Implemented logic to calculate company size before/after layoffs where percentage data is available.
- **Standardization**: Unified disparate sources (Layoffs.fyi, Peerlist) into a single master schema.
- **Geocoding**: Automated GPS coordinate retrieval (Latitude/Longitude) for global mapping.

## [ About the Data ]

This dataset serves as the comprehensive, master record of global tech layoffs tracked by this project. It is designed to give you a clear, chronological view of how employment in the technology sector has been affected by economic shifts from March 2020 through May 2026.

We have structured the data to help you answer questions like:
- **Which industries were hit hardest?**
- **Are layoffs trending up or down over time?**
- **Where are these companies located?**

We have carefully cleaned and standardized the information from various sources (such as Layoffs.fyi and Peerlist) to ensure consistency, including adding geographic location data to enable our interactive maps.

## [ Dataset Description ]

The primary dataset used in this project is `tech_layoffs_csv/tech_layoffs_til_2026.csv`. It contains detailed telemetry on global tech layoffs from March 2020 through May 2026.

### Schema Specification
- **Nr**: Primary key; sequential index of the layoff event.
- **Company**: Name of the organization.
- **Location_HQ**: Primary city of operation/headquarters.
- **Region**: High-level geographic area (e.g., San Francisco Bay Area, Cascadia).
- **USState**: US-based state name; "non" for international locations.
- **Country**: Full country name.
- **Continent**: Continent of the HQ location.
- **Laid_Off**: Absolute number of staff impacted in the specific event.
- **Date_layoffs**: Canonical date of the announcement (YYYY-MM-DD).
- **Percentage**: Relative impact of the layoff on the total workforce.
- **Company_Size_before_Layoffs**: Estimated total headcount immediately preceding the event.
- **Company_Size_after_layoffs**: Estimated total headcount following the impact.
- **Industry**: Sector classification (e.g., AI, Crypto, Retail, Healthcare).
- **Stage**: Investment stage of the company (e.g., Seed, Series A-J, Post-IPO, Acquired).
- **Money_Raised_in__mil**: Total venture capital/funding raised in USD millions.
- **Year**: Calendar year extracted from the layoff date.
- **latitude / longitude**: Geospatial coordinates for mapping visualizations.

## [ EXECUTION_PROTOCOL ]

1.  **Environment Setup**
    Ensure the `analytics_env` conda environment is active.
    ```bash
    source /Users/ulrike_imac_air/miniforge3/bin/activate
    conda activate analytics_env
    ```

2.  **Dependency Injection**
    Load the required modules for the runtime environment.
    ```bash
    pip install pandas plotly folium geopy notebook
    ```

3.  **Database Initialization**
    Execute the setup script to build the data warehouse.
    ```sql
    \i tech_layoffs_sql/setupTechLayoffs2026.sql
    ```

4.  **Run Analysis**
    Launch the Jupyter kernels to process the latest telemetry.
    ```bash
    jupyter notebook tech_layoffs_analysis/tech_layoffs_2026.ipynb
    ```

---

_// End of transmission_
