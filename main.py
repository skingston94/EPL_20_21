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


#Using Python Graph Gallery, I have gotten info on running a bar chart.
#First I will create two lists, player_yellows & the amount of yellows they received
players_yellows= ['McGinn', 'Maguire', 'Gallagher', 'Phillips', 'Luiz', 'Hojbjerg', 'Holgate']
yellows= [12, 11, 11, 10, 10, 9, 9]
#Now I will plot the players_yellows on the x axis, and yellows on y axis
plt.bar(players_yellows, yellows)
#Label both axis'
plt.xlabel('Players')
plt.ylabel('Yellows')
#Title the graph
plt.title('Players to receive most Yellow Cards 20/21')
#I'll need to add more numbers to make the graph visually better
plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
#Graph appears with plt.show()
plt.show()


#Now I want to find out what odds these 7 players should be for a yellow card in each match
##I now have each of the players minutes, which I will create as a list below
player_mins= [3330, 3047, 2531, 2428, 2781, 3420, 2287]
#I want to tidy this up so I can view the yellows and minutes altogether. Here I am using Dictionary on the lists
dict1= {'players_yellows': players_yellows, 'yellows': yellows, 'player_mins':player_mins}
df= pd.DataFrame(dict1)
df
#I need to divide the lists now to find the players yellows per minute
#I have used truediv and the below code, where I found on https://www.tutorialspoint.com/dividing-two-lists-in-python
from operator import truediv
print('player_mins:' + str(player_mins))
print('yellows:' + str(yellows))
minutes_p_yellow= list(map(truediv, player_mins, yellows))
print(minutes_p_yellow)

#Now I want to find the price we would make each player to receive a yellow card
#I want to show this info on a line plot
#Visually, this would be best as it shows a stark difference between the top vs bottom players
#This shows that even though Hojbjerg and Gallagher received the same amount of yellows, their price should be much different
#Gallagher received a yellow card once every 230 minutes, vs 1 in every 380 mins for Hojbjerg
#If we simply divide these mins per yellow by 90(minutes in a football match) we get each players price in decimal form
#Example, Gallagher= 230.09/90 is 2.56, meaning he is expected to get 1 yellow every 2.56 matches
#Thus, his price is 2.56, meaning if you place €1 on him to be booked, you would get back €2.56
#I will now use a for loop to show this, and create the line plot to show the difference between the players prices
prices=[minutes/90 for minutes in minutes_p_yellow]
print(prices)
fig, ax= plt.subplots()
plt.plot(players_yellows, prices)
plt.xlabel('Players')
plt.ylabel('Yellow Card Price')
plt.title('Price per Player for Yellow Card- EPL 20/21')
plt.show()
