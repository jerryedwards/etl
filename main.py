from dbCredentials import mysql_db_config
import sqlQueries as queries
from etl import extract_csv, etl_process


def main():

    data = extract_csv()

    # mysql
    for config in mysql_db_config:

        try:
            etl_process(data, config, queries, 'mysql')

        except Exception as e:
            print('error message: {}'.format(e))
            continue
    
    # pymongo

    

if __name__ == '__main__':
    main()