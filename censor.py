def censor(text,word):
  if word in text:
  	text = text.replace(word,"*" * len(word))
  return text

print (censor("I love him so much love him SO much", "love"))
