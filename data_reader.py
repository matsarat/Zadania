class DataReader(object):
    def __init__(self, path_to_file):
        file = open(path_to_file)
        self.lines = [line.strip() for line in file.readlines()]
        file.close()


    def get_table(self, separator):
        table = []
        for index in range(1, len(self.lines)):
            line = self.lines[index]
            columns = line.split(separator)
            table.append(columns)
        return table

