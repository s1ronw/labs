class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.directories = {}
        self.files = {}

    def add_directory(self, name):
        if name not in self.directories:
            self.directories[name] = Directory(name, parent=self)

    def add_file(self, name, size):
        self.files[name] = size

    def get_size(self):
        size = sum(self.files.values())
        for dir in self.directories.values():
            size += dir.get_size()
        return size

def parse_input(input_lines):
    root = Directory('/')
    current_dir = root

    for line in input_lines:
        line = line.strip()
        if line.startswith('$ cd'):
            target = line.split(' ')[-1]
            print(f"Changing directory to: {target}")
            if target == '/':
                current_dir = root
            elif target == '..':
                current_dir = current_dir.parent
            else:
                if target not in current_dir.directories:
                    print(f"Directory {target} does not exist, creating it.")
                    current_dir.add_directory(target)
                current_dir = current_dir.directories[target]
        elif line.startswith('$ ls'):
            continue
        elif line.startswith('dir'):
            dirname = line.split(' ')[-1]
            current_dir.add_directory(dirname)
        else:
            size, filename = line.split(' ')
            current_dir.add_file(filename, int(size))

    return root

def find_small_directories(root, max_size=100000):
    small_dirs = []

    def dfs(directory):
        size = directory.get_size()
        if size <= max_size:
            small_dirs.append(size)
        for subdir in directory.directories.values():
            dfs(subdir)

    dfs(root)
    return small_dirs

with open('input_4.txt', 'r') as file:
    lines = file.readlines()

root_directory = parse_input(lines)

small_directories = find_small_directories(root_directory)

result = sum(small_directories)

print("The sum of the total sizes of directories with at most 100000 is:", result)