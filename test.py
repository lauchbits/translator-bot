import googletrans

for attr in googletrans.LANGUAGES:
       print(attr, googletrans.LANGUAGES[attr])

print(len(googletrans.LANGUAGES))