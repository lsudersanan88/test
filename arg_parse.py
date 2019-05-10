
import sys
import argparse


parser = argparse.ArgumentParser(description='')
parser.add_argument('input', action="store")
parser.add_argument('doc', nargs='?', default=None)
parser.add_argument('comp', nargs='?', default=None)
try:
    args = parser.parse_args()
except:
    parser.print_help()
    sys.exit(1)
print('1st argument :: {}'.format(args.input));
print('2nd argument :: {}'.format(args.doc));
print('3rd argument :: {}'.format(args.comp));

"""
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('input', action="store")
    parser.add_argument('doc', nargs='?', default=None)
    parser.add_argument('comp', nargs='?', default=None)
    try:
        args = parser.parse_args()
    except:
        parser.print_help()
        sys.exit(1)
    print('1st argument :: {}'.format(args.input));
    print('2nd argument :: {}'.format(args.doc));
    print('3rd argument :: {}'.format(args.comp));
    
"""
