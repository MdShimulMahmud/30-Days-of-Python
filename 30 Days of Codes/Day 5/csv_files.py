import csv

# file = open('example.csv')

# file_reader = csv.reader(file)

# # data = list(file_reader)
# # print(data) 

# for row in file_reader:
#     print("Row no. "+str(file_reader.line_num)+" "+str(row))

output_file = open("output.csv",'w',newline='')

file_writer = csv.writer(output_file)

file_writer.writerow([1,2,3,4,5])
file_writer.writerow([3,4,5,6,7])
output_file.close()