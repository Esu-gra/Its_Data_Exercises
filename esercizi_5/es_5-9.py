#esercizio 5-9

users=[]
len=len(users)
for i in users:
    if i =="admin":
        print("Hello admin , would you like to see a status report?")
    else:
        print(f"Hello {i}, thank you for logging in again")
 

if  len==0:
    print("non abbiamo utenti ")
 