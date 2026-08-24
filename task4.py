class TextFileReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_content(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return file.read()

    def count_lines(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return len(file.readlines())

    def count_words(self):
        content = self.read_content()
        return len(content.split())

    def count_characters(self):
        content = self.read_content()
        return len(content)