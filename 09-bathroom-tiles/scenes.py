from utilities import *
from string import digits

import manimpango

PALETTE = ["#b91e2f", "#f68828", "#cdd190", "#122f30"]
REDUCED_PALETTE = PALETTE[:2]

DIRECTIONS = [RIGHT, UP, LEFT, DOWN]

NOTES_SCALE = 0.8
NOTES_COLOR = GRAY

QUESTION_MARK_SCALE = 3

INDICATE_SCALE = 1.5


def is_hex_color(str):
    """Yeah I know, this is not pretty."""
    return (
        len(str) == 7
        and str.startswith("#")
        and all([c in digits + "abcdef" for c in str.lower()[1:]])
    )


def get_text_speed(text, speed_by_char=0.095):
    return len("".join(text.split())) * speed_by_char


def get_item_by_direction(items, direction):
    for i, d in enumerate(DIRECTIONS):
        if (direction == d).all():
            return items[i]


class PartialFlash(AnimationGroup):
    def __init__(
        self,
        point: np.ndarray,
        start_angle=0,
        end_angle=TAU,
        line_length: float = 0.3,
        num_lines: int = 6,
        flash_radius: float = 0.9,
        line_stroke_width: int = 2,
        color: str = WHITE,
        time_width: float = 1,
        run_time: float = 1.0,
        **kwargs,
    ) -> None:
        self.point = point.get_center()
        self.color = color
        self.line_length = line_length
        self.num_lines = num_lines
        self.flash_radius = flash_radius
        self.line_stroke_width = line_stroke_width
        self.run_time = run_time
        self.time_width = time_width
        self.animation_config = kwargs
        self.start_angle = start_angle
        self.end_angle = end_angle

        self.lines = self.create_lines()
        animations = self.create_line_anims()
        super().__init__(*animations, group=self.lines)

    def create_lines(self) -> VGroup:
        lines = VGroup()
        for angle in np.arange(
            self.start_angle,
            self.end_angle + ((self.end_angle - self.start_angle) / self.num_lines) / 2,
            (self.end_angle - self.start_angle) / self.num_lines,
        ):
            line = Line(self.point, self.point + self.line_length * RIGHT)
            line.shift((self.flash_radius) * RIGHT)
            line.rotate(angle, about_point=self.point)
            lines.add(line)
        lines.set_color(self.color)
        lines.set_stroke(width=self.line_stroke_width)
        return lines

    def create_line_anims(self) -> Iterable["ShowPassingFlash"]:
        return [
            ShowPassingFlash(
                line,
                time_width=self.time_width,
                run_time=self.run_time,
                **self.animation_config,
            )
            for line in self.lines
        ]


class Tile(VMobject):
    TEXT_SCALE = 0.6
    TEXT_OFFSET = 1 / 3.35

    def __str__(self):
        return f"Tile({self.colors})"

    __repr__ = __str__

    def __init__(self, colors, size=1):
        colors = list(map(str, colors))

        super().__init__()

        self.border = Square(size, color=WHITE)
        self.add(self.border)

        self.size = size

        self.colors = colors

        self.cross = VGroup()
        self.cross.add(
            Line(
                start=(UP + RIGHT) * self.size / 2,
                end=(DOWN + LEFT) * self.size / 2,
                stroke_width=1,
            )
        )
        self.cross.add(
            Line(
                end=(DOWN + RIGHT) * self.size / 2,
                start=(UP + LEFT) * self.size / 2,
                stroke_width=1,
            )
        )

        self.add(self.cross)

        self.color_objects = VGroup()
        for color, direction in zip(colors, DIRECTIONS):
            self.set_color_in_direction(color, direction, new=True)

        self.add_to_back(self.color_objects)

    def set_color_in_direction(self, color, direction, new=False):
        for i, d in enumerate(DIRECTIONS):
            if (direction == d).all():
                break

        self.colors[i] = color

        triangle = Polygon(
            np.array([self.size / 2 + self.get_x(), self.size / 2 + self.get_y(), 0]),
            np.array([self.size / 2 + self.get_x(), -self.size / 2 + self.get_y(), 0]),
            [self.get_x(), self.get_y(), 0],
            stroke_width=1,
            color=WHITE,
        ).rotate(PI / 2 * i, about_point=([self.get_x(), self.get_y(), 0]))

        if is_hex_color(color):
            triangle.set_fill(color, 1)

            if new:
                self.color_objects.add(triangle)
            else:
                self.color_objects[i] = triangle
        else:
            text = (
                Tex(color)
                .scale(Tile.TEXT_SCALE * self.size)
                .shift(direction * self.size * Tile.TEXT_OFFSET)
            )

            if new:
                self.color_objects.add(text)
            else:
                self.color_objects[i] = text

    def get_color_in_direction(self, direction):
        return get_item_by_direction(self.colors, direction)

    def get_color_object_in_direction(self, direction):
        return get_item_by_direction(self.color_objects, direction)

    def animateWrite(self):
        return AnimationGroup(
            Write(self.cross),
            AnimationGroup(
                Write(self.get_color_object_in_direction(LEFT)),
                Write(self.get_color_object_in_direction(UP)),
                Write(self.get_color_object_in_direction(RIGHT)),
                Write(self.get_color_object_in_direction(DOWN)),
            ),
            Write(self.border),
            lag_ratio=0.2,
        )


class Wall(VMobject):
    def __init__(self, colors, input=None, width=3, height=5, size=1):
        super().__init__()

        colors = list(map(str, colors))

        # input overwrites the width
        if input is not None:
            width = len(input)

        self.input = input

        width *= size
        height *= size

        self.border = Rectangle(width=width, height=height)

        self.size = size

        self.tiles = VGroup()
        self.add(self.tiles)

        self.tile_position_dictionary = {}

        self.add(self.border)

        self.colors = colors

        self.color_objects = VGroup()
        self.color_object_characters = []

        self.w = width
        self.h = height

        for color, direction in zip(colors, DIRECTIONS):
            self.set_color_in_direction(color, direction, new=True)

        self.add(self.color_objects)

    def set_color_in_direction(self, color, direction, new=False):
        for i, d in enumerate(DIRECTIONS):
            if (direction == d).all():
                break

        c = 0.4  # outer offset
        d = 0  # inner offset

        # yeah, not pretty
        # I was tired and didn't want to think
        if (direction == UP).all():
            pos = [
                np.array([self.w / 2, self.h / 2 + d, 0]),
                np.array([self.w / 2 - c, self.h / 2 + c, 0]),
                np.array([-self.w / 2 + c, self.h / 2 + c, 0]),
                np.array([-self.w / 2, self.h / 2 + d, 0]),
            ]
        if (direction == DOWN).all():
            pos = [
                np.array([self.w / 2, -self.h / 2 - d, 0]),
                np.array([self.w / 2 - c, -self.h / 2 - c, 0]),
                np.array([-self.w / 2 + c, -self.h / 2 - c, 0]),
                np.array([-self.w / 2, -self.h / 2 - d, 0]),
            ]
        if (direction == LEFT).all():
            pos = [
                np.array([-self.w / 2 - d, self.h / 2, 0]),
                np.array([-self.w / 2 - c, self.h / 2 - c, 0]),
                np.array([-self.w / 2 - c, -self.h / 2 + c, 0]),
                np.array([-self.w / 2 - d, -self.h / 2, 0]),
            ]
        if (direction == RIGHT).all():
            pos = [
                np.array([self.w / 2 + d, self.h / 2, 0]),
                np.array([self.w / 2 + c, self.h / 2 - c, 0]),
                np.array([self.w / 2 + c, -self.h / 2 + c, 0]),
                np.array([self.w / 2 + d, -self.h / 2, 0]),
            ]

        if (direction == UP).all() and self.input is not None:
            g = VGroup()

            self.input_colors = []
            self.input_lines = []
            self.color_object_characters.append([])

            for i in range(len(self.input) + 1):
                c = (0.25 if i in (0, len(self.input)) else 0.5) * self.size
                line = Line(
                    start=[-self.w / 2 + i * self.size, self.h / 2, 0],
                    end=[-self.w / 2 + i * self.size, self.h / 2 + c, 0],
                )

                g.add(line)
                self.input_lines.append(line)

                if i < len(self.input):
                    p = [-self.w / 2 + (i + 0.5) * self.size, self.h / 2, 0]

                    text = (
                        Tex(self.input[i])
                        .scale(Tile.TEXT_SCALE * self.size)
                        .move_to(p)
                        .align_to(p, DOWN)
                        .shift(UP * Tile.TEXT_OFFSET / 2)
                    )

                    self.input_colors.append(text)
                    self.color_object_characters[-1].append(text)

                    g.add(text)

            if new:
                self.color_objects.add(g)
            else:
                self.color_objects[i] = g
        else:
            g = VGroup()

            side = Polygon(*pos).set_stroke(WHITE)
            if is_hex_color(color):
                g.add(side.set_fill(color, 1))

                if new:
                    self.color_object_characters.append(None)
                else:
                    self.color_object_characters[i] = None
            else:
                g.add(side)

                text = Tex(color).scale(Tile.TEXT_SCALE * self.size).move_to(side)

                g.add(text)

                if new:
                    self.color_object_characters.append(text)
                else:
                    self.color_object_characters[i] = text
            if new:
                self.color_objects.add(g)
            else:
                self.color_objects[i] = g

    def to_positive_coordinates(self, x, y):
        """Done so we can use -1."""
        return x % self.w, y % self.h

    def get_tile_position(self, x, y):
        x, y = self.to_positive_coordinates(x, y)

        return (
            Square(self.size)
            .align_to(self.border, UP + LEFT)
            .shift([x * self.size, -y * self.size, 0])
            .get_center()
        )

    def add_tiles(self, tiles, positions, **kwargs):
        for t, p in zip(tiles, positions):
            self.add_tile(t, *p, **kwargs)

    def add_tile(self, tile, x, y, copy=False):
        x, y = self.to_positive_coordinates(x, y)

        if copy:
            tile = tile.copy()

        tile.move_to(self.get_tile_position(x, y))

        self.tiles.add(tile)

        # TODO: sort by tile position dictionary!

        self.tile_position_dictionary[(x, y)] = tile

        return tile

    def get_tile(self, x, y):
        x, y = self.to_positive_coordinates(x, y)

        return self.tile_position_dictionary[(x, y)]

    def remove_tile(self, tile):
        self.tiles.remove(tile)

    def get_color_object_in_direction(self, direction):
        return get_item_by_direction(self.color_objects, direction)

    def get_color_in_direction(self, direction):
        if (direction == UP).all() and self.input is not None:
            return self.input
        else:
            return get_item_by_direction(self.colors, direction)

    def get_color_object_characters_in_direction(self, direction):
        return get_item_by_direction(self.color_object_characters, direction)

    def animateWrite(self):
        return AnimationGroup(
            AnimationGroup(*[t.animateWrite() for t in self.tiles], lag_ratio=0.1),
            Write(self.border),
            AnimationGroup(
                Write(self.get_color_object_in_direction(LEFT)),
                Write(self.get_color_object_in_direction(UP))
                if self.input is None
                else AnimationGroup(
                    AnimationGroup(
                        *[Write(c) for c in self.input_colors], lag_ratio=0.04
                    ),
                    AnimationGroup(
                        *[FadeIn(l) for l in self.input_lines], lag_ratio=0.04
                    ),
                    lag_ratio=0.3,
                ),
                Write(self.get_color_object_in_direction(RIGHT)),
                Write(self.get_color_object_in_direction(DOWN)),
            ),
            lag_ratio=0.2,
        )

    def animateFillFlash(self):
        c = PI / 6
        return [
            PartialFlash(
                Dot().next_to(self, LEFT).shift(RIGHT * 0.8),
                start_angle=PI / 2 + c,
                end_angle=(PI / 2) * 3 - c,
            ),
            PartialFlash(
                Dot().next_to(self, RIGHT).shift(LEFT * 0.8),
                start_angle=-PI / 2 + c,
                end_angle=PI / 2 - c,
            ),
        ]


class TileSet(VMobject):
    def __init__(self, *tiles, rows=1):
        super().__init__()

        self.tiles = VGroup(*tiles)
        self.tiles.arrange_in_grid(rows=rows, buff=0.6)

        self.commas = VGroup()

        n = len(tiles)
        for i in range(n - 1):
            self.commas.add(
                Tex("\Large $,$")
                .next_to(self.tiles[i], DOWN + RIGHT, buff=0)
                .shift(UP * 0.07 + RIGHT * 0.1)
            )

        brace_offset = -0.25
        self.braces = VGroup(
            BraceBetweenPoints(
                Point().next_to(self.tiles[0], UP + LEFT).get_center(),
                Point().next_to(self.tiles[0], DOWN + LEFT).get_center(),
                direction=LEFT,
            ).shift(LEFT * brace_offset),
            BraceBetweenPoints(
                Point().next_to(self.tiles[-1], UP + RIGHT).get_center(),
                Point().next_to(self.tiles[-1], DOWN + RIGHT).get_center(),
                direction=RIGHT,
            ).shift(RIGHT * brace_offset),
        )

        self.add(self.tiles)
        self.add(self.commas)
        self.add(self.braces)

    def animateWrite(self):
        return AnimationGroup(
            AnimationGroup(*[t.animateWrite() for t in self.tiles], lag_ratio=0.1),
            Write(self.commas),
            Write(self.braces),
            lag_ratio=0.2,
        )

    def __getitem__(self, i):
        return self.tiles[i]

    def __len__(self):
        return len(self.tiles)

    def __iter__(self):
        return iter(self.tiles)


def IndicateColorCharacter(char):
    return Indicate(char, color=YELLOW, scale=INDICATE_SCALE)


def find_tiling_recursive(i, j, tileset: List[Tile], wallarray, w, h):
    def at(x, y):
        return wallarray[y + 1][x + 1]

    def set(x, y, tile):
        wallarray[y + 1][x + 1] = tile

    # if we're past (on the very right tile)
    if i == w:
        # check if the tile on the left is ok
        if at(i - 1, j).get_color_in_direction(RIGHT) != at(
            i, j
        ).get_color_in_direction(LEFT):
            return

        if j == h - 1:
            return wallarray

        i = 0
        j += 1

    for tile in tileset.tiles:
        if at(i, j - 1).get_color_in_direction(DOWN) != tile.get_color_in_direction(UP):
            continue

        if at(i - 1, j).get_color_in_direction(RIGHT) != tile.get_color_in_direction(
            LEFT
        ):
            continue

        # if we're last row
        if j == h - 1:
            if at(i, j + 1).get_color_in_direction(UP) != tile.get_color_in_direction(
                DOWN
            ):
                continue

        set(i, j, tile)
        result = find_tiling_recursive(i + 1, j, tileset, wallarray, w, h)
        if result is not None:
            return result
        set(i, j, None)


def find_tiling(tileset: List[Tile], wall: Wall, max_height=1):
    """Find if there exists a tiling of maximal height for a given wall."""
    w = wall.w
    for h in range(1, max_height + 1):
        wallarray = [[None] * (w + 2) for _ in range(h + 2)]

        for i in range(1, w + 1):
            wallarray[0][i] = Tile([None, None, None, wall.input[i - 1]])

        for i in range(1, w + 1):
            wallarray[-1][i] = Tile(
                [None, wall.get_color_in_direction(DOWN), None, None]
            )

        for i in range(1, h + 1):
            wallarray[i][-1] = Tile(
                [None, None, wall.get_color_in_direction(RIGHT), None]
            )

        for i in range(1, h + 1):
            wallarray[i][0] = Tile(
                [wall.get_color_in_direction(LEFT), None, None, None]
            )

        result = find_tiling_recursive(0, 0, tileset, wallarray, w, h)

        if result is not None:
            wall = Wall(wall.colors, wall.input, height=h)

            for x in range(w):
                for y in range(h):
                    wall.add_tile(result[y + 1][x + 1], x, y, copy=True)

            return wall


def animate_tile_pasting(tile, wall, positions, speed=0.07, run_time=1.2):
    def DelayedTransform(x, y, t):
        return Transform(
            x,
            y,
            run_time=run_time + t,
            rate_func=lambda a: smooth(
                a if t == 0 else (0 if a < t else (a - t) / (1 - t))
            ),
        )

    n = len(positions)

    from_tiles = [tile.copy() for _ in range(n)]
    to_tiles = [
        tile.copy().move_to(wall.get_tile_position(*position)) for position in positions
    ]

    return (
        [
            DelayedTransform(from_tiles[i], to_tiles[i], speed * (n - i - 1))
            for i in range(n)
        ],
        from_tiles,
        positions,
    )


class WriteReverse(Write):
    """A special write for a tile and wall (since we want the animation to be reversed)."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, reverse=True)


examples = {
    "even_size": (
        Wall([BLACK, None, BLACK, BLACK], height=1, input="111111"),
        TileSet(
            Tile([PALETTE[2], 1, PALETTE[1], PALETTE[0]]),
            Tile([PALETTE[1], 1, PALETTE[2], PALETTE[0]]),
        ),
    ),
    "divby3": (
        Wall([0, None, 0, PALETTE[0]], height=1, input="10110111"),
        TileSet(
            Tile([0, 0, 0, PALETTE[0]]),
            Tile([1, 0, 1, PALETTE[0]]),
            Tile([2, 0, 2, PALETTE[0]]),
            Tile([1, 1, 0, PALETTE[0]]),
            Tile([2, 1, 1, PALETTE[0]]),
            Tile([0, 1, 2, PALETTE[0]]),
        ),
    ),
    "parentheses": (
        Wall([PALETTE[3], None, PALETTE[3], PALETTE[3]], input="(()())()", height=2),
        TileSet(
            Tile([PALETTE[2], "(", PALETTE[3], PALETTE[3]]),
            Tile([PALETTE[3], ")", PALETTE[2], PALETTE[3]]),
            Tile([PALETTE[3], "(", PALETTE[3], PALETTE[1]]),
            Tile([PALETTE[3], PALETTE[1], PALETTE[3], PALETTE[1]]),
            Tile([PALETTE[1], PALETTE[3], PALETTE[1], PALETTE[3]]),
            Tile([PALETTE[1], PALETTE[1], PALETTE[3], PALETTE[3]]),
            Tile([PALETTE[3], PALETTE[0], PALETTE[1], PALETTE[3]]),
            Tile([PALETTE[3], PALETTE[0], PALETTE[3], PALETTE[0]]),
            Tile([PALETTE[3], ")", PALETTE[3], PALETTE[0]]),
            Tile([PALETTE[3], PALETTE[3], PALETTE[3], PALETTE[3]]),
        ),
    ),
    "parentheses_log": (
        Wall([PALETTE[1], None, PALETTE[0], BLACK], input="(((())))"),
        TileSet(
            Tile([1, "(", PALETTE[0], BLACK]),
            Tile([BLACK, BLACK, PALETTE[0], BLACK]),
            Tile([0, "(", 1, "+"]),
            Tile([1, "(", 0, BLACK]),
            Tile([1, "+", BLACK, BLACK]),
            Tile([1, BLACK, 1, BLACK]),
            Tile([0, BLACK, 0, BLACK]),
            Tile([BLACK, BLACK, 0, BLACK]),
            Tile([0, ")", 1, BLACK]),
            Tile([1, ")", 0, "-"]),
            Tile([PALETTE[1], ")", 1, BLACK]),
            Tile([0, "-", 1, BLACK]),
            Tile([1, "-", 0, "-"]),
            Tile([BLACK, "-", 1, BLACK]),
            Tile([PALETTE[1], BLACK, BLACK, BLACK]),
            Tile([PALETTE[1], BLACK, 0, BLACK]),
            Tile([BLACK, BLACK, BLACK, BLACK]),
        ),
    ),
    "palindrome": (
        Wall([PALETTE[0], None, PALETTE[1], BLACK], input="10100101"),
        TileSet(
            Tile([RED, "1", PALETTE[1], BLACK]),
            Tile([PALETTE[0], "1", RED, BLACK]),
            Tile([RED, "1", RED, "1"]),
            Tile([RED, "0", RED, "0"]),
            Tile([PALETTE[0], BLACK, PALETTE[0], BLACK]),
            Tile([PALETTE[1], BLACK, PALETTE[1], BLACK]),
            Tile([BLUE, "0", PALETTE[1], BLACK]),
            Tile([PALETTE[0], "0", BLUE, BLACK]),
            Tile([BLUE, "1", BLUE, "1"]),
            Tile([BLUE, "0", BLUE, "0"]),
            Tile([PALETTE[0], "0", PALETTE[1], BLACK]),
            Tile([PALETTE[0], "1", PALETTE[1], BLACK]),
        ),
    ),
}


class FadeOutDirection(Transform):
    def __init__(
        self,
        mobject,
        dir,
        rate_func=smooth,
        move_factor=0.35,
        run_time=1,
        **kwargs,
    ) -> None:
        self.move_factor = move_factor
        self.obj = mobject
        self.dir = dir
        super().__init__(mobject, rate_func=rate_func, run_time=run_time, **kwargs)

    def create_target(self) -> "Mobject":
        target = self.obj.copy().shift(self.dir * self.move_factor).set_opacity(0)
        return target


def FadeOutUp(obj, *args, **kwargs):
    return FadeOutDirection(obj, UP, *args, **kwargs)


def FadeOutDown(obj, *args, **kwargs):
    return FadeOutDirection(obj, DOWN, *args, **kwargs)


class FadeInDirection(Transform):
    def __init__(
        self,
        mobject,
        dir,
        rate_func=lambda x: smooth(1 - x),
        move_factor=0.35,
        run_time=1,
        **kwargs,
    ) -> None:
        self.move_factor = move_factor
        self.obj = mobject
        self.dir = -dir
        super().__init__(mobject, rate_func=rate_func, run_time=run_time, **kwargs)

    def create_target(self) -> "Mobject":
        target = self.obj.copy().shift(self.dir * self.move_factor).set_opacity(0)
        return target


def FadeInUp(obj, *args, **kwargs):
    return FadeInDirection(obj, UP, *args, **kwargs)


def FadeInDown(obj, *args, **kwargs):
    return FadeInDirection(obj, DOWN, *args, **kwargs)


class HighlightedTex(Tex):
    def __init__(self, text, sep="|", color=YELLOW):
        super().__init__(*[s for s in text.split(sep) if len(s) != 0])

        c = 0
        for i in range(0 if text[0] == sep else 1, len(self), 2):
            if type(color) is str:
                self[i].set_color(color)
            else:
                self[i].set_color(color[c])
                c += 1


def WriteText(text):
    return Write(
        text,
        run_time=get_text_speed(
            text.text if isinstance(text, Text) else text.tex_string
        ),
    )


class BumpUp(Transform):
    def __init__(
        self,
        mobject: "Mobject",
        move_factor: float = 0.35,
        rate_func=there_and_back,
        **kwargs,
    ) -> None:
        self.move_factor = move_factor
        self.obj = mobject
        super().__init__(mobject, rate_func=rate_func, **kwargs)

    def create_target(self) -> "Mobject":
        target = self.obj.copy().shift(UP * self.move_factor)
        return target


class Motivation(MovingCameraScene):
    def construct(self):
        p1 = SVGMobject("assets/pillar.svg").scale(2.8).shift(LEFT * 4.8)
        p2 = SVGMobject("assets/pillar.svg").scale(2.8).shift(RIGHT * 4.8)

        ft = Text("Eureka!", font="Gelio Pasteli").scale(2)

        archimedes = (
            Text("– Archimedes", font="Gelio Pasteli")
            .scale(0.7)
            .next_to(ft, DOWN)
            .align_to(ft, RIGHT)
        )

        g = VGroup(ft, archimedes).move_to(ORIGIN)

        text_write_duration = 1.6

        self.play(
            FadeInUp(p1),
            FadeInUp(p2),
        )

        self.play(
            AnimationGroup(
                Write(ft, run_time=text_write_duration),
                Write(archimedes, run_time=text_write_duration),
                lag_ratio=0.8,
            )
        )

        offset = 1.2

        ft2 = Text("Bathroom tiles!").scale(1.0).shift(DOWN * offset)
        tom = Text("- Tom").scale(0.6).next_to(ft2, DOWN).align_to(ft2, RIGHT)

        g2 = VGroup(ft2, tom)
        g2.move_to(ORIGIN).shift(DOWN * offset)

        laptop = SVGMobject("assets/laptop.svg").shift(DOWN * 1.5)
        water = (
            SVGMobject("assets/water.svg")
            .scale(0.35)
            .next_to(laptop, UP + LEFT)
            .shift(RIGHT * 0.75 + DOWN * 0.73)
        )
        bolt = (
            SVGMobject("assets/bolt.svg").scale(0.30).move_to(laptop).shift(UP * 0.37)
        )

        self.play(
            g.animate.shift(UP * offset),
            FadeInUp(laptop),
        )

        self.play(
            AnimationGroup(
                FadeInUp(water),
                Write(bolt),
                lag_ratio=0.5,
            )
        )

        self.play(
            AnimationGroup(
                FadeOutUp(VGroup(water, bolt, laptop)),
                AnimationGroup(
                    Write(ft2, run_time=text_write_duration),
                    Write(tom, run_time=text_write_duration / 3),
                    lag_ratio=0.8,
                ),
                lag_ratio=1,
            )
        )

        # bug?
        self.add(ft2)
        self.add(tom)

        w = 9
        h = 3

        wall = Wall(PALETTE, width=w, height=h)

        bl = BraceBetweenPoints([-w / 2, h / 2, 0], [-w / 2, -h / 2, 0])
        blt = Tex("\\footnotesize h").next_to(bl, LEFT * 0.5)

        bu = BraceBetweenPoints(
            [-w / 2, h / 2, 0], [w / 2, h / 2, 0], direction=UP
        ).scale([-1, 1, 0])
        but = Tex("\\footnotesize w").next_to(bu, UP * 0.5)

        self.play(
            AnimationGroup(
                AnimationGroup(*map(FadeOutUp, self.mobjects)),
                Write(wall.border),
                lag_ratio=0.8,
            )
        )

        self.play(Write(bu), Write(but))
        self.play(Write(bl), Write(blt))

        seed(3)
        tiles = [
            [Tile([choice(PALETTE) for _ in range(4)]) for _ in range(w)]
            for _ in range(h)
        ]

        for i in range(w):
            for j in range(h):
                wall.add_tile(tiles[j][i], i, j)

        self.play(
            AnimationGroup(*[FadeIn(t.border) for t in wall.tiles], lag_ratio=0.01)
        )

        tile = wall.get_tile(w // 2, h // 2)
        zoom_ratio = 0.2

        self.play(
            self.camera.frame.animate.scale(zoom_ratio).move_to(tile),
            rate_func=smooth,
            run_time=1.5,
        )

        self.play(AnimationGroup(Write(tile.cross), lag_ratio=0.3))

        self.bring_to_front(tile.border)

        for c in tile.color_objects:
            self.bring_to_back(c)
        self.bring_to_front(tile)

        self.play(
            *[
                FadeIn(tile.get_color_object_in_direction(d))
                for d in [LEFT, UP, RIGHT, DOWN]
            ],
            tile.border.animate.set_color(WHITE),
        )

        for t in wall.tiles:
            for c in t.color_objects:
                self.bring_to_back(c)
            self.bring_to_front(t)

        self.play(
            AnimationGroup(
                self.camera.frame.animate.scale(1 / zoom_ratio).move_to(ORIGIN),
                rate_func=smooth,
                run_time=1.5,
            ),
            *[t.border.animate.set_color(WHITE) for t in wall.tiles if t is not tile],
            *[Write(t.cross) for t in wall.tiles if t is not tile],
            *[Write(t.color_objects) for t in wall.tiles if t is not tile],
        )

        # color rows + columns
        changes = {}
        seed(1)
        for count, (i1, i2) in enumerate(
            zip((range(w - 1), range(w)), (range(h), range(h - 1)))
        ):
            for i in i1:
                for j in i2:
                    p1, p2 = (i, j), (i + 1, j) if not count else (i, j + 1)
                    d1, d2 = (RIGHT, LEFT) if not count else (DOWN, UP)

                    c1, c2 = tiles[p1[1]][p1[0]].get_color_in_direction(d1), tiles[
                        p2[1]
                    ][p2[0]].get_color_in_direction(d2)
                    new_color = choice([c1, c2])

                    if p1 not in changes:
                        changes[p1] = tiles[p1[1]][p1[0]].animate
                    changes[p1].set_color_in_direction(new_color, d1)

                    if p2 not in changes:
                        changes[p2] = tiles[p2[1]][p2[0]].animate
                    changes[p2].set_color_in_direction(new_color, d2)
        self.play(*changes.values())
        self.play(
            AnimationGroup(
                FadeOut(VGroup(bl, blt, bu, but)),
                Write(wall.color_objects),
                lag_ratio=0.6,
            )
        )

        changes = {}

        for count, iterable in enumerate([range(w), range(h)]):
            for x in iterable:
                for index in range(2):
                    y = ((0, h - 1) if not count else (0, w - 1))[index]
                    direction = ((UP, DOWN) if not count else (LEFT, RIGHT))[index]

                    if count:
                        i, j = y, x
                    else:
                        i, j = x, y

                    if tiles[j][i].get_color_in_direction(
                        direction
                    ) != wall.get_color_in_direction(direction):

                        if (i, j) not in changes:
                            changes[(i, j)] = tiles[j][i].animate
                        changes[(i, j)].set_color_in_direction(
                            wall.get_color_in_direction(direction), direction
                        )

        self.play(*changes.values())

        tiles = [
            Tile(
                [
                    REDUCED_PALETTE[1],
                    REDUCED_PALETTE[1],
                    REDUCED_PALETTE[0],
                    REDUCED_PALETTE[1],
                ]
            ),
            Tile(
                [
                    REDUCED_PALETTE[1],
                    REDUCED_PALETTE[1],
                    REDUCED_PALETTE[1],
                    REDUCED_PALETTE[1],
                ]
            ),
            Tile(
                [
                    REDUCED_PALETTE[0],
                    REDUCED_PALETTE[1],
                    REDUCED_PALETTE[1],
                    REDUCED_PALETTE[1],
                ]
            ),
        ]

        tileset = TileSet(*tiles)

        self.play(
            AnimationGroup(
                *[FadeOut(t) for t in wall.tiles], lag_ratio=0.01, run_time=1
            )
        )

        for t in wall.tiles:
            wall.remove_tile(t)

        wall.generate_target()
        wall.target.shift(DOWN * 1.1)
        wall.target.get_color_object_in_direction(LEFT).set_fill(REDUCED_PALETTE[0])
        wall.target.get_color_object_in_direction(DOWN).set_fill(REDUCED_PALETTE[1])
        wall.target.get_color_object_in_direction(RIGHT).set_fill(REDUCED_PALETTE[0])

        tileset.next_to(wall.target, UP).shift(UP * 0.5)

        self.play(
            AnimationGroup(MoveToTarget(wall), tileset.animateWrite(), lag_ratio=0.8),
        )

        question = Tex("?").scale(QUESTION_MARK_SCALE).move_to(wall)

        self.play(Write(question))
        self.play(FadeOutUp(question))

        animations1, tiles1, positions1 = animate_tile_pasting(
            tiles[-1], wall, [(-1, i) for i in range(h)]
        )
        animations2, tiles2, positions2 = animate_tile_pasting(
            tiles[0], wall, [(0, i) for i in range(h)]
        )

        self.play(*animations1, *animations2)

        wall.add_tiles(tiles1, positions1)
        wall.add_tiles(tiles2, positions2)

        from_tile_wrong = tiles[-1].copy()

        cross_size = 0.6

        cross = VGroup()
        r1 = Line(
            start=(UP + LEFT) * cross_size,
            end=(DOWN + RIGHT) * cross_size,
            stroke_width=6,
        ).set_stroke("#8b0000")
        r2 = Line(
            start=(RIGHT + UP) * cross_size,
            end=(DOWN + LEFT) * cross_size,
            stroke_width=6,
        ).set_stroke("#8b0000")

        cross.add(r1)
        cross.add(r2)

        self.play(
            from_tile_wrong.animate.move_to(wall.get_tile_position(4, 0)).rotate(
                -PI / 2
            )
        )

        cross.move_to(from_tile_wrong)

        self.play(Write(cross, run_time=0.5))
        self.play(FadeOutUp(from_tile_wrong), FadeOutUp(cross))

        animations, tiles, positions = animate_tile_pasting(
            tiles[1],
            wall,
            [(i, j) for i in reversed(range(1, w - 1)) for j in reversed(range(h))],
            speed=0.03,
        )

        self.play(*animations)

        wall.add_tiles(tiles, positions)

        self.play(
            wall.get_color_object_in_direction(UP).animate.set_fill(REDUCED_PALETTE[0])
        )

        self.play(*[FadeOut(wall.get_tile(i, 0)) for i in range(wall.w)])
        for i in range(wall.w):
            wall.remove_tile(wall.get_tile(i, 0))

        self.play(FadeOut(wall), FadeOut(tileset))


TASK_OFFSET = 0.6 * UP
WALL_OFFSET = 1.7 * DOWN
TILESET_OFFSET = UP * 0.7


class ProgrammingModel(Scene):
    @fade
    def construct(self):
        title = Tex("\Large Programming model")

        self.play(FadeInUp(title))
        self.play(title.animate.shift(UP * 2.5))

        text = [
            (Tex("Input:"), HighlightedTex("|colors| on the |top side| of the wall")),
            (
                Tex("Program:"),
                HighlightedTex(
                    "finite set of |tile types| and the |remaining wall colors|"
                ),
            ),
            (
                Tex("Output:"),
                HighlightedTex(
                    "|accept| if there exists valid tiling, else |reject|",
                    color=[GREEN, RED],
                ),
            ),
        ]

        # align text to a grid
        text_scale = 0.85
        for i in range(len(text)):
            text[i][0].scale(text_scale).next_to(text[i - 1][0], DOWN).align_to(
                text[i - 1][0], RIGHT
            )
            text[i][1].scale(text_scale).next_to(text[i][0], RIGHT)

        # and move it
        g = VGroup()
        for i in range(len(text)):
            g.add(text[i][0])
            g.add(text[i][1])
        g.move_to(ORIGIN).shift(UP * 0.7)

        wall, tileset = examples["even_size"]
        wall = wall.shift(DOWN * 2)

        self.play(WriteText(text[0][0]))

        self.play(WriteText(text[0][1]), wall.animateWrite())

        tileset.next_to(wall, RIGHT, buff=1)

        g = VGroup(tileset, wall)

        self.play(wall.animate.set_x(wall.get_x() - g.get_x()))

        tileset.next_to(wall, RIGHT, buff=1)

        self.play(WriteText(text[1][0]))

        self.play(
            WriteText(text[1][1]),
            AnimationGroup(
                tileset.animateWrite(),
                AnimationGroup(
                    wall.get_color_object_in_direction(LEFT).animate.set_fill(
                        PALETTE[1]
                    ),
                    wall.get_color_object_in_direction(DOWN).animate.set_fill(
                        PALETTE[0]
                    ),
                    wall.get_color_object_in_direction(RIGHT).animate.set_fill(
                        PALETTE[1]
                    ),
                ),
                lag_ratio=1,
            ),
        )

        self.play(WriteText(text[2][0]))

        self.play(WriteText(text[2][1]))

        self.play(
            AnimationGroup(
                AnimationGroup(
                    FadeOutUp(title),
                    *[
                        FadeOutUp(text[i][j])
                        for i in range(len(text))
                        for j in range(len(text[0]))
                    ],
                ),
                AnimationGroup(
                    tileset.animate.move_to(ORIGIN).shift(TILESET_OFFSET),
                    wall.animate.move_to(ORIGIN).shift(WALL_OFFSET),
                ),
                lag_ratio=0.0,
            ),
            run_time=1.5,
        )

        task = (
            HighlightedTex(
                r"{\bf Task:} |accept| input \(\Leftrightarrow\) it has even length",
                color=GREEN,
            )
            .next_to(tileset, UP)
            .shift(TASK_OFFSET)
        )

        self.play(FadeInUp(task))

        for i in range(wall.w // 2):
            animations, tiles, positions = animate_tile_pasting(
                tileset[i % 2], wall, [(i, 0)]
            )
            animations2, tiles2, positions2 = animate_tile_pasting(
                tileset[(i + 1) % 2], wall, [(wall.w - i - 1, 0)]
            )
            self.play(*animations, *animations2)

            if i != wall.w // 2 - 1:
                self.play(
                    Swap(tileset[0], tileset[1], path_arc=160 * DEGREES, run_time=1.25)
                )

            wall.add_tiles(tiles, positions)
            wall.add_tiles(tiles2, positions2)

        self.play(*wall.animateFillFlash())

        wall_old = wall
        tileset_old = tileset
        task_old = task

        wall, tileset = examples["divby3"]
        tileset.move_to(ORIGIN).shift(TILESET_OFFSET)
        wall.move_to(ORIGIN).shift(WALL_OFFSET)

        task = (
            HighlightedTex(
                r"{\bf Task:} |accept| input \(\Leftrightarrow\) \# of ones is divisible by 3",
                color=GREEN,
            )
            .next_to(tileset, UP)
            .shift(TASK_OFFSET)
        )

        # TODO: maybe edit this later
        self.play(
            AnimationGroup(
                AnimationGroup(
                    FadeOutUp(wall_old), FadeOutUp(tileset_old), FadeOutUp(task_old)
                ),
                AnimationGroup(FadeInUp(wall), FadeInUp(tileset), FadeInUp(task)),
                lag_ratio=0.6,
            )
        )

        nums = [
            Tex(str(wall.input[: i + 1].count("1")), color=NOTES_COLOR)
            .scale(NOTES_SCALE)
            .next_to(wall.get_color_object_characters_in_direction(UP)[i], UP)
            for i in range(len(wall.input))
        ]

        self.play(
            AnimationGroup(
                *[
                    BumpUp(
                        wall.get_color_object_characters_in_direction(UP)[i],
                        run_time=1.0,
                    )
                    for i in range(len(wall.input))
                    if wall.input[i] == "1"
                ],
                lag_ratio=0.08,
            )
        )

        nums = [
            Tex(str(wall.input[: i + 1].count("1")), color=NOTES_COLOR)
            .scale(NOTES_SCALE)
            .next_to(wall.get_color_object_characters_in_direction(UP)[i], UP)
            for i in range(len(wall.input))
        ]

        nums_lag = 0.3
        nums_run_time = 1.5

        self.play(
            AnimationGroup(
                *([FadeInUp(n) for n in nums]),
                lag_ratio=nums_lag,
                run_time=nums_run_time,
            ),
        )

        nums_transformed = [
            Tex(str(wall.input[: i + 1].count("1") % 3), color=NOTES_COLOR)
            .scale(NOTES_SCALE)
            .move_to(nums[i])
            for i in range(len(nums))
        ]

        self.play(
            AnimationGroup(
                *[
                    AnimationGroup(
                        FadeOutUp(a, move_factor=0.25), FadeInUp(b, move_factor=0.25)
                    )
                    for a, b in zip(nums[3:], nums_transformed[3:])
                ],
                lag_ratio=nums_lag,
                run_time=nums_run_time,
            )
        )

        bs = []

        brace_offset = 0.25
        for i, (text, start, end) in enumerate(
            [
                ("carry", tileset[0], tileset[2]),
                ("increment", tileset[3], tileset[5]),
            ]
        ):
            b = BraceBetweenPoints(
                Point().next_to(start, UP + LEFT, buff=0).get_center(),
                Point().next_to(end, UP + RIGHT, buff=0).get_center(),
                direction=UP,
                color=NOTES_COLOR,
            ).scale([-1, NOTES_SCALE, 1])

            bl = (
                Tex(text, color=NOTES_COLOR)
                .next_to(b, UP)
                .scale(NOTES_SCALE)
                .shift(DOWN * 0.1)
            )

            bs += [b, bl]

            self.play(
                FadeInUp(b),
                FadeInUp(bl)
                if i == 1
                else AnimationGroup(FadeInUp(bl), task.animate.shift(UP * 0.3)),
            )

            self.play(
                AnimationGroup(
                    *[
                        AnimationGroup(
                            IndicateColorCharacter(
                                t.get_color_object_in_direction(LEFT)
                            ),
                            IndicateColorCharacter(
                                t.get_color_object_in_direction(RIGHT)
                            ),
                            lag_ratio=0.1,
                        )
                        for t in tileset
                    ][i * 3 : (i + 1) * 3],
                    lag_ratio=0.65,
                )
            )

        for i, (tile, positions) in enumerate(
            [
                (3, [(0, 0)]),
                (1, [(1, 0)]),
                (4, [(2, 0)]),
                (5, [(3, 0)]),
                (0, [(4, 0)]),
                (3, [(5, 0)]),
                (4, [(6, 0)]),
                (5, [(7, 0)]),
            ]
        ):
            animations, tiles, positions = animate_tile_pasting(
                tileset[tile], wall, positions
            )

            self.play(*animations, run_time=1 - (i / wall.w) * 0.5)
            self.play(
                IndicateColorCharacter(tiles[0].get_color_object_in_direction(RIGHT)),
                IndicateColorCharacter((nums if i < 3 else nums_transformed)[i]),
                run_time=1 - (i / wall.w) * 0.5,
            )

            wall.add_tiles(tiles, positions)

        self.play(*wall.animateFillFlash())

        self.play(
            AnimationGroup(
                *[
                    IndicateColorCharacter(
                        wall.get_color_object_characters_in_direction(UP)[i]
                    )
                    for i in range(len(wall.input))
                    if wall.input[i] == "1"
                ],
                lag_ratio=0.08,
            )
        )

        self.play(
            FadeOutUp(wall),
            FadeOutUp(tileset),
            FadeOutUp(task),
            *[FadeOutUp(n) for n in nums + nums_transformed + bs],
        )


class TimeComplexity(Scene):
    def construct(self):
        title = Tex("\Large Time Complexity")

        self.play(FadeInUp(title))

        traditional = Tex("Traditional model")
        traditional_text = (
            Tex(
                "\parbox{15em}{Minimum number of instructions needed to compute the solution, based on the size of the input.}"
            )
            .scale(0.7)
            .next_to(traditional, DOWN)
            .shift(DOWN * 0.2)
        )

        for i, j in ((0, 7), (15, 27), (35, 42), (64, 80)):
            traditional_text[0][i:j].set_color(YELLOW)

        traditional_group = VGroup(traditional, traditional_text)
        traditional_group.move_to(ORIGIN).shift(LEFT * 3.2 + UP * 0.5)

        bathroom = Tex("Bathroom model")
        bathroom_text = (
            HighlightedTex(
                "\parbox{15em}{Minimum number of rows needed to accept the input, based on the size of the input.}"
            )
            .scale(0.7)
            .next_to(bathroom, DOWN)
            .shift(DOWN * 0.2)
        )

        for i, j in ((0, 7), (15, 19), (27, 33), (52, 73)):
            bathroom_text[0][i:j].set_color(YELLOW)

        bathroom_group = VGroup(bathroom, bathroom_text)
        bathroom_group.move_to(ORIGIN).shift(RIGHT * 3.2 + UP * 0.5)

        self.play(
            AnimationGroup(
                title.animate.shift(UP * 2.5),
                AnimationGroup(FadeInUp(traditional), FadeInUp(bathroom), run_time=0.8),
                lag_ratio=0.2,
            )
        )

        self.play(Write(traditional_text, run_time=3))

        traditional_examples = (
            Tex(
                r"""
                \begin{itemize}
                \itemsep0em
                \item {\bf Bubble sort:} \(\mathcal{O}(n^2)\)
                \item {\bf Binary search:} \(\mathcal{O}(\log n)\)
                \end{itemize}
                """
            )
            .scale(0.7)
            .next_to(traditional_text, DOWN)
            .shift(DOWN * 0.2)
        )

        bathroom_examples = (
            Tex(
                r"""
                \begin{itemize}
                \itemsep0em
                \item {\bf Even length:} \(\mathcal{O}(1)\)
                \item {\bf 3\(n\) ones in input:} \(\mathcal{O}(1)\)
                \end{itemize}
                """
            )
            .scale(0.7)
            .next_to(bathroom_text, DOWN)
            .shift(DOWN * 0.2)
        )

        n = 17
        self.play(FadeInUp(traditional_examples[0][0:n]))
        self.play(FadeInUp(traditional_examples[0][n:]))

        question = (
            Tex("?")
            .scale(QUESTION_MARK_SCALE)
            .move_to(VGroup(bathroom_text, *bathroom_examples))
        )

        self.play(Write(question))

        self.play(
            AnimationGroup(
                FadeOutDown(question),
                Write(bathroom_text, run_time=3),
                lag_ratio=0.3,
            )
        )

        n = 16
        self.play(
            AnimationGroup(
                FadeInUp(bathroom_examples[0][0:n]),
                FadeInUp(bathroom_examples[0][n:]),
                lag_ratio=0.1,
            )
        )


        self.play(
            *[
                FadeOutUp(c)
                for c in [
                    title,
                    bathroom,
                    traditional,
                    bathroom_text,
                    traditional_text,
                    bathroom_examples,
                    traditional_examples,
                ]
            ]
        )


class ParenthesesExample(Scene):
    def construct(self):
        self.next_section(skip_animations=True)

        task = HighlightedTex(
            r"{\bf Task:} |accept| input \(\Leftrightarrow\) parentheses are balanced",
            color=GREEN,
        )

        self.play(FadeInUp(task))

        parentheses = Tex("$(\ (\ )\ (\ )\ )\ (\ )$").next_to(task, DOWN).scale(2)

        self.play(
            AnimationGroup(
                task.animate.shift(UP),
                FadeInUp(parentheses),
            )
        )

        def BracketBetweenPoints(
            p1, p2, direction=UP, color=WHITE, width=0.06, height=0.22, **kwargs
        ):
            w = width
            h = height

            r1 = Rectangle(width=w, height=h).next_to(p1, direction, buff=0)
            r3 = Rectangle(width=w, height=h).next_to(p2, direction, buff=0)

            r2 = (
                Rectangle(width=(abs(p1[0] - p2[0]) + w), height=w)
                .align_to(r1, direction)
                .set_x((r1.get_x() + r3.get_x()) / 2)
            )

            return Union(r1, r2, r3, fill_color=color, fill_opacity=1, stroke_width=0)

        braces = [
            BracketBetweenPoints(
                Dot().next_to(parentheses[0][0], DOWN, buff=0.1).get_center(),
                Dot().next_to(parentheses[0][5], DOWN, buff=0.1).get_center(),
                direction=DOWN,
                height=0.43,
                color=GRAY,
            ).scale(0.95),
            BracketBetweenPoints(
                Dot().next_to(parentheses[0][1], DOWN, buff=0.1).get_center(),
                Dot().next_to(parentheses[0][2], DOWN, buff=0.1).get_center(),
                direction=DOWN,
                color=GRAY,
            ).scale(0.78),
            BracketBetweenPoints(
                Dot().next_to(parentheses[0][3], DOWN, buff=0.1).get_center(),
                Dot().next_to(parentheses[0][4], DOWN, buff=0.1).get_center(),
                direction=DOWN,
                color=GRAY,
            ).scale(0.78),
            BracketBetweenPoints(
                Dot().next_to(parentheses[0][6], DOWN, buff=0.1).get_center(),
                Dot().next_to(parentheses[0][7], DOWN, buff=0.1).get_center(),
                direction=DOWN,
                color=GRAY,
            ).scale(0.78),
        ]

        self.play(
            FadeInUp(braces[0], move_factor=0.1),
            FadeInUp(braces[1], move_factor=0.1),
            FadeInUp(braces[2], move_factor=0.1),
            FadeInUp(braces[3], move_factor=0.1),
            run_time=0.65,
        )

        wall, tileset = examples["parentheses"]
        tileset_scale = 0.7

        tileset.scale(tileset_scale)

        tileset.move_to(ORIGIN).shift(TILESET_OFFSET).shift(UP * 0.5)
        wall.move_to(ORIGIN).shift(WALL_OFFSET * 0.8)

        for i in range(len(wall.input)):
            wall.get_color_object_in_direction(UP).remove(
                wall.get_color_object_characters_in_direction(UP)[i]
            )

        self.play(
            AnimationGroup(
                AnimationGroup(
                    task.animate.next_to(tileset, UP).shift(TASK_OFFSET * 0.8),
                    AnimationGroup(
                        FadeOutUp(braces[0], move_factor=0.1),
                        FadeOutUp(braces[1], move_factor=0.1),
                        FadeOutUp(braces[2], move_factor=0.1),
                        FadeOutUp(braces[3], move_factor=0.1),
                        run_time=0.5,
                    ),
                    *[
                        Transform(
                            parentheses[0][i],
                            wall.get_color_object_characters_in_direction(UP)[i].copy(),
                        )
                        for i in range(len(wall.input))
                    ],
                    run_time=1,
                ),
                AnimationGroup(
                    FadeInUp(wall),
                    FadeInUp(tileset),
                    run_time=0.7,
                ),
                lag_ratio=0.3,
            )
        )

        tileset.scale(1 / tileset_scale)

        result_wall = find_tiling(tileset, wall, max_height=2)

        for i in range(wall.w):
            for j in range(wall.h):
                wall.add_tile(result_wall.get_tile(i, j), i, j, copy=True)

        tileset.scale(tileset_scale)

        self.play(
            AnimationGroup(*[t.animateWrite() for t in wall.tiles], lag_ratio=0.01)
        )

        self.play(*wall.animateFillFlash())

        for i in range(wall.w):
            for j in range(wall.h):
                wall.remove_tile(result_wall.get_tile(i, j))

        fade_coefficient = 0.8
        parentheses_coefficient = 0.085

        shift = 0.5

        def highlight_parentheses(indexes, prev_indexes=[[]]):
            if prev_indexes == [[]]:
                for i in range(wall.w):
                    parentheses[0][i].scale(INDICATE_SCALE).shift(
                        UP * parentheses_coefficient
                        + (ORIGIN if i in indexes else DOWN * shift)
                    )
                    parentheses[0][i].save_state()
                    parentheses[0][i].scale(1 / INDICATE_SCALE).shift(
                        DOWN * parentheses_coefficient
                        + (ORIGIN if i in indexes else UP * shift)
                    )

            for i in range(wall.w):
                if i in prev_indexes[0]:
                    parentheses[0][i].save_state()

            result = AnimationGroup(
                *[
                    (
                        parentheses[0][i].animate.restore()
                        if i in indexes and i not in prev_indexes[0]
                        else (
                            parentheses[0][i]
                            .animate.scale(1 / INDICATE_SCALE)
                            .shift(DOWN * parentheses_coefficient)
                        ).fade(fade_coefficient)
                        if i not in indexes and i in prev_indexes[0]
                        else parentheses[0][i].animate.fade(fade_coefficient)
                    )
                    for i in range(wall.w)
                ]
            )

            prev_indexes[0] = indexes

            return result

        def highlight_tiles(indexes, cache=[[[]]]):
            first = False
            if cache == [[[]]]:
                first = True
                cache[0] = [(i, j) for i in range(wall.w) for j in range(wall.h)]

            for i in range(wall.w):
                for j in range(wall.h):
                    if (i, j) in cache[0]:
                        if first:
                            wall.shift(ORIGIN if (i, j) in indexes else DOWN * shift)

                        wall.get_tile(i, j).save_state()

                        if first:
                            wall.shift(ORIGIN if (i, j) in indexes else UP * shift)

            result = AnimationGroup(
                *[
                    wall.get_tile(i, j).animate.fade(fade_coefficient)
                    if (i, j) not in indexes and (i, j) in cache[0]
                    else wall.get_tile(i, j).animate.restore()
                    if (i, j) in indexes
                    else wall.get_tile(i, j).animate.fade(0)
                    for i in range(wall.w)
                    for j in range(wall.h)
                ],
                run_time=0.75,
            )

            cache[0] = indexes

            return result

        self.next_section()

        self.play(highlight_parentheses([0, 5]))

        self.play(highlight_tiles([(0, 0), (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (5, 0)]))

        brace_offset = 0.25
        bs = []
        for i, (text, start, end) in enumerate(
            [
                ("single", tileset[0], tileset[1]),
                ("opening", tileset[2], tileset[2]), # TODO: here; combine opening and closing
                ("path creation", tileset[3], tileset[7]),
                ("closing", tileset[8], tileset[8]),
                ("fill", tileset[9], tileset[9]),
            ]
        ):
            b = BraceBetweenPoints(
                Point().next_to(start, UP + LEFT, buff=0).get_center(),
                Point().next_to(end, UP + RIGHT, buff=0).get_center(),
                direction=UP,
                color=NOTES_COLOR,
            ).scale([-1, NOTES_SCALE, 1])

            bl = (
                Tex(text, color=NOTES_COLOR)
                .next_to(b, UP)
                .scale(NOTES_SCALE)
                .shift(DOWN * 0.1)
            )

            bs += [b, bl]

            if i == 4:
                bl.shift(UP * 0.08)

            if i == 0:
                b.shift(DOWN * shift)
                bl.shift(DOWN * shift)
                self.play(
                    task.animate.shift(UP * shift / 2),
                    parentheses.animate.shift(DOWN * shift),
                    wall.animate.shift(DOWN * shift),
                    tileset.animate.shift(DOWN * shift),
                    FadeInUp(b, move_factor=0.1),
                    FadeInUp(bl, move_factor=0.1),
                )

                self.play(
                    highlight_parentheses([1, 2, 3, 4, 6, 7]),
                    highlight_tiles([(2, 0), (1, 0), (3, 0), (4, 0), (6, 0), (7, 0)]),
                )

            else:
                self.play(FadeInUp(b), FadeInUp(bl))

        self.next_section(skip_animations=True)
