# > ./tech_layoffs_tracker

> **SYSTEM_STATUS**: ONLINE
> **CURRENT_TARGET**: 2025 Global Workforce Metrics

## [ ROOT_ACCESS ]

This repository acts as the central mainframe for intercepting, parsing, and visualizing layoff telemetry from the global tech sector. It leverages SQL for data structuring and Python/R kernels for high-level statistical analysis and geospatial plotting.

## [Data Sources]

https://peerlist.io/layoffs-tracker
https://layoffs.fyi/
https://companiesmarketcap.com/tech/largest-tech-companies-by-number-of-employees

## [ FILESYSTEM_MAP ]

```bash
/root
├── tech_layoffs_analysis/   # [BIN] Analysis kernels (Python/R) & Plotly modules
├── tech_layoffs_csv/        # [DAT] Raw payloads (til end of 2025
├── tech_layoffs_sql/        # [SQL] Database schemas & ETL scripts
└── tech_layoffs_pictures/   # [IMG] Rendered visual artifacts
```

## [ OPERATION_LOG ]

- **[COMPLETED]** :: 2024 Data Aggregation & Archival.
- **[RUNNING]** :: 2025 Data Ingestion.
- **[ACTIVE]** :: Geospatial mapping & interactive dashboard generation.

## [ EXECUTION_PROTOCOL ]

1.  **Dependency Injection**
    Load the required modules for the runtime environment.

    ```bash
    pip install pandas plotly notebook
    ```

2.  **Database Initialization**
    Execute the setup script to build the data warehouse.

    ```sql
    \i tech_layoffs_sql/setupTechLayoffs.sql
    ```

3.  **Run Analysis**
    Launch the Jupyter kernels to process the stream.
    ```bash
    jupyter notebook tech_layoffs_analysis/tech_layoffs_2025.ipynb
    ```

---

_// End of transmission_
