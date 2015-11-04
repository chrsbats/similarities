
import gzip
import ujson
from string import punctuation, digits
import os

punctuation = set(punctuation) - set("'-") 
max_w = 20.0

directory = os.path.abspath(os.path.join(os.path.dirname(__file__)))
#Counts from proceesing all of wikipedia
name = directory + '/news_idf.jsn.gz'
f = gzip.open(name, 'rb')
idf = ujson.loads(f.read())
f.close()

def valid_word(w):
    #two letter words are not generally helpful
    if len(w) < 3:
        return False
    #First 76 words are stop words. Word 80 is "U.S."
    if w in idf:
        if idf[w][0] < 80:
            return False
    return True


def ngrams(text,size=2):
    ngrams = []
    for i in range(len(text)-(size-1)):
        ngrams.append(' '.join(text[i:i+size]))
    return ngrams

def count(some_dict,some_list):
    for x in some_list:
        count = some_dict.get(x,0)
        some_dict[x] = count + 1

def count_ngrams(text):
    #Differs to the one in docfreq because we need to count them.
    #text = text.lower()
    for p in punctuation:
        text = text.replace(p,' ')
    one_gram = [t for t in text.split()]
    text = {}
    count(text,one_gram)
    for n in range(2,4):
        count(text,ngrams(one_gram,n))
    return text

def tfidf(text):
    words = count_ngrams(text)

    result = {}
    keywords = {}
    for w in words.keys():
        if valid_word(w):
            if w in idf:
                result[w] = words[w] * idf[w][1]
            else:
                #For unique phrases, don't match large ngrams for sake of speed. 
                if len(w.split()) == 1:
                    w_lowered = w.lower()
                    if w_lowered not in stop_words:
                        if w_lowered in result:
                            result[w_lowered] = result[w_lowered] + words[w] * max_w
                        else:
                            result[w_lowered] = words[w] * max_w
    return result


stop_words = set([
 'a',
 'about',
 'above',
 'after',
 'again',
 'against',
 'all',
 'am',
 'an',
 'and',
 'any',
 'are',
 'as',
 'at',
 'be',
 'because',
 'been',
 'before',
 'being',
 'below',
 'between',
 'both',
 'but',
 'by',
 'can',
 'did',
 'do',
 'does',
 'doing',
 'don',
 'down',
 'during',
 'each',
 'few',
 'for',
 'from',
 'further',
 'had',
 'has',
 'have',
 'having',
 'he',
 'her',
 'here',
 'hers',
 'herself',
 'him',
 'himself',
 'his',
 'how',
 'i',
 'if',
 'in',
 'into',
 'is',
 'it',
 'its',
 'itself',
 'just',
 'me',
 'more',
 'most',
 'my',
 'myself',
 'no',
 'nor',
 'not',
 'now',
 'of',
 'off',
 'on',
 'once',
 'only',
 'or',
 'other',
 'our',
 'ours',
 'ourselves',
 'out',
 'over',
 'own',
 's',
 'same',
 'she',
 'should',
 'so',
 'some',
 'such',
 't',
 'than',
 'that',
 'the',
 'their',
 'theirs',
 'them',
 'themselves',
 'then',
 'there',
 'these',
 'they',
 'this',
 'those',
 'through',
 'to',
 'too',
 'under',
 'until',
 'up',
 'very',
 'was',
 'we',
 'were',
 'what',
 'when',
 'where',
 'which',
 'while',
 'who',
 'whom',
 'why',
 'will',
 'with',
 'you',
 'your',
 'yours',
 'yourself',
 'yourselves'])

