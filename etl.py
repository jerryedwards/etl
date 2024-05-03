import os
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine


def extract_csv():

    f = os.path.abspath('AAPL.csv')
    data = pd.read_csv(f)
    df = pd.DataFrame(data)

    return df


def etl_process(data, db_config, queries, db_platform):
  
    print('connecting to db: ' + db_config['database'])
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()

    try:
        cursor.execute(queries.dropTable)
    except Exception as e:
        print('error dropping table: {}'.format(e))

    try:
        cursor.execute(queries.createTable)
    except Exception as e:
        print('error creating table: {}'.format(e))
  
    if db_platform == 'mysql':

        user = db_config['user']
        pwd = db_config['password']
        host = db_config['host']
        db = db_config['database']
    
        engine = create_engine('mysql+mysqlconnector://' + user + ':' + pwd + '@' + host + '/' + db)

        try: 
            data.to_sql(con=engine, name='applstocks', if_exists='append', index=False)
        except Exception as e:
            print('error creating mysql table: {}'.format(e))

    cnx.close()