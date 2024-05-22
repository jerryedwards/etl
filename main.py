from dbCredentials import mysql_config, mongodb_config
import queries
from etl import extract_csv, etl_process


def main():

    data = extract_csv()

    # mysql
    # for config in mysql_config:

        #try:
         #   etl_process(data, config, queries, 'mysql')

        #except Exception as e:
         #   print('error message [mysql]: {}'.format(e))
          #  continue
    
    # mongodb
    for config in mongodb_config:
        try:
            etl_process(data, config, queries, 'mongodb')

        except Exception as e:
            print('error message [mongodb]: {}'.format(e))
            continue

if __name__ == '__main__':
    main()
