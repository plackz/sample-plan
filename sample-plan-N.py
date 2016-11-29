#! python3
# sample-plan.py

# TODO: add normal, tightened, reduced inspection
# TODO: make a function with command line arguments

import lotSizeCode, sampleSizeNormal

sampleSize = sampleSizeNormal.sampleSizeNormal

# TODO: add in while statements as error proofing
# add logic to change input number to one of the maximums

counter = 0

while counter < 1:
    print('What size is the lot?')
    lotSize = int(input())
    if lotSize >= 500001:
        lotSize = 500001
    elif lotSize >= 150001:
        lotSize = 500000
    elif lotSize >= 35001:
        lotSize = 150000
    elif lotSize >= 10001:
        lotSize = 35000
    elif lotSize >= 3201:
        lotSize = 10000
    elif lotSize >= 1201:
        lotSize = 3200
    elif lotSize >= 501:
        lotSize = 1200
    elif lotSize >= 281:
        lotSize = 500
    elif lotSize >= 151:
        lotSize = 280
    elif lotSize >= 91:
        lotSize = 150
    elif lotSize >= 51:
        lotSize = 90
    elif lotSize >= 26:
        lotSize = 50
    elif lotSize >= 16:
        lotSize = 25
    elif lotSize >= 9:
        lotSize = 15
    else:
        lotSize = 8

    print('Choose an inspection level. (II(default), S-1, S-2, S-3, S-4, I, III)')
    inspectionLevel = input()
    if inspectionLevel == '':
        inspectionLevel = 'II'


    print('Choose AQL. (1.0(default) or 1.5)')
    aqlLevel = input()
    if aqlLevel == '':
        aqlLevel = '1.0'

    if aqlLevel == '1.0' or '':
        aqlLevel = 'aql-1'
    elif aqlLevel == '1.5':
        aqlLevel = 'aql-1.5'
    else:
        print('not 1.0 or 1.5')

    sampleLookUp = lotSizeCode.lostSizeCode[lotSize][inspectionLevel]

    print()
    print('Lot size max: ' + str(lotSize))
    print('Inspection level: ' + str(inspectionLevel))
    print('Sample code: ' + str(sampleLookUp))
    print()

    # TODO: make it sort so accept is always first

    print('Sample size: ' + str(sampleSize[sampleLookUp]['sampleQty']))
    print('Accept/Reject: ' + str(sampleSize[sampleLookUp][aqlLevel]))
    print()

    print('Do you have another query? Y/N' )
    counterInput = input()
    if counterInput is 'Y' or 'y':
        counter = 0
        print()
    else:
        counter = 1
