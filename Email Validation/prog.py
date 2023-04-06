email = input("Enter your email: ")  #ga@.in
if len(email)>=6:
    if email[0].isalpha():
        if ('@' in email) and (email.count("@")==1):
            if (email[-4]==".") or (email[-3]=="."):
                pass
            else:
                print("Wrong email 4")
        else:
            print("Wrong email 3")  
    else:
        print("Wrong email 2")
else:
    print("Wrong email 1")



