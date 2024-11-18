class WordsFinder:

    def __init__(self, *files_name):
        self.files_name = files_name

    def get_all_words(self):
        all_words_dict = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']

        for file_name in self.files_name:
            words = []
            with open(self.files_name, encoding = 'utf-8') as file:
                for lines in file:
                    lines = lines.lower()
                    for symbol in punctuation:
                        line = line.replace(symbol, ' ')
                    split_words = lines.split(sep = ' ')
                    words.extend(split_words)
                all_words_dict[file_name] = words

            return all_words_dict

    def find(self, word):

        words_search = self.get_all_words()
        found_words = {}

        for searched_word in words_search.items():
            with open(self.files_name, encoding = 'utf-8') as file:
                word_byte = file.tell()
                if searched_word == word:
                    found_words[self.files_name] = word_byte
                    found_words.update({self.files_name: word_byte})

        return found_words

finder2 = WordsFinder(['test_1', 'test_2'])
print(finder2.find('woe'))










