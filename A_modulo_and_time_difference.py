from data_reader import DataReader
data_reader = DataReader("sums_in_loop.txt")
data = data_reader.get_table_int(" ")
print(data)

time_difference_list = []

for line in data:
    first_date_sec = (line[0]*24)*60*60 + line[1]*60*60 + line[2]*60 + line[3]
    second_date_sec = (line[4]*24)*60*60 + line[5]*60*60 + line[6]*60 + line[7]
    time_difference = second_date_sec - first_date_sec

    day_difference = int(time_difference/86400)
    hour_difference = int((time_difference % 86400)/3600)
    minute_difference = int(((time_difference % 86400) % 3600) / 60)
    second_difference =  int(((time_difference % 86400) % 3600) % 60)
    time_difference_list.append("(" + str(day_difference) + " " + str(hour_difference) + " " + str(minute_difference) + " " + str(second_difference) + ")")

print(*time_difference_list)


