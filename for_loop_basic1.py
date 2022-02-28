# Basic - Print all integers from 0 to 150.
def question1():
    for i in range(150):
        print(i)
question1()        

# Multiples of Five - Print all the multiples of 5 from 5 to 1,000

def question2():
    for i in range(5,1001,5):
        print(i)
question2()        

# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
def question3():
    for i in range(100):
        print(i)
        if i%5==0:
            print("coding")
        if i%10==0:
            print("coding dojo")
question3()            

# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
def question4():
    sum = 0
    for i in range(500001):
        if i%2==1:
            sum += i 
    print(sum)
question4()   

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
def question5():
    for i in range(2018,0,-4):
        print(i)
question5()     

# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)            

def question6():
    lowNum=2
    highNum=9
    mult=3
    output=''
    for i in range(lowNum,highNum+1,1):
        if i%mult == 0:
            output+=str(i)+', '
    print(output)            
question6()    