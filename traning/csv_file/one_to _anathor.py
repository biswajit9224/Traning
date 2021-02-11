import csv

# l = []
# with open('csv_file/_covid_data.csv') as csv_object:
    
#     for i in csv_object:
#         l.append(i)
# with open('csv_file/one_to_one.csv', 'w') as one:
#     for j in l:
#         one.write(j)


# string = input('enter a string: ')

# with open('D:/file_hand.txt') as e:
#     data = e.readlines()
#     for i in data:
#         if string in i:
#             print(i.title())

def _search(search, i):
    if search in i:
        return i

  
with open('csv_file/errors.log') as log_object:
    l = []
    data = csv.reader(log_object)
    for i in data:
        if _search('INFO', i):
            

