import urllib.request
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from bs4 import BeautifulSoup

response = urllib.request.urlopen('https://en.wikipedia.org/wiki/SpaceX')# Looks at the wiki page
html = response.read()
soup = BeautifulSoup(html, "html5lib")
text = soup.get_text(strip=True)

tokens = [t for t in text.split()]
clean_tokens = tokens[:]
sr = stopwords.words('english')

for token in tokens:
    if token in stopwords.words('english'):
        clean_tokens.remove(token)

freq = nltk.FreqDist(clean_tokens)

for key, val in freq.items():
    if val > 5:
        print(str(key) + ':' + str(val))

freq.plot(10,cumulative =False)
#freq.tabulate(10) used to get the new visual representation 
