import sys 
import random 

def yn_valid():  #to valididate input reponse of user when asked for 'Y' for yes or 'N' for no
    while True:
        y_n_value=input('Enter Y/N').lower().strip()
        if y_n_value not in ('y', 'n'): 
            sys.stdout.write('\033[F') 
            sys.stdout.write('\033[K') 
            print('Please enter a valid response: Y/N')
            
        else:
            return y_n_value
             

def req_less_len(condition, length): #to ensure that a single given condition does not exceed minimum lenght and that it is not negative
        while True:
            try:
                inp='Enter how many minimum '+condition+' your password requires \n'
                condition_req=int(input(inp))
                
                if condition_req>length or condition_req<0:
                    sys.stdout.write('\033[F')
                    sys.stdout.write('\033[K')
                    print('Please enter a number between 0 and', length)
                else:
                    return condition_req
                    break
                
            except ValueError:
                print('Please enter a number')
                
            
def pass_condition_check(condition, min_required,in_password): #to check password against the given conditions. Output: how many of that condition user password lacks 
    global dum
    if in_password<min_required:
        x=min_required-in_password
        print('Your given password does not meet given requirement of', condition,'by', x, 'characters')
        dum=1
        return x
    else:
        print('Your password meet minimum', condition,' requirement')
        return 0
    
    
    
def randchr_pass_update(extra_needed, type_chr): #updates user password by adding 'extra_needed' number of 'type_chr' characters
    Charac={'Upper':'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'Lower':'abcdefghijklmnopqrstuvwxyz', 'Special':'!@#$%^&*()|~₹_-+=?><.,', 'Number':'123456789', 'All_chr':'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()|~₹_-+=?><.,123456789'}            
    
    global new_pass
    for i in range(extra_needed):
        x=random.randint(0, len(new_pass))
        new_pass.insert(x, random.choice(Charac[type_chr]))



#inputing the password and storing data about it 
#creates and gives values to the number of each type of character user password has
password=input('Please enter the password you want checked \n')
Len_pass=len(password)
Upp_count=Low_count=Spe_count=Num_count=0
for i in password:
    if i.isupper():
        Upp_count+=1
    elif i.islower():
        Low_count+=1
    elif i.isnumeric():
        Num_count+=1
    elif not i.isalnum():
        Spe_count+=1
        
        
               
print('Do you want to customize your password conditions \n \nIf you press N,you will proceed under standard conditions \n(Standard Conditions: \n-Minimum length is 8 \n-At least one uppercase character  \n-At least one lowercase character \n-At least one special character \n-At least one numerical character)')
Customize=yn_valid()    

if Customize=='y':
    
#establishing the conditions to check user password against 
    Length_req=int(input('Enter the minimum length you want your password to be'))
    Upper_req=req_less_len('uppercase letters', Length_req)
    Lower_req=req_less_len('lowercase letters', Length_req)
    Special_req=req_less_len('special characters', Length_req)
    Number_req=req_less_len('numbers', Length_req)
    
    
    #Ensuring that the individual requirements do not exceed minimum length 
    #assumes Length_req, Upper_req, Lower_req, Special_req, Number_req exist and are valid. keeps them valid
    
    if Upper_req+Lower_req+Special_req+Number_req>Length_req:
        print('Your individual requirements combined exceed given minimum length by', (Upper_req+Lower_req+Special_req+Number_req)-Length_req)
        print("Press 'Y' if you want to re-enter the values")
        print("Press 'N' if you want us to extend minimum length to match requirements")
        
        re_enter=yn_valid()
        if re_enter=='n':
            Length_req=Upper_req+Lower_req+Special_req+Number_req
            print('Minimum length has been updated to fit given requirements')
        
        elif re_enter=='y':
            
            #validates the requirements so they are less than or equal to min length
            while True:
                print('Press: \n1 to re-enter all values \n2 to re-enter only required length \n3 to re-enter only required number of uppercase character \n4 to re-enter only required number of lowercase character \n5 to re-enter only required number of special character \n6 to re-enter only required number of numerical character')
                
                
                while True:
                    #gives user choice to change all values or one specific value
                    
                    value_change=int(input())
                    if value_change==1:
                        Length_req=int(input('Enter the minimum length you want your password to be'))
                        Upper_req=req_less_len('uppercase letters', Length_req)
                        Lower_req=req_less_len('lowercase letters', Length_req)
                        Special_req=req_less_len('special characters', Length_req)
                        Number_req=req_less_len('numbers', Length_req)
                        
                    elif value_change==2:
                        Length_req=int(input('Enter the minimum length you want your password to be'))
                        break
                    elif value_change==3:
                        Upper_req=req_less_len('uppercase letters', Length_req)
                        break
                    elif value_change==4:
                        Lower_req=req_less_len('lowercase letters', Length_req)
                        break
                    elif value_change==5:
                        Special_req=req_less_len('special characters', Length_req)
                        break
                    elif value_change==6:
                        Number_req=req_less_len('numbers', Length_req)
                        break
                    else:
                        print('Please enter a valid value from the given menu')
                        print('Press: \n1 to re-enter all values \n2 to re-enter only required length \n3 to re-enter only required number of uppercase character \n4 to re-enter only required number of lowercase character \n5 to re-enter only required number of special character \n6 to re-enter only required number of numerical character')
                             
                        
                #breaking out of loop when the requirements are less than or equal to min length         
                if Upper_req+Lower_req+Special_req+Number_req<=Length_req:
                    break
                

else:
    Length_req=8
    Upper_req=1
    Lower_req=1    
    Special_req=1
    Number_req=1
    
    
    
#checking password against the entered conditions
dum=0 #to check if any condition is violated: if violated, it will make dum=1
uc=lc=sc=nc=lenc=0
lenc=pass_condition_check('length', Length_req, Len_pass)
uc=pass_condition_check('uppercase letters', Upper_req, Upp_count)
lc=pass_condition_check('lowercase letters', Lower_req, Low_count)
sc=pass_condition_check('special characters', Special_req, Spe_count)
nc=pass_condition_check('numbers', Number_req, Num_count)

    
if dum!=0:
    print('Would you like us to internally add the missing conditions?')
    print("\tNote: The added letters, numbers, and/or special characters are randomized and your new password will be displayed at the end")
    pass_change=yn_valid()
    
    
    if pass_change=='y':
        
        new_pass=list(password)
    
        randchr_pass_update(uc, 'Upper')
        randchr_pass_update(lc, 'Lower')
        randchr_pass_update(sc, 'Special')
        randchr_pass_update(nc, 'Number')
        
        lenc=Length_req-(len(new_pass))
        randchr_pass_update(lenc, 'All_chr')    
            
        
        Password_updated=''
        for i in new_pass:
            Password_updated+=i
            
        
        print('Your new password that meets your given conditions is', Password_updated)
        print('Thank you for visiting us!')
        
    else:
        print('Thank you for visiting us!')
        
else:
    print("Your password meets all your given equirements!")            
    print('Thank you for visiting us!')
    print("You're good to go")
        