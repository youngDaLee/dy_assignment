import sys


class Transformer(object):
    """Convert numbers from base 10 integers to base N strings and back again.
    Sample usage:
    >>> base20 = Transformer('0123456789abcdefghij')
    >>> base20.from_decimal(1234)
    '31e'
    >>> base20.to_decimal('31e')
    1234
    """
    decimal_digits = '0123456789'

    def __init__(self, digits):
        self.digits = digits

    def from_decimal(self, i):
        return self._convert(i, self.decimal_digits, self.digits)

    def to_decimal(self, s):
        return int(self._convert(s, self.digits, self.decimal_digits))

    def _convert(self, number, fromdigits, todigits):
        if fromdigits == self.decimal_digits:
            # (from_decimal) convert decimal to n_digits
            n = len(todigits)
            res = ''
            while number >= n:
                rmd = number % n
                number = number//n
                res = self.digits[rmd] + res
            res = self.digits[number] + res

        else:
            # (to_decimal) convert n_digits to decimal
            n = len(fromdigits)
            res = 0
            num_len = len(number)
            for i in range(num_len):
                res += self.digits.index(number[i]) * (n ** (num_len-i-1))

        return res


if __name__ == '__main__':
    binary_transformer = Transformer('01')
    hex_transformer = Transformer('0123456789ABCDEF')
    base62_transformer = Transformer('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz')
