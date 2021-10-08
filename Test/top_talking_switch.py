import  re
from csv import  DictReader
S = '''
switch-names, ports, Incoming BPS, Outgoing BPS
SW-A, ge-0/0/1, 1234, 3432
SW-B, ge-0/0/2, 323232, 232312
SW-C, ge-0/0/3, 32423, 342312
SW-D, ge-0/0/3, 121, 243
SW-E, ge-0/0/4, 534233432, 2532423
SW-F, ge-0/0/4, 23232, 332323
'''

pattern = re.compile(r'.*')
bps = pattern.findall(S)
lst = []
for data in bps:
    if data:
        lst.append(data.split(','))

dict = {}
for i in range(1, len(lst)):
    dict[lst[i][0]] = [lst[i][2], lst[i][3]]
#
sortbyval = {k:v for k, v in (sorted(dict.items(), key=lambda v:v[0], reverse=True)) }

print(sortbyval)

with open('switchfile.csv') as f:
    dict_reader = DictReader(f)

    data_dict = {}
    for data in dict_reader:
        data_dict[data['switch-names']] = [data['Incoming-BPS'], data[' Outgoing-BPS']]

    sortval = {k:v for k, v in sorted(data_dict.items(), key=lambda v:v[1], reverse=True) }
    print(sortval)