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

> - __Hypothesis 1__
> - Alpha = 0.05
> - H_0: Contract type is independent of customer churn.
> - H_a: Contract type is not independent of customer churn.
> - Outcome: I rejected the null hypothesis.

> - __Hypothesis 2__
> - Alpha = 0.05
> - H_0: The average number of customers that churn with a monthly contract <= the average number of customers that churn without a monthly contract.
> - H_a: The average number of customers that churn with a monthly contract > the average number of customers that churn without a monthly contract.
> - Outcome: I rejected the null hypothesis. 

> - __Hypothesis 3__
> - Alpha = 0.05
> - H_0: Internet service type is independent of customer churn.
> - H_a: Internet service type is not independent of customer churn.
> - Outcome: I rejected the null hypothesis.

> - __Hypothesis 4__
> - Alpha = 0.05
> - H_0: The average number of customers that churn with fiber optic internet <= the average number of customers that churn without fiber optic internet.
> - H_a: The average number of customers that churn with fiber optic internet > the average number of customers that churn without fiber optic internet.
> - Outcome: I rejected the null hypothesis.

> - __Hypothesis 5__
> - Alpha = 0.05
> - H_0: Payment type is independent of customer churn.
> - H_a: Payment type is not independent of customer churn.
> - Outcome: I rejected the null hypothesis.

> - __Hypothesis 6__
> - Alpha = 0.05
> - H_0: The average number of customers that churn with manual payments <= the average number of customers that churn with automatic payments.
> - H_a: The average number of customers that churn with manual payments > the average number of customers that churn with automatic payments.
> - Outcome: I rejected the null hypothesis.

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Executive Summary - Conclusions & Next Steps
<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

> - Through data exploration and statistical analysis, I found customer contract type, payment type, and internet service type to all be significant drivers of churn.
> - I constructed and evaluated over 200 Random Forest Classifier models with varying max_depth and min_samples_leaf hyperparameter values. 
> - Ultimately, my final model was chosen as my best model based on its accuracy score (\~80%), higher recall rate (\~52%), and low indication of being over fit.
> - My final model outperformed the baseline model which had an accuracy score of about 73%.
> - Created a csv file containing customer_id, probability of churn, and prediction of whether or not each customer churned using the test results of my final model.

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Pipeline Stages Breakdown

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

##### Plan
- [x] Create README.md with data dictionary, project and business goals, come up with initial hypotheses.
- [x] Acquire data from the Codeup Database and create a function to automate this process. Save the function in an acquire.py file to import into the Final Report Notebook.
- [x] Clean and prepare data for the first iteration through the pipeline, MVP preparation. Create a function to prepare data with encoding for modeling, and another function to prepare data without encoding for exploration. Store the functions in a prepare.py module, and prepare data in Final Report Notebook by importing and using the function.
- [x]  Clearly define at least two hypotheses, set an alpha, run the statistical tests needed, reject or fail to reject the Null Hypothesis, and document findings and takeaways.
- [x] Establish a baseline accuracy and document well.
- [x] Train at least three different classification models.
- [x] Evaluate models on train and validate datasets.
- [x] Choose the model that performs the best and evaluate that single model on the test dataset.
- [x] Create csv file with customer_id, the probability of churn, and the model's prediction for each observation in my test dataset.
- [x] Document conclusions, takeaways, and next steps in the Final Report Notebook.

___

##### Plan -> Acquire
> - Store functions that are needed to acquire data from the customers, contract_types, internet_service_types, and payment_types tables from the telco_churn database on the Codeup data science database server; make sure the acquire.py module contains the necessary imports to run my code.
> - The final function will return a pandas DataFrame.
> - Import the acquire function from the acquire.py module and use it to acquire the data in the Final Report Notebook.
> - Complete some initial data summarization (`.info()`, `.describe()`, `.value_counts()`, ...).
> - Plot distributions of individual variables.
___

##### Plan -> Acquire -> Prepare
> - Store functions needed to prepare the telco data; make sure the module contains the necessary imports to run the code. The final function should do the following:
    - Split the data into train/validate/test.
    - Handle any missing values.
    - Handle erroneous data and/or outliers that need addressing.
    - Encode variables as needed.
    - Create any new features, if made for this project.
> - Import the prepare function from the prepare.py module and use it to prepare the data in the Final Report Notebook.
___

##### Plan -> Acquire -> Prepare -> Explore
> - Answer key questions, my hypotheses, and figure out the features that can be used in a classification model to best predict the target variable, churn. 
> - Run at least 2 statistical tests in data exploration. Document my hypotheses, set an alpha before running the tests, and document the findings well.
> - Create visualizations and run statistical tests that work toward discovering variable relationships (independent with independent and independent with dependent). The goal is to identify features that are related to customer churn (the target), identify any data integrity issues, and understand 'how the data works'. If there appears to be some sort of interaction or correlation, assume there is no causal relationship and brainstorm (and document) ideas on reasons there could be correlation.
> - Summarize my conclusions, provide clear answers to my specific questions, and summarize any takeaways/action plan from the work above.
___

##### Plan -> Acquire -> Prepare -> Explore -> Model
> - Establish a baseline accuracy to determine if having a model is better than no model and train and compare at least 3 different models. Document these steps well.
> - Train (fit, transform, evaluate) multiple models, varying the algorithm and/or hyperparameters you use.
> - Compare evaluation metrics across all the models you train and select the ones you want to evaluate using your validate dataframe.
> - Feature Selection (after initial iteration through pipeline): Are there any variables that seem to provide limited to no additional information? If so, remove them.
> - Based on the evaluation of the models using the train and validate datasets, choose the best model to try with the test data, once.
> - Test the final model on the out-of-sample data (the testing dataset), summarize the performance, interpret and document the results.
___

##### Plan -> Acquire -> Prepare -> Explore -> Model -> Deliver
> - Introduce myself and my project goals at the very beginning of my notebook walkthrough.
> - Summarize my findings at the beginning like I would for an Executive Summary. (Don't throw everything out that I learned from Storytelling) .
> - Walk Codeup Data Science Team through the analysis I did to answer my questions and that lead to my findings. (Visualize relationships and Document takeaways.) 
> - Clearly call out the questions and answers I am analyzing as well as offer insights and recommendations based on my findings.

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Reproduce My Project

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

You will need your own env file with database credentials along with all the necessary files listed below to run my final project notebook. 
- [x] Read this README.md
- [ ] Download the aquire.py, prepare.py, explore.py, model.py, and final_report.ipynb files into your working directory
- [ ] Add your own env file to your directory. (user, password, host)
- [ ] Run the final_report.ipynb notebook