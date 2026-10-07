"""Hirst-style spot painting drawn with turtle."""

from collections.abc import Iterable
from pathlib import Path

import colorgram

type Colour = tuple[int, int, int]
"""A colour as red, green and blue values from 0 to 255."""

REFERENCE_IMAGE_PATH = (
    Path(__file__).resolve().parent.parent / "assets" / "20260524_132700.jpg"
)

# More than a Hirst painting has colours; colorgram returns fewer when the image
# has fewer, so the palette is never padded.
EXTRACTED_COLOUR_COUNT = 30

# A colour counts as a white shade when red, green and blue are all at or above
# this value: such dots are invisible on the white background (SC3 of BC-001).
WHITE_THRESHOLD = 240


def is_white_shade(colour: Colour) -> bool:
    """Return whether red, green and blue are all at or above the threshold."""
    return all(channel >= WHITE_THRESHOLD for channel in colour)


def remove_white_shades(colours: Iterable[Colour]) -> list[Colour]:
    """Return the colours without white shades, in their original order."""
    return [colour for colour in colours if not is_white_shade(colour)]


def extract_palette(
    image_path: Path, colour_count: int = EXTRACTED_COLOUR_COUNT
) -> list[Colour]:
    """Return the image's colours without white shades, most common first.

    Raises FileNotFoundError when the image does not exist.
    """
    extracted = colorgram.extract(str(image_path), colour_count)
    colours = [(found.rgb.r, found.rgb.g, found.rgb.b) for found in extracted]
    return remove_white_shades(colours)
