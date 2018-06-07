morse = {
   'a': "..",
   'b': '.-',
   'c': '--',
   ' ': ' '
}

message = "a ab abc aa bb cc"

morse_message = ""
for word in message:
   for c in word:
       morse_message += morse[c]

print(morse_message)