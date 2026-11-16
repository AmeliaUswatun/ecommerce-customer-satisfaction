# E-Commerce Customer Satisfaction Analysis

Dashboard and data analysis project using the E-Commerce Public Dataset.
This project examines customer satisfaction from two business
perspectives: delivery performance and product-category review outcomes.

## Project Overview

The analysis is intended to help management identify operational areas
associated with lower customer satisfaction and prioritize further
evaluation.

### Business Questions

1.  **Delivery performance:** How is delivery punctuality associated
    with customer review scores during the analysis period?
2.  **Product-category satisfaction:** Which product categories have the
    highest proportion of low-satisfaction orders during the analysis
    period?

## Key Findings

### 1. Delivery Performance

-   Orders delivered on time had an average review score of
    approximately **4.29/5**.
-   Late-delivered orders had an average review score of approximately
    **2.57/5**.
-   The average review score declined as the delivery delay increased:
    -   On time / early: **4.29**
    -   Late by 1--3 days: **3.77**
    -   Late by 4--7 days: **2.32**
    -   Late by more than 7 days: **1.73**

These results indicate an association between delivery delay and lower
customer review scores. They do not establish causation.

### 2. Product-Category Satisfaction

The analysis identifies categories with a relatively high proportion of
low-satisfaction orders. Examples include:

-   Fashion Male Clothing: **26.13%**
-   Office Furniture: **22.64%**
-   Audio: **21.90%**

For category comparisons, categories with fewer than 30 orders are
excluded from the ranking to reduce the influence of very small samples.

A review is treated as low satisfaction when the **average review score
at order level is 2 or below**. Since reviews are associated with orders
rather than individual products, category results represent an
association between orders and the categories contained in those orders;
they should not be interpreted as product-specific ratings.

## Dashboard

**Public Streamlit dashboard:**\
https://ecommerce-customer-satisfaction-awynoayknlfu455xev2zpe.streamlit.app/

The dashboard provides: - Executive overview and key performance
indicators - Purchase-date range filter - Delivery performance
analysis - Customer satisfaction by delivery-delay duration -
Product-category low-satisfaction comparison - Category
evaluation-priority analysis - Data methodology and interpretation notes

## Repository Structure

``` text
ecommerce-customer-satisfaction/
├── dashboard/
│   └── dashboard.py
├── data/
│   ├── orders_dataset.csv
│   ├── order_reviews_dataset.csv
│   ├── order_items_dataset.csv
│   ├── products_dataset.csv
│   └── product_category_name_translation.csv
├── notebook.ipynb
├── requirements.txt
├── README.md
└── url.txt
```

## Run the Dashboard Locally

1.  Clone or download this repository.

2.  Open a terminal in the project root directory.

3.  Create and activate a virtual environment.

    **Windows PowerShell:**

    ``` powershell
    py -m venv .venv
    .\.venv\Scripts\Activate.ps1
    ```

4.  Install the dependencies:

    ``` bash
    python -m pip install -r requirements.txt
    ```

5.  Run the Streamlit application from the project root:

    ``` bash
    streamlit run dashboard/dashboard.py
    ```

The five CSV files must remain in the root-level `data/` directory,
alongside the `dashboard/` directory.

## Methodology Notes

-   Review scores are on a scale of 1--5.
-   Multiple review records associated with an order are aggregated
    using the mean review score for order-level analysis.
-   Delivery analysis includes delivered orders with both actual and
    estimated delivery timestamps.
-   A delivery is classified as on time when the actual delivery
    timestamp is not later than the estimated delivery timestamp.
-   Low satisfaction is defined as an order-level average review score
    of **2 or below**.
-   For category analysis, an order may be associated with multiple
    product categories. Each order-category combination is counted once.
-   Category comparisons exclude categories with fewer than 30
    associated orders.

## Limitations

-   The analysis is observational and describes associations, not causal
    effects.
-   Order-level reviews do not provide a direct rating for each product
    in a multi-category order.
-   Results depend on the available records and the selected analysis
    period.

## Files

-   `notebook.ipynb`: data analysis workflow, from data understanding
    and cleaning through exploration, visualization, and conclusions.
-   `dashboard/dashboard.py`: Streamlit dashboard source code.
-   `data/`: CSV datasets used by the notebook and dashboard.
-   `requirements.txt`: Python dependencies.
-   `url.txt`: public dashboard URL.
