import random as rm
import math

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


## "I beseech you, in the bowels of Christ, think it possible that you may be mistaken."
## -- Oliver Cromwell, namesake of Cromwell's rule
def cromwell(p):
    if p == 100:
        return(99)
    elif p == 0:
        return(1)
    else:
        return(p)

while True:
    ## Pick an intro at random
    i = int(rm.uniform(0,len(sentence_intros)))
    intro = sentence_intros[i]

    raw_input(intro[:-1] + "...")

    ## Randomly choose to give a probability or a range of probabilities
    if rm.random() > 0.33:
        low = 80
        high = 40
        while (low > high) | (low == high):
            ## Generate a pair of probabilities
            low = cromwell(10 * rm.randint(0,10))
            high = cromwell(10 * rm.randint(0,10))

        print(str(low) + "%" + "-" + str(high) + "%" + ".")

    else:
        ## Generate a probability that is in the interval (0,1)
        p = int(10 * rm.randint(0,10))
        p = cromwell(p)

        print(str(p) + "%" + ".")
    raw_input()



## Improvements to be made
# Having granularity down to 5% would feel more natural
# Add flow that allows for sentence endings.
# Go as low as 0.5% or as high as 99.5%?
