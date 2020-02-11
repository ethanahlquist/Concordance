from hash_quad import *
import string

class Concordance:

    def __init__(self):
        self.stop_table = None          # hash table for stop words
        self.concordance_table = None   # hash table for concordance

    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        try:
            f = open(filename)
            f.close()
        except FileNotFoundError:
            raise FileNotFoundError

        self.stop_table = HashTable(191)
        String = ""

        with open(filename, "r") as ins:
            for line in ins:
                for ch in line:
                    String += ch

                String = String.strip("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789  \t\n\r\v\f'""")
                #String = String.strip(' \t\n\r\v\f')
                String = String.lower()

                self.stop_table.insert(String, 0)
                String = ""


    def load_concordance_table(self, filename):
        """ Read words from input text file (filename) and insert them into the concordance hash table, 
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
        Starting size of hash table should be 191: self.concordance_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        try:
            f = open(filename)
            f.close()
        except FileNotFoundError:
            raise FileNotFoundError

        self.concordance_table = HashTable(191)
        String = ""
        line_num = 0

        with open(filename, "r") as ins:
            for line in ins:
                line_num += 1
                for ch in line:
                    if ch in """!"#$%&()*+,-./:;<=>?@[\]^_{|}~0123456789  \t\n\r\v\f""":
                        String += " "
                    elif ch in """ '` """:
                        pass
                    else:
                        String += ch

                String = String.lower()
                line_list = String.split()
                line_list.sort()

                for i in range(len(line_list)):
                    if self.stop_table.in_table(line_list[i]):
                        pass
                    elif i != len(line_list)-1:
                        if line_list[i] != line_list[i+1]:
                            self.concordance_table.insert(line_list[i], line_num)
                    else:
                        self.concordance_table.insert(line_list[i], line_num)
                String = ""


    def write_concordance(self, filename):
        """ Write the concordance entries to the output file(filename)
        See sample output files for format."""
        out_string = ""
        return_table = list(filter(None, self.concordance_table.hash_table))
        return_table.sort()

        for i in range(len(return_table)):
            out_string += return_table[i][0] + ": "
            for j in range(len(return_table[i][1])):
                out_string += (str(return_table[i][1][j]) + " ")
            out_string = out_string[:len(out_string)-1]
            out_string += "\n"
        out_string = out_string[:len(out_string) - 1]

        with open(filename, 'w') as f:
            f.write(out_string)
            f.close()
