text=input('enter your main text :')
separate=input('enter  text seprator :')
joine=input('enter text splicer :')
print(text)
seperate_text=text.split(separate)
joine_text=joine.join(seperate_text)
print(joine_text)