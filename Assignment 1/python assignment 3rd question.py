#creating brothers tuple
brothers = ('chintu','bantu')
print('',type(brothers))

#creating sisters tuple
sisters = ('sita','gita')
print('',type(sisters))

#combining both tuples to siblings
siblings = brothers + sisters
print(siblings)

#printing number of siblings
print("number of siblings are ",len(siblings))

#changing tuple to list and adding father and mother's name
siblings_list = list(siblings)
print(siblings_list)
siblings_list.append('Raghu')
siblings_list.append('Madhavi')
print(siblings_list)

#converting it to tuple family_members
family_members = tuple(siblings_list)
print(family_members)
print('',type(family_members))
