#
# Write a script that counts repetitions of words in a input string
#
# example input="lorem LOREM LoREM,. ipsum.. IPSUM, ipsum dolorem dolorem, fre fr er er erer jujuju JUJUJU juju"
#
# expected output=7
#

input = "lorem LOREM LoREM,. ipsum.. IPSUM, ipsum dolorem dolorem, fre fr er er erer jujuju JUJUJU juju"

import re

splitted = [word.lower() for word in filter(None, re.split(" |,|\\.", input))]

repetitions = {}
for word_index in range(0, len(splitted)-1):
  word = splitted[word_index]
  if word not in repetitions:
    repetitions[word] = 0
    for search_index in range(word_index+1, len(splitted)-1):
      if splitted[search_index] == word:
        repetitions[word] += 1

output = 0
for word in repetitions:
  output += repetitions[word]

print(output)
