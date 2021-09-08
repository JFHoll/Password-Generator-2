import random

adjectives_file = open("english-adjectives.txt", "r")
adjectives = adjectives_file.readlines()


nouns_file = open("english-nouns.txt", "r")
nouns = nouns_file.readlines()

pass_adj = random.choice(adjectives).strip('\n')
pass_noun = random.choice(nouns).strip('\n')
pass_number = str(random.randrange(100, 999))

password = (pass_adj + pass_noun + pass_number)
print(password)

