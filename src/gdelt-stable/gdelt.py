"""
An interface for what kinds of paramaters the many different type of gdelt 
datasets have. Parameters are based on the fields of the gdelt object made
(v1 event, v1 global (GKG), v2 event, v2 global(GKG), Visual graph, etc.).
"""

from dataclasses import dataclass
from typing import Optional, Iterable, Iterator

@dataclass
class gdeltEvent:
    """one singular record of the gdeltEvents1 set"""
    
    # EventID and attributes
    GlobalEventID : int
    Day : int
    MonthYear: int
    Year: int
    FractionDate : float

    # Actor1 attributes
    Actor1Code: Optional[str]
    Actor1Name: Optional[str]
    Actor1CountryCode: Optional[str]
    Actor1KnownGroupCode: Optional[str]
    Actor1EthnicCode: Optional[str]
    Actor1Religion1Code: Optional[str]
    Actor1Religion2Code: Optional[str]
    Actor1Type1Code: Optional[str]
    Actor1Type2Code: Optional[str]
    Actor1Type3Code: Optional[str]
 
    # Actor2 attributes
    Actor2Code: Optional[str]
    Actor2Name: Optional[str]
    Actor2CountryCode: Optional[str]
    Actor2KnownGroupCode: Optional[str]
    Actor2EthnicCode: Optional[str]
    Actor2Religion1Code: Optional[str]
    Actor2Religion2Code: Optional[str]
    Actor2Type1Code: Optional[str]
    Actor2Type2Code: Optional[str]
    Actor2Type3Code: Optional[str]
 
    # Event action attributes
    IsRootEvent: bool
    EventCode: str
    EventBaseCode: str
    EventRootCode: str
    QuadClass: int
    GoldsteinScale: float
    NumMentions: int
    NumSources: int
    NumArticles: int
    AvgTone: float
 
    # Actor1 event geography
    Actor1Geo_Type: Optional[int]
    Actor1Geo_Fullname: Optional[str]
    Actor1Geo_CountryCode: Optional[str]
    Actor1Geo_ADM1Code: Optional[str]
    Actor1Geo_Lat: Optional[float]
    Actor1Geo_Long: Optional[float]
    Actor1Geo_FeatureID: Optional[int]
 
    # Actor2 event geography
    Actor2Geo_Type: Optional[int]
    Actor2Geo_Fullname: Optional[str]
    Actor2Geo_CountryCode: Optional[str]
    Actor2Geo_ADM1Code: Optional[str]
    Actor2Geo_Lat: Optional[float]
    Actor2Geo_Long: Optional[float]
    Actor2Geo_FeatureID: Optional[int]
 
    # Action event geography
    ActionGeo_Type: Optional[int]
    ActionGeo_Fullname: Optional[str]
    ActionGeo_CountryCode: Optional[str]
    ActionGeo_ADM1Code: Optional[str]
    ActionGeo_Lat: Optional[float]
    ActionGeo_Long: Optional[float]
    ActionGeo_FeatureID: Optional[int]
 
    # Data management fields
    DATEADDED: int
    SOURCEURL: Optional[str] = None 
    


class gdeltEvents1:
    def __init__(self, events: list[gdeltEvent]):
        self.events = events
        return self
        