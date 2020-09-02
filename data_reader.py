class DataReader(object):
    def __init__(self, path_to_file):
        file = open(path_to_file)
        lines = file.readlines()
        file.close()
        self.lines = []
        for line in lines:
            self.lines.append(line.strip())


    def get_table(self, separator):
        table = []
        for index in range(1, len(self.lines)):
            line = self.lines[index]
            columns = line.split(separator)
            table.append(columns)
        return table

    def get_table_int(self, separator):
        table = []
        for index in range(1, len(self.lines)):
            line = self.lines[index]
            columns = line.split(separator)
            table.append(list(map(int, columns)))
        return table
