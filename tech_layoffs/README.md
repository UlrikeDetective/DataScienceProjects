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
