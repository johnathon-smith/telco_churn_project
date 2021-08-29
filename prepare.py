import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

#The following function will be used to alter senior_citizen original values in prep_without_encoding.
def yes_or_no(value):
    if value == 1:
        return 'Yes'
    elif value == 0:
        return 'No'

#The following function will be used in the prep functions to return the train, validate, and test splits
def train_validate_test_split(df, target, seed = 123):
    '''
    This function takes in a dataframe, the name of the target variable
    (for stratification purposes), and an integer for a setting a seed
    and splits the data into train, validate and test. 
    Test is 20% of the original dataset, validate is .30*.80= 24% of the 
    original dataset, and train is .70*.80= 56% of the original dataset. 
    The function returns, in this order, train, validate and test dataframes. 
    '''
    train_validate, test = train_test_split(df, test_size=0.2, 
                                            random_state=seed, 
                                            stratify=df[target])
    
    train, validate = train_test_split(train_validate, test_size=0.3, 
                                       random_state=seed,
                                       stratify=train_validate[target])
    return train, validate, test

def prep_without_encoding(telco):
    telco.drop_duplicates(inplace = True)

    #Only use rows where tenure is greater than zero
    telco = telco[telco.tenure > 0].copy()

    #Convert total_charges to float
    telco.total_charges = telco.total_charges.str.strip()
    telco.total_charges = telco.total_charges.str.replace('[$,]','', regex = True)
    telco.total_charges = telco.total_charges.astype(float)

    #Select all categorical columns (ignoring customer_id since it will be dropped)
    cat_cols = telco.select_dtypes('object').columns[1:]

    #Strip all leading and trailing whitespace from each categorical column
    for col in cat_cols:
        telco[col] = telco[col].str.strip()

    #drop unnecessary columns
    telco.drop(columns = ['customer_id', 'internet_service_type_id', 'contract_type_id', 'payment_type_id', 'contract_type_id.1', 'internet_service_type_id.1', 'payment_type_id.1'], inplace = True)

    #For the explore stage, I want my categorical values to be easy to read.
    #So I will convert the senior_citizen column to 'object' datatype and change its values to 'yes' or 'no'.
    telco.senior_citizen = telco.senior_citizen.astype(object)
    telco.senior_citizen = telco.senior_citizen.apply(yes_or_no)

    return train_validate_test_split(telco, 'churn')

def prep_with_encoding(telco):
    #Run general cleaning operations from previous function
    telco.drop_duplicates(inplace = True)

    #Only use rows where tenure is greater than zero
    telco = telco[telco.tenure > 0].copy()

    #Convert total_charges to float
    telco.total_charges = telco.total_charges.str.strip()
    telco.total_charges = telco.total_charges.str.replace('[$,]','', regex = True)
    telco.total_charges = telco.total_charges.astype(float)

    #Select all categorical columns (ignoring customer_id since it will be dropped)
    cat_cols = telco.select_dtypes('object').columns[1:]

    #Strip all leading and trailing whitespace from each categorical column
    for col in cat_cols:
        telco[col] = telco[col].str.strip()

    #drop unnecessary columns
    telco.drop(columns = ['customer_id', 'internet_service_type_id', 'contract_type_id', 'payment_type_id', 'contract_type_id.1', 'internet_service_type_id.1', 'payment_type_id.1'], inplace = True)

    #For the explore stage, I want my categorical values to be easy to read.
    #So I will convert the senior_citizen column to 'object' datatype and change its values to 'yes' or 'no'.
    telco.senior_citizen = telco.senior_citizen.astype(object)
    telco.senior_citizen = telco.senior_citizen.apply(yes_or_no)

    #Select all categorical columns
    cat_cols = telco.select_dtypes('object').columns

    #Create dummy variables and concat to telco dataframe
    dummy_df = pd.get_dummies(telco[cat_cols], drop_first = True)
    telco = pd.concat([telco, dummy_df], axis = 1)

    #Drop columns of type 'object'
    telco = telco.drop(columns = cat_cols)

    #Rename churn_yes 
    telco.rename(columns = {'churn_Yes':'churn'}, inplace = True)

    return train_validate_test_split(telco, 'churn')

