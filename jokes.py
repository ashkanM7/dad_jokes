import requests
from random import choice
import pyfiglet 
from colorama import init
from termcolor import colored
init()

header = pyfiglet.figlet_format("DAD JOKE 3000!")
c_header = colored(header, color="green")
print(c_header)

user_input = input("What would you like to search for?")
url = "https://icanhazdadjoke.com/search"
res = requests.get(
  url, 
  headers={"Accept":"application/json"},
  params={"term": user_input}
  ).json()
  
num_jokes = res['total_jokes']
results = res['results']

if num_jokes > 1:
  print(f"I found {num_jokes} jokes about {user_input}. Here's one:")
  print(choice(results)['joke'])
elif num_jokes == 1:
  print(f"I found one joke about {user_input}")
  print(results[0]['joke'])
else:
  print(F"Sorry, I couldn't find a joke with your term {user_input}")