#! python3
# sample-plan-reduced.py

# TODO: add normal, tightened, reduced inspection
# TODO: make a function with command line arguments

import lotSizeCode, singleReduced

code = lotSizeCode
sReduc = singleReduced

# TODO: add in while statements as error proofing
# add logic to change input number to one of the maximums

running = True

while running:
    print('============================================================')
    print('ISO 2859-1:1999 Reduced Inspection Sampling Program')
    print('============================================================')      
    print('Enter lot size. (enter 0 to exit)')
    lotSize = int(input())

    if lotSize == 0:
        break
    elif lotSize >= 500001:
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

    sampleLookUp = code.lotSizeCode[lotSize][inspectionLevel]

    print()
    print('Lot size max: ' + str(lotSize))
    print('Inspection level: ' + str(inspectionLevel))
    print('Sample code: ' + str(sampleLookUp))
    print()

    # TODO: make it sort so accept is always first

    print('Sample size: ' + str(sReduc.inspectionTable[sampleLookUp]['sampleQty']))
    print('Accept/Reject: ' + str(sReduc.inspectionTable[sampleLookUp][aqlLevel]))
    print() 
