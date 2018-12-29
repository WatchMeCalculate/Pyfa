from sqlalchemy.orm import reconstructor
import datetime
import time


class EsiFittingMap(object):
    def __init__(self, fitID, esiFitID, ssoCharacterId):
        self.fitID = fitID
        self.esiFitID = esiFitID
        self.ssoCharacterID = ssoCharacterId

    @reconstructor
    def init(self):
        pass

    @property
    def ssoCharacter(self):
        return self.__ssoCharacter

    def __repr__(self):
        return "esiFittingMap(fitID={}, esiFitId={}, ssoCharacterID={}) at {}".format(
            self.fitID, self.esiFitID, self.ssoCharacterID, hex(id(self))
        )
