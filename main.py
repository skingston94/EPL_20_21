# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#Importing pandas
import pandas as pd
#Naming the data of the file I have downloaded, which is Premier League players data from the season 2020/2021.
data= pd.read_csv('EPL_20_21.csv')
#Printing this dataset- Dataset found on Kaggle- https://www.kaggle.com/atasaygin/premier-league-player-analysis


#The below are the imports needed for this project
#I have downloaded matplotlib, pandas, numpy and seaborn from File-Settings-Python Interpreter
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#Example to look at data in first 7 rows- Test to make sure data is running correctly
Top10 = pd.read_csv('EPL_20_21.csv', nrows=20, header=None)
#Sorting players by total number of yellow cards
print(data.sort_values(['Yellow_Cards', 'Name'], ascending=[False, False]))
#After trial and error, I've sorted the top 7 players to get most yellow cards (anyone with 9+).
#I've used Pandas dataframe nlargest to find the top 7 players
data_frame=data.nlargest(7, 'Yellow_Cards')
print(data_frame)

#Now, I will create a list from these 7 players so I can create a bar chart
players_yellows= ['McGinn', 'Maguire', 'Gallagher', 'Phillips', 'Luiz', 'Hojbjerg', 'Holgate']
yellows= [12, 11, 11, 10, 10, 9, 9]
plt.plot(players_yellows, yellows)
plt.show()



