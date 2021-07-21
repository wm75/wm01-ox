import random
import sys


def random_seq(length):
    return ''.join(random.choices('AGCT', k=length))


if len(sys.argv) < 2:
    print('Need to know the length of the sequence to generate')
else:
    print(random_seq(int(sys.argv[1])))
