"""Test task for the position of Python Intern"""


class NumberFormatter:
    """Required class "NumberFormatter"""

    def parse_int(self, string):
        """Takes string. Returns integer"""
        if len(string) > 0:
            if string[0] != '-' and string[0] != '+':
                string = '+' + string
            if 2 <= len(string) <= 2 ** 32 - 1:
                symbols = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
                for i in string[1:-1]:
                    if i not in symbols:
                        return 'Invalid data'
                return int(string)
        return 'Invalid data'


if __name__ == '__main__':
    str_value = NumberFormatter()
    test_cases = ['02', '-02', '+889', '1', '+05']
    COUNT = 0
    while COUNT < len(test_cases):
        int_value = str_value.parse_int(test_cases[COUNT])
        print(int_value)
        COUNT += 1
