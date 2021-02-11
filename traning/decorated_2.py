
'''
DEMO_CODE_OF_DECORATOR
def log(func):

    def wrapper(*args):
        print('hallo i am inside in wrapper')
        print(args)
        return func(*args)

    print('hallo i am inside the log')

    return wrapper

@log
def add(a,b):
    print(a+b)
add(1,2)

'''





# # logging decorator
#
# def logging(msg, ss):
#     def log(func):
#         print('inside log_function')
#         print(msg)
#
#         def wrapper(*args, **kwargs):
#             print(msg)
#             print('inside wrapper_function')
#             data = func(*args, **kwargs)
#             return data
#
#         return wrapper
#
#     return log
#
#
# @logging('hallo', ss='hi')
# def add(a, b):
#     print(a + b)
#
#
# def sub(a, b):
#     print(a - b)
#
#
# def mul(a, b):
#     print(a * b)
#
#
# def string(name):
#     print(f'hi {name}')
#
#
# add(3, 5)
def check(exp_types, actual_types):
    for i,j in zip(exp_types, actual_types):
        if not isinstance(j, i):
            raise ValueError




def mul(a, b):
    print(a * b)