import pandas
music_data = pandas.read_csv('music.csv')
# input data set
x = music_data.drop(columns=['genre'])
# output data set
y = music_data['genre']