names =  input("Enter names seperated by comas: ")
assignments = input("Enter assignments seperated by comas: ")
grades =  input("Enter grades seperated by comas: ")

# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
nstr = str (names)
nameslist = nstr.split (",")
print(nameslist)
	
astr = str (assignments)
list = astr.split (",")
assignmentslist = []
for i in list:
	assignmentslist.append(int(i))
	
	
gstr = str (grades)
list = gstr.split (",")
gradeslist = []
for i in list:
	gradeslist.append(int(i))

# convert each element as integers
li = []
for i in list:
	li.append(int(i))	
	

for i in range(len(nameslist)):
    print("Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n".format(nameslist[i],assignmentslist[i],gradeslist[i],(gradeslist[i]+assignmentslist[i]*2)))

