"""Hirst-style spot painting drawn with turtle."""

import random
import turtle
from collections.abc import Callable, Iterable, Sequence
from pathlib import Path
from typing import Protocol

import colorgram

type Colour = tuple[int, int, int]
"""A colour as red, green and blue values from 0 to 255."""

type Position = tuple[int, int]
"""A point on the turtle screen as x and y, in screen units."""

REFERENCE_IMAGE_PATH = (
    Path(__file__).resolve().parent.parent / "assets" / "20260524_132700.jpg"
)

# More than a Hirst painting has colours; colorgram returns fewer when the image
# has fewer, so the palette is never padded.
EXTRACTED_COLOUR_COUNT = 30

GRID_ROWS = 10
GRID_COLUMNS = 10

DOT_SIZE = 20

# Distance between the centres of neighbouring dots, along rows and columns.
DOT_SPACING = 50

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


class DotPen(Protocol):
    """The two turtle operations that drawing dots needs."""

    def goto(self, position: Position, /) -> None:
        """Move to the position."""
        ...

    def dot(self, size: int, colour: Colour, /) -> None:
        """Draw a dot of the size and colour at the current position."""
        ...


def create_pen(screen: turtle.TurtleScreen) -> turtle.RawTurtle:
    """Return a hidden turtle with its pen up on a screen that takes RGB colours.

    The pen is up and the turtle is hidden so that the painting shows no trail
    and no cursor; the screen takes colours as 0 to 255 values, as `Colour` does.
    """
    screen.colormode(255)
    pen = turtle.RawTurtle(screen)
    pen.hideturtle()
    pen.penup()
    return pen


def dot_positions() -> list[Position]:
    """Return the centre of every dot, rows from the bottom up, left to right.

    The grid is centred on the origin, the middle of the turtle window, so the
    whole painting fits in a window of the default size.
    """
    left = -DOT_SPACING * (GRID_COLUMNS - 1) // 2
    bottom = -DOT_SPACING * (GRID_ROWS - 1) // 2
    return [
        (left + column * DOT_SPACING, bottom + row * DOT_SPACING)
        for row in range(GRID_ROWS)
        for column in range(GRID_COLUMNS)
    ]


def draw_dots(
    pen: DotPen,
    palette: Sequence[Colour],
    choose_colour: Callable[[Sequence[Colour]], Colour] = random.choice,
) -> None:
    """Draw a dot at every dot position, each in a colour chosen from the palette.

    Raises ValueError when the palette has no colours.
    """
    if not palette:
        raise ValueError("The palette has no colours to draw with.")
    for position in dot_positions():
        pen.goto(position)
        pen.dot(DOT_SIZE, choose_colour(palette))


def main() -> None:
    """Draw the painting with the reference image's palette, then wait for a click."""
    screen = turtle.Screen()
    # Animating the 100 moves takes about 20 seconds on screen, against the 30
    # allowed (SC6 of BC-001), so draw unseen and show the whole painting at once.
    screen.tracer(0)
    pen = create_pen(screen)
    draw_dots(pen, extract_palette(REFERENCE_IMAGE_PATH))
    screen.update()
    screen.exitonclick()


if __name__ == "__main__":
    main()
