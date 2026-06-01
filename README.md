# Churn Analysis Project

## Overview

This project analyzes customer churn behavior to identify key drivers and segment customers based on their likelihood to churn. The goal is to extract actionable insights that can support targeted retention strategies.

The analysis focuses on customer tenure, pricing, service adoption, payment behavior, and household characteristics.

Rather than focusing on complex predictive modeling, the emphasis is on behavioral interpretation and business-oriented segmentation.

---

## Key Objective

The main objective of this project is to understand which customer profiles are most associated with churn and how these patterns can inform retention strategies across different segments of the customer base.

---

## Project Structure

The project is organized into three main notebooks:

- `01_data_cleaning.ipynb`  
  Data preprocessing, handling missing values, and feature preparation.

- `02_eda.ipynb`  
  Exploratory data analysis of key variables such as tenure, charges, services, and churn distribution. This notebook uses SQL queries connected to a local database.

- `03_churn_analysis.ipynb`  
  Interaction analysis, feature engineering, and customer segmentation based on behavioral and structural attributes.

Additionally, a supporting script is used to initialize the local database required for SQL-based analysis.

- `src/create_database.py`  
  Creates and populates the local database used in notebooks `02` and `03`.

---

## Project Setup & Execution Flow

Before running the analysis notebooks, the environment must be properly set up.

### 1. Install dependencies

```bash
pip install -r requirements.txt
````

---

### 2. Create the database

Before running notebooks `02_eda.ipynb` and `03_churn_analysis.ipynb`, initialize the local database:

```bash
python src/create_database.py
```

This step is required because SQL queries used in the analysis depend on the locally created database.

---

### 3. Run the notebooks

Execute the notebooks in the following order:

1. `01_data_cleaning.ipynb`
2. `02_eda.ipynb`
3. `03_churn_analysis.ipynb`

Each step builds upon the previous one, moving from raw data preparation to exploratory analysis and finally to customer segmentation.

---

## Feature Engineering

The following derived features were created to support the analysis:

* `service_count`: number of additional services subscribed by each customer
* `tenure_group`: segmentation of customers by lifecycle stage
* `monthly_charge_group`: segmentation by pricing level

These features allow for a more structured analysis of customer behavior and churn patterns.

---

## Key Insights

* Customer tenure is the strongest structural driver of churn, with higher churn concentrated in early lifecycle stages.
* Pricing impacts churn primarily among low-tenure customers.
* Service adoption is associated with lower churn and reflects overall engagement rather than isolated behavior.
* Fiber optic customers show significantly higher churn rates compared to other internet types.
* Payment method is a strong behavioral signal, with electronic check users showing higher churn.
* Household structure (partners and dependents) is associated with lower churn.

---

## Customer Segments Identified

### High-Risk Segment

* Low tenure
* High monthly charges
* Limited service adoption
* Fiber optic internet
* Electronic check payment
* Paperless billing

---

### Stable Segment

* Long tenure
* Broader service adoption
* Automatic payment methods
* Lower churn sensitivity

---

### Transitional Segment

* Medium tenure
* Mixed behavioral and pricing characteristics
* Requires monitoring rather than immediate intervention

---

## Business Implications

* Retention efforts should prioritize early-stage customers, especially in the first months of the lifecycle.
* Pricing sensitivity should be considered jointly with tenure rather than in isolation.
* Fiber optic customers may require improved onboarding and value communication.
* Payment method can be used as a simple and effective churn risk indicator.
* Service adoption should be interpreted as a proxy for engagement depth.

---

## Tools & Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook
* SQLite (local database)

---

## Notes & Limitations

The results represent statistical associations observed in a cross-sectional dataset and should not be interpreted as causal relationships. Some customer segments may contain relatively small sample sizes, which can introduce variability in subgroup-level comparisons.

---

## Final Remark

This project focuses on extracting business insights from customer data through structured analysis and segmentation, emphasizing interpretability, reproducibility, and decision support over complex modeling.
