

class Scanner(object):
    def __init__(self, regex, code):
        self.regex_list  = regex
        self.code = code
        self.tokens = scan(code)


    def match(i, line):
        start = line[i:]
        for regex, token in reges_list:
            match = regex.match(start)
            if match:
                begin, end = match.span()
                return token , start[:end], end
            return None , start, None

    def  scan(self, code):
        script = []

        for line in code:
            i = 0
            while i < len(line):
                token, string, end = match(i, line)
                assert token, "Failed to match line %s" % string
                if token:
                   i += end
                   script.append((token, string, i, end)) 

        return script
