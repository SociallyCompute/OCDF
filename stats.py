import json
import re
import operator

# 'Electronics.json'
# 'Toys_and_Games.json'

def counts():

    product_counts = {}

    for line in open('Toys_and_Games.json'):
        d = json.loads( line )

        id = d['product/productId']

        if id not in product_counts:
            product_counts[ id ] = 0

        product_counts[ id ] += 1

    for p in product_counts:
        print p, ',', product_counts[p]

def questionmarks():

    for line in open('Toys_and_Games.json'):

        d = json.loads( line )

        t = ''

        if 'review/summary' in d:
            t = d['review/summary']

        t += d['review/text']

        m = re.search('\?\?+', t)

        if m:
            print len( m.group(0) )
        else:
            print 0



def users():

    counts = {}

    for line in open('Toys_and_Games.json'):
        d = json.loads( line )

        id = d['review/userId']

        if id not in counts:
            counts[ id ] = 0

        counts[ id ] += 1

    for line in open('Electronics.json'):
        d = json.loads( line )

        id = d['review/userId']

        if id not in counts:
            counts[ id ] = 0

        counts[ id ] += 1

    print sorted( counts.items(), key=operator.itemgetter(1) )

if __name__ == '__main__':
    users()
