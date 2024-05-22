import os
import pandas as pd
import mysql.connector
import pymongo
from sqlalchemy import create_engine


def extract_csv():

    f = os.path.abspath('AAPL.csv')
    data = pd.read_csv(f)
    df = pd.DataFrame(data)

    return df


def etl_process(data, db_config, queries, db_platform):

    print('connecting to ' + db_platform + ': ' + db_config['database'])

    if db_platform == 'mysql':

        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor()

        try:
            cursor.execute(queries.mysqlDropTable)
        except Exception as e:
            print('error dropping mysql table: {}'.format(e))

        try:
            cursor.execute(queries.mysqlCreateTable)
        except Exception as e:
            print('error creating mysql table: {}'.format(e))

        user = db_config['user']
        pwd = db_config['password']
        host = db_config['host']
        database = db_config['database']

        engine = create_engine('mysql+mysqlconnector://' + user + ':' + pwd + '@' + host + '/' + database)

        try: 
            data.to_sql(con=engine, name='applstocks', if_exists='append', index=False)
        except Exception as e:
            print('error creating mysql table: {}'.format(e))

        cnx.close()

    if db_platform == 'mongodb':

        host = db_config['host']
        port = db_config['port']
        database = db_config['database']

        mongoDict = data.to_dict(orient='records')
        client = pymongo.MongoClient('mongodb://' + host + ':' + port + '/')

        db=client[database]
        collection = db["appleStocks"]

        try: 
            collection.insert_many(mongoDict)
        except Exception as e:
            print('error inserting mongdb collection: {}'.format(e))
