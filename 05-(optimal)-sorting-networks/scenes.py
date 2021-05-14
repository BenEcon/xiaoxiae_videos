from utilities import *


networks = [
        None,
        [#1
            [],
        ],
        [#2
            [[(0, 1)]],
        ],
        [#3
            [[(1, 2)]],
            [[(0, 1)]],
            [[(1, 2)]],
        ],
        [#4
            [[(0, 1), (2, 3)]],
            [[(1, 3)], [(0, 2)]],
            [[(1, 2)]],
        ],
        [#5
            [[(1, 2), (3, 4)]],
            [[(1, 3)], [(0, 2)]],
            [[(2, 4)], [(0, 3)]],
            [[(0, 1), (2, 3)]],
            [[(1, 2)]],
        ],
        [#6
            [[(0, 1), (2, 3), (4, 5)]],
            [[(0, 2), (3, 5)], [(1, 4)]],
            [[(0, 1), (2, 3), (4, 5)]],
            [[(1, 2), (3, 4)]],
            [[(2, 3)]],
        ],
        [#7
            [[(1, 2), (3, 4), (5, 6)]],
            [[(0, 2), (4, 6)], [(3, 5)]],
            [[(2, 6)], [(1, 5)], [(0, 4)]],
            [[(2, 5)], [(0, 3)]],
            [[(2, 4)], [(1, 3)]],
            [[(0, 1), (2, 3), (4, 5)]],
        ],
        [#8
            [[(0, 7)], [(1, 6)], [(2, 5)], [(3, 4)]],
            [[(0, 3), (4, 7)], [(1, 2), (5, 6)]],
            [[(0, 1), (2, 3), (4, 5), (6, 7)]],
            [[(3, 5)], [(2, 4)]],
            [[(1, 2), (3, 4), (5, 6)]],
            [[(2, 3), (4, 5)]],
            [[(3, 4)]],
        ],
        [#9
            [[(1, 8)], [(2, 7)], [(3, 6)], [(4, 5)]],
            [[(0, 2), (6, 7)], [(1, 4), (5, 8)]],
            [[(2, 6), (7, 8)], [(0, 3), (4, 5)]],
            [[(0, 1), (3, 5)], [(2, 4), (6, 7)]],
            [[(1, 3), (5, 7)], [(4, 6)]],
            [[(1, 2), (3, 4), (5, 6), (7, 8)]],
            [[(2, 3), (4, 5)]],
        ],
    ]


class SortingNetwork(VMobject):
    def __init__(
            self,
            network,
            n,
            height = 2.5,
            width = 5.5,
    ):
        super().__init__()

        self.n = n
        self.width = width
        self.height = height

        major_circles_radius = 0.05
        minor_circles_radius = 0.11

        self.starting_circles = [Circle(major_circles_radius, color=WHITE).set_fill(WHITE, opacity=1) for _ in range(n)]
        self.ending_circles = [Circle(major_circles_radius, color=WHITE).set_fill(WHITE, opacity=1) for _ in range(n)]

        # starting circles
        for i, circle in enumerate(self.starting_circles):
            circle.move_to(((i / (n - 1)) * height - height / 2) * UP + LEFT * width / 2)
            self.add(circle)

        # ending circles
        for i, circle in enumerate(self.ending_circles):
            circle.move_to(((i / (n - 1)) * height - height / 2) * UP + RIGHT * width / 2)
            self.add(circle)

        # lines
        self.lines = []
        for a, b in zip(self.starting_circles, self.ending_circles):
            self.lines.append(Line(a.get_center(), b.get_center()))
            self.add(self.lines[-1])

        layer_spacing = 1
        sublayer_spacing = 0.3
        position = layer_spacing
        number = 1

        # add appropriately spaced comparators
        self.comparators = []
        self.comparator_titles = []
        for layer in network:
            subpos = position
            for sublayer in layer:
                self.comparators.append([position, sublayer])
                position += sublayer_spacing
                subpos += position
            subpos = (subpos - position) / len(layer)
            self.comparator_titles.append((subpos, Tex(f"${number}$")))
            number += 1
            position = position - sublayer_spacing + layer_spacing

        # normalize the positions of the comparators accordingly
        for comparator in self.comparators:
            comparator[0] /= position

        for i in range(len(self.comparator_titles)):
            pos, text = self.comparator_titles[i]
            pos /= position
            text.move_to(UP * (height / 2) * 1.4 + RIGHT * (-width / 2 + width * pos))
            self.comparator_titles[i] = (pos, text)

        # transform the sublayer list into (a, b, Circle(a), Circle(b), line) list
        # a little messy but w/e
        for position, sublayer in self.comparators:
            for i in range(len(sublayer)):
                a, b = sublayer[i]

                a_circle = Circle(minor_circles_radius, color=WHITE).move_to(UP * ((a / (n - 1)) * height - height / 2) + RIGHT * (-width / 2 + width * position)).set_fill(WHITE, opacity=1)
                b_circle = Circle(minor_circles_radius, color=WHITE).move_to(UP * ((b / (n - 1)) * height - height / 2) + RIGHT * (-width / 2 + width * position)).set_fill(WHITE, opacity=1)
                line = Line(a_circle.get_center(), b_circle.get_center())

                sublayer[i] = (a, b, a_circle, b_circle, line)

                self.add(a_circle)
                self.add(b_circle)
                self.add(line)

        for _, text in self.comparator_titles:
            self.add(text)

    def animate_sort(self, scene, numbers = None, rate_func=linear, duration=10):
        """Animate a sorting of numbers."""
        if numbers is None:
            numbers = [i + 1 for i in range(self.n)]
            shuffle(numbers)

        number_circles = []
        number_labels = []
        for i, circle in enumerate(self.starting_circles):
            number_circle = Circle(0.15, color=WHITE).set_fill(WHITE, opacity=1).move_to(circle.get_center())
            label = Tex(f"${numbers[i]}$").move_to(circle.get_center()).set_color(BLACK).scale(0.5)

            number_circles.append(number_circle)
            number_labels.append(label)

        scene.play(*map(Write, number_circles))
        scene.play(*map(Write, number_labels))

        def tmp(ob, dt):

            pos, _, _, = number_circles[0].get_center()
            pos += self.width / 2
            pos /= self.width

            for circle, label in zip(number_circles, number_labels):
                label.move_to(circle.get_center())

            for position, compars in self.comparators:
                if pos > position > pos - dt:
                    for a, b, _, _, _ in compars:
                        if numbers[a] < numbers[b]:
                            number_labels[a], number_labels[b] = number_labels[b], number_labels[a]
                            numbers[a], numbers[b] = numbers[b], numbers[a]


        number_labels[0].add_updater(tmp)

        numbers_copy = list(numbers)
        flash_positions = []

        for position, compars in self.comparators:
            for a, b, _, _, _ in compars:
                if numbers_copy[a] < numbers_copy[b]:
                    numbers_copy[a], numbers_copy[b] = numbers_copy[b], numbers_copy[a]
                    flash_positions.append([position, number_circles[a]])
                    flash_positions.append([position, number_circles[b]])

        scene.play(
                *[circle.animate.shift(self.width * RIGHT) for circle in number_circles],
                *[Flash(obj, rate_func=partial(lambda p, x: 0 if (rate_func(x) - p) < 0 else (rate_func(x) - p) * 10 if (rate_func(x) - p) <= 0.1 else 1, pos), run_time=duration) for pos, obj in flash_positions],
                run_time = duration,
                rate_func=rate_func,
                )

        scene.play(
                   *map(FadeOut, number_circles),
                   *map(FadeOut, number_labels),
                )

        # TODO: barvy tam, kudy jeli

class Intro(Scene):
    @fade
    def construct(self):
        sn = SortingNetwork(networks[8], 8, width=8, height=5)

        self.play(Write(sn))

        sn.animate_sort(self)

        self.play(Unwrite(sn))

