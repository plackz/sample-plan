#! python3
# sample-plan.py

# TODO: add normal, tightened, reduced inspection
# TODO: convert this data to a module like census2010.py (automate the boring stuff)
# TODO: make a function with command line arguments

lotSizeCode = {8: {'S-1': 'A',
                   'S-2': 'A',
                   'S-3': 'A',
                   'S-4': 'A',
                   'I': 'A',
                   'II': 'A',
                   'III': 'B',
                   },
               15: {'S-1': 'A',
                   'S-2': 'A',
                   'S-3': 'A',
                   'S-4': 'A',
                   'I': 'A',
                   'II': 'B',
                   'III': 'C',
                   },
               25: {'S-1': 'A',
                   'S-2': 'A',
                   'S-3': 'B',
                   'S-4': 'B',
                   'I': 'B',
                   'II': 'C',
                   'III': 'D',
                   },
               50: {'S-1': 'A',
                   'S-2': 'B',
                   'S-3': 'B',
                   'S-4': 'C',
                   'I': 'C',
                   'II': 'D',
                   'III': 'E',
                   },
               90: {'S-1': 'B',
                   'S-2': 'B',
                   'S-3': 'C',
                   'S-4': 'C',
                   'I': 'C',
                   'II': 'E',
                   'III': 'F',
                   },
               150: {'S-1': 'B',
                   'S-2': 'B',
                   'S-3': 'C',
                   'S-4': 'D',
                   'I': 'D',
                   'II': 'F',
                   'III': 'G',
                   },
               280: {'S-1': 'B',
                   'S-2': 'C',
                   'S-3': 'D',
                   'S-4': 'E',
                   'I': 'E',
                   'II': 'G',
                   'III': 'H',
                   },
               500: {'S-1': 'B',
                   'S-2': 'C',
                   'S-3': 'D',
                   'S-4': 'E',
                   'I': 'F',
                   'II': 'H',
                   'III': 'J',
                   },
               1200: {'S-1': 'C',
                   'S-2': 'C',
                   'S-3': 'E',
                   'S-4': 'F',
                   'I': 'G',
                   'II': 'J',
                   'III': 'K',
                   },
               3200: {'S-1': 'C',
                   'S-2': 'D',
                   'S-3': 'E',
                   'S-4': 'G',
                   'I': 'H',
                   'II': 'K',
                   'III': 'L',
                   },
               10000: {'S-1': 'C',
                   'S-2': 'D',
                   'S-3': 'F',
                   'S-4': 'G',
                   'I': 'J',
                   'II': 'L',
                   'III': 'M',
                   },
               35000: {'S-1': 'C',
                   'S-2': 'D',
                   'S-3': 'F',
                   'S-4': 'H',
                   'I': 'K',
                   'II': 'M',
                   'III': 'N',
                   },
               150000: {'S-1': 'D',
                   'S-2': 'E',
                   'S-3': 'G',
                   'S-4': 'J',
                   'I': 'L',
                   'II': 'N',
                   'III': 'P',
                   },
               500000: {'S-1': 'D',
                   'S-2': 'E',
                   'S-3': 'G',
                   'S-4': 'J',
                   'I': 'M',
                   'II': 'P',
                   'III': 'Q',
                   },
               500001: {'S-1': 'D',
                   'S-2': 'E',
                   'S-3': 'H',
                   'S-4': 'K',
                   'I': 'N',
                   'II': 'Q',
                   'III': 'R',
                   }
               }

sampleSize = {'A': {'sampleQty': 2,
                    'aql-1': {'accept': 0, 'reject': 1},
                    'aql-1.5': {'accept': 0, 'reject': 1},
                    },
              'B': {'sampleQty': 3,
                    'aql-1': {'accept': 0, 'reject': 1},
                    'aql-1.5': {'accept': 0, 'reject': 1},
                    },          
              'C': {'sampleQty': 5,
                    'aql-1': {'accept': 0, 'reject': 1},
                    'aql-1.5': {'accept': 0, 'reject': 1},
                    },
              'D': {'sampleQty': 8,
                    'aql-1': {'accept': 0, 'reject': 1},
                    'aql-1.5': {'accept': 0, 'reject': 1},
                    },
              'E': {'sampleQty': 13,
                    'aql-1': {'accept': 0, 'reject': 1},
                    'aql-1.5': {'accept': 0, 'reject': 1},
                    },
              'F': {'sampleQty': 20,
                    'aql-1': {'accept': 0, 'reject': 1},
                    'aql-1.5': {'accept': 1, 'reject': 2},
                    },
              'G': {'sampleQty': 32,
                    'aql-1': {'accept': 1, 'reject': 2},
                    'aql-1.5': {'accept': 1, 'reject': 2},
                    },
              'H': {'sampleQty': 50,
                    'aql-1': {'accept': 1, 'reject': 2},
                    'aql-1.5': {'accept': 2, 'reject': 3},
                    },
              'J': {'sampleQty': 80,
                    'aql-1': {'accept': 2, 'reject': 3},
                    'aql-1.5': {'accept': 3, 'reject': 4},
                    },
              'K': {'sampleQty': 125,
                    'aql-1': {'accept': 3, 'reject': 4},
                    'aql-1.5': {'accept': 5, 'reject': 6},
                    },
              'L': {'sampleQty': 200,
                    'aql-1': {'accept': 5, 'reject': 6},
                    'aql-1.5': {'accept': 7, 'reject': 8},
                    },
              'M': {'sampleQty': 315,
                    'aql-1': {'accept': 7, 'reject': 8},
                    'aql-1.5': {'accept': 10, 'reject': 11},
                    },
              'N': {'sampleQty': 500,
                    'aql-1': {'accept': 10, 'reject': 11},
                    'aql-1.5': {'accept': 14, 'reject': 15},
                    },
              'P': {'sampleQty': 800,
                    'aql-1': {'accept': 14, 'reject': 15},
                    'aql-1.5': {'accept': 21, 'reject': 22},
                    },
              'Q': {'sampleQty': 1250,
                    'aql-1': {'accept': 21, 'reject': 22},
                    'aql-1.5': {'accept': 21, 'reject': 22},
                    },
              'R': {'sampleQty': 2000,
                    'aql-1': {'accept': 21, 'reject': 22},
                    'aql-1.5': {'accept': 21, 'reject': 22},
                    }           
              }

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

sampleLookUp = lotSizeCode[lotSize][inspectionLevel]

print()
print('Lot size max: ' + str(lotSize))
print('Inspection level: ' + str(inspectionLevel))
print('Sample code: ' + str(sampleLookUp))
print()

# TODO: make it sort so accept is always first

print('Sample size: ' + str(sampleSize[sampleLookUp]['sampleQty']))
print('Accept/Reject: ' + str(sampleSize[sampleLookUp][aqlLevel]))
