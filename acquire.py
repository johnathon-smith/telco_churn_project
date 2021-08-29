import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import env
import os

def get_sql_url(database):
    return f'mysql+pymysql://{env.user}:{env.password}@{env.host}/{database}'

def get_telco_data():
    file_name = 'telco.csv'

    if os.path.isfile(file_name):
        return pd.read_csv(file_name)
    else:
        df = pd.read_sql("""SELECT * FROM customers 
                            JOIN contract_types ON contract_types.contract_type_id = customers.contract_type_id
                            JOIN internet_service_types ON internet_service_types.internet_service_type_id = customers.internet_service_type_id
                            JOIN payment_types ON payment_types.payment_type_id = customers.payment_type_id;""", get_sql_url('telco_churn'))
        df.to_csv(file_name, index = False)

        return df

#The following function will be used in the show_dists function
def get_vars_to_vis(telco):
    #Get column names
    cols = telco.columns
    
    #Set up empty list
    vars_to_vis = []
    
    #Use loop to check for 'id' in column name and exclude them from the list
    for col in cols:
        if 'id' not in col:
            vars_to_vis.append(col)
    
    return vars_to_vis

#The following function will plot the histograms of all relevant variables in the telco data set.
#Does not include columns that have 'id' in the name.
def show_dists(telco):
    vars_to_vis = get_vars_to_vis(telco)
    
    for col in vars_to_vis:
        plt.hist(telco[col], align = 'left')
        plt.title(col)
        plt.show()