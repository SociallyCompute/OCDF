import gzip
import json
import operator

def parse(filename):
  f = gzip.open(filename, 'r')
  entry = {}
  for l in f:
    l = l.strip()
    colonPos = l.find(':')
    if colonPos == -1:
      yield entry
      entry = {}
      continue
    eName = l[:colonPos]
    rest = l[colonPos+2:]
    entry[eName] = rest
  yield entry


datas = {}

for e in parse("Arts.txt.gz"):
    id = '-1'

    if 'product/productId' in e:
        id = e['product/productId']

    if id not in datas:
        datas[ id ] = 0
    datas[ id ] += 1
#    if 'review/text' in e:
#        print e['review/text']
#        print e
#        print ''

# print sorted( datas.items(), key=operator.itemgetter(1) )

# for e in parse("Arts.txt.gz"):
#
#    if 'product/productId' in e:
#        if e['product/productId'] == 'B000BS01KK':
#            print e['review/text']

# seen = []

#for e in parse("Arts.txt.gz"):

#    if 'product/productId' in e:
#        print ''
#        print e['review/text']
#        seen.append( e['product/productId'] )


keys = [
'therefore',
'wherefore',
'accordingly',
'conclude',
'entails that',
'hence',
'thus',
'consequently',
'infer',
'whence',
'implies',
]

print 'foo'

for e in parse("Arts.txt.gz"):

    if 'review/text' not in e:
        e['review/text'] = ''

    flag = False

    for key in keys:
        if key in e['review/text'].lower():
            flag = True

    if flag:
        print e['review/text']
