email = input("Enter your email address: ")
k,j,d = 0,0,0

# rule 1
if len(email)>=6:
    # rule 2
    if email[0].isalpha() :
        # rule 3
        if ('@' in email) and (email.count('@')==1):
            # rule 4
            if (email[-4]=='.') ^ (email[-3]=='.'):

                # iterate rule 5 and 6 
                for i in email:
                    if i.isspace():
                        k=1
                    elif i.isalpha():
                        if i.isupper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=='_' or i=='.' or i=='@':
                        continue
                    else:
                        d=1

                if k==1 or j==1 or d==1:
                    print("Invalid email: Email should not contain spaces, uppercase letters, or special characters other than '_', '.', and '@'.")
                else:
                    print("Valid email address.email validated successfully.")

            else:
                print('. is not in the correct position. It should be either 3rd or 4th from the end.')
        else:
            print("Invalid email: Email should contain exactly one '@' symbol.")
    else:
        print("Invalid email: Email should start with an alphabet.")
else:
    print("Invalid email: Email should be at least 6 characters long.your email is short ...")
