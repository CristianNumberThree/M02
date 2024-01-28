#Cristian Escobedo
#M02 Lab-Case Study v1.3
#The purpose of this program is to determine whether the student being specified belongs in of two possible categories and if they do not then they are considered neutral
#Declaration of variables
name=""
gpa=0.0
ZZZ="ZZZ"

#While loop that asks for a name and a gpa
while name != ZZZ:

    #Asks for a student name to be used later for results or ask for the variable ZZZ to end the program
    print("Enter a student's last name and press enter to continue / type ZZZ and press enter to quit")

    #The first string variable stored for labeling purposes
    name=input()

    #Determines that if the string entered is ZZZ to deviate from the normal loop
    if name == ZZZ:

        #The exit statement
        print("End of program close window")
        break

    #Continues if ZZZ was not entered
    else:
        
        #statement that prints asking for a float value to compare in the if statement
        print("Enter the student's GPA and press enter")
        
        #The variable to be compared
        gpa=float(input())
        
        #Checkpoint 1 if the GPA applies then the student recieves a special status
        if gpa > 3.49:
            print(name,"has made the Dean's List")
        
        #Checkpoint 2 if the GPA didn't apply to the above checkpoint but this checkpoint does apply then a statement prints
        elif gpa > 3.25:
            print(name,"has made the Honor Roll")
        
        #Statement that prints if niether of the above mentioned statuses applies
        else:
            print("No status change for",name)
