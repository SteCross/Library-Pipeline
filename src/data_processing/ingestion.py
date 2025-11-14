import sys
sys.path.append('/path/to/library-pipeline/src')
from data_processing.ingestion import load_csv

df = load_csv('data/circulation_data.csv')
print(df.head())
print(df.info())