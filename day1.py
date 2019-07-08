import math

# primitive type
my_int = 1
my_float = 1.1
my_string = "string"
my_bool = True
none_type = None

# dynamically typed example
print("float: ", my_float)
my_new_int = int(my_float)
print("my new int: ", my_new_int)
my_new_int = round(my_float)
print("my new int round: ", my_new_int)
my_new_int = math.ceil(my_float)
print("my new int ceil: ", my_new_int)

# colections
# if keys are the same one will just get removed silently 
# not ordered 
my_empty_dict = {}
my_dict = {
	"key1": "value1",
	"key2": "value2"
}
print("my_dict: ", my_dict)

# lists, like arrays
my_empty_list = []
my_list = [1,2,3]
print("my_list: ", my_list)

dict_value = my_dict["key1"] # will raise error
dict_value = my_dict.get("key1", "default value goes here") # wont raise error if key doenst exist. will return default value

list_value = my_list[0]
list_value = my_list[-1]

print("list_value: ", list_value)

# tuples

my_tuples = ()
#immutible
#doesnt need ()
my_one_item_tuple = (1) #not a tuple, thinks its an  int
my_tuple = (1, )
my_tuple = (1, 2)

def return_two_things():
	# do stuff
	thing = 1
	thing2 = 2
	return thing, thing2

example = 1, # would be a tuple

print("return two things: ", return_two_things())

value1, value2 = return_two_things()
print("value1: ", value1)
print("value2: ", value2)

triple = 1,2,3

# sets

my_set = set()
my_set = {1}
my_set = {1,2}
#sets cant have dups

my_list = [1,2,3,4,4]
my_set = set(my_list)
print("my_set: ", my_set)

x = 1
y = 2

z = x ** y # exponets 
z = x % y # mod

# conditionals 

if x == 1: # checks type and value
	print("x is 1")
else:
	print("x is not 1")
	
if x <= 1:
	print("x <= 1")
elif x > 1:
	print("else if")

example = {
	1: "one",
	2: "two",
	3: "three"
}

if x in example:
	y = example[x]

#loops

# i = 0 dont need its assumed 
for i in range(10): # exclusive range
	print("loop: ", i)
	# i += 1 dont need its assumed

#range(4, 19, 2) start, end, jump by value

for key, value in  my_dict.items():
	#stuff
	print("stuff: ", value)

j = 0
while j < 5:
	print("loop: ",j)
	j += 1

print("hello" + str(j))
print(f'hello {j}')