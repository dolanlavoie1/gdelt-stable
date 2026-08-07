"""
GDELT Visual Global Knowledge Graph (VGKG) 1.0 record definitions.
"""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class LabelV1:
    """One block of the LABELS and/or LOGOS fields.

    Since the two fields are identical in format this definitions is reused.
    """

    Description: Optional[str]
    Score: Optional[float]

    MID: Optional[str]


@dataclass
class GeoLandmarkV1:
    """One block of the GEOLANDMARKS field."""

    Description: Optional[str]
    Score: Optional[float]
    Latitude: Optional[float]
    Longitude: Optional[float]


@dataclass
class SafeSearchV1:
    """The Google SafeSearch estimates of the SAFESEARCH field."""

    ViolenceLikelihood: Optional[int]
    MedicalLikelihood: Optional[int]
    SpoofLikelihood: Optional[int]
    AdultLikelihood: Optional[int]


@dataclass
class FaceV1:
    """One block of the FACES field."""

    DetectionConfidence: Optional[float]
    RollAngle: Optional[float]
    PanAngle: Optional[float]
    TiltAngle: Optional[float]
    LandmarkingConfidence: Optional[float]
    BoundingBox: List[str]
    EmotionSorrowLikelihood: Optional[int]
    EmotionAngerLikelihood: Optional[int]
    HeadwearLikelihood: Optional[int]
    EmotionJoyLikelihood: Optional[int]
    EmotionSurpriseLikelihood: Optional[int]
    UnderExposedLikelihood: Optional[int]
    BlurredLikelihood: Optional[int]


@dataclass
class VGKGV1:
    """One image record of the GDELT VGKG 1.0 file."""

    DATE: int
    DocumentIdentifier: Optional[str]
    ImageURL: Optional[str]
    Labels: List[LabelV1] = field(default_factory=list)
    GeoLandmarks: List[GeoLandmarkV1] = field(default_factory=list)
    Logos: List[LabelV1] = field(default_factory=list)
    SafeSearch: Optional[SafeSearchV1] = None
    Faces: List[FaceV1] = field(default_factory=list)
    OCR: List[str] = field(default_factory=list)


class VGKGV1Collection:
    """A list of image records from the GDELT VGKG 1.0 file."""
