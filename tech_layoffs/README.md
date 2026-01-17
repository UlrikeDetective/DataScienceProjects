# > ./tech_layoffs_tracker

> **SYSTEM_STATUS**: ONLINE
> **CURRENT_TARGET**: 2025 Global Workforce Metrics

## [ ROOT_ACCESS ]
This repository acts as the central mainframe for intercepting, parsing, and visualizing layoff telemetry from the global tech sector. It leverages SQL for data structuring and Python/R kernels for high-level statistical analysis and geospatial plotting.

## [ FILESYSTEM_MAP ]

```bash
/root
├── tech_layoffs_analysis/   # [BIN] Analysis kernels (Python/R) & Plotly modules
├── tech_layoffs_csv/        # [DAT] Raw payloads (2024 archives + 2025 live stream)
├── tech_layoffs_sql/        # [SQL] Database schemas & ETL scripts
└── tech_layoffs_pictures/   # [IMG] Rendered visual artifacts
```

## [ OPERATION_LOG ]

*   **[COMPLETED]** :: 2024 Data Aggregation & Archival.
*   **[RUNNING]**   :: 2025 Q1/Q2 Data Ingestion.
*   **[ACTIVE]**    :: Geospatial mapping & interactive dashboard generation.

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
*// End of transmission*
