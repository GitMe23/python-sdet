import csv

with open('utilities/loanapp.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    # print(csvReader)
    # print(list(csvReader))
    names = []
    status = []
    for row in csvReader:
        names.append(row[0])
        status.append(row[1])

print(names)
print(status)
index = names.index('Joe')
loan_status = status[index]
print(index, ' loan status is', loan_status)

with open('utilities/loanapp.csv', 'a') as wFile:
    write = csv.writer(wFile)
    write.writerow(["Bob", "rejected"])
