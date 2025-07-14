class HashMap:

    def __init__(self):
        self.size = 100
        self.array = [None for i in range(self.size)]

    def get_index(self, key):
        if not isinstance(key, str):
            raise KeyError("Key must be string")
        return hash(key) % self.size

    def set_value(self, key, value):
        index = self.get_index(key=key)

        data = self.array[index]

        if data is None:
            self.array[index] = [(key, value)]
            return True

        if isinstance(data, list):

            for i, (i_key, _value) in enumerate(data):
                if i_key == key:
                    data[i] = (key, value)
                    return True

            data.append((key, value))

        return True

    def get_value(self, key):
        index = self.get_index(key)

        data = self.array[index]

        if data is None:
            raise KeyError(f"{key} Not found")

        for _key, _value in data:
            if _key == key:
                return _value

        raise KeyError(f"{key} Not found")

    def delete(self, key):
        index = self.get_index(key)
        data: list = self.array[index]

        if data is None:
            raise KeyError(f"{key} not found")

        found = False
        for i, (_key, value) in enumerate(data):
            if _key == key:
                data.pop(i)
                found = True
                break

        if not found:
            raise KeyError(f"{key} not found")

        if not data:
            self.array[index] = None

        return True

    def get_keys(self):
        keys = []

        for data in self.array:
            if data is None:
                continue

            for key, _ in data:
                keys.append(key)

        return keys

    def has_key(self, key):

        index = self.get_index(key)
        data = self.array[index]

        if data is None:
            return False

        for _key, _ in data:
            if _key == key:
                return True

        return False


if __name__ == "__main__":

    hash_map = HashMap()

    hash_map.set_value("name", "bhushan")
    hash_map.set_value("age", 27)
    hash_map.get_value("name")
    print(hash_map.get_value("name"))
    print(hash_map.get_value("age"))
    print(hash_map.get_keys())
