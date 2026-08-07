"""
GDELT Television Global Knowledge Graph (TV-GKG) record definitions.

Broadcasts are encoded in the standard GKG 2.1 format and use the GKGV2
record, so no separate record is defined here. However there are fields
that are disabled specifically for the television collection and are
defined here.
"""


DISABLED_FIELDS = (
    "SharingImage",
    "RelatedImages",
    "SocialImageEmbeds",
    "SocialVideoEmbeds",
    "Quotations",
    "AllNames",
    "EnhancedDates",
    "Amounts",
    "TranslationInfo",
)


class TVGKGV2Collection:
    """A list of broadcast records from the GDELT TV-GKG file."""
