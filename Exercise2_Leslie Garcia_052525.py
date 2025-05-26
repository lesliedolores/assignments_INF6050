print("\033[2J\033[H", end="", flush=True) # clears, ensures no new line
# and ensures immediate print
# the ansi code here is interpreted as clearing the screen with `\033[2J` but it
# doesn't move the cursor back to the beginning which is why `\033[H` is used x=5
import sys
book = 'The great gatsby'
book = book.lower() 
author = ' F. Scott Fitzgerald'
check1 = int(0)
check2 = int(0)
check3 = int(0)

#This is the defined function which will promt three times in a 'while' loop, until the 3 words are guessed
def guess_function():
    while True:
        try:
         print("There are three words in the title, please guess a word")
         word_1 = str(input())
         word_1= word_1.lower()           #Function lower() will conver all the variables in teh string word_1 into lower caps.
         if word_1 == 'quit':
           print("Thank you for participating, Good bye!")
           sys.exit()

         if word_1 in book:   #if word_1 is in the book string then it will go into the if loop
          global check1
          global check2
          global check3
          
          if word_1 =="the" and check1 == 0 :
             print("You guessed the 1st word ")
             check1 += 1
             
             return
          if word_1 =="great" and check2 == 0 :
             print("you guessed the 2nd word")
             check2 += 1
             return
          if word_1 =="gatsby" and check3 == 0:
             print("you guessed the third word")
             check2 +=  1
             return
          
          
         else:
          print("There are no matches ")
        except ValueError:
         print('You guessed a word')
         return
    
#The main program starts here 
print("Please guess the name of the book. Hint: This book was adapted into a movie. \n " \
"Hint: The main chartacter was played by Leonardo Di  Caprio")
print("The AUTHOR IS: ", author)
print(" Hint 2: There are 3 words in the title ")
print(" Hint 3: The book takes place during the Jazz Age on Long Island and is narrated in first person")
print(" The final hint: The book starts with the letter T")
print("At any point, if you would like to exit just type: QUIT")  #option for user to exit out
count = 0   
while count <3 :    # create loop while cycle until the three words of the book tittle are guessed. 
   #Varibalbe count starts at zero and will add +1 with each word guessed. 
   ##Loop  will continue until the count variable equals 3
   guess_function()   # CALLING  function guess_fuction()
   count += 1 
   print("number of words guessed", count)
print("HURRAY!!!!!! you guessed the 3 words, the book name is  The Great Gatsby")
