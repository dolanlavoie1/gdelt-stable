"""
GDELT Global Knowledge Graph (GKG) 2.1 record definitions.

Unlike the 1.0 set, the GKG 2.1 set contains a single file type holding one
record per document, with the counts-only file discontinued. Fields prefaced
with "V1" in the documentation are unchanged from the 1.0 format, those
prefaced with "V2" carry the character offset of each reference in the
document. I likely could have reused the object definition but felt it was
better to keep all object types contained in their own file. 
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class LocationV2:
    """One location block of the V1LOCATIONS and V2ENHANCEDLOCATIONS fields.

    Also serves as the geography of a Count block. Geo_ADM2Code and Offset are
    populated for V2ENHANCEDLOCATIONS only, cross-reference the Geo_FeatureID
    of a Count against V2ENHANCEDLOCATIONS to resolve its ADM2 code.
    """

    Geo_Type: Optional[int] = None
    Geo_Fullname: Optional[str] = None
    Geo_CountryCode: Optional[str] = None
    Geo_ADM1Code: Optional[str] = None
    Geo_ADM2Code: Optional[str] = None
    Geo_Lat: Optional[float] = None
    Geo_Long: Optional[float] = None
    Geo_FeatureID: Optional[str] = None
    Offset: Optional[int] = None


@dataclass
class CountV2:
    """One Count block of the V1COUNTS and V2.1COUNTS fields.

    Offset is populated for V2.1COUNTS only.
    """

    CountType: str
    Count: int
    ObjectType: Optional[str] = None
    Geo: LocationV2 = field(default_factory=LocationV2)
    Offset: Optional[int] = None


@dataclass
class EnhancedNameV2:
    """A list of all orgs/companies refrenced in the document along with
    character offsets
    """

    Name: str
    Offset: Optional[int] = None


@dataclass
class ToneV2:
    """The seven comma-delimited emotional dimensions of the V1.5TONE field."""

    Tone: float
    PositiveScore: float
    NegativeScore: float
    Polarity: float
    ActivityReferenceDensity: float
    SelfGroupReferenceDensity: float
    WordCount: int


@dataclass
class EnhancedDateV2:
    """One date block of the V2.1ENHANCEDDATES field."""

    Resolution: int
    Month: int
    Day: int
    Year: int
    Offset: Optional[int] = None


@dataclass
class GCAMV2:
    """The content analysis dimensions of the V2GCAM field.

    Dimensions are keyed "DictionaryID.DimensionID". Only dimensions with one
    or more matches are reported, an absent dimension scores 0.
    """

    # The reserved "wc" key
    WordCount: Optional[int] = None

    # The reserved "nwc" key, absent unless a native language dictionary matched
    NativeWordCount: Optional[int] = None

    # The "c" prefixed word count dimensions
    Counts: Dict[str, int] = field(default_factory=dict)

    # The "v" prefixed average value dimensions
    Values: Dict[str, float] = field(default_factory=dict)


@dataclass
class QuotationV2:
    """One quotation block of the V2.1QUOTATIONS field."""

    Offset: int
    Length: int
    Quote: str
    Verb: Optional[str] = None


@dataclass
class AmountV2:
    """One amount block of the V2.1AMOUNTS field."""

    Amount: float
    Object: Optional[str] = None
    Offset: Optional[int] = None


@dataclass
class TranslationInfoV2:
    """The provenance(ownership) of the V2.1TRANSLATIONINFO field.

    Blank for documents originally in English.
    """

    SRCLC: Optional[str] = None
    ENG: Optional[str] = None


@dataclass
class CitationV2:
    """One citation of the V2EXTRASXML CITEDREFERENCESLIST block.

    Only available for the academic journal article subcollection, fields may
    be absent or out of order.
    """

    Authors: List[str] = field(default_factory=list)
    Title: Optional[str] = None
    BookTitle: Optional[str] = None
    Date: Optional[str] = None
    Journal: Optional[str] = None
    Volume: Optional[str] = None
    Issue: Optional[str] = None
    Pages: Optional[str] = None
    Institution: Optional[str] = None
    Publisher: Optional[str] = None
    Location: Optional[str] = None
    Marker: Optional[str] = None


@dataclass
class GKGV2:
    """One document record of the GDELT GKG 2.1 file."""

    # Extracted fields
    GKGRecordID: str
    DATE: int
    SourceCollectionIdentifier: int
    SourceCommonName: Optional[str] = None
    DocumentIdentifier: Optional[str] = None
    Counts: List[CountV2] = field(default_factory=list)
    EnhancedCounts: List[CountV2] = field(default_factory=list)
    Themes: List[str] = field(default_factory=list)
    EnhancedThemes: List[EnhancedNameV2] = field(default_factory=list)
    Locations: List[LocationV2] = field(default_factory=list)
    EnhancedLocations: List[LocationV2] = field(default_factory=list)
    Persons: List[str] = field(default_factory=list)
    EnhancedPersons: List[EnhancedNameV2] = field(default_factory=list)
    Organizations: List[str] = field(default_factory=list)
    EnhancedOrganizations: List[EnhancedNameV2] = field(default_factory=list)
    Tone: Optional[ToneV2] = None
    EnhancedDates: List[EnhancedDateV2] = field(default_factory=list)
    GCAM: Optional[GCAMV2] = None
    SharingImage: Optional[str] = None
    RelatedImages: List[str] = field(default_factory=list)
    SocialImageEmbeds: List[str] = field(default_factory=list)
    SocialVideoEmbeds: List[str] = field(default_factory=list)
    Quotations: List[QuotationV2] = field(default_factory=list)
    AllNames: List[EnhancedNameV2] = field(default_factory=list)
    Amounts: List[AmountV2] = field(default_factory=list)
    TranslationInfo: Optional[TranslationInfoV2] = None
    ExtrasXML: List[CitationV2] = field(default_factory=list)


class GKGV2Collection:
    """A list of document records from the GDELT GKG 2.1 file."""
