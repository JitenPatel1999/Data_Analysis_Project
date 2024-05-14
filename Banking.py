import pandas as pd
#Creating the first dataframe for the first 5 bank clients
Bank_df_1 = pd.DataFrame({'Bank ID': [1, 2, 3, 4, 5],
                         'First Name': ['Jack', 'Jason', 'Avery', 'Ethan', 'Alex'],
                         'Last Name': ['Brian', 'Colin', 'Owen', 'Angea', 'Michael']})
#Creating the second dataframe for the next 5 bank clients
Bank_df_2 = pd.DataFrame({'Bank ID': [6, 7, 8, 9, 10],
                         'First Name': ['Frank', 'Mason', 'Audrey', 'Xander', 'Nami'],
                         'Last Name': ['Cynthia', 'Zoro', 'Luffy', 'Dennis', 'Nojiko']})
#Adding a new column to both dataframes that displays the bank client's annual salary
Bank_df_1.insert(3, 'Annual Salary [$/year]',[75000, 40000, 100000, 60000, 80000], True)
Bank_df_2.insert(3, 'Annual Salary [$/year]',[85000, 60000, 150000, 20000, 90000], True)
#Merging both the dataframes into one dataframe
Bank_all = pd.concat([Bank_df_1, Bank_df_2])
#Creating the new bank client
New_client = pd.DataFrame({'Bank ID': [11],
                           'First Name':['Jiten'],
                           'Last Name':['Patel'],
                           'Annual Salary [$/year]':[200000]})
#Adding a new client to the bank
New_Bank = pd.concat([Bank_all, New_client])
print(New_Bank)

