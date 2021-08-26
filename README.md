## Telco Churn Classification Project

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Project Summary
<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

#### Project Objectives
> - Document code, process (data acquistion, preparation, exploratory data analysis and statistical testing, modeling, and model evaluation), findings, and key takeaways in a Jupyter Notebook report.
> - Create modules (acquire.py, prepare.py) that make your process repeateable.
> - Construct a model to predict customer churn using classification techniques.
> - Deliver a 5 minute presentation consisting of a high-level notebook walkthrough using your Jupyter Notebook from above; your presentation should be appropriate for your target audience.
> - Answer panel questions about your code, process, findings and key takeaways, and model.

#### Business Goals
> - Find drivers for customer churn at Telco. Why are customers churning?
> - Construct a ML classification model that accurately predicts customer churn.
> - Document your process well enough to be presented or read like a report.

#### Audience
> - Codeup Data Science team

#### Project Deliverables
> - A Jupyter Notebook Report showing process and analysis with the goal of finding drivers for customer churn. 
> - a README.md file containing the project description with goals, initial hypotheses, a data dictionary, project planning (lay out your process through the data science pipeline), instructions or an explanation of how someone else can recreate your project and findings (What would someone need to be able to recreate your project on their own?), answers to your hypotheses, key findings, recommendations, and takeaways from your project.
> - A notebook walkthrough presentation with a high-level overview of your project
> - All necessary modules to make my project reproducible
> - a CSV file with customer_id, probability of churn, and prediction of churn. (1=churn, 0=not_churn).

#### Project Context
> - The Telco data set I'm using came from the Codeup Database.
> - Find out more about the Telco Customer Churn Dataset [here](https://www.kaggle.com/blastchar/telco-customer-churn).


#### Data Dictionary

|Target|Datatype|Definition|
|:-------|:---------|:------------|
| Churn | Object | Whether the customer churned or not (Yes or No) |

|Feature|Datatype|Definition|
|:-------|:---------|:------------|
| customer_id | Object | Customer ID |
| gender | Object | Whether the customer is a male or a female |
| senior_citizen | int64 | Whether the customer is a senior citizen or not (1, 0) |
| partner | Object | Whether the customer has a partner or not (Yes, No) |
| dependents | Object | Whether the customer has dependents or not (Yes, No) |
| tenure | int64 | Number of months the customer has stayed with the company |
| phone_service | Object | Whether the customer has a phone service or not (Yes, No) |
| multiple_lines | Object | Whether the customer has multiple lines or not (Yes, No, No phone service) |
| online_security | Object | Whether the customer has online security or not (Yes, No, No internet service) |
| online_backup | Object | Whether the customer has online backup or not (Yes, No, No internet service) |
| device_protection | Object | Whether the customer has device protection or not (Yes, No, No internet service) |
| tech_support | Object | Whether the customer has tech support or not (Yes, No, No internet service) |
| streaming_tv | Object | Whether the customer has streaming TV or not (Yes, No, No internet service) |
| streaming_movies | Object | Whether the customer has streaming movies or not (Yes, No, No internet service) |
| paperless_billing | Object | Whether the customer has paperless billing or not (Yes, No) |
| monthly_charges | float64 | The amount charged to the customer monthly |
| total_charges | Object | The total amount charged to the customer |
| contract_type | Object | The contract term of the customer (Month-to-month, One year, Two year) |
| internet_service_type | Object | Customer’s internet service provider (DSL, Fiber optic, No) |
| payment_type | Object | The customer’s payment method (Electronic check, Mailed check, Bank transfer (automatic), Credit card (automatic)) |

#### Initial Hypotheses

> - ** Hypothesis 1 **
> - Alpha = 0.05
> - $H_0$: 