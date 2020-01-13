import sys
import json

from bitcoin.rpc import RawProxy

class BlockManager:
    __rawProxy = RawProxy()

    def getLastBlockHash(self): 
        return self.__rawProxy.getblockhash(self.__rawProxy.getblockcount())

    def getLastBlockInfo(self):
        return self.__rawProxy.getblock(self.getLastBlockHash())
