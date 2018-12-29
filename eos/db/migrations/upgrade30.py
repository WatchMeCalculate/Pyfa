"""
Migration 30

- adds esi fitting to sso character map
"""
import sqlalchemy


def upgrade(saveddata_engine):
    saveddata_engine.execute(
        """
            CREATE TABLE `esiFittingMap` (
                `fitID` INTEGER NOT NULL,
                `ssoCharacterID` INTEGER NOT NULL,
                `esiFitID` INTEGER,
                FOREIGN KEY(`fitID`) REFERENCES `fits`(`ID`) On Delete cascade,
                FOREIGN KEY(`ssoCharacterID`) REFERENCES `ssoCharacter`(`ID`) on delete cascade,
                PRIMARY KEY(`fitID`,`ssoCharacterID`)
            )
        """
    )
