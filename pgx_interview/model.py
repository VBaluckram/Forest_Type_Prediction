"""
Train and test model to correctly determine the value in the Label column.

See the below files for additional documentation about the provided data:
    - data/original_data.info - in depth details about the original data set
    - data/data.info - modifications made by PGx for purposes of this exercise
"""
import pandas as pd
import sqlalchemy as sa
from sklearn.model_selection import train_test_split


def load_data(database, tablename):
	"""Load the data from Sqlite3 into pandas dataframe."""
	pass
	

def train_model(data):
	"""Build your model."""
	pass	
	
	
def test_model(model, data):
	"""Test your model."""
	pass


def main():
    """Controller function for this module."""
    database = ''
    tablename = ''
    data = load_data(database, tablename)
    train_data, test_data = train_test_split(data,)

    model = train_model(train_data)
    test_model(model, test_data)

 
if __name__ == '__main__':
    main()
