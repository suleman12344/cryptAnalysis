import enchant


chipherText = 'OLSSV'
plaintext_list=[]

alphabet = []
for i in range(26):
  alphabet.append(chr(65 + i))


def findIndex(value):
  index = 0
  for i in range(len(alphabet)):
    if alphabet[i] == value:
      index =  i
  return index
    
#decryption of chiphertext to find the real plaintext or hidden message
def decrypy(chipherText,plaintext_list):
  plaintext = ''
  for j in range (25):
    for i in range(len(chipherText)):
      if chipherText[i] == ' ':
        plaintext += ' '
      else:
        index=findIndex(chipherText[i])
        index = (index - j) % 26
        plaintext += alphabet[index]
    plaintext_list.append(plaintext)
    print(plaintext)
    plaintext = ''
    
def check_plainText(plaintext_list):
    dictionary = enchant.Dict("en_US")
    for sentence in plaintext_list:
        sentence_split = sentence.split()
        if all(dictionary.check(word) for word in sentence_split):
            return True, sentence
    return False, None
  


decrypy(chipherText,plaintext_list)
is_valid, valid_sentence = check_plainText(plaintext_list)

if is_valid:
    print("Valid sentence found:", valid_sentence)
else:
    print("No valid English sentence found.")


#Encryption of valid sentence and all the chipertext will be valid

chipherText_list=[]
def encryption(valid_sentence,chipherText_list):
  print("ChiperTexts for",valid_sentence)
  cipherText = ''
  for j in range (25):
    for i in range(len(valid_sentence)):
      if valid_sentence[i] == ' ':
        cipherText += ' '
      else:
        index=findIndex(chipherText[i])
        index = (index + j) % 26
        cipherText += alphabet[index]
    chipherText_list.append(cipherText)
    print(cipherText)
    cipherText = ''

encryption(valid_sentence,chipherText_list)



