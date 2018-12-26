from eos.db.saveddata.esifittingmap import EsiFittingMap as EFMObj
import eos.db


class EsiFittingMap(object):
    instance = None

    @classmethod
    def getInstance(cls):
        if cls.instance is None:
            cls.instance = EsiFittingMap()

        return cls.instance

    @staticmethod
    def getEsiFittingCharacters(fitID):
        return eos.db.getFittingCharacters(fitID)

    @staticmethod
    def deleteFittingMap(fitID, ssoCharacterID):
        fittingMap = eos.db.getFittingMap(fitID, ssoCharacterID)
        eos.db.remove(fittingMap)
        eos.db.commit()

    @staticmethod
    def AddCharacterFitting(fitID, characterID, esiFitID=None):
        newEsiFitting = EFMObj(fitID, esiFitID, characterID)
        eos.db.save(newEsiFitting)
        eos.db.commit()

    @staticmethod
    def UpdateCharacterFitting(fitID, characterID, esiFitID):
        fittingMap = eos.db.getFittingMap(fitID, characterID)
        fittingMap.esiFitID = esiFitID
        eos.db.save(fittingMap)
        eos.db.commit()
