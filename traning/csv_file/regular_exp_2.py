import re

# a = re.findall(r'hello', "hello world")

# a = re.findall('hello', "Hello world", re.IGNORECASE)

# a = re.findall(r'.', "hello world")

# a = re.findall(r'h.', "hello")

# a = re.findall(r'a.b', "acb")

# a = re.findall(r'a.b', "a b")

# a = re.findall(r"^hello", "hello world")

# a = re.findall(r"hello$", "world hello")

# a = re.findall(r'a.a', "ana")

# a = re.findall(r'a..a', "anna")

# a = re.findall(r'a.*a', "annnnknna")

# a = re.findall(r'a.*a', 'aa')

# a = re.findall(r"^a.*a$", "anna")

# a = re.findall(r"^a.*a$", "hello anna")

# a = re.findall(r"an*a", "hello ana")

# a = re.findall(r"an*a", "hello aa")

# a = re.findall(r"an*a", "hello annna")

# a = re.findall(r"an*a", "amma")

# a = re.findall(r'a.*a', 'abcad')

# re.findall(r'a.*a$', 'abcad')

# re.findall(r'a.*a$', 'abcada')

# re.findall(r'a.+a', 'ana')

# re.findall(r'a.+a', 'aa')

# re.findall(r'an?a', "ana")

# re.findall(r'an?a', "anna")

# re.findall(r'colou?r', "colour")

# re.findall(r'colou?r', "what color do you like")

# re.findall(r"[aeiou]", "hello")

# re.findall(r'[0-9]', 'The cost of the book is Rs.100')

# re.findall(r'[0-9]+', 'The cost of the book is Rs.100')

# re.findall(r"\d", 'The cost of the book is Rs.100')

# re.findall(r"\d+", 'The cost of the book is Rs.100')

# re.findall(r'[abcd]', 'hello world')

# re.findall(r'[abcd]', 'abcdefghijk')

# re.findall(r'[abcd]+', 'abcdefghijkab')

# re.findall(r'[^0-9]', 'Rs.100')

# re.findall(r'\D', 'Rs.100')

# re.findall(r"\w", "hello")

# re.findall(r"\w+", "hello")

# re.findall(r"\W", "hello world welcome to Python")

# re.findall(r'\w+', 'hello there')

# re.findall(r'\w+', 'hello_there')

# re.findall(r'\s', 'hello there    Hello')

# re.findall(r'\S', 'hello there    Hello')

# re.findall(r'\d\d\d\d\d\d', '560001')

# re.findall(r'\d{6}', '560001')

# re.findall(r'\w{3,5}', 'hi')

# re.findall(r'\w{3,5}', 'hello')

# re.findall(r'\w{3,5}', 'helloworld')

# re.findall(r'\w{3,5}', 'helloworld')

# re.findall(r'\w{3,}', 'hello')

# re.findall(r'\w{3,}', 'hi')

# re.findall(r'\w{1,}', 'hi')

# re.findall(r'\w{0,}', '')

# re.findall(r'^\w{0,1}$', 'hi')

# re.findall(r'^\w{0,1}$', 'h')


# print(a)

# search_ip_adress = r'^\d{3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'#112.23.34.497(valid_ip_adress)
# pan = ['ABCDE1234X', 'et4teg', 'asf34f']
# search_pan_card = r'[A-Z]{5}\d{4}[A-Z]$'#ABCDE1234X(valid_pan_number)
# _lincks = [
#     'https://www.python.org'
#     'https://www.python.com'
#     'https://www.python.com'
#     'http://www.python.com.us'
# ]

file_formats = ['Graphics Interchange Format',
                'Advanced Audio Coding',
                'cascading style sheets',
                'HyperText Markup Language',
                'Joint Photographic Experts Group',
                'content management system',
                'Tagged Image File Format',
                'Windows Media Audio',
                'Comma Seperated Values',
                'JavaScript Object Notation'
                ]
pattern1 = r'\b[A-Z]|[A-Z]'
# search_file_format = r'[A-Z]'
# for i in file_formats:
#     data = re.findall(search_file_format, i)
#     if data:
#         print(''.join(data))

# _dates = ['2019-01-02', '2019-13-02', '2019-12-26', '26-08-2019', '20-19-20', '2019-12-31', '2019-12-32']


# search_date_format = r'^\d{4}-[0-1][0-2]-([0-2][0-9]|3[0-1])$'

# for i in _dates:
#     data = re.findall(search_date_format, i)
#     if data:
#         print(data)

# _formats = ['00:00:00', '23:59:59', '24:00:00', '1:59:20', '12:9:10', '10:20:8']

# search_time_format = r'[0-2][0-4]:[0-5][0-9]:[0-5][0-9]'
data = ''' hai hello hai
how hii hai '''



# for i in file_formats:
#     data = re.findall(pattern1, i)
#     if data:
#         print(data)




