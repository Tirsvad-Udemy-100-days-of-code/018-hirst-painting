"""Tests for the colour palette helpers of the Hirst painting program."""

from pathlib import Path

import pytest
from PIL import Image

from hirst_painting import (
    REFERENCE_IMAGE_PATH,
    Colour,
    extract_palette,
    is_white_shade,
    remove_white_shades,
)

STRIPE_WIDTH = 20


def _write_stripes(path: Path, colours: list[Colour]) -> None:
    """Save an image of vertical stripes, one flat stripe per colour."""
    image = Image.new("RGB", (STRIPE_WIDTH * len(colours), STRIPE_WIDTH))
    for index, colour in enumerate(colours):
        left = index * STRIPE_WIDTH
        image.paste(colour, (left, 0, left + STRIPE_WIDTH, STRIPE_WIDTH))
    image.save(path)


@pytest.mark.parametrize(
    "colour",
    [
        (255, 255, 255),
        (240, 240, 240),
        (245, 250, 241),
    ],
)
def test_is_white_shade_when_all_channels_at_or_above_240(colour: Colour) -> None:
    assert is_white_shade(colour)


@pytest.mark.parametrize(
    "colour",
    [
        (239, 239, 239),
        (255, 255, 239),
        (239, 255, 255),
        (255, 239, 255),
        (200, 30, 40),
        (0, 0, 0),
    ],
)
def test_is_not_white_shade_when_any_channel_below_240(colour: Colour) -> None:
    assert not is_white_shade(colour)


def test_remove_white_shades_keeps_order_and_drops_white() -> None:
    colours: list[Colour] = [
        (255, 255, 255),
        (200, 30, 40),
        (245, 245, 245),
        (30, 90, 160),
        (240, 240, 240),
    ]

    assert remove_white_shades(colours) == [(200, 30, 40), (30, 90, 160)]


def test_remove_white_shades_returns_empty_list_when_all_white() -> None:
    assert remove_white_shades([(255, 255, 255), (240, 240, 240)]) == []


def test_remove_white_shades_returns_empty_list_when_no_colours() -> None:
    assert remove_white_shades([]) == []


def test_remove_white_shades_accepts_any_iterable() -> None:
    colours = ((colour, 30, 40) for colour in (200, 255))

    assert remove_white_shades(colours) == [(200, 30, 40), (255, 30, 40)]


def test_remove_white_shades_leaves_input_unchanged() -> None:
    colours: list[Colour] = [(255, 255, 255), (200, 30, 40)]

    remove_white_shades(colours)

    assert colours == [(255, 255, 255), (200, 30, 40)]


def test_extract_palette_returns_colours_without_white_shades(tmp_path: Path) -> None:
    image_path = tmp_path / "stripes.png"
    _write_stripes(
        image_path,
        [(200, 30, 40), (255, 255, 255), (30, 90, 160), (240, 240, 240)],
    )

    assert set(extract_palette(image_path)) == {(200, 30, 40), (30, 90, 160)}


def test_extract_palette_returns_requested_count_when_image_has_more_colours(
    tmp_path: Path,
) -> None:
    image_path = tmp_path / "stripes.png"
    _write_stripes(
        image_path,
        [(200, 30, 40), (30, 90, 160), (20, 120, 60), (90, 40, 130)],
    )

    assert len(extract_palette(image_path, colour_count=2)) == 2


def test_extract_palette_raises_when_image_is_missing(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        extract_palette(tmp_path / "missing.png")


def test_reference_image_palette_has_two_colours_and_no_white_shade() -> None:
    palette = extract_palette(REFERENCE_IMAGE_PATH)

    assert len(palette) >= 2
    assert not any(is_white_shade(colour) for colour in palette)
