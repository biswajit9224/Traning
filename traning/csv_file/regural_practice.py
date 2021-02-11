import re
EXPR = r""
def ip_get(list_,file_name,list_ip):
    with open(file_name) as file_object:
        for each in file_object:
            data = re.findall("[/]\d{1,2}\.\d{1,2}\.\d{1,2}\.\d{1,2}:\d{4}",each)
            if data:
                re.sub("[/]\d{1,2}\.\d{1,2}\.\d{1,2}\.\d{1,2}:\d{4}",each,"kanha")
            # re.sub("[/]\d{1,2}\.\d{1,2}\.\d{1,2}\.\d{1,2}:\d{4}",each,"kanha")
ip_get([],"errors_.log",[])
 



# ['127.0.0:0','127.256.0:0','255.255.255:255','127.0.0:1237']
# (1[0-9][0-9]|2[0-5][0-5])|\.
##reg_x='(1[0-9][0-9]|2[0-5][0-5]|[0-9]|[0-9][0-9])\.(1[0-9][0-9]|2[0-5][0-5]|[0-9]|[0-9][0-9])\.(1[0-9][0-9]|2[0-5][0-5]|[0-9]|[0-9][0-9]):([0-9]|[0-9][0-9]|[0-9][0-9][0-9]|[0-9][0-9][0-9][0-9])'
##reg_x='(((1[0-9][0-9]|2[0-5][0-5]|[0-9]|[0-9][0-9])[\.:]){3})([0-9]|[0-9][0-9]|[0-9][0-9][0-9]|[0-9][0-9][0-9][0-9])'


# def ip_get(list_,file_name,list_ip):
#     with open(file_name) as file_object:
#         for each in file_object:
#             list_.append(each)
#         for ip_search in list_:
#             expect = re.sub("[/]\d{1,2}\.\d{1,2}\.\d{1,2}\.\d{1,2}:\d{5}",ip_search)
#             if expect:
#                 list_ip.append(expect)
#         print(len(list_ip))
#         print(list_ip[:10])
        
# ip_get([],"errors_.log",[])