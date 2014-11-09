import json
import sys

def scores( f ):

    for line in open(f):
        data = json.loads( line )

        print data['review/score']

if __name__ == '__main__':

    scores( sys.argv[1] )
