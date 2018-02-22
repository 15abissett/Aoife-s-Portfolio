def hello(): #this prforms a person saying hello
greetings=['hello', 'leave me alone', 'good morning'] #this lists out possible greetings
if choice=="hello":
  print("well hello to you too!")
  
elif choice=="leave me alone":
  print("fine be like that then!")
  
else:
  print("ermmm okkk")
  
from time import sleep #this imports sound
print("welcome to the Bissett music factory!!!")
sleep(2)
answer=input("what mood are you in???") #gives you a choice to see what mood you are in
while True:
  print("what is your mood")
  moods=['happy','sad','positive']#lists out moods
 if choice=="happy":
    print("how about bohemian rhapsody!!!!")
    
 elif choice=="sad":
  print("awhh how about your song by elton john")
  
else:
print("i think thriller would go down well")


def function(file):
    with open('file.txt', 'r') as f:
        contents = f.readlines()
    lines = []
    for line in f:
        lines.append(line)
    print(contents)  #this is from stack overfow it shows you how to open a file
