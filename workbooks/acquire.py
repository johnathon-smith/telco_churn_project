import pandas as pd
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