my_dict={'John':1951, 'Ann':1970, 'Richard':2001}
print(my_dict)
print(my_dict['John'])
print(my_dict.get('Kate'))
my_dict.update({'Jimmy':2003, 'Nikki':1987})
print(my_dict)
a=my_dict.pop('Ann')
print(a)
print(my_dict)

my_set={1,2,4,7,1, (23,46,89), 'cat', 'dog', 5,1,1,2}
print(my_set)
my_set.update([6, 0])
print(my_set)
my_set.remove('cat')
print(my_set)

