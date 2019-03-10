#!/usr/bin/env python3
import random
import argparse

def stats(output):
    import statistics
    print('Mean: '+str(statistics.mean(output)))
    print('P. Standard Deviation: '+str(statistics.pstdev(output)))
    print('Median: '+str(statistics.median(output)))
    try:
        print('Mode: '+str(statistics.mode(output)))
    except:
        pass
    print('Sum: '+str(sum(output)))

parser=argparse.ArgumentParser()
parser.add_argument('-a', help='Sets lower limit, default 1 or 0 when not specified', type=int, nargs='?', default=1, const=0)
parser.add_argument('numDigits', help='Number of random values to get', type=int, nargs='?', default=1)
parser.add_argument('-b', help='The upper limit for the randomizer. Default 6',type=int, default=6)
parser.add_argument('-z', help='Sets to a 0-9 spread rather than default 1-6. overrides -a,-b', action='store_true')
parser.add_argument('-s', '--stats', help='Prints sum of random numbers', action='store_true')
parser.add_argument('--sort', help='Sorts values lowest to highest', action='store_true')
parser.add_argument('--rsort', help='Sorts values highest to lowest', action='store_true')
args=parser.parse_args()
if args.z:
    args.a, args.b = 0, 9
random.seed()
output=[]
for i in range(0, int(args.numDigits)):
    output.append(random.randint(args.a, args.b))
if args.sort:
    output=sorted(output)
elif args.rsort:
    output=sorted(output, reverse=True)
print(output)
if args.stats:
    stats(output)
