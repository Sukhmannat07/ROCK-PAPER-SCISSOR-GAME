'''1 for rock
-1 for scissor 
0 for paper '''
computer = 0 
you=input("enter your choice :")
youdict={"r":1,"s":-1,"p":0}
younum=youdict[you]
if (computer==younum):
    print ("its a draw")
else:
    if(computer==1 and younum==-1):
        print ("you loose")
    elif(computer==1 and younum==0):
        print ("you win")
    elif(computer==0 and younum==1):
        print ("you loose")
    elif(computer==-1 and younum==1):
        print ("you win")
    elif(computer==0 and younum==-1):
        print ("you win ")
    elif(computer==1 and younum==-1):
        print ("you loose")
    else:
        print("something went wrong")
        
