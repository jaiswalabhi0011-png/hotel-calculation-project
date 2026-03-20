# 1 import the random module
import random

#2 crate subject
subject = [
    "Shahrukh khan",
    "Virat kohli",
    "NIrmala sitaraman",
    "A Mumbai cat",
    "Prime minister modi ji",
    "Auto rickshaw Driver from delhi",
    
]

actions = [
   "launches",
   "cancels",
   "dances with",
   "eats",
   "declares war on",
   "orders",
   "celebrates",

]

places_or_things = [
    "at red fort",
    "in mumbai local train",
    "a plate of samosa",
    "a ganga ghat",
    "during ipl match",
    "at india gate",
]

#3 start the headline generation loop
while True:
    subject = random.choice(subject)
    action = random.choice(actions)
    places_or_things = random.choice(places_or_things)
    
    headline = f"BREAKING NEWS: {subject} {action} {places_or_things}   "
    print("\n" + headline)
    
    user_input = input("\n Do you want another headline? (yes/no)").strip()
    if user_input == "no":
        break
    #print goodbye message
    print("\nThanks for using the fake news Headline Generator.Have a fun day")
        