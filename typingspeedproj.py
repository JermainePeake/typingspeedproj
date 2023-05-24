'''
#read from a text file
file = open('typingproj.txt', 'r')
file.readlines()
file.close()

#allow user input and store it in a variable to be analyzed
inpt = input('begin typing:')
print(inpt)

#analyze user input for errors
if inpt == file:
    print('perfect accuracy 100%, u are a sexy savage')
if inpt != file:#check each character between the two texts
    #(the inpt and the file) and for each one that is in the file
    #but different in the inpt, add 1 to a counter and mark it in the
    #index
####################################################################################################################
#to do this accuracy check, I think I could do a for loop
#for every character in the string and for every character in ty
#if ch is equal to c, do nothing and continue?
#if i use a while loop:
#while len(string != 0), if string[ch] == ty[c], continue
#if string[ch] != ty[c], add 1 to counter, mark it in the index:
#print(str[ch]) and continue
ccounter = 0
wcounter = 0
string = "I'm the shit I farted I don't know how to potty."
string2 = "im THe shid I farted I dont kno how to party."
for ch in string:
    for c in string2:
        if ch == c:
            ccounter += 1
        if ch != c:
            wcounter += 1
print(ccounter,wcounter)
#with this nested for loop thing I had the right idea because according to chatgpt:
#Nested for loops are used when you need to iterate over multiple sequences (such as lists or strings) simultaneously
#which is exactly what i'm trying to do:
for outer_item in outer_sequence:
    for inner_item in inner_sequence:
        # do something with outer_item and inner_item
This means that the inner loop is executed in full for each iteration of the outer loop:

list1 = [1, 2, 3]
list2 = [4, 5, 6]

for num1 in list1:
    for num2 in list2:
        print(num1, num2)
#outputs:
1 4
1 5
1 6
2 4
2 5
2 6
3 4
3 5
3 6
#the first item in the first list is outputted 3 times and each item in the second list is outputted accordingly
#considering this i believe there is a way to achieve my goal here using a nested for loop, but now I will try
#sometihng else
Second, your nested loops are comparing each character in
string with every character in string2, which will result in duplicate comparisons and incorrect counts.
you are incrementing wcounter every time ch is not equal to c, which will count every possible pair of
characters that are not equal, resulting in a much larger count than the actual number of unique characters

#now im gonna try this accuracy thing with a while loop
#if i use a while loop:
#while len(string != 0), if string[ch] == ty[c], continue
#if string[ch] != ty[c], add 1 to counter, mark it in the index:
#print(str[ch]) and continue
ccounter = 0
wcounter = 0
string = "I'm the shit I farted I don't know how to potty."
string2 = "im THe shid I farted I dont kno how to party."
for i in string:
    while len(string) != 0:
        if string[i] == string2[i]:
            ccounter += 1
            continue
        else:
            wcounter += 1
            continue
print(ccounter,wcounter)


    
ccounter = 0
wcounter = 0
string = "I'm the shit I farted I don't know how to potty."
string2 = "im THe shid I farted I dont kno how to party."
news = ""
for i in string:
    if string[i] == string2[i]:#string indices must be int not str
        ccounter += 1
    else:
        wcounter += 1
    news += i

print(news, ccounter, wcounter)
#what I tried to do here is have the output be a new string
#what I can do with this is either put where the characters are equal
#or where the characters are not equal in this new string.
#if I choose not equal then I can count the length of the new string
#and get the amount of characters incorrect that way

ccounter = 0
wcounter = 0
string = "I'm the shit I farted I don't know how to potty."
string2 = "im THe shid I farted I dont kno how to party."
for i in string:
    if string2[i] not in string[i]:#same problem, string indices must be int not str
        wcounter += 1
    else:
        ccounter +=1

print(ccounter, wcounter)

#iterating through each letter of a string
string = 'baptism onion fire poop aids'
string2 = 'baptism shit fuck kms aids'

#ccounter = 0

string1 = "I'm the shit I farted I don't know how to potty."
string2 = "I'm the shid I farted I don't kno How to potty.."
wcounter = 0#this way of comparing the doesnt work because the strings must be the same size
for i in range(len(string1)):#never fully understood this until now tbh
    if string1[i] != string2[i]:
        wcounter +=1
print(wcounter)

#to fix this issue of different sized strings I could use the first string as a baseline,
#like set it as the minimum length
string1 = "hello"
string2 = "hell"

wcounter = 0
for i in range(min(len(string1), len(string2))):
    if string1[i] != string2[i]:
        wcounter += 1

print(wcounter)


string1 = "hello world"
string2 = "hella wyrld"
counter = 0
for i in range(len(string1)):
    if string1[i] != string2[i]:
        counter += 1
print(counter)
#####################################################################################################################
string1 = "I'm the shit I farted I don't know how to potty."
string2 = "i'm THe shid I farted I dont kno how to party."
string1 = string1.lower()
string2 = string2.lower()
wcounter = 0
for i in range(min(len(string1), len(string2))):
    if string1[i] != string2[i]:
        wcounter += 1

for i in range(min(len(string1), len(string2)), max(len(string1), len(string2))):#this is how to compare strings no matter what lenght
    wcounter += 1

print(wcounter)

#############################################MILESTONE MOMENT#######################################################################################
#after about 10 or more attempts and a few tears, and a lil bit of blood
#this code will compare 2 strings and output the amount of characters different in the second one from
#the first one
#this number will be displayed as mistyped characters
#to add to this I want the user to have some way of seeing where they messed up not just how much they messed up
#to do that, the easiest thing would be to output what they typed right below the given text
#or the super hard way would be to show each indice where there was a mistype.
#also I need to calculate the percentage for the actual accuracy and for this i will use a function.
#####################################################################################################################
#to calculate the accuracy percentage:
def acc(wcounter):
    accuracy = wcounter / len(string1)
    percent = float(accuracy) *100
    print('accuracy: {:.1f}%'.format(percent))#I was unaware of the format function until now
print(acc(wcounter))#also at this point i tried to use stackoverflow, it did not help at all.
#############################################################################################

#accuracy portion of this project is complete, i think.
#now we can begin to find out how fast the user types
#to do that, we will definitly have to use the time module, as the timer
#I'm about to look it up but first, I think the formula for calculating
#the typing speed, would involve the number of words (or characters?) typed
#the amount of time they were typed in
#so I think it would be something like time/words typed

#i need a timer object or something
from datetime import datetime
print(datetime.strptime('01:00','%M:%S'))

#read from a text file

file = open('typingproj.txt', 'r')
file.readlines()
file.close()

#allow user input and store it in a variable to be analyzed
inpt = input('begin typing:')
print(inpt)

def two_digits(val):
    s = str(val)
    if len(s) == 1:
        s = '0' + s
    return s

class Timer:
    def __init__(self, minutes=0, seconds=0):
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        return two_digits(self.__minutes) + ":" + \
               two_digits(self.__seconds)
                n
    def next_second(self):
        self.__seconds += 1
        if self.__seconds > 59:
            self.__seconds = 0
            self.__minutes += 1
            if self.__minutes > 59:
                self.__minutes = 0
                
    def prev_second(self):
        self.__seconds -= 1
        if self.__seconds < 0:
            self.__seconds = 59
            self.__minutes -= 1
            if self.__minutes < 0:
                self.__minutes = 59
                
timer = Timer(1, 00)
print(timer)
timer.prev_second()
print(timer)

#Currently (at the time im writing this) the output is:
#23:59:59
#00:00:00
#23:59:59
#I am going to get rid of the hours
#now I need to set it to 1 minute
#now I would need it to continually countdown until it reaches 0, so for this
#i will get rid of the 'next_second' part, since we are only interested in the previous seconed
#i've just realized that this may be different from actually counting down from 1 minute.
#at this point the output is now:
#01:00
#00:59
#an ive realized that I can make the code count down to 00:00, but, that would not represent
#actual time

#################################################################################################
#this is the time for the typing test
import time
time.sleep(60)
print('end test')#I just spent probably like an hour basically trying to figure these 3 lines fml

####################################################################################################
#full disclosure^ this is not my code it is someone elses from the class I was in
class Timer:
def __init__(self,hr,min,sec ):
self.__hr = hr
self.__min = min
self.__sec = sec

def __str__(self):
return timeFormat(self.__hr,self.__min,self.__sec)

def next_second(self):
if self.__sec == 59:
self.__sec = 00
if self.__min == 59:
self.__min = 00
if self.__hr == 23:
self.__hr = 00
else:
self.__hr+=1
else:
self.__min +=1

else:
self.__sec +=1
def prev_second(self):
if self.__sec == 00:
self.__sec = 59
if self.__min == 00:
self.__min = 59
if self.__hr == 00:
self.__hr = 23
else:
self.__hr -=1
else:
self.__min -=1

else:
self.__sec -=1

def timeFormat(hr,min,sec):
if sec <10:
sec = '0'+str(sec)
if min <10:
min = '0'+str(min)
if hr<10:
hr = '0'+str(hr)
return f'{hr}:{min}:{sec}'
###^^This is the bit that I forgot, the time format, I thought I could just
#format it within the return statement but no I forgot to make this method.
timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
#########################################################################################
#^this is mine

#putting together what i have so far, we are:
#reading and printing from a text file
#taking user input and calculating there mistyped characters and accuracy
#giving 1 minute for the test

#read from a text file
file = open('typingproj.txt', 'r')
file.readlines()
print(file)#do i print before or after i close?
file.close()

#allow user input and store it in a variable to be analyzed
inpt = input('begin typing:')
print(inpt)

#calculate mistyped characters and accuracy
if inpt == file:
    print('perfect accuracy 100%, u are a sexy savage')
if inpt != file:#check each character between the two texts
    #(the inpt and the file) and for each one that is in the file
    #but different in the inpt, add 1 to a counter and mark it in the
    #index
string1 = "I'm the shit I farted I don't know how to potty."
string2 = "i'm THe shid I farted I dont kno how to party."
string1 = string1.lower()
string2 = string2.lower()
wcounter = 0
for i in range(min(len(string1), len(string2))):
    if string1[i] != string2[i]:
        wcounter += 1

for i in range(min(len(string1), len(string2)), max(len(string1), len(string2))):#this is how to compare strings no matter what lenght
    wcounter += 1

print(wcounter)
#accuracy function
def acc(wcounter):
    accuracy = wcounter / len(string1)
    percent = float(accuracy) *100
    print('accuracy: {:.1f}%'.format(percent))#I was unaware of the format function until now
print(acc(wcounter))
#
#this is the time for the typing test
import time
time.sleep(60)
print('end test')
#now i need the calculation on how fast the user has typed, which as i said before i think the formula is
#time/characters##this is incorrect
#the equation is characters/5 = WPM
WPM = len(inpt)/5
WPM = (len(inpt)/5) / 1)

print(((48/5)/ .30))

#I believe this is all of the necessary components for my typing test, now I just need to put it all together
#as classes and objects
#as well as figure out how to actually open and read from a text file.
#idk if the code from chatgpt will work, but im thinking about separating it into multiple classes
#to add to the complexity of this project.


#i'm not done yet but before i forget, im gonna list the concepts covered in this project:

#time methods and modules
#for loops
#strings
#I/O operation

#I'm gonna cheat a lil bit rn i think and ask chatgpt to put this all together and see what happens
#i kinda regret this, it feels like cheating... it probably is

file = open("typingproj.txt",'r')
file = file.readlines()
print(file)#this actuallly does output from the text file, i just have no idea what file.
#file.close()

###since im not sure how operating with file from the IDLE environemnt works yet im just gonna
#copy from the anarchist cookbook by hand for a large string:
cookbook = """The method of making tear gas is so simple that anyone can do it. The two things to
remember are care and caution. You will need a certain amount of equipment but, just like the chemicals,
it is available from any hobby shop, or home chemical supplier. If you don't already own a gas mask,
go out and get one. They are sold at Army-Navy stores for under ten dollars. Listed below are the
materials necesssary: 1.Work in a garage, or outside if possible - not in the kitchen.
2. Mix ten parts of glycerine with two parts of sodium bisulfate, in flask (No.3), and heat. Do not fill more than
one-third of flask, as mixture froths when heated, When the frothing begins, adjust heat.""""

#this is the time calculation because the actual formula for WPM is
#WPM = (len(inpt)/5) / 1)
#WPM = (characters /5) / time)
print(((60/5)/60*10))
#################################################################
from time import sleep
seconds = 0
while True:
    try:
        seconds +=1
        sleep(1)
    except KeyboardInterrupt:#this will output the number of seconds it takes to type the prompt
        print(seconds) #so the equation will be ((len(self.inpt) /5) /seconds *.10#a little confused on the 10
        break# besides the calculation itself, i need to put the seconds in another function and pass that
        #into the 'calculate_wpm' function
    ####################################################################


print(((48/5)/.10))
string = 'four score and 11 buttcheeks ago'
print(len(string))
print(((len(string)/5)/.5))#I believe this is the right equation, but i need to turn my number of seconds
#into a
#Just made a realization that i dont need to take the number of seconds
#the test will be 1 minute, and the program will count the users input
#print(((len(inpt)/5)/1))


import time
class TypingTest:
    def __init__(self, filename):#the constructor sets up all of the components involved in the operation
        self.filename = filename#the name of the file to be passed to the constructor
        self.text = self.read_text_file()#text is the string read from the file
        self.inpt = None#users input
        self.wcounter = None#mistype counter
        self.accuracy = None#self explanatory
        self.elapsed_time = None
    
    def read_text_file(self):#the file to be opened,
        with open(self.filename, 'r') as f:
            return f.read()
    
    def start(self):
        self.inpt = input('Begin typing: ')
        self.calculate_accuracy()
        self.calculate_wpm()

    def calculate_accuracy(self):
        self.wcounter = 0
        for i in range(min(len(self.text), len(self.inpt))):
            if self.text[i] != self.inpt[i]:
                self.wcounter += 1

        for i in range(min(len(self.text), len(self.inpt)), max(len(self.text), len(self.inpt))):
            self.wcounter += 1

        self.accuracy = (1 - self.wcounter / len(self.text)) * 100
        print('Accuracy: {:.1f}%'.format(self.accuracy))

    def calculate_wpm(self):#WPM = (len(inpt)/5) / 1)
        self.elapsed_time = 60
        wpm = ((len(self.inpt) / 5) /1)
        print('WPM: {:.1f}'.format(wpm))

    def run(self):
        self.start()
        while self.elapsed_time > 0:
            time.sleep(1)
            self.elapsed_time -= 1
            print('end of test')
            break

test = TypingTest("""typingproj.txt """)
#print(TypingTest
#print(TypingTest.filename)
test.run()
print(test.elapsed_time)

    def time(self):#I think the function would look something like this???
        seconds = 0
while True:
    try:
        seconds +=1
        sleep(1)
    except KeyboardInterrupt:#this will output the number of seconds it takes to type the prompt
        print(seconds) #so the equation will be ((len(self.inpt) /5) /seconds *.10#a little confused on the 10
        break
        


test = TypingTest("""typingproj.txt """)
#print(TypingTest.filename)
test.run()
#this code seems to work but WPM calcualtion is off, and it needs to display the text to be typed
#but the accuracy seems to work
#finishing up tonight, my 3rd night of working on this (i tink)
#still don't know what file this is coming from, still need to work on the timer, i think i made some kind of
#progress with the wpm calculation tho.






































import time
class TypingTest:
    def __init__(self, filename):#the constructor sets up all of the components involved in the operation
        self.filename = filename#the name of the file to be passed to the constructor
        self.text = self.read_text_file()#text is the string read from the file
        self.inpt = None#users input
        self.wcounter = None#mistype counter
        self.accuracy = None#self explanatory
        self.elapsed_time = None
    
    def read_text_file(self):#4th  #the file to be opened,
        with open(self.filename, 'r') as f:
            return f.read()
    
    def start(self):#2nd
        self.take_nap()
        self.inpt = input('Begin typing: ')#inpt is entered #I NEED THE FUCKING GODDAMN INPUT AND TIMER TO START AT THE SAME TIME BUT IT SEEMS IMPOSSIBLE
        #raise KeyboardInterrupt#first i thought the program has to stop after the input
        self.calculate_accuracy()#jump to accuracy calculation
        self.calculate_wpm()
        #raise KeyboardInterrupt#then I thought no, it has to stop after the calculations

    
    def calculate_accuracy(self):#3rd
        self.wcounter = 0
        for i in range(min(len(self.text), len(self.inpt))):
            if self.text[i] != self.inpt[i]:
                self.wcounter += 1
        for i in range(min(len(self.text), len(self.inpt)), max(len(self.text), len(self.inpt))):
            self.wcounter += 1

        self.accuracy = (1 - self.wcounter / len(self.text)) * 100
        print('Accuracy: {:.1f}%'.format(self.accuracy))#


    def calculate_wpm(self):#WPM = (len(inpt)/5) / 1)#4th#
        self.elapsed_time = 60
        wpm = ((len(self.inpt) / 5) /1)
        print('WPM: {:.1f}'.format(wpm))

    def run(self):#1st
        print('when the text appears begin')
        time.sleep(3)
        print(self.text)
        self.start()#This input thing didn't exist
        #input('press enter to stop')#so the first thing the program does is find out mistyped characters and calculate your accuracy
        #while self.elapsed_time > 0:#5th#elapsed time should probably be deleted
            #because elapsed time will stay at 0, the sleep still happens, but the program runs until you hit enter basically
            #time.sleep(1)
            #self.elapsed_time -= 1#elapsed time is set to 60 in the 'calculate wpm' function, and is subtracted by 1. this does not
        print('end of test')###subtract 1 each time sleep decrements(new word learned lol)
            #break
    def take_nap(self):#this was seconds
        for i in range(60, 50, -1):
            time.sleep(1)
            print(i)
        try:
            raise KeyboardInterrupt
        except KeyboardInterrupt as e:
            print('end of test')
            self.calculate_accuracy()
            self.calculate_wpm()
            
        #print(self.calculate_accuracy())
        #print(self.calculate_wpm())
        #raise KeyboardInterrupt#now I have to figure out how to keep it here but still do the calculations
        #self.calculate_accuracy()
        #self.calculate_wpm()
            
        
        #self.elapsed_time=0



test = TypingTest("""typingproj.txt """)#this had a 1
#print(TypingTest
#print(TypingTest.filename)
test.run()
#the only changes chatgpt helped with this time were, just the parameters for the object, take_nap, and maybe one other thing
#and that input below the self.start(), which turns out to be unnecessary
#the problem now is that 'begin typing' appears after the sleep function is done. but if that input line
#above the take_nap line, then the timer wouldnt start until after the input is in.
#to fix this, i could have the first line in the run function say 'when you see the text start typing', and another
#sleep function that counts down from 3 or 5.
#but, because it basically does what i want it to do now, i wanna focus on the calculations because they are still
#fucked

#5/12/2023, coming back to this project about three weeks later. I still need to make the take_nap function and the begin typing input thing happen at around the same time
#but more importantly i need the end of test things to output when the count is dont.
#so how do I make the input stop once the countdown is over?
#maybe a for loop? or the map function?
#I need something to alert the code that the time has stopped
#maybe use the except function to do a keyboardinterrupt on the input once the sleep function is done.

#TypingTest.take_nap()
#with the take nap function as the
#5/14: I finally got the code to stop once the timer runs out, so now I just need to rearrange stuff so that
#the calculations are still outputted, as well as change the error message
#5/15 remember that the raise keyboard interrupt line must go in the take nap thing, for now.
#as I have it now, timer, input, raise keyboardinterrrupt as 'end of test' which allows
# the calculations to be outputted, but you still have to press enter to stop the test
#if i just have the keyboardinterrupt line without the try except thing it stops at the timer but doesnt output
#the calculations

try:
            raise KeyboardInterrupt
        except KeyboardInterrupt as e:
            print('end of test')
            print(e)

print(test.elapsed_time)

#I need to find out what file my code is getting the prompt from, and make it long enough that itll take a whole minute to type
#This way I don't need to keep track of time, I can just do the wpm calcualtion with 1 minute as part of the equation
#With that, I also need to make sure that the program stops once the sleep function is at 0
#find the file, change it. ##################################File is successfully found and changed############################################################################
#make the function stop once sleep is finished.
#and I want to display the text to be typed at the start (or run) of the program##############################text to be typed is successfully displayed##############################################
#after having tested the program, right now I still have to figure out how to stop the program once sleep has finished
#and im questioning if my accuracy AND wpm calculations are correct (I already knew my wpm was off but accuracy too?, hella wack)

import time
#how do I connect these so that elapsed time goes down by 1 every second, or in other words, as sleep is run
#or how do i 
class Student:
    def take_nap(self, seconds):
        print("I'm very tired. I have to take a nap. See you later.")
        time.sleep(seconds)
        print("I slept well! I feel great!")


student = Student()
student.take_nap(5)

import time
class Student:
    def take_nap(self, seconds):
        tim = '60'
        time.sleep(seconds)
        tim="59"
        time.sleep(seconds)
        tim='58'
        time.sleep(seconds)
        tim='57'
        time.sleep(seconds)
        tim="56"
        time.sleep(seconds)
        tim='55'
        time.sleep(seconds)
        tim='54'
        time.sleep(seconds)
        tim="53"
        time.sleep(seconds)
        tim='52'
        time.sleep(seconds)
        tim='51'
        time.sleep(seconds)
        tim="50"
        time.sleep(seconds)
        tim='49'
        print(tim)

student = Student()
student.take_nap(1)
#alright so i figured out how to make sleep run as a background to the program
#(probably not the best way to do it but it works so fuck you)
#now i just need to implement this into the program.

import time
def take_nap(seconds):
    for i in range(60, 50, -1):
        time.sleep(seconds)
        print(i)

take_nap(2)

import time


class TypingTest:
    def __init__(self, filename):
        self.filename = filename
        self.text = self.read_text_file()
        self.inpt = None
        self.wcounter = None
        self.accuracy = None
        self.elapsed_time = None

    def read_text_file(self):
        with open(self.filename, 'r') as f:
            return f.read()

    def start(self):
        self.take_nap()
        self.inpt = input('Begin typing: ')
        self.calculate_accuracy()
        self.calculate_wpm()

    def calculate_accuracy(self):
        self.wcounter = sum(1 for i, j in zip(self.text, self.inpt) if i != j)
        self.wcounter += abs(len(self.text) - len(self.inpt))
        self.accuracy = (1 - self.wcounter / len(self.text)) * 100
        print('Accuracy: {:.1f}%'.format(self.accuracy))

    def calculate_wpm(self):
        self.elapsed_time = 60
        wpm = len(self.inpt) / 5
        print('WPM: {:.1f}'.format(wpm))

    def run(self):
        print(self.text)
        self.start()
        input('Press Enter to end the test.')#this is the first difference between this and mine,
        print('End of test.')#I knew that while loop was fucked

    def take_nap(self):
        for i in range(60, 49, -1):
            time.sleep(1)
            print(i)
        self.elapsed_time = 0


test = TypingTest('typingproj.txt')
test.run()

import threading
import time

class TypingTest:
    def __init__(self):
        self.stop_b = False

    def a(self):
        t = threading.Thread(target=self.b)
        t.start()

        for i in range(5):
            time.sleep(1)
            print(f"A: {i}")

        #self.stop_b = True

    def b(self):
        while not self.stop_b:
            time.sleep(1)
            print("B: running")
        print("B: stopped")

test = TypingTest()
test.a()



#I'm keeping this because by fucking with some brackets (i think) i was able to make it output accuracy right before
#the keyboardinterrupt
when the text appears begin
The method of making tear gas is so simple that anyone can do it. The two things to
remember are care and caution. You will need a certain amount of equipment but, just like the chemicals,
it is available from any hobby shop, or home chemical supplier. If you don't already own a gas mask,
go out and get one. They are sold at Army-Navy stores for under ten dollars. Listed below are the
materials necesssary: 1.Work in a garage, or outside if possible - not in the kitchen.
2. Mix ten parts of glycerine with two parts of sodium bisulfate, in flask (No.3), and heat. Do not fill more than
one-third of flask, as mixture froths when heated, When the frothing begins, adjust heat.

60
59
58
57
56
55
54
53
52
51
end of test
Begin typing: The method of making tear gas is so simple that anyone can do it. 
Accuracy: 9.7%
Traceback (most recent call last):
  File "C:\sers\afron\AppData\Local\Programs\Python\Python311\typingspeedproj.py", line 625, in <module>
    test.run()
  File "C:sers\afron\AppData\Local\Programs\Python\Python311\typingspeedproj.py", line 592, in run
    self.start()#This input thing didn't exist
  File "C:\sers\afron\AppData\Local\Programs\Python\Python311\typingspeedproj.py", line 567, in start
    self.calculate_wpm()
  File "C:sers\afron\AppData\Local\Programs\Python\Python311\typingspeedproj.py", line 585, in calculate_wpm
    wpm = (len(self.inpt / 5) /1)
TypeError: unsupported operand type(s) for /: 'str' and 'int'
'''
import time

class TypingTest:
    def __init__(self, filename):
        self.filename = filename
        self.text = self.read_text_file()
        self.inpt = None
        self.wcounter = None
        self.accuracy = None
        self.elapsed_time = None

    def read_text_file(self):
        with open(self.filename, 'r') as f:
            return f.read()

    def start(self):
        print('When the text appears, begin typing.')
        time.sleep(3)  # Wait for 3 seconds before displaying the text
        print(self.text)
        start_time = time.time()  # Record the start time
        self.inpt = input('Begin typing: ')
        end_time = time.time()  # Record the end time
        self.elapsed_time = end_time - start_time
        self.calculate_accuracy()
        self.calculate_wpm()
        raise KeyboardInterrupt

    def calculate_accuracy(self):
        self.wcounter = 0
        for i in range(min(len(self.text), len(self.inpt))):
            if self.text[i] != self.inpt[i]:
                self.wcounter += 1
        for i in range(min(len(self.text), len(self.inpt)), max(len(self.text), len(self.inpt))):
            self.wcounter += 1

        self.accuracy = (1 - self.wcounter / len(self.text)) * 100
        print('Accuracy: {:.1f}%'.format(self.accuracy))

    def calculate_wpm(self):
        wpm = (len(self.inpt) / 5) / (self.elapsed_time / 60)
        print('WPM: {:.1f}'.format(wpm))

    def run(self):
        self.start()
        print(self.elapsed_time)
        print('End of test')

test = TypingTest("typingproj.txt")
test.run()

