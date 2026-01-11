#Password Strength Checker
import sys 
import random as r

#taking in the conditions user wants
password=input('Please enter the password you want checked \n')


print('Do you want to customize your password conditions \n \nIf you press N,you will proceed under standard conditions \n(Standard Conditions: \n-Minimum length is 8 \n-At least one uppercase character  \n-At least one lowercase character \n-At least one special character \n-At least one numerical character)')
while True:
    Customize=input('Enter Y/N').lower().strip()
    if Customize not in ('y', 'n'): 
        sys.stdout.write('\033[F') 
        sys.stdout.write('\033[K') 
        print('Please enter a valid response: Y/N')
    else:
        break 
    

if Customize=='y':
    length_req=int(input('Enter the minimum length you want your password to be'))
    
    while True:
        try:
            Upper_req=int(input('Enter how many minimum uppercase letters your password requires \n'))
            
            if Upper_req>length_req or Upper_req<0:
                sys.stdout.write('\033[F')
                sys.stdout.write('\033[K')
                print('Please enter a number between 0 and', length_req)
            else:
                break
            
        except ValueError:
            print('Please enter a number')

        
    
    while True:
        try:
            
            Lower_req=int(input('Enter how many minimum lowercase letters your password requires \n'))
            if Lower_req>length_req or Lower_req<0:
                sys.stdout.write('\033[F')
                sys.stdout.write('\033[K')
                print('Please enter a number between 0 and', length_req)
            else:
                break
        except ValueError:
            print('Please enter a number')
            
    while True:
        try:
            
            Special_req=int(input('Enter how many minimum special characters your password requires \n'))
            if Special_req>length_req or Special_req<0:
                sys.stdout.write('\033[F')
                sys.stdout.write('\033[K')
                print('Please enter a number between 0 and', length_req)
            else:
                break
            
        except ValueError:
            print('Please enter a number')
            
            
        
    while True:
        
        try:
            Number_req=int(input('Enter how many minimum numbers your password requires \n'))
            
            if Number_req>length_req or Number_req<0:
                sys.stdout.write('\033[F')
                sys.stdout.write('\033[K')
                print('Please enter a number between 0 and', length_req)
            else:
                break
            
        except ValueError:
            print('Please enter a number')
        
        
    if Upper_req+Lower_req+Special_req+Number_req>length_req:
        print('Your requirements require minimum length of password to be', Upper_req+Lower_req+Special_req+Number_req)
        print('Minimum length has been updated to fit given requirements')
        length_req=Upper_req+Lower_req+Special_req+Number_req

        
        
    #arranging what the password actually has    
    

    length_pass=len(password)
    Upper_pass=[]
    Lower_pass=[]
    Number_pass=[]
    Special_pass=[]

    for i in password:
        if i.isupper():
           Upper_pass.append(i) 
        elif i.islower():
            Lower_pass.append(i)
        elif i.isnumeric():
            Number_pass.append(i)
        elif not i.isalnum():
            Special_pass.append(i)
            
    #checking password against the entered conditions
    dum=0 #to check if any condition is violated

    uc=lc=sc=nc=0
    
    if length_pass<length_req:
        x=length_req-length_pass
        print('Your given password is shorter than required by', x, 'characters')
        dum=1
    else:
        print('Your password meet minimum length requirement')
        
    if len(Upper_pass)<Upper_req:
        uc=Upper_req-len(Upper_pass)
        print('Your given password has', uc, 'less uppercase characters than you require')
        dum=1
    else:
        print('Your password meet minimum uppercase alphabet requirement')
    
    if len(Lower_pass)<Lower_req:
        lc=Lower_req-len(Lower_pass)
        print('Your given password has', lc, 'less lowercase characters than you require')
        dum=1
    else:
        print('Your password meet minimum lowercase alphabet requirement')
        
    if len(Special_pass)<Special_req:
        sc=Special_req-len(Special_pass)
        print('Your given password has', sc, 'less special characters than you require')
        dum=1
    else:
        print('Your password meet minimum special character requirement')

    if len(Number_pass)<Number_req:
        nc=Number_req-len(Number_pass)
        print('Your given password has', nc, 'less numerical characters than you require')
        dum=1
    else:
        print('Your password meet minimum number requirement')
        
    
    if dum!=0:
        print('Would you like us to internally add the missing conditions?')
        print("\tNote: The added letters, numbers, and/or special characters are randomized and your new password will be displayed at the end")
        pass_change=input('Press Y/N for the above: \n').lower().strip()
        while True:
            if pass_change not in ('y', 'n'): 
                sys.stdout.write('\033[F') 
                sys.stdout.write('\033[K') 
                print('Please enter a valid response: Y/N')
            else:
                break 
            
        
        if pass_change=='y':
            Upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            Lower='abcdefghijklmnopqrstuvwxyz'
            Special='!@#$%^&*()|~₹_-+=?><.,'
            Number='123456789'
            Charac=Upper+Lower+Special+Number
            
            new_pass=list(password)
            for i in range(uc):
                x=r.randint(0, len(new_pass))
                new_pass.insert(x, r.choice(Upper))
                
            for i in range(lc):
                x=r.randint(0, len(new_pass))
                new_pass.insert(x, r.choice(Lower))
                
            for i in range(sc):
                x=r.randint(0, len(new_pass))
                new_pass.insert(x, r.choice(Special))
                
            for i in range(nc):
                x=r.randint(0, len(new_pass))
                new_pass.insert(x, r.choice(Number))
                
            lenc=length_req-len(new_pass)
            for i in range(lenc):
                x=r.randint(0, len(new_pass))
                new_pass.insert(x, r.choice(Charac))
                
                
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
        
        
        
else:
    if len(password)<8:
        print('your password is', 8-len(password), 'shorter than required')
    
    u=l=s=n=0
    has_upper=has_lower=has_number=has_special=False
    for i in password:
        if i.isupper():
            has_upper=True
            u=1
        elif i.islower():
            has_lower=True
            l=1
        elif i.isnumeric():
            has_number=True
            n=1
        elif not i.isalnum():
            has_special=True
            s=1
            
            
    if not has_upper:
        print('Your password does not have an uppercase character')
    if not has_lower:
        print('Your password does not have a lowercase character')
    if not has_number:
        print('Your password does not have a numerical character')
    if not has_special:
        print('Your password does not have a special character')
    
    if u==1 and l==1 and s==1 and n==1 and len(password)>=8:
        pass
    else:
        print('Would you like us to internally add the missing conditions?')
        print("\tNote: The added letters, numbers, and/or special characters are randomized and your new password will be displayed at the end")
        pass_change=input('Press Y/N for the above: \n').lower().strip()
        while True:
            if pass_change not in ('y', 'n'): 
                sys.stdout.write('\033[F') 
                sys.stdout.write('\033[K') 
                print('Please enter a valid response: Y/N')
            else:
                break 
            
        
        if pass_change=='y':
            Upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            Lower='abcdefghijklmnopqrstuvwxyz'
            Special='!@#$%^&*()|~₹_-+=?><.,'
            Number='123456789'
            Charac=Upper+Lower+Special+Number
            
            new_pass=list(password)
            if u==0:
                x=r.randint(0, len(new_pass))
                new_pass.insert(x, r.choice(Upper))
                
            if l==0:
                x=r.randint(0, len(new_pass))
                new_pass.insert(x, r.choice(Lower))
                
            if s==0:
                x=r.randint(0, len(new_pass))
                new_pass.insert(x, r.choice(Special))
                
            if n==0:
                x=r.randint(0, len(new_pass))
                new_pass.insert(x, r.choice(Number))
                
            lenc=8-len(new_pass)
            for i in range(lenc):
                x=r.randint(0, len(new_pass))
                new_pass.insert(x, r.choice(Charac))
                
                
            Password_updated=''
            for i in new_pass:
                Password_updated+=i
                
            
            print('Your new password is', Password_updated)
            print('Thank you for visiting us!')
            