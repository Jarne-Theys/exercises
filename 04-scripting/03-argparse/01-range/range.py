import argparse
parser = argparse.ArgumentParser(prog='ranger')
parser.add_argument('start')
parser.add_argument('end')
parser.add_argument('-x', '--exclusive', action='store_true')
parser.add_argument('--step', default=1)

args = parser.parse_args()

start = int(args.start)
end = int(args.end)
exclusive = args.exclusive
step = int(args.step)

if exclusive == True:
    for x in range(start, end, step):
        print(x)
else:
    for x in range(start, end + 1, step):
        print(x)
