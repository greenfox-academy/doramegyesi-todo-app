import sys
print(sys.argv)

text = open("todo_app.txt", "r")
todo_list = text.readlines()
text.close()

def print_todo_list():
    if len(todo_list) == 0:
        print("No todos for today, man!")
    else:
        for todo in range(len(todo_list) + 1):
            print(str(todo) + " " + (todo_list[todo - 1]))

def controller():
    if sys.argv[1] == "-l":
        print_todo_list()


controller()




#if len(arguments) == 0:
#    print('')
#else:
	#if( arguments[0] == '-l' ):
		#print('something', arguments[1])

def print_help():
    help_info =    ["Python todo application",
                    "=======================",
                    "Command line arguments:",
                    "-l Lists all the tasks",
                    "-a Adds a new task",
                    "-r Removes a task",
                    "-c Completes task"]

    for content in help_info:
        print(content)
