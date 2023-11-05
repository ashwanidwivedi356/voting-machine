n=int(input("number of voter :"))
voters_name=[]
voters_age=[]
for i in range(n):
    voters_name.append(input("Voters Name :"))
    voters_age.append(int(input("Voters Age :")))
voters=dict(zip(voters_age,voters_name))
for i,j in list(voters.items()):
    if i<18:
        voters.pop(i)
candiate_1=input("Candidate First Name :")
candiate_2=input("Candidate Second Name :")
c_1=0
c_2=0
for i,j in voters.items():
    vote=input("Enter The Candiate Name Whom You Wanted To Voted :")
    if vote==candiate_1:
        c_1+=1
    elif vote==candiate_2:
        c_2+=1
    else:
        pass 
if c_1>c_2:
    print(candiate_1,"Win by",(c_1-c_2),"Votes")
elif c_2>c_1:
    print(candiate_2,"is winner",(c_2-c_1),"Votes")
elif c_1==c_2:
    print("Draw")
else:
    print("No Result")
