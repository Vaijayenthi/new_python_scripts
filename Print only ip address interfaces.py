Print only ip address interfaces
text_input = '''Router# show ip interface brief
Interface             IP-Address      OK?    Method Status     
GigabitEthernet0/1    unassigned      YES    unset  up         
GigabitEthernet0/2    192.168.190.235 YES    unset  up         
GigabitEthernet0/3    unassigned      YES    unset  up         
GigabitEthernet0/4    192.168.191.2   YES    unset  up         
TenGigabitEthernet2/1 unassigned      YES    unset  up         
TenGigabitEthernet2/2 unassigned      YES    unset  up         
TenGigabitEthernet2/3 unassigned      YES    unset  up         
TenGigabitEthernet2/4 unassigned      YES    unset  down       
GigabitEthernet36/1   unassigned      YES    unset  down        down
GigabitEthernet36/2   unassigned      YES    unset  down        down
GigabitEthernet36/11  unassigned      YES    unset  down       
GigabitEthernet36/25  unassigned      YES    unset  down       
Te36/45               unassigned      YES    unset  down       
Te36/46               unassigned      YES    unset  down       
Te36/47               unassigned      YES    unset  down       
Te36/48               unassigned      YES    unset  down       
Virtual36             unassigned      YES    unset  up         
y = text_input.strip(" ")
y = y.split('\n')
z=[]
ele = "192"
i=0
value = len(y)
print(y)

#output y = ['Router# show ip interface brief', 'Interface             IP-Address      OK?    Method Status     \tProtocol', 'GigabitEthernet0/1    unassigned      YES    unset  up         \tup', 'GigabitEthernet0/2    192.168.190.235 YES    unset  up         \tup', 'GigabitEthernet0/3    unassigned      YES    unset  up         \tup', 'GigabitEthernet0/4    192.168.191.2   YES    unset  up         \tup', 'TenGigabitEthernet2/1 unassigned      YES    unset  up         \tup', 'TenGigabitEthernet2/2 unassigned      YES    unset  up         \tup', 'TenGigabitEthernet2/3 unassigned      YES    unset  up         \tup', 'TenGigabitEthernet2/4 unassigned      YES    unset  down       \tdown', 'GigabitEthernet36/1   unassigned      YES    unset  down        down', 'GigabitEthernet36/2   unassigned      YES    unset  down        down', 'GigabitEthernet36/11  unassigned      YES    unset  down       \tdown', 'GigabitEthernet36/25  unassigned      YES    unset  down       \tdown ', 'Te36/45               unassigned      YES    unset  down       \tdown', 'Te36/46               unassigned      YES    unset  down       \tdown', 'Te36/47               unassigned      YES    unset  down       \tdown', 'Te36/48               unassigned      YES    unset  down       \tdown', 'Virtual36             unassigned      YES    unset  up         \tup' ]
fruits = y
newlist = []

for x in fruits:
  if "192" in x:
    newlist.append(x)

print(newlist)
