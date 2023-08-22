ls_dict = [
    {'language': 'Python','Django': True},
    {'language': 'Python','Django': True},
    {'language': 'Python','Django': False},
    {'language': 'Python','Django': True},
    {'language': 'Python','Django': True},
    {'language': 'Python','Django': False},

    {'language': 'Python', 'ML': True},
    {'language': 'Python', 'ML': False},
    {'language': 'Python', 'ML': False},
    {'language': 'Python', 'ML': True},
    {'language': 'Python', 'ML': False},

    {'language': 'C++', 'ML': False},
    {'language': 'C++', 'ML': True},
    {'language': 'C++', 'ML': False},
    {'language': 'C++', 'ML': True},

    {'language': 'C++', 'Computer Vision': False},
    {'language': 'C++', 'Computer Vision': True},
    {'language': 'C++', 'Computer Vision': False},
    {'language': 'C++', 'Computer Vision': False},

    {'language': 'Python', 'React': True},
    {'language': 'Python', 'React': True},
    {'language': 'Python', 'React': False},
    {'language': 'Python', 'React': True},
    {'language': 'Python', 'React': False},
    {'language': 'Python', 'React': False},
]

out = {}
for i in ls_dict:
    language = i['language']
    del i['language']
    if language not in out:
        out[language] = []
    computer = [py for py, value in i.items() if value]
    for py in computer:
        found = False
        for lang_item in out[language]:
            if py in lang_item:
                lang_item[py] += 1
                found = True
                break
        if not found:
            out[language].append({py: 1})
print(out)




# output = {
#     "python": [ {'django': 4}, {'React': 3}, {"ML": 2}],
#     "C++": [ {'Computer Vision': 1}, {"ML": 2}]
# }

from itertools import groupby
from operator import itemgetter
data = [
    {"claim_number": "TX1048-22024-C639", "total_paid": 278.29, "card_paid": 228.29},
    {"claim_number": "TX1048-22086-C647", "total_paid": 161.81, "card_paid": 261.81},
    {"claim_number": "TX1048-22081-C648", "total_paid": 261.81, "card_paid": 386.81},
    {"claim_number": "TX1048-22024-C639", "total_paid": 318.29, "card_paid": 468.29},
    {"claim_number": "TX1048-22081-C648", "total_paid": 318.29, "card_paid": 418.29},
    {"claim_number": "TX1048-22086-C647", "total_paid": 0.0,    "card_paid": 10.0},
    {"claim_number": "TX1048-22024-C639", "total_paid": 10.0,   "card_paid": 20.0}
]

# lis = []
# claim= {}
# for i in data:
#     claim_number = i["claim_number"]
#     total_paid = i["total_paid"]
#     card_paid = i["card_paid"]
#     if claim_number in claim:
#         claim[claim_number]["total_paid"] += total_paid
#         claim[claim_number]["card_paid"] += card_paid
#     else:
#         claim[claim_number] = {
#             "claim_number": claim_number,
#             "total_paid": total_paid,

#             "card_paid": card_paid,
#             "difference":  card_paid-total_paid 
#         }

#         print()
# for claim in claim.values():
#     # if claim["difference"] < 0:
#         lis.append(claim)
# print(lis)





def getsummed(claim_number,elems):
    d = {'claim_number': claim_number, 'total_paid': 0, 'card_paid': 0,'difference':0}
    for e in elems:
        d['total_paid'] += e['total_paid']
        d['card_paid'] += e['card_paid']
        d["difference"] = d['total_paid']- d['card_paid']
    return d
def sortedgroupby(iterable, key):
    return groupby(sorted(iterable, key=key), key=key)
print([getsummed(gpr, groups) for gpr, groups in sortedgroupby(data, key=itemgetter('claim_number'))])


# output = [
#     {"claim_number": "TX1048-22024-C639", "total_paid": 606.58, "card_paid": 716.58, "difference": -110},
# ]





# out = {}

# myDictionary = { 'python': [], 'c++': []}
# # print(myDictionary)
# lis = []
# # out = {}

# for i in ls_dict:
#     for key,value in i.items():
#         if key=='language' and value=='Python':
        
#                 if key=='Django' and value==True:            
#                     myDictionary[key]=myDictionary.get(key,0)+1
#                 elif key=='ML' and value==True:
#                     myDictionary[key]=myDictionary.get(key,0)+1
#                 elif key=='React' and value==True:
#                     myDictionary[key]=myDictionary.get(key,0)+1
                    
        
# print(myDictionary)





# out=[{'claim_number':"TX1048-22024-C639"}]

# for i in data:
#     claim = i['claim_number']
#     total_paid = i['total_paid']
#     print(total_paid)
    
#     if claim == "TX1048-22024-C639" :

# res= sum([x['total_paid']for x in data])
# k= sum([x['card_paid']for x in data])
# l= res -k
# out.append(res)
# out.append(k)
# out.append(l)

# print(out)
# print(res,k,l)
