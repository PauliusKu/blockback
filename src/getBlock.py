import sys
import json

from blockManager import BlockManager
from decimalEncoder import DecimalEncoder

print("1. Test smth.")
p1 = BlockManager()
#a = p1.getLastBlockHash()
a = p1.getLastBlockInfo()

with open('/home/user029/bce/files/lastblock.json', 'w') as json_file:
    json.dump(a, json_file, cls=DecimalEncoder)

