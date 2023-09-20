fnm=input("enter firstname:")
lnm=input("enter lastname:")

if fnm.isalpha() and lnm.isalpha():
    email=input("enetr an email address:")
    if email.islower():
        pass
    else:
        print('error!please enter proper email')

    mobile=input('enter your 10 digit mobile number:')

    if len(mobile)==10:
        print("firstname:",fnm)
        print("lastname:",lnm)
        print("email:",email)
        print("mobile:",mobile)
        print("your data has been saved!")

    else:
        print("error!please enter valid mobile number")

else:
    print("enter!something went wrong...try again")

                        