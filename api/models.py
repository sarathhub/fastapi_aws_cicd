from api.database import Base
from sqlalchemy import Column, Integer, String, Boolean, CHAR

class Country(Base):
    __tablename__ = 'tbl_Country'

    CountryID = Column(Integer, primary_key=True, autoincrement=True)
    CountryName = Column(String(100), nullable=False)
    Geography = Column(String(100))
    CountryISOCode = Column(CHAR(2), nullable=False)
    CountryISO3Code = Column(CHAR(3), nullable=False)
    CurrencyName = Column(String(50))
    CurrencyCode = Column(CHAR(3))
    DisplayFlag = Column(Boolean, default=True)