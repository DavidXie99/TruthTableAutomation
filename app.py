import funcs

ass_name = input("Which assignment is this? ")

var_names = []
while 1:
    var_name = input("Enter your variable name\n (enter -1 to quit): ")
    if var_name == '-1':
        break
    var_names.append(var_name)


funcs.generateTable(var_names,ass_name)

print("Done")
    
