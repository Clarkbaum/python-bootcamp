# letters number unerscores for varibles names
# cant start with a number
# can start with an underscore -- but this implies its private

x = 1

if x is not None:
	pass	# placeholder

my_list = [1,2,3]
if x in my_list:
	pass

# string manipulation

my_string = "HELLO"
my_string = my_string.lower()
print("my_string: ", my_string)

print("length of string: ", len(my_string))

my_string = "hello "
print(f"my_string: [{my_string.strip()}]")

my_string = "1 2 3 4 5"
my_string_parts = my_string.split(" ")

my_string = "abcde"
print("string ab", my_string[0:2]) # exclusive
print("string ab", my_string[:2])
print("string cde", my_string[2:])
print("string e", my_string[-1])
print("string abcd", my_string[:-1])


