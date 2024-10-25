class WordsFinder:
    def __init__(self, *file_names: str) -> None:
        self.file_names = file_names

    def get_all_words(self) -> dict:
        all_words = {}

        for file_name in self.file_names:
            with open(file_name, "r", encoding="utf-8") as file:
                line = file.read().lower()

                for punctuation in [",", ".", "=", "!", "?", ";", ":", " - "]:
                    line = line.replace(punctuation, "")

                words = line.split()
                all_words[file_name] = words

        return all_words

    def find(self, word: str) -> dict:
        search_result = {}
        word = word.lower()

        for file_name, words in self.get_all_words().items():
            if word in words:
                search_result[file_name] = words.index(word) + 1

        return search_result

    def count(self, word: str) -> dict:
        word_count = {}

        for file_name, words in self.get_all_words().items():
            word_count[file_name] = words.count(word.lower())

        return word_count


finder2 = WordsFinder("test_file.txt")
print(finder2.get_all_words())  # Все слова
print(finder2.find("TEXT"))  # 3 слово по счёту
print(finder2.count("teXT"))  # 4 слова teXT в тексте всего
