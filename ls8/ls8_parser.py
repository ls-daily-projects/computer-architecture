class LS8Parser():
    lines_of_code = []

    def load_loc_from_file(self, filename, line_parser):
        with open(filename, "r") as file:
            for line in file:
                parsed_line = line_parser(line)

                if not parsed_line:
                    continue

                self.lines_of_code.append(parsed_line)

        return self

    def parse_line(self, line):
        line = line.strip()

        if not line:
            return None

        if line.startswith("#"):
            return None

        if "#" in line:
            line = line.split("#")[0]

        return line

    def parse(self, filename):
        if not filename:
            raise TypeError("'filename' is a required argument")

        self.load_loc_from_file(filename, self.parse_line)

        return self
