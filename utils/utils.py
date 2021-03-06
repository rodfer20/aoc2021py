from os import mkdir
from os.path import exists
from sys import stderr, exit

class Utils:
    def __init__(self):
        self.input_dir = "inputs"
        self.output_dir = "outputs"
        self.input_format = "day@-input.txt".split("@")
        self.output_format = "day@-output.txt".split("@")


    def select_day(self, day):
        self.day = day

    
    def get_day(self) -> int:
        return self.day


    def format_path(self, fd) -> str:
        if fd == 1:
            formatted_txt = f"{self.output_dir}/{self.output_format[0]}{self.day}{self.output_format[1]}"
        elif fd == 0:
            formatted_txt = f"{self.input_dir}/{self.input_format[0]}{self.day}{self.input_format[1]}"
        else:
            stderr.write("[!] Error formatting text, incorrect fd given")
            formatted_txt = str(self.day)
        return formatted_txt


    def read_file(self, file, fmt) -> list:
        if fmt == "csv/int":
            with open(file) as fp:
                data = fp.read()
            return list(map(int, data[0].split(',')))
        if fmt == "int":
            with open(file) as fp:
                return list(int(line) for line in fp)
        if fmt == "str":
            with open(file) as fp:
                return list(str(line).split("\n")[0] for line in fp)

    def read_input(self, fmt):
        file = self.format_path(0)
        if not exists(self.input_dir):
            mkdir(self.input_dir)
        if not exists(file):
            stderr.write(f"[!] Error finding input file {file}\n")
            exit(0)
        self.input_ls = self.read_file(file, fmt)


    def write_output(self, output):
        self.output = output
        file = self.format_path(1)
        if not exists(self.output_dir):
            mkdir(self.output_dir)
        with open(file, 'w') as fp:
            fp.write(f"part1: {self.output[0]}\npart2: {self.output[1]}")
        print(f"part1: {self.output[0]}\npart2: {self.output[1]}")

