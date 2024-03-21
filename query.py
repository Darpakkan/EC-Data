import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

def get_all_parties(df):
    print(df['Name of the Political Party'].unique())
    return

def get_donors_of_party(df, party_name):
    filtered_df = df.loc[merged_df['Name of the Political Party'] == party_name].sort_values(by='Denominations')
    print("Total No of Donors: " + f"{len(filtered_df)}")
    print(filtered_df[['Name of the Purchaser', 'Date of Purchase', 'Denominations']].to_markdown())
    return filtered_df[['Name of the Purchaser', 'Date of Purchase', 'Denominations']]

df1 = pd.read_csv("file1.csv", delimiter="|")
df2 = pd.read_csv("file2.csv", delimiter="|")
df = merged_df = pd.merge(df1, df2, on=['Bond Number', 'Denominations'], how='inner')


# get_donors_of_party(df, "BHARATIYA JANATA PARTY")
get_donors_of_party(df, "AAM AADMI PARTY")