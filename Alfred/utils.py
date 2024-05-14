def read_key(key_path):
    with open(key_path, "r") as file:
        line = file.readline()
        key = line.strip()
        return key

