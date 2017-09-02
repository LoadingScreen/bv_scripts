import random

## A script with the purpose of countering
## anchoring effects when assigning probabilities

## randomly generate probabilities that are output to
## the console as verbal statements


## Make a set of sentence fragments
sentence_intros = ["Feels like ",
"I think it's something like ",
"Definitely more than ",
"Probably not below ",
"I would be surprised if it was higher than ",
"Somewhere in the neighborhood of ",
"Somewhere in the range of ",
"Oh, I dunno; maybe like ",
"Well, just think about it--it has to be something like ",
"I might update if I thought about it more, but maybe ",
"On baserates, I would guess...",
"I'd bet at "]

## Pick an intro at random
i = int(random.uniform(0,len(sentence_intros)))
intro = sentence_intros[i]

## Generate a probability that is in the interval (0,1)
prob = int(10 * round(random.randint(0,10)))
if prob == 100:
    prob = 99
elif prob == 0:
    prob == 1

print(intro + str(prob) + "%" + ".")
