#! python3
# sample-plan.py

# TODO: add normal, tightened, reduced inspection
# TODO: convert this data to a module like census2010.py (automate the boring stuff)
# TODO: make a function with command line arguments

import lotSizeCode, sampleSizeNormal, sampleSizeReduced, sampleSizeTightened

sampN = sampleSizeNormal
sampR = sampleSizeReduced
sampT = sampleSizeTightened



# TODO: add in while statements as error proofing
# add logic to change input number to one of the maximums

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

print('Choose an inspection level. (S-1, S-2, S-3, S-4, I, II(default), III)')
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

print('Choose normal, reduced, tightened inspection. (n=1, r=0, t=2)')
inspectionPlan = int(input())

# TODO need to fix
'''
n = 'Normal'
r = 'Reduced'
t = 'Tightened'

inspectionPlanName = inspectionPlan(if n then return 'Normal') # may be a seprate function

if inspectionPlan == 'r' or 'R':
    inspectionPlanName = 'Reduced'
elif inspectionPlan == 'n' or 'N':
    inspectionPlanName = 'Normal'
elif inspectionPlan == 't' or 'T':
    inspectionPlanName = 'Tightened'
else:
    print('error. not n,t, or r.')
'''

sampleLookUp = lotSizeCode.lotSizeCode[lotSize][inspectionLevel]

print()
print('Lot size max: ' + str(lotSize))
print('Inspection level: ' + str(inspectionLevel))
print('Sample code: ' + str(sampleLookUp))
print(str(inspectionPlan) + ' inspection.')
print()

# TODO: make it sort so accept is always first

# TODO: not working always going to else block
if str(inspectionPlan) == 1:
    # TODO: need to make a function to reduce code
    print('Sample size: ' + str(sampN.sampleSizeNormal[sampleLookUp]['sampleQty']))
    print('Accept/Reject: ' + str(sampN.sampleSizeNormal[sampleLookUp][aqlLevel]))
    print()
elif str(inspectionPlan) == 0:
    # TODO: need to make a function to reduce code
    print('Sample size: ' + str(sampR.sampleSizeReduced[sampleLookUp]['sampleQty']))
    print('Accept/Reject: ' + str(sampR.sampleSizeReduced[sampleLookUp][aqlLevel]))
    print()
else:
    # TODO: need to make a function to reduce code
    print('Sample size: ' + str(sampT.sampleSizeTightened[sampleLookUp]['sampleQty']))
    print('Accept/Reject: ' + str(sampT.sampleSizeTightened[sampleLookUp][aqlLevel]))
    print()
