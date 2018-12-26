from sqlalchemy import (
    Table,
    Column,
    Integer,
    ForeignKey,
    String,
    DateTime,
    Float,
    UniqueConstraint,
)
from sqlalchemy.orm import relation, mapper
import datetime

from eos.db import saveddata_meta
from eos.saveddata.esifittingmap import EsiFittingMap

esiFittingMap = Table(
    "esiFittingMap",
    saveddata_meta,
    Column("esiFitID", Integer, nullable=True),
    Column("ssoCharacterID", ForeignKey("ssoCharacter.ID"), primary_key=True),
    Column("fitID", ForeignKey("fits.ID"), primary_key=True),
)

mapper(EsiFittingMap, esiFittingMap)
