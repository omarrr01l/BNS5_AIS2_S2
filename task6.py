def read_txt_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return None

class UserExtractor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.usernames = {}

    def extract_usernames(self):
        content = read_txt_file(self.file_path)
        if content is None:
            return {}
        
        lines = content.strip().split('\n')
        for line in lines:
            if ':' in line:
                username, password = line.strip().split(':', 1)
                self.usernames[username] = password
        return self.usernames