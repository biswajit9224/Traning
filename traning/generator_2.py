import time
#
#
# def logging_generator():
#     with open('D:/csv_file/airlines.log') as log_object:
#         for each in log_object:
#             yield each
#             # time.sleep(0.5)
#
#
# def logging_normal():
#     with open('D:/csv_file/airlines.log') as log_object:
#         return log_object.readline()
#
#
# def check(search, line):
#     if search in line:
#         yield line
#         # time.sleep(0.5)
#
#
# for each_line in logging_generator():
#     for match in check('WARN', each_line):
#         print(match)
#         time.sleep(0.5)

# Generator that produces one line when asked for it
# def g_read_log():
#     with open('csv_file/airlines.log') as f:
#         for line in f:
#             yield line


# # Generator that searches for a partucular pattern
# def _grep(pattern, line):
#     if pattern in line:
#         return line


# # lines = read_log()
# for line in g_read_log():
#     for match in _grep('SUCCESS', line):
#         print(match)
#         time.sleep(1)



# def _log():
#     with open('csv_file/airlines.log') as e:
#         for i in e:
#             yield i

# def _search(search_, line):
#     if search_ in line:
#         return line

# for line in _log():
#     for match in _search('SUCCESS', line):
#         print(match)
#         time.sleep(0.5)

data = ['biswajit is a devloper', 'sonu is a painter', 'pinu is a team leader']
def _search(search_, line):
    if search_ in line:
        yield line

for i in data:
    for j in _search('pinu',i):
        print(_search('pinu',i))
        print(i)


# data = ['biswajit is a devloper', 'sonu is a painter', 'pinu is a team leader']
# def _search(search_, line):
#     if search_ in line:
#         yield line

# for i in data:
#     if _search('pinu',i):
#         print(_search('pinu',i))
#         print(i)




