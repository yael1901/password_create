#!/usr/bin/env python3
#--------------------------------------------------------------------------------------------------
#cabesera y variables globales 
#--------------------------------------------------------------------------------------------------
 
import random
topics = ('Technology', 'Sustainability', 'Travel', 'Science', 'Growth', 'Art', 'History', 'Music', 'Literature', 'Sports')

x = True
#--------------------------------------------------------------------------------------------------
 #menu
#--------------------------------------------------------------------------------------------------





print('/////////////////////////////////////////////////\n')
print('********        ********      ********        ********      ********        ********       *******      ********')        
print('********        ********      ********        ********      ********        ********       *******      ********')        
print('********        ********      ********        ********      ********        ********       *******      ********')        
print('********        ********      ********        ********      ********        ********       *******      ********')        
print('********        ********      ********        ********      ********        ********       *******      ********')        
print('********        ********      ********        ********      ********        ********       *******      ********')        
print('********        ********      ********        ********      ********        ********       *******      ********')        
print('********        ********      ********        ********      ********        ********       *******      ********')        
print('********        ********      ********        ********      ********        ********       *******      ********')        
print(' **********************        *****************************************************        ******************* ')
print('   ******************            *************************************************            ***************   ')
print('     **************                *********************************************                ***********  \n   ')

print("password creator")
print("uwu")
print('/////////////////////////////////////////////////\n')



print("in this program you can create password with you want")

print('if you wacht menu choose paramether h')







#--------------------------------------------------------------------------------------------------
 #inicio de el bucle
#--------------------------------------------------------------------------------------------------
 
 
while  x == True:
    lether =     input(str("chose you opcion> "))
#--------------------------------------------------------------------------------------------------
# funciones  
#--------------------------------------------------------------------------------------------------    
    def e():
        
        
        random_element = random.choice(topics)
        word_1 = input(str(f"Enter your favorite topic from {random_element}> "))
        word_list = list(word_1)
        password = [] 
        for lether in word_list:
            cuantic_number = random.randint(0,1)
            
            if lether == ' ':
                lether = '_'
                password.append(lether)
            
            elif lether == 'A':
                if cuantic_number == 1 :
                    lether = '4'
                    password.append(lether)
                else:
                    password.append(lether)

            elif lether == 'a':
                if cuantic_number == cuantic_number:
                    lether = '@'
                    password.append(lether)
                else:
                    password.append(lether)
            
            elif lether == 'E':
                if cuantic_number == 1 :
                    lether = '3'
                    password.append(lether)
                else:
                    password.append(lether)

            elif lether == 'O':
                if cuantic_number == cuantic_number :
                    lether = '0'
                    password.append(lether)
                else:
                    password.append(lether)

            elif lether == 'o':
                if cuantic_number == cuantic_number :
                    lether = '0'
                    password.append(lether)
                else:
                    password.append(lether)

            elif lether == 'l':
                if cuantic_number == 1 :
                    lether = '1'
                    password.append(lether)
                else:
                    password.append(lether)
            
            elif lether == 'i':
                if cuantic_number == 1 :
                    lether = '1'
                    password.append(lether)
                else:
                    password.append(lether)
            
            elif lether == 'C':
                if cuantic_number == 1 :
                    lether = '<'
                    password.append(lether)
                else:
                    password.append(lether)

            elif lether == 'c':
                if cuantic_number == 1 :
                    lether = '<'
                    password.append(lether)
                else:
                    password.append(lether)
            else:
                password.append(lether)
            
        password_new = ''.join(password)
        print(password_new)
    
        print("\n\nThis password should only be used temporarily and must be changed immediately.")
    def m():
       #-------------------------------------------------------------------------------hacemos eleccion de temas aleatoris        
        random_element = random.choice(topics)
        random_element_second = random.choice(topics)
       #-------------------------------------------------------------------------------------------preguntamos sobre temas            
        word_first = input(str(f"Enter your favorite topic from {random_element}> "))
        word_second = input(str(f"Enter your favorite topic from {random_element_second}> "))
       #----------------------------------------------------combinamos temas y las cambiamos de orden para mayor seguridad                         
        combination = []
        combination.append(word_first)        
        combination.append(word_second)
        random.shuffle(combination)
        combination.insert(1,"_")
       #---------------------------------------------------------sacamos elementos para volverlos caracteres para su modificacion
        element_first = (combination.pop(0))
        element_second = (combination.pop(0))
        element_third = (combination.pop(0))
        
       #-----------------------------------------------------------------agrego todas las palabras para su iteracion 
      #     word_list = []
      #      word_list.append(element_first)
      #       word_list.append(element_second)
      #        word_list.append(element_third)
        
      #------------------------------------------------------------------union de los caracteres en una lista unica
        word_list_second = [] 
        
        for element in element_first:
            word_list_second.append(element)
        
        for element in element_second:
            word_list_second.append(element)
    
        
        for element in element_third:
            word_list_second.append(element)
        
           
      #----------------------------------------------------------------------cambio de caracteres
        password = []
        for lether in word_list_second:
            cuantic_number = random.randint(0,1)
            
            if lether == ' ':
                lether = '_'
                password.append(lether)
            
            elif lether == 'A':
                if cuantic_number == 1 :
                    lether = '4'
                    password.append(lether)
                else:
                    password.append(lether)

            elif lether == 'a':
                if cuantic_number == cuantic_number:
                    lether = '@'
                    password.append(lether)
                else:
                    password.append(lether)
            
            elif lether == 'E':
                if cuantic_number == 1 :
                    lether = '3'
                    password.append(lether)
                else:
                    password.append(lether)

            elif lether == 'O':
                if cuantic_number == cuantic_number :
                    lether = '0'
                    password.append(lether)
                else:
                    password.append(lether)

            elif lether == 'o':
                if cuantic_number == cuantic_number :
                    lether = '0'
                    password.append(lether)
                else:
                    password.append(lether)

            elif lether == 'l':
                if cuantic_number == 1 :
                    lether = '1'
                    password.append(lether)
                else:
                    password.append(lether)

            elif lether == 'i':
                if cuantic_number == 1 :
                    lether = '1'
                    password.append(lether)
                else:
                    password.append(lether)
            
            elif lether == 'C':
                if cuantic_number == 1 :
                    lether = '<'
                    password.append(lether)
                else:
                    password.append(lether)

            elif lether == 'c':
                if cuantic_number == 1 :
                    lether = '<'
                    password.append(lether)
                else:
                    password.append(lether)
            else:
                password.append(lether)
            
        
        password_new = ''.join(password)
        print(password_new)
    
        print("\n\nThis password is secure but isn't the best.")


         

    
    
    def H():
        
       #-------------------------------------------------------------------------------hacemos eleccion de temas aleatoris        
            random_element = random.choice(topics)
            random_element_second = random.choice(topics)
            random_element_third = random.choice(topics)
       #-------------------------------------------------------------------------------------------preguntamos sobre temas            
            word_first = input(str(f"Enter your favorite topic from {random_element}> "))
            word_second = input(str(f"Enter your favorite topic from {random_element_second}> "))
            word_third = input(str(f"Enter your favorite topic from {random_element_third}"))
       #----------------------------------------------------combinamos temas y las cambiamos de orden para mayor seguridad                         
            combination = []
            combination.append(word_first)        
            combination.append(word_second)
            combination.append(word_third)
            random.shuffle(combination)
            combination.insert(1,"_")
            combination.insert(3,"_")
       #---------------------------------------------------------sacamos elementos para volverlos caracteres para su modificacion
            element_first = (combination.pop(0))
            element_second = (combination.pop(0))
            element_third = (combination.pop(0))
            element_fourth = (combination.pop(0))
            element_fifth = (combination.pop(0))
       #-----------------------------------------------------------------agrego todas las palabras para su iteracion 
      #     word_list = []
      #      word_list.append(element_first)
      #       word_list.append(element_second)
      #        word_list.append(element_third)
        
      #------------------------------------------------------------------union de los caracteres en una lista unica
            word_list_second = [] 
        
            for element in element_first:
                word_list_second.append(element)
            
            for element in element_second:
                word_list_second.append(element)
    
        
            for element in element_third:
                word_list_second.append(element)


            for element in element_fourth:
                word_list_second.append(element)
    
        
            for element in element_fifth:
                word_list_second.append(element)
            

            #----------------------------------------------------------------------cambio de caracteres
            password = []
            for lether in word_list_second:
                cuantic_number = random.randint(0,1)
            
                if lether == ' ':
                    lether = '_'
                    password.append(lether)
            
                elif lether == 'A':
                    if cuantic_number == 1 :
                        lether = '4'
                        password.append(lether)
                    else:
                        password.append(lether)

                elif lether == 'a':
                    if cuantic_number == cuantic_number:
                        lether = '@'
                        password.append(lether)
                    else:
                        password.append(lether)
            
                elif lether == 'E':
                    if cuantic_number == 1 :
                        lether = '3'
                        password.append(lether)
                    else:
                        password.append(lether)

                elif lether == 'O':
                    if cuantic_number == cuantic_number :
                        lether = '0'
                        password.append(lether)
                    else:
                        password.append(lether)

                elif lether == 'o':
                    if cuantic_number == cuantic_number :
                        lether = '0'
                        password.append(lether)
                    else:
                        password.append(lether)

                elif lether == 'l':
                    if cuantic_number == 1 :
                        lether = '1'
                        password.append(lether)
                    else:
                        password.append(lether)

                elif lether == 'i':
                    if cuantic_number == 1 :
                        lether = '1'
                        password.append(lether)
                    else:
                        password.append(lether)
            
                elif lether == 'C':
                    if cuantic_number == 1 :
                        lether = '<'
                        password.append(lether)
                    else:
                        password.append(lether)

                elif lether == 'c':
                    if cuantic_number == 1 :
                        lether = '<'
                        password.append(lether)
                    else:
                        password.append(lether)
                else:
                    password.append(lether)
            
        
            password_new = ''.join(password)
            print(password_new)
    
            print("\n\nThis password is the best.")
    
    def h():
        print('you can create "insegure password" "medium passwords" "insane password"')

 
        print("chose the opcion correct for you\n")
        print("'h' for help menu")
        print("'e' for easy password >>> this password is easy and short but is insegure")
        print("'m' for medium password>>> this password is medium, easy and have more security")
        print("'H' for insane password >>> this password is hard, is hard and very secure\n")
    
#--------------------------------------------------------------------------------------------------
#parametros 
#--------------------------------------------------------------------------------------------------

   

    if lether == 'e':
        e()

    elif lether == 'm':
        m()
  
    elif lether == 'H':
        H()

    elif lether == 'h':
        h()    
    else :
        h()

