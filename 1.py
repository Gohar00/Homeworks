from abc import ABC, abstractmethod

class DataStorageSystem(ABC):
    @abstractmethod
    def save(self, key, data):
        pass

    @abstractmethod
    def load(self, key):
        pass

    @abstractmethod
    def delete(self, key):
        pass

class FileStorage(DataStorageSystem):
    def __init__(self, file_path):
        self.file_path = file_path

    def save(self, key, data):
        with open(self.file_path, 'a') as file:
            file.write(f"{key}:{data}\n")

    def load(self, key):
        with open(self.file_path, 'r') as file:
            for line in file:
                line_key, line_data = line.strip().split(':')
                if line_key == key:
                    return line_data
        return None

    def delete(self, key):
        lines = []
        with open(self.file_path, 'r') as file:
            for line in file:
                line_key, _ = line.strip().split(':')
                if line_key != key:
                    lines.append(line)

        with open(self.file_path, 'w') as file:
            file.writelines(lines)

class DatabaseStorage(DataStorageSystem):
    def __init__(self):
        self.data = {}

    def save(self, key, data):
        self.data[key] = data

    def load(self, key):
        return self.data.get(key, None)

    def delete(self, key):
        if key in self.data:
            del self.data[key]


if __name__ == "__main__":
  
    file_storage = FileStorage("data.txt")
    file_storage.save("name", "Alice")
    print(file_storage.load("name"))  
    file_storage.delete("name")

  
    db_storage = DatabaseStorage()
    db_storage.save("name", "Bob")
    print(db_storage.load("name"))  
    db_storage.delete("name")
