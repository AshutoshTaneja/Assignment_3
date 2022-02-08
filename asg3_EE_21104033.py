"""----------------------question1----------------------"""
print("Question1")
userInputStr = input("Enter a string: ")
if(len(userInputStr.split()) > 1):  #splits the string into array of words and then checks its length

    #splits the input string in a list of words using split() method then...
    #...adds "<number of occurances> "<the word>"," for each word in the list to a new list
    words = ["%d \"%s\","%(userInputStr.split().count(a),a) for a in userInputStr.split()]  #uses list comprehension

    wordsFiltered = list(set(words)) #converts the list words to a set hence filtering it and then converts it to list again

    print("The String contains: ", *wordsFiltered)
else:
    #adds "<number of occurances> '<the character>'," for each character in the word string to a list
    characters = ["%d '%s',"%(userInputStr.count(a),a) for a in userInputStr] 
    charactersFiltered = list(set(characters))
    print("The String contains:", *charactersFiltered)




"""----------------------question2----------------------"""
print("\nQuestion2")
inputDay = int(input("Day-"))
inputMonth = int(input("Month-"))
inputYear = int(input("Year-"))

def isLeapYear(year):
    if(year%4 == 0):
        if(year%400 == 0):
            return True
        elif(year%100 == 0):    #a year is not considered a leap year if it's divisible by 100 provided it's not divisible by 400
            return False
        else:
            return True
    return False

if((inputDay >= 1 and inputDay <= 31) and (inputMonth >= 1 and inputMonth <= 12) and (inputYear >= 1800 and inputYear <= 2025)): #checks if the input date lies within given constraints 
    if(inputMonth == 2 and isLeapYear(inputYear) and inputDay == 29): 
        print(f"Next Date is: 01/03/{inputYear}")
    elif(inputMonth == 2 and inputDay > 28):    
        print(f"Error: Input Date is out of range for given month and year.")   #***produces error if user enters a date that is out of range for february month***
    elif(inputMonth == 2 and not isLeapYear(inputYear) and inputDay == 28):
        print(f"Next Date is: 01/03/{inputYear}")   
    elif(inputDay == 31 and inputMonth == 12):
        print(f"Next Date is: 01/01/{inputYear+1}")
    elif((inputMonth == 4 or inputMonth == 6 or inputMonth == 9 or inputMonth == 11) and inputDay == 30):
        print(f"Next Date is: 01/{inputMonth+1:02d}/{inputYear}")
    elif((inputMonth == 4 or inputMonth == 6 or inputMonth == 9 or inputMonth == 11) and inputDay == 31):
        print("Error: Input Date is out of range for given month.")   #***produces error if user enters a date that is out of range for months with 30 days***
    elif(inputDay == 31):
        print(f"Next Date is: 01/{inputMonth+1:02d}/{inputYear}")
    else:
        print(f"Next Date is: {inputDay+1:02d}/{inputMonth:02d}/{inputYear}")
else:
    print("Error: Input date fails to meet the constraints: \n1<=Month<=12\n1<=Day<=31\n1800<=Year<=2025") #***produces error if user enters a date that fails to meet the given constraints***




"""----------------------question3----------------------"""
print("\nQuestion3")
list = [3,9,16,23,2,1,5,43]
print([(a,a*a) for a in list])  #using list comprehension




"""----------------------question4----------------------"""
print("\nQuestion4")
inputGrade = int(input("Enter your Grade Point: "))
performanceDict = {10:"Outstanding", 9:"Excellent", 8:"Very Good", 7:"Good", 6:"Average", 5:"Below Average", 4:"Poor"}
gradeDict = {10:"A+", 9:"A", 8:"B+", 7:"B", 6:"C+", 5:"C", 4:"D"}
if(inputGrade <= 10 and inputGrade >= 4):
    print("Your Grade is '%s' and %s Performance."%(gradeDict[inputGrade],performanceDict[inputGrade]))
else:
    print("Error: Grade is out of range.")




"""----------------------question5----------------------"""
print("\nQuestion5")
patternStr = "ABCDEFGHIJK"
i = len(patternStr)
while(i != -1):
    print(" "*int((len(patternStr)-i)/2) + patternStr[0:i] + " "*int((len(patternStr)-i)/2))
    i -= 2




"""----------------------question6----------------------"""
print("\nQuestion6")
studentName = input("Name: ")
studentSID = int(input("SID: "))
studentsInfo = {studentSID: studentName}
while(input("Type 'Y' to enter more student information Else type 'N' to leave.\n") == "Y"):    #inputs student name and SID till user wants 
    studentName = input("Name: ")
    studentSID = int(input("SID: "))
    studentsInfo[studentSID] = studentName

    #part a.
print("\nPart a.")
for key,value in studentsInfo.items():
    print(key, " : ", value)

    #part b.
print("\nPart b.")
def findKey(val):   #finds keys to specific values in dictionary
    for key,value in studentsInfo.items():
        if(val == value):
            return key
sortedByValues = []
for value in sorted(studentsInfo.values()):
    sortedByValues.append((findKey(value), value)) #adds tupple (<key>, <value>) to list according to sorted values
print(dict(sortedByValues))    #converts list to dict keeping order intact

    #part c.
print("\nPart c.")
sortedByKeys = []
for key in sorted(studentsInfo.keys()):
    sortedByKeys.append((key, studentsInfo[key]))
print(dict(sortedByKeys))

    #part d.
print("\nPart d.")
print(studentsInfo[int(input("Enter student SID to get student's name: "))])




"""----------------------question7----------------------"""
print("\nQuestion7")
terms = int(input("How many terms of fibonacci series do you want to print: ")) #Since the number of terms to print is not mentioned in the question user input is taken
a = 0
b = 1
seriesArray = [0,1]
for _ in range(0,terms-2):
    c = a+b
    a = b
    b = c
    seriesArray.append(c)
print("The Fibonacci series is: ", *seriesArray)
print("Average of the above Fibonacci series is %.2f"%(sum(seriesArray)/len(seriesArray))) #prints average of series by dividing sum by number of terms(lenth of array)




"""----------------------question8----------------------"""
print("\nQuestion8")
Set1 = {1,2,3,4,5}
Set2 = {2,4,6,8}
Set3 = {1,5,9,13,17}
    #part a.
print("Part a." ,end = " ")
Set4 = Set1-Set2 | Set2-Set1
print(Set4)
    #part b.
print("Part b." ,end = " ")
Set5 = Set1 - (Set1&Set2 | Set1&Set3) | Set2 - (Set2&Set1 | Set2&Set3) | Set3 - (Set3&Set1 | Set3&Set1)
print(Set5)
    #part c.
print("Part c." ,end = " ")
Set6 = Set1&Set2 | Set2&Set3 | Set1&Set3
print(Set6)
    #part d.
print("Part d." ,end = " ")
Set7 = set([a for a in range(1,11) if a not in Set1])
print(Set7)
    #part e.
print("Part e." ,end = " ")
Set8 = set([a for a in range(1,11) if a not in (Set1 | Set2 | Set3)])
print(Set8) 
