"""
GDELT Historical American Books Archive (HABA) GKG record definitions.

The two book collections, Internet Archive and HathiTrust, are encoded in the
GKG 2.1 format and share its column ordering, so the record below mirrors the
GKGV2 footprint. The differences are that DATE is a four-digit publication
year rather than a timestamp, that several columns carry no data for either
collection and exist only to keep the column ordering aligned with the other
GDELT datasets, and that each record is followed by the book level metadata of
whichever collection it came from. As with the 2.1 set the object definitions
are repeated here rather than imported so that all object types stay contained
in their own file.

"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional

NOT_USED_FIELDS = (
    "SharingImage",
    "RelatedImages",
    "SocialImageEmbeds",
    "SocialVideoEmbeds",
    "TranslationInfo",
    "Extras",
)

HATHITRUST_DISABLED_FIELDS = (
    "Quotations",
    "Amounts",
)

SOURCE_COLLECTIONS = {
    7: "InternetArchiveBooks",
    8: "HathiTrustBooks",
}


@dataclass
class LocationV2:
    """
    One location block of the LOCATIONS and/or V2LOCATIONS fields.

    Also serves as the geography of a Count block. Geo_ADM2Code and Offset are
    populated for V2LOCATIONS only, cross-reference the Geo_FeatureID of a
    Count against V2LOCATIONS to resolve its ADM2 code.
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
    """
    One Count block of the COUNTS and/or V2COUNTS fields.

    Offset is populated for V2COUNTS only. Unlike the primary GDELT event
    stream these records carry no unique identifier and are not dated.
    """

    CountType: str
    Count: int
    ObjectType: Optional[str] = None
    Geo: LocationV2 = field(default_factory=LocationV2)
    Offset: Optional[int] = None


@dataclass
class EnhancedNameV2:
    """
    One name block of a V2 name field along with its character offset.

    Shared by V2THEMES, V2PERSONS, V2ORGANIZATIONS and ALLNAMES since the four
    are identical in format. A name mentioned multiple times in a book appears
    once per mention.
    """

    Name: str
    Offset: Optional[int] = None


@dataclass
class ToneV2:
    """The seven comma-delimited emotional dimensions of the TONE field."""

    Tone: float
    PositiveScore: float
    NegativeScore: float
    Polarity: float
    ActivityReferenceDensity: float
    SelfGroupReferenceDensity: float
    WordCount: int


@dataclass
class EnhancedDateV2:
    """
    One date block of the DATES field.

    Resolution is 4 for a month-day date without a year, 3 for a fully
    resolved day-level date, 2 for a month and year date and 1 for a year only
    date. Month and Day hold 0 where the resolution does not supply them, as
    does Year for Resolution 4 dates.
    """

    Resolution: int
    Month: int
    Day: int
    Year: int
    Offset: Optional[int] = None


@dataclass
class GCAMV2:
    """
    The content analysis dimensions of the V2GCAM field.

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
    """
    One quotation block of the QUOTATIONS field.

    Internet Archive only, see HATHITRUST_DISABLED_FIELDS.
    """

    Offset: int
    Length: int
    Quote: str
    Verb: Optional[str] = None


@dataclass
class AmountV2:
    """
    One amount block of the AMOUNTS field.

    Internet Archive only, see HATHITRUST_DISABLED_FIELDS.
    """

    Amount: float
    Object: Optional[str] = None
    Offset: Optional[int] = None


@dataclass
class InternetArchiveBookMeta:
    """
    The BookMeta_ record level metadata of an Internet Archive book.

    Provided as is in the raw form it takes in the Internet Archive metadata
    record, so the same author, publisher or language may appear under several
    spellings and formats and careful filtering is often needed.
    """

    BookMeta_Identifier: Optional[str] = None
    BookMeta_Title: Optional[str] = None
    BookMeta_Creator: List[str] = field(default_factory=list)
    BookMeta_Subjects: List[str] = field(default_factory=list)
    BookMeta_Publisher: Optional[str] = None
    BookMeta_Language: Optional[str] = None
    BookMeta_Year: Optional[str] = None
    BookMeta_Date: Optional[str] = None
    BookMeta_Sponsor: Optional[str] = None
    BookMeta_Contributor: Optional[str] = None
    BookMeta_ScanningCenter: Optional[str] = None
    BookMeta_Collections: List[str] = field(default_factory=list)
    BookMeta_AddedDate: Optional[str] = None
    BookMeta_ScannedImages: Optional[int] = None
    BookMeta_DownloadsJune2015: Optional[int] = None
    BookMeta_CallNumber: Optional[str] = None
    BookMeta_IdentifierBib: Optional[str] = None
    BookMeta_IdentifierArk: Optional[str] = None
    BookMeta_OCLDID: Optional[str] = None
    BookMeta_FullText: Optional[str] = None


@dataclass
class HathiTrustBookMeta:
    """
    The BookMeta_ record level metadata of a HathiTrust book.

    Compiled from the MARC XML record of the book and provided as-is. The
    field set differs from the Internet Archive because the two collections
    use different metadata schemas, and even the common fields can differ in
    contents and formatting. The GDELT documentation leaves the last several
    columns unlabeled, so their names here follow the BigQuery schema.
    """

    BookMeta_Identifier: Optional[str] = None
    BookMeta_Date: Optional[int] = None
    BookMeta_AddedDate: Optional[int] = None
    BookMeta_Contributor: Optional[str] = None
    BookMeta_InternetArchiveIdentifier: Optional[str] = None
    BookMeta_Title: Optional[str] = None
    BookMeta_Subjects: List[str] = field(default_factory=list)
    BookMeta_Authors: List[str] = field(default_factory=list)
    BookMeta_CorporateAuthors: List[str] = field(default_factory=list)
    BookMeta_Publisher: Optional[str] = None
    BookMeta_Source: Optional[str] = None
    BookMeta_PublisherDate: Optional[str] = None


@dataclass
class HABAGKG:
    """One book record of the GDELT Historical American Books Archive."""

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

    TranslationInfo: Optional[str] = None
    Extras: Optional[str] = None

    BookMeta: Optional[InternetArchiveBookMeta | HathiTrustBookMeta] = None


class HABAGKGCollection:
    """A list of book records from the GDELT Historical American Books Archive."""
