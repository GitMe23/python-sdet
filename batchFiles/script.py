import csv

# simple script to read in a csv, use as python list of tuples and (over)write back to new csv

file = open('example.csv', 'r')
reader = csv.reader(file)
next(reader)
mylist = list(reader)
file.close()

for row in mylist:
    if int(row[0]) <= 2000:
        row[1] = 'less !'
    if int(row[0]) > 2000:
        row[1] = 'More than 2000'

new_list = open('example.csv', 'w')
writer = csv.writer(new_list)
headers = ('Applicant ID', 'Status')
writer.writerow(headers)
writer.writerows(mylist)
new_list.close()
