# Churn Analysis Report

## 1. Introduction

This report presents the results of a churn analysis aimed at identifying customer characteristics and behavioral patterns associated with churn.

The focus of the analysis is on tenure, pricing, service adoption, payment behavior, and household structure, with the objective of understanding how these factors interact in shaping churn risk profiles.

The analysis was conducted in three stages: data cleaning, exploratory data analysis, and interaction-based analysis. This structure enabled a progression from isolated variable analysis to a more integrated view of customer behavior.

It is important to note that the results presented in this report describe statistical associations observed in the dataset and should not be interpreted as causal effects. Additionally, some customer segments contain relatively small sample sizes, which may introduce variability in subgroup-level comparisons.


## 2. Methodology

The analysis began with preprocessing and validation of the customer dataset, followed by exploratory analysis of key variables, including contract type, tenure, monthly charges, internet service, payment method, and household characteristics.

To support deeper analysis, derived variables were created:

* `service_count`: number of additional services subscribed
* `tenure_group`: segmentation of customers by lifecycle stage
* `monthly_charge_group`: segmentation by pricing level

These transformations allowed the analysis to move beyond isolated variable effects and examine how combinations of attributes relate to churn behavior.

The focus of the methodology was not predictive modeling, but rather behavioral segmentation and interpretation of churn patterns.


## 3. Key Findings

### 3.1 Customer tenure is the primary structural driver of churn

Tenure is the most consistent variable associated with churn behavior.

Churn is heavily concentrated in the early stages of the customer lifecycle, with a steep decline after the initial months. This suggests that customer retention is primarily a lifecycle-driven phenomenon, where early engagement plays a critical role in long-term stability.

While tenure alone does not explain all variation in churn, it strongly conditions the impact of other variables such as pricing and service adoption.


### 3.2 Pricing sensitivity depends on customer maturity

Higher monthly charges are associated with increased churn, but this relationship is not uniform across the customer base.

The effect of price is significantly stronger among low-tenure customers, indicating that customers in early lifecycle stages are more sensitive to perceived cost.

In contrast, long-tenure customers show substantially lower churn sensitivity even at higher price levels, suggesting that accumulated value perception or switching costs may reduce price-driven churn over time.


### 3.3 Service adoption reflects customer engagement rather than isolated behavior

Customers with a higher number of subscribed services tend to show lower churn rates.

However, service adoption is not independent of other variables. Customers with more services also tend to have higher tenure and different pricing structures, indicating that service adoption is better interpreted as a proxy for overall customer engagement rather than a standalone retention driver.


### 3.4 Internet service type is a strong segmentation variable

Internet service type shows strong separation in churn behavior:

* Fiber optic customers exhibit the highest churn rates
* Customers without internet service exhibit very low churn rates
* DSL customers tend to fall in an intermediate range

This suggests that infrastructure type or service experience may play a relevant role in churn propensity.

In contrast, phone-related variables (such as multiple lines) show limited discriminatory power in explaining churn differences.


### 3.5 Payment behavior is a strong behavioral signal

Payment method is one of the clearest behavioral indicators of churn risk.

Customers using electronic check show significantly higher churn rates compared to other payment methods.

Automatic payment methods (credit card and bank transfer) are associated with lower churn, suggesting that payment automation correlates with higher customer stability, potentially due to reduced friction or stronger commitment.


### 3.6 Household structure correlates with retention

Customers with partners or dependents show lower churn rates compared to single customers.

This pattern suggests that household stability may be associated with higher service continuity, although this relationship should be interpreted as correlational rather than causal.


## 4. Customer Segmentation

### 4.1 High-Risk Segment

This segment is characterized by a combination of behavioral and lifecycle factors:

* Low tenure
* High monthly charges
* Limited service adoption
* Fiber optic internet
* Electronic check payment
* Paperless billing

This group represents the highest concentration of churn risk and is most sensitive to early lifecycle interventions.


### 4.2 Stable Segment

This segment shows consistently low churn risk:

* Long tenure
* Lower or moderate monthly charges
* Broader service adoption
* Automatic payment methods
* Presence of partner or dependents

Customers in this group exhibit stronger retention stability and lower volatility in churn behavior.


### 4.3 Transitional Segment

This segment includes customers with mixed characteristics:

* Medium tenure
* Mixed service adoption levels
* Moderate charges
* Variable payment behavior

This group requires monitoring, as its churn behavior is less predictable and depends on combinations of factors rather than single variables.


## 5. Business Implications

### 5.1 Focus retention efforts on early lifecycle customers

The first months of the customer relationship represent the highest-risk period for churn. Retention strategies should prioritize this stage.


### 5.2 Align pricing strategy with customer maturity

Pricing sensitivity is significantly higher among low-tenure customers. This suggests that pricing interventions may be more effective when targeted at early-stage customers rather than applied uniformly.


### 5.3 Improve onboarding experience for high-risk service types

Fiber optic customers show structurally higher churn rates, indicating a need to evaluate onboarding, expectation setting, and perceived value delivery for this segment.


### 5.4 Use payment method as a behavioral risk indicator

Customers using electronic check represent a higher-risk group and may benefit from targeted migration toward automatic payment methods.


### 5.5 Treat service adoption as an engagement proxy

Service usage should be interpreted as a proxy for customer engagement depth rather than as an independent causal driver of retention.


## 6. Conclusion

Churn in this dataset is primarily driven by the interaction between customer lifecycle stage, pricing exposure, service engagement, payment behavior, and household structure.

Rather than being explained by a single dominant factor, churn emerges from a combination of structural (tenure), economic (pricing), and behavioral (payment and engagement) dimensions.

This segmentation provides a practical basis for prioritizing retention strategies, particularly by focusing on early lifecycle customers and high-risk behavioral profiles.
