class Lexicon(object):
    def __init__(self):
        self.pairs = {}
        directions = ['north', 'south', 'east', 'west',
                      'down', 'up', 'left', 'right', 'back']
        verbs = ['go', 'stop', 'kill', 'eat']
        stops = ['the', 'in', 'of', 'from', 'at', 'it']
        nouns = ['door', 'bear', 'princess', 'cabinet']
        groups = {'direction': directions, 'verb': verbs,
                  'stop': stops, 'noun': nouns}
        for group_name, group_list in groups.items():
            for list_element in group_list:
                self.pairs.update({list_element: group_name})

    def scan(self, sentence):
        scan_list = []
        for word in sentence.split():
            if word.lower() in self.pairs.keys():
                scan_list.append((self.pairs[word.lower()], word))
            else:
                try:
                    scan_list.append(('number', int(word)))
                except ValueError:
                    scan_list.append(('error', word))
        return scan_list


lexicon = Lexicon()
