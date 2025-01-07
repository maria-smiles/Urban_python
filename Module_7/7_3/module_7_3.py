# Задача "Найдёт везде":


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def  get_all_words(self):

        import re
        all_words = {}
        for name in self.file_names:
            with open(name, encoding='utf-8') as file:
                word_list = []
                for line in file:
                    line = line.lower()

                    line = re.sub(r'[!\"#$%&()*+,-./:;<=>?@\[\\\]^_`{|}~]', '', line)
                    line = line.split()
                    for word in line:
                        word_list.append(word)
                all_words[name] = word_list
        return all_words

#
#
    def find(self, word):
        pos = {}
        word_ = word.lower()
        all_words = self.get_all_words()
        for key, words in all_words.items():
            if word_ in words:
                pos[key] = words.index(word_)+1
        #- метод, где word - искомое слово.
        # Возвращает словарь, где ключ - название файла,
        # значение - позиция первого такого слова в списке слов этого файла.
        return pos

    def count(self, word):
        count = {}
        word_ = word.lower()
        all_words = self.get_all_words()
        for key, words in all_words.items():
            if word_ in words:
                count[key] = words.count(word_)
        # count(self, word) - метод, где word - искомое слово.
        # Возвращает словарь, где ключ - название файла,
        # значение - количество слова word в списке слов этого файла.
        return count



# Пример выполнения программы:
#
finder2 = WordsFinder('test_file.txt')
#
print(finder2.get_all_words()) # Все слова
#
print(finder2.find('TEXT')) # 3 слово по счёту
#
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
#
finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
#
# Вывод на консоль:
#
# {'test_file.txt': ["it's", 'a', 'text', 'for', 'task', 'найти', 'везде', 'используйте', 'его', 'для', 'самопроверки', 'успехов', 'в', 'решении', 'задачи', 'text', 'text', 'text']}
#
# {'test_file.txt': 3}
#
# {'test_file.txt': 4}

