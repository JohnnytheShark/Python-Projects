import csv
#open the file
file = open("original.csv","r")
#Define a reader
Reader = csv.reader(file,delimiter=",")
#Output all the content of the csv file
for f in Reader:
    print(f)
file.close()

#Portion of the code to write to the csv file 
newRecord = ["2020","Corona","Virus","Health-Department"]
#Open the file in append mode
file = open("original.csv","a")
#Declare a writer variable
wrt = csv.writer(file)
#write the new record 
wrt.writerow(newRecord)
file.close()
