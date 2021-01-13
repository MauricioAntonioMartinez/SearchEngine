


class MetadataStractor:
    TOP_NUMBER = 5
    constraints = ['la', 'la', 'los', 'las', 'un', 'uno', 'unos', 'con', 'en', 'como', 'son', 'más', 'a', 'se', 'es', 'su', 'al',
                'una', 'unas', 'yo', 'tu', 'el', 'nosotros', 'vosotros', 'te', 'y', 'o', 'que', 'si', 'luego', 'por', 'donde', 'aunque', 'de', 'del', 'cual', 'sino', 'para', 'ante', 'hasta', 'hacia', 'dónde', 'qué', 'cómo', 'cuándo', 'mediante', 'sobre', 'hasta']
    verb_endings = ['ar', 'er', 'ir', 're', 'oir', 'se']

    def __init__(self,content):
        self.content = content
    def find_metadata(self ):
        words = []
        for line in self.content.split(' '): 
            line = line.strip()
            if line != "":
                words.append(line)
        top_words = []
        words = self.filter_words(words)
        for word in set(words):
            top_words.append({"word": word, "count": words.count(word)})
        top_words.sort(key=lambda x:  x['count'])
        top_words.reverse()
        self.print_tops(top_words)
        return [wr["word"] for wr in  top_words[:5]]

    def filter_words(self,words):
        return [w for w in words if w.isalpha() and w.lower()
                not in self.constraints and all([not w.lower().endswith(end) for end in self.verb_endings])]


    def print_tops(self,words):
        n = self.TOP_NUMBER
        print('-- Metadata --')
        for (index, top) in enumerate(words):
            if n == 0:
                break
            word = top['word']
            count = top['count']
            print(f'{word}: {count}')
            if len(words) != index+1 and words[index+1]['count'] != count:
                n -= 1
