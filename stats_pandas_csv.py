import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.options.display.max_rows = 9

tline = '===================================='

# Reats CSV data from specified file
# and trims up column names off whitespace.
def get_csv_data(filename):
    data_frame = pd.read_csv(filename, sep=';')
    data_frame.columns = data_frame.columns.str.strip()
    return data_frame


def print_sorted_by_age_and_height(data):
    print('Participants (sorted by age, then height):')
    print(tline)
    print(data.sort_values(by=['Age', 'Height']))
    print('\n\n')


def print_averages(data):
    print('Averages (rounded):')
    print(tline)
    avg_age = np.round(data['Age'].mean(), 1)
    avg_height = np.round(data['Height'].mean(), 2)
    avg_weight = np.round(data['Weight'].mean(), 2)
    print(f'Average age:\t{avg_age} yrs')
    print(f'Average height:\t{avg_height} cm')
    print(f'Average weight:\t{avg_weight} KG')
    print('\n\n')


def plot(data):
    data.plot(kind='bar')

df = get_csv_data('./data.csv')
print_sorted_by_age_and_height(df)
print_averages(df)
#plot(df)

