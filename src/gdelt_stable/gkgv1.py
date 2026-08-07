"""
GDELT Global Knowledge Graph (GKG) 1.0 record definitions.

The GKG set contains two file types,count and graph each with
their respective fields per documentation.
"""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class CountV1:
    """Primary attributes of a GDELT GKG 1.0 Count File record."""

    DATE: int
    NumArts: int
    CountType: str
    Number: int
    ObjectType: Optional[str] = None


@dataclass
class CountGeoV1:
    """Geography of a GDELT GKG 1.0 Count File record."""

    Geo_Type: Optional[int] = None
    Geo_Fullname: Optional[str] = None
    Geo_CountryCode: Optional[str] = None
    Geo_ADM1Code: Optional[str] = None
    Geo_Lat: Optional[float] = None
    Geo_Long: Optional[float] = None
    Geo_FeatureID: Optional[str] = None


@dataclass
class CountLinkedV1:
    """Linked events and source information of a GDELT GKG 1.0 Count File record."""

    CAMEOEventIDs: Optional[str] = None
    Sources: Optional[str] = None
    SourceURLs: Optional[str] = None


@dataclass
class CountFileV1:
    """One record of the GDELT GKG 1.0 Count File."""

    # Primary attributes
    Count: CountV1

    # Geography
    Geo: CountGeoV1 = field(default_factory=CountGeoV1)

    # Linked events and source information
    Linked: CountLinkedV1 = field(default_factory=CountLinkedV1)


@dataclass
class ToneV1:
    """The six comma-delimited emotional dimensions of the Graph File TONE field."""

    Tone: float
    PositiveScore: float
    NegativeScore: float
    Polarity: float
    ActivityReferenceDensity: float
    SelfGroupReferenceDensity: float


@dataclass
class GraphV1:
    """One nameset record of the GDELT GKG 1.0 Graph File"""

    # Primary attributes
    DATE: int
    NumArts: int
    Counts: List[CountV1] = field(default_factory=list)
    Themes: List[str] = field(default_factory=list)
    Locations: List[CountGeoV1] = field(default_factory=list)
    Persons: List[str] = field(default_factory=list)
    Organizations: List[str] = field(default_factory=list)

    # Emotion
    Tone: Optional[ToneV1] = None

    # Linked events and source information
    CAMEOEventIDs: Optional[str] = None
    Sources: Optional[str] = None
    SourceURLs: Optional[str] = None


class CountFileV1Collection:
    """A list of count records from the GDELT GKG 1.0 Count File."""


class GraphV1Collection:
    """A list of nameset records from the GDELT GKG 1.0 Graph File."""
