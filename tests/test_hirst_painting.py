"""Tests for the colour palette helpers of the Hirst painting program."""

import tkinter
import turtle
from collections import Counter
from collections.abc import Iterator, Sequence
from dataclasses import dataclass, field
from pathlib import Path

import pytest
from PIL import Image

import hirst_painting
from hirst_painting import (
    REFERENCE_IMAGE_PATH,
    Colour,
    DotPen,
    Position,
    create_pen,
    dot_positions,
    draw_dots,
    extract_palette,
    is_white_shade,
    main,
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


@pytest.fixture(scope="session")
def tk_root() -> Iterator[tkinter.Tk]:
    """Create one hidden Tk window for the whole run.

    Starting Tk again and again in one process fails now and then on Windows
    (Tk cannot read its own library files), so every test shares this one.
    """
    root = tkinter.Tk()
    root.withdraw()
    yield root
    root.destroy()


@pytest.fixture
def canvas(tk_root: tkinter.Tk) -> Iterator[tkinter.Canvas]:
    """Yield a canvas on the hidden window, so no window appears."""
    canvas = tkinter.Canvas(tk_root)
    yield canvas
    canvas.destroy()


@pytest.fixture
def screen(canvas: tkinter.Canvas) -> turtle.TurtleScreen:
    """Return a turtle screen that draws on the hidden canvas."""
    return turtle.TurtleScreen(canvas)


def test_create_pen_hides_the_turtle(screen: turtle.TurtleScreen) -> None:
    assert not create_pen(screen).isvisible()


def test_create_pen_lifts_the_pen(screen: turtle.TurtleScreen) -> None:
    assert not create_pen(screen).isdown()


def test_create_pen_switches_the_screen_to_255_level_colours(
    screen: turtle.TurtleScreen,
) -> None:
    create_pen(screen)

    assert screen.colormode() == 255


def test_create_pen_draws_on_the_given_screen(screen: turtle.TurtleScreen) -> None:
    assert create_pen(screen).getscreen() is screen


def test_dot_positions_returns_100_positions() -> None:
    assert len(dot_positions()) == 100


def test_dot_positions_are_all_different() -> None:
    positions = dot_positions()

    assert len(set(positions)) == len(positions)


def test_dot_positions_have_10_heights_with_10_dots_each() -> None:
    dots_per_height = Counter(y for _, y in dot_positions())

    assert list(dots_per_height.values()) == [10] * 10


def test_dot_positions_are_50_apart_along_each_row() -> None:
    positions = dot_positions()

    for start in range(0, 100, 10):
        row = positions[start : start + 10]
        assert [x for x, _ in row] == list(range(-225, 226, 50))
        assert len({y for _, y in row}) == 1


def test_dot_positions_are_50_apart_between_rows() -> None:
    heights = sorted({y for _, y in dot_positions()})

    assert heights == list(range(-225, 226, 50))


def test_dot_positions_start_bottom_left_and_fill_rows_upward() -> None:
    positions = dot_positions()

    assert positions[0] == (-225, -225)
    assert positions[1] == (-175, -225)
    assert positions[10] == (-225, -175)
    assert positions[-1] == (225, 225)


def test_dot_positions_are_centred_on_the_origin() -> None:
    positions = dot_positions()

    assert min(x for x, _ in positions) == -max(x for x, _ in positions)
    assert min(y for _, y in positions) == -max(y for _, y in positions)


class RecordingPen:
    """A pen that records the dots it was asked to draw and where."""

    def __init__(self) -> None:
        """Start at the origin with no dots drawn."""
        self.position: Position = (0, 0)
        self.dots: list[tuple[Position, int, Colour]] = []

    def goto(self, position: Position, /) -> None:
        """Remember the position the next dot is drawn at."""
        self.position = position

    def dot(self, size: int, colour: Colour, /) -> None:
        """Record a dot at the current position."""
        self.dots.append((self.position, size, colour))


PALETTE: list[Colour] = [(200, 30, 40), (30, 90, 160), (20, 120, 60)]


def test_draw_dots_draws_a_dot_at_every_position_in_order() -> None:
    pen = RecordingPen()

    draw_dots(pen, PALETTE)

    assert [position for position, _, _ in pen.dots] == dot_positions()


def test_draw_dots_draws_dots_of_size_20() -> None:
    pen = RecordingPen()

    draw_dots(pen, PALETTE)

    assert {size for _, size, _ in pen.dots} == {20}


def test_draw_dots_colours_every_dot_from_the_palette() -> None:
    pen = RecordingPen()

    draw_dots(pen, PALETTE)

    assert {colour for _, _, colour in pen.dots} <= set(PALETTE)


def test_draw_dots_asks_the_chooser_for_the_colour_of_each_dot() -> None:
    pen = RecordingPen()
    asked: list[Sequence[Colour]] = []

    def choose_last(colours: Sequence[Colour]) -> Colour:
        asked.append(colours)
        return colours[-1]

    draw_dots(pen, PALETTE, choose_colour=choose_last)

    assert len(asked) == 100
    assert {colour for _, _, colour in pen.dots} == {(20, 120, 60)}


def test_draw_dots_raises_when_the_palette_is_empty() -> None:
    with pytest.raises(ValueError, match="no colours"):
        draw_dots(RecordingPen(), [])


def _item_option(canvas: tkinter.Canvas, item: int, option: str) -> str:
    """Return one option of a canvas item, such as its width or fill colour."""
    # typeshed leaves Canvas.itemcget untyped, which strict mypy refuses to call.
    return str(canvas.itemcget(item, option))  # type: ignore[no-untyped-call]


def _drawn_dots(canvas: tkinter.Canvas) -> list[tuple[Position, str]]:
    """Return the position and fill colour of every dot on the canvas.

    Turtle draws a dot as a round-capped line whose width is the dot size.
    """
    dots: list[tuple[Position, str]] = []
    for item in canvas.find_all():
        is_dot = (
            str(canvas.type(item)) == "line"
            and _item_option(canvas, item, "width") == "20.0"
        )
        if is_dot:
            x, y = canvas.coords(item)[:2]
            dots.append(((round(x), -round(y)), _item_option(canvas, item, "fill")))
    return dots


def _other_lines(canvas: tkinter.Canvas) -> int:
    """Count the line items that are not dots, such as a trail behind the pen."""
    lines = [item for item in canvas.find_all() if str(canvas.type(item)) == "line"]
    return len(lines) - len(_drawn_dots(canvas))


def test_draw_dots_draws_100_dots_at_the_dot_positions_on_a_real_turtle(
    screen: turtle.TurtleScreen, canvas: tkinter.Canvas
) -> None:
    screen.tracer(0)
    pen = create_pen(screen)

    draw_dots(pen, PALETTE)

    positions = [position for position, _ in _drawn_dots(canvas)]
    assert sorted(positions) == sorted(dot_positions())


def test_draw_dots_colours_the_dots_of_a_real_turtle_from_the_palette(
    screen: turtle.TurtleScreen, canvas: tkinter.Canvas
) -> None:
    screen.tracer(0)
    pen = create_pen(screen)

    draw_dots(pen, PALETTE)

    palette_fills = {f"#{red:02x}{green:02x}{blue:02x}" for red, green, blue in PALETTE}
    assert {fill for _, fill in _drawn_dots(canvas)} <= palette_fills


def test_draw_dots_draws_no_trail_between_dots(
    screen: turtle.TurtleScreen, canvas: tkinter.Canvas
) -> None:
    screen.tracer(0)
    pen = create_pen(screen)
    other_lines_before = _other_lines(canvas)

    draw_dots(pen, PALETTE)

    assert _other_lines(canvas) == other_lines_before


@dataclass
class MainRun:
    """What happened during one run of main() on a fake screen."""

    events: list[str] = field(default_factory=list)
    palettes: list[Sequence[Colour]] = field(default_factory=list)
    animation_while_drawing: list[int] = field(default_factory=list)


@pytest.fixture
def main_run(monkeypatch: pytest.MonkeyPatch, canvas: tkinter.Canvas) -> MainRun:
    """Run main() once with drawing and the click wait replaced by recorders."""
    run = MainRun()

    class RecordingScreen(turtle.TurtleScreen):
        def update(self) -> None:
            run.events.append("update")

        def exitonclick(self) -> None:
            run.events.append("exitonclick")

    screen = RecordingScreen(canvas)

    def record_draw(pen: DotPen, palette: Sequence[Colour]) -> None:
        run.events.append("draw_dots")
        run.palettes.append(palette)
        run.animation_while_drawing.append(screen.tracer())

    monkeypatch.setattr(turtle, "Screen", lambda: screen)
    monkeypatch.setattr(hirst_painting, "draw_dots", record_draw)
    main()
    return run


def test_main_draws_with_the_palette_of_the_reference_image(
    main_run: MainRun,
) -> None:
    assert main_run.palettes == [extract_palette(REFERENCE_IMAGE_PATH)]


def test_main_turns_the_animation_off_while_drawing(main_run: MainRun) -> None:
    assert main_run.animation_while_drawing == [0]


def test_main_shows_the_painting_then_waits_for_a_click(main_run: MainRun) -> None:
    assert main_run.events == ["draw_dots", "update", "exitonclick"]
