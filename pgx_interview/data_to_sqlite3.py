"""Load data from a flat file into a sqlite database."""
import pandas as pd
import sqlalchemy as sa


def load_csv_to_sql(file_path, database='data.db', tablename='ForestCoverage'):
    """Function definition to convert csv into SQLite3"""
    data = pd.read_csv(file_path)
    engine = sa.create_engine(f'sqlite:///{database}')
    data.to_sql(tablename, engine, index=False)

if __name__ == '__main__':
    # TODO: Fill in path to train_data.csv
    file_path = ''
    load_csv_to_sql(file_path)
