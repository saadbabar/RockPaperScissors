
import random
def main():
  p=1
  while p ==1:
    print("Rock, Paper, Scissors")

    x=input("(rock), (paper) or (scissors): ")

  

    cpu= random.randint(1,3)
    Rock= 1
    Paper=2
    Scissors=3

    if x == "rock" and cpu == Rock:
      print("cpu displays rock")
      print("tie")

    elif x== "rock" and cpu == Paper:
      print("cpu displays paper")
      print("cpu wins")

    elif x== "rock" and cpu == Scissors:
      print("Cpu displays scissors")
      print("you win")

    elif x=="paper" and cpu == Rock:
      print("cpu displays rock")
      print("you win")

    elif x=="paper" and cpu== Paper:
      print("cpu displays rock")
      print("tie")

    elif x=="paper" and  cpu== Scissors:
      print("cpu displays scissors")
      print("cpu wins")

    elif x=="scissors" and cpu == Rock:
      print("cpu displays rock")
      print("cpu wins")

    elif x=="scissors" and cpu==Paper:
      print("cpu displays paper")
      print("you win")

    elif x=="scissors" and cpu==Scissors:
      print("cpu displays scissors")
      print("tie")

    elif x=="quit":
      print("game over")
    

    else:
      print("error")

    playagain=input("playagain(y/n)")

    if playagain=="y":
      p=1
    else:
      p=0


  
  
main()
