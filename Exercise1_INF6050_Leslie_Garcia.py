
name = input('what is your name? ') #create a variable name with input function to assign a value
while True: #Create loop until human variable is selected
    species = input('Please enter if you are a "human" or "dog": ').lower() #Assign variable name, depending the input a question will be asked

    while species != 'human' and species != 'dog': #if value is dog or human then next question will be asked 
         species = input('Please enter "human" or "dog" exactly as written: ').lower()

    if species == 'dog': #create a variable name with input function to assign a value
         dog_age = input('How old are you (in dog years)? ') #create a variable name with input function to assign a value
         print('Wow! A ' + dog_age + '-year-old dog, that can type! That is awesome!/n')
    
    elif species == 'human': #if species matches 'human' then next set of questions
         print('Hello, human, are you sure you are not a dog? JK')
         break
#ok, human questions, now
school = input (' What is the name of your school? ') #create a variable name for the school with input function to assign a value
program = input (' What is the name of your program? ') #create string variable name for the program, assign value with input function
level = input('Grad or Undergrad? Choose wisely. ').lower() #create string variable and assigning value through input function, again!!! using function ".lower()" to convert the string value into lowercase    
     
while level != 'grad' and level != 'undergrad':
        level = input('Please enter "Grad" or "Undergrad" exactly as written: ').lower()
print(name +' is studying at ' + school + ' in the ' + program + ' program; ' + level +' level. ' 'Verified: is not a dog!!')