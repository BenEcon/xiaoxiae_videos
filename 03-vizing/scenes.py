from utilities import *


class BeforeIntro(Scene):
    def construct(self):
        petersen=nx.petersen_graph()
        tutte=nx.tutte_graph()
        complete=nx.complete_graph(8)

        A = Graph.from_networkx(petersen, layout="planar", layout_scale=2).shift(UP * 1.5 + LEFT * 3)
        B = Graph.from_networkx(tutte, layout="spring", layout_scale=2.5).rotate(PI / 4).shift(DOWN * 2)
        C = Graph.from_networkx(complete, layout="circular", layout_scale=1.5).shift(UP * 1.5 + RIGHT * 3)


        self.play(
                Write(A),
                Write(B),
                Write(C),
                )
        self.play( A.edges[(0, 1)].animate.set_color(RED),
                    A.edges[(0, 4)].animate.set_color(BLUE), 
                    A.edges[(0, 5)].animate.set_color(GREEN), 
                    A.edges[(1, 2)].animate.set_color(PINK), 
                    A.edges[(1, 6)].animate.set_color(BLUE), 
                    A.edges[(2, 3)].animate.set_color(BLUE), 
                    A.edges[(2, 7)].animate.set_color(GREEN), 
                    A.edges[(3, 4)].animate.set_color(GREEN), 
                    A.edges[(3, 8)].animate.set_color(RED), 
                    A.edges[(4, 9)].animate.set_color(PINK), 
                    A.edges[(5, 7)].animate.set_color(PINK), 
                    A.edges[(5, 8)].animate.set_color(BLUE), 
                    A.edges[(6, 8)].animate.set_color(GREEN), 
                    A.edges[(6, 9)].animate.set_color(RED), 
                    A.edges[(7, 9)].animate.set_color(BLUE),
                    B.edges[(0, 1)].animate.set_color(RED),
                    B.edges[(0, 2)].animate.set_color(GREEN),
                    B.edges[(0, 3)].animate.set_color(BLUE),
                    B.edges[(1, 4)].animate.set_color(GREEN),
                    B.edges[(1, 26)].animate.set_color(BLUE),
                    B.edges[(2, 10)].animate.set_color(BLUE),
                    B.edges[(2, 11)].animate.set_color(RED),
                    B.edges[(3, 18)].animate.set_color(RED),
                    B.edges[(3, 19)].animate.set_color(GREEN),
                    B.edges[(4, 5)].animate.set_color(BLUE),
                    B.edges[(4, 33)].animate.set_color(RED),
                    B.edges[(5, 6)].animate.set_color(RED),
                    B.edges[(5, 29)].animate.set_color(GREEN),
                    B.edges[(6, 7)].animate.set_color(BLUE),
                    B.edges[(6, 27)].animate.set_color(GREEN),
                    B.edges[(7, 8)].animate.set_color(GREEN),
                    B.edges[(7, 14)].animate.set_color(RED),
                    B.edges[(8, 9)].animate.set_color(RED),
                    B.edges[(8, 38)].animate.set_color(BLUE),
                    B.edges[(9, 10)].animate.set_color(GREEN),
                    B.edges[(9, 37)].animate.set_color(BLUE),
                    B.edges[(10, 39)].animate.set_color(RED),
                    B.edges[(11, 12)].animate.set_color(BLUE),
                    B.edges[(11, 39)].animate.set_color(GREEN),
                    B.edges[(12, 13)].animate.set_color(GREEN),
                    B.edges[(12, 35)].animate.set_color(RED),
                    B.edges[(13, 14)].animate.set_color(BLUE),
                    B.edges[(13, 15)].animate.set_color(RED),
                    B.edges[(14, 34)].animate.set_color(GREEN),
                    B.edges[(15, 16)].animate.set_color(BLUE),
                    B.edges[(15, 22)].animate.set_color(GREEN),
                    B.edges[(16, 17)].animate.set_color(GREEN),
                    B.edges[(16, 44)].animate.set_color(RED),
                    B.edges[(17, 18)].animate.set_color(BLUE),
                    B.edges[(17, 43)].animate.set_color(RED),
                    B.edges[(18, 45)].animate.set_color(GREEN),
                    B.edges[(19, 20)].animate.set_color(BLUE),
                    B.edges[(19, 45)].animate.set_color(RED),
                    B.edges[(20, 21)].animate.set_color(RED),
                    B.edges[(20, 41)].animate.set_color(GREEN),
                    B.edges[(21, 22)].animate.set_color(BLUE),
                    B.edges[(21, 23)].animate.set_color(GREEN),
                    B.edges[(22, 40)].animate.set_color(RED),
                    B.edges[(23, 24)].animate.set_color(RED),
                    B.edges[(23, 27)].animate.set_color(BLUE),
                    B.edges[(24, 25)].animate.set_color(GREEN),
                    B.edges[(24, 32)].animate.set_color(BLUE),
                    B.edges[(25, 26)].animate.set_color(RED),
                    B.edges[(25, 31)].animate.set_color(BLUE),
                    B.edges[(26, 33)].animate.set_color(GREEN),
                    B.edges[(27, 28)].animate.set_color(RED),
                    B.edges[(28, 29)].animate.set_color(BLUE),
                    B.edges[(28, 32)].animate.set_color(GREEN),
                    B.edges[(29, 30)].animate.set_color(RED),
                    B.edges[(30, 31)].animate.set_color(GREEN),
                    B.edges[(30, 33)].animate.set_color(BLUE),
                    B.edges[(31, 32)].animate.set_color(RED),
                    B.edges[(34, 35)].animate.set_color(BLUE),
                    B.edges[(34, 38)].animate.set_color(RED),
                    B.edges[(35, 36)].animate.set_color(GREEN),
                    B.edges[(36, 37)].animate.set_color(RED),
                    B.edges[(36, 39)].animate.set_color(BLUE),
                    B.edges[(37, 38)].animate.set_color(GREEN),
                    B.edges[(40, 41)].animate.set_color(BLUE),
                    B.edges[(40, 44)].animate.set_color(GREEN),
                    B.edges[(41, 42)].animate.set_color(RED),
                    B.edges[(42, 43)].animate.set_color(GREEN),
                    B.edges[(42, 45)].animate.set_color(BLUE),
                    B.edges[(43, 44)].animate.set_color(BLUE),
                    C.edges[(0, 1)].animate.set_color(RED),
                    C.edges[(0, 2)].animate.set_color(GREEN),
                    C.edges[(0, 3)].animate.set_color(BLUE),
                    C.edges[(0, 4)].animate.set_color(ORANGE),
                    C.edges[(0, 5)].animate.set_color(PINK),
                    C.edges[(0, 6)].animate.set_color(WHITE),
                    C.edges[(0, 7)].animate.set_color(GRAY),
                    C.edges[(1, 2)].animate.set_color(WHITE),
                    C.edges[(1, 3)].animate.set_color(GREEN),
                    C.edges[(1, 4)].animate.set_color(GRAY),
                    C.edges[(1, 5)].animate.set_color(ORANGE),
                    C.edges[(1, 6)].animate.set_color(BLUE),
                    C.edges[(1, 7)].animate.set_color(PINK),
                    C.edges[(2, 3)].animate.set_color(ORANGE),
                    C.edges[(2, 4)].animate.set_color(PINK),
                    C.edges[(2, 5)].animate.set_color(BLUE),
                    C.edges[(2, 6)].animate.set_color(GRAY),
                    C.edges[(2, 7)].animate.set_color(RED),
                    C.edges[(3, 4)].animate.set_color(RED),
                    C.edges[(3, 5)].animate.set_color(GRAY),
                    C.edges[(3, 6)].animate.set_color(PINK),
                    C.edges[(3, 7)].animate.set_color(WHITE),
                    C.edges[(4, 5)].animate.set_color(WHITE),
                    C.edges[(4, 6)].animate.set_color(GREEN),
                    C.edges[(4, 7)].animate.set_color(BLUE),
                    C.edges[(5, 6)].animate.set_color(RED),
                    C.edges[(5, 7)].animate.set_color(GREEN),
                    C.edges[(6, 7)].animate.set_color(ORANGE),
                    )

        self.play(
                Write(A),
                Write(B),
                Write(C),
                rate_func=lambda t: smooth(1-t))

        self.remove(A)
        self.remove(B)
        self.remove(C)

        vertices = [1, 2, 3, 4]

        edges = [(2, 3), (2,4), (1,4), (3, 4)]
        g = Graph(vertices, edges, layout="circular", layout_scale=3, labels=True).rotate(-PI / 4)

        for i in g._labels:
            g._labels[i].scale(0)

        self.play(Write(g))

        self.play(
                g.edges[(2, 4)].animate.set_color(RED),
                g.edges[(3, 4)].animate.set_color(GREEN),
                g.edges[(1, 4)].animate.set_color(BLUE),
                g.edges[(2, 3)].animate.set_color(BLUE),
                )

        visuallyChangeColor(self, [(g.edges[(2, 3)], RED)])

class Intro(Scene):
    @fade
    def construct(self):
        title = Tex("\Huge Vizing's Theorem")

        self.play(Write(title))

        self.play(ApplyMethod(title.shift, UP * 2))

        text = Tex("\parbox{23em}{Let $\Delta(G)$ be the maximum degree of a graph $G$. Then the ","number of colors $\chi'$"," needed to ","edge color"," $G$ is ","$$\Delta(G) \le \chi' \le \Delta(G) + 1$$}")
        highlightText(text)

        text.next_to(title, 1.3 * DOWN)

        self.play(Write(text), run_time=4)

class Example(Scene):
    @fade
    def construct(self):
        vertices = [1, 2, 3, 4, 5]

        edges = [(2, 3), (2,4), (1,4), (1, 5), (3, 4)]
        g = Graph(vertices, edges, layout="circular", layout_scale=3, labels=True)

        for i in g._labels:
            g._labels[i].scale(0)

        self.play(Write(g), run_time=3)

        text = Tex("$\Delta(G) = 3$")
        text.next_to(g.vertices[2], 6 * RIGHT)

        text2 = Tex("$\chi'(G) = \Delta(G)$")
        text2.next_to(text, DOWN)

        self.play(Write(text))

        self.play(
                g.edges[(2, 4)].animate.set_color(RED),
                g.edges[(3, 4)].animate.set_color(GREEN),
                g.edges[(1, 4)].animate.set_color(BLUE),
                g.edges[(1, 5)].animate.set_color(RED),
                g.edges[(2, 3)].animate.set_color(BLUE),
                )

        self.play(Write(text2))

        h = Graph(vertices, edges + [(3, 5), (2, 5)], layout="circular", layout_scale=3, labels=True)

        self.play(
                Write(h.edges[(3, 5)]),
                Write(h.edges[(2, 5)]),
                )

        text3 = Tex("$+\ 1$")
        text3.next_to(text2, RIGHT)

        self.play(
                h.edges[(3, 5)].animate.set_color(YELLOW),
                h.edges[(2, 5)].animate.set_color(GREEN),
                )

        self.play(Write(text3))

class Degree(Scene):
    @fade
    def construct(self):
        vertices = [1, 2, 3, 4, 5, 6]

        edges = [(2, 3), (2,4), (1,6), (3, 4), (4, 1), (4, 5)]
        g = Graph(vertices, edges, layout="circular", layout_scale=3, labels=True)

        for i in g._labels:
            g._labels[i].scale(0)

        self.play(Write(g))

        replaces = [
                Tex("$2$").move_to(g._labels[1]).set_color(BLACK),
                Tex("$2$").move_to(g._labels[2]).set_color(BLACK),
                Tex("$2$").move_to(g._labels[3]).set_color(BLACK),
                Tex("$4$").move_to(g._labels[4]).set_color(BLACK),
                Tex("$1$").move_to(g._labels[5]).set_color(BLACK),
                Tex("$1$").move_to(g._labels[6]).set_color(BLACK),
                ]

        self.play(
                *map(FadeIn, replaces)
                )

        self.play(
                *[ApplyMethod(replace.shift, 2 * RIGHT) for replace in replaces] ,
                ApplyMethod(g.shift, 2 * RIGHT)
                )

        deg2 = Tex("$\Delta(G) = 4$").next_to(g._labels[4], LEFT * 9)

        self.play(Write(deg2))
        self.play(Indicate(g.vertices[4]))

class FreeColor(Scene):
    @fade
    def construct(self):
        vertices = [1, 2, 3, 4, 5]

        edges = [(2, 3), (2,4), (1,4), (1, 5), (3, 4), (3, 5), (2, 5)]
        g = Graph(vertices, edges, layout="circular", layout_scale=3, labels=True)

        for i in g._labels:
            g._labels[i].scale(0)

        g.edges[(2, 4)].set_color(RED)
        g.edges[(3, 4)].set_color(GREEN)
        g.edges[(1, 4)].set_color(BLUE)
        g.edges[(1, 5)].set_color(RED)
        g.edges[(2, 3)].set_color(BLUE)
        g.edges[(3, 5)].set_color(YELLOW)
        g.edges[(2, 5)].set_color(GREEN)

        self.play(Write(g), run_time=4)

        a = Circle(radius=0.07, fill_opacity=1, color=GREEN).next_to(g.vertices[1], UP * 0.7).shift(LEFT * 0.15)
        aa = Circle(radius=0.07, fill_opacity=1, color=YELLOW).next_to(g.vertices[1], UP * 0.7).shift(RIGHT * 0.15)
        b = Circle(radius=0.07, fill_opacity=1, color=YELLOW).next_to(g.vertices[2], UP * 0.7)
        c = Circle(radius=0.07, fill_opacity=1, color=RED).next_to(g.vertices[3], UP * 0.7)
        d = Circle(radius=0.07, fill_opacity=1, color=YELLOW).next_to(g.vertices[4], DOWN * 0.7)
        e = Circle(radius=0.07, fill_opacity=1, color=BLUE).next_to(g.vertices[5], DOWN * 0.7)

        self.play(
                FadeIn(a),
                FadeIn(aa),
                FadeIn(b),
                FadeIn(c),
                FadeIn(d),
                FadeIn(e),
                )

        visuallyChangeColor(self, [(g.edges[(2, 4)], YELLOW), (b, RED), (d, RED)])    
        visuallyChangeColor(self, [(g.edges[(3, 4)], RED), (c, GREEN), (d, GREEN)])    

class LowerBound(Scene):
    @fade
    def construct(self):
        title = Tex("\Large Lower bound")

        self.play(Write(title))

        self.play(ApplyMethod(title.shift, 2 * UP))

        N = 7
        vertices = [i + 1 for i in range(N)]

        edges = [(1, i + 1) for i in range(1, N)]
        g = Graph(vertices, edges, layout="circular", layout_scale=1.5)
        g.next_to(title, 3 * DOWN)

        self.play(Write(g))

        self.play(
                g.edges[(1, 2)].animate.set_color(RED),
                g.edges[(1, 3)].animate.set_color(GREEN),
                g.edges[(1, 4)].animate.set_color(BLUE),
                g.edges[(1, 5)].animate.set_color(YELLOW),
                g.edges[(1, 6)].animate.set_color(PINK),
                g.edges[(1, 7)].animate.set_color(GRAY),
                )

        self.play(ApplyMethod(g.shift, 2 * LEFT))

        text = Tex("$\Delta(G)\le \chi'(G)$")
        text.next_to(g, 3 * RIGHT)

        self.play(Write(text))

class UpperBound(Scene):
    @fade
    def construct(self):
        title = Tex("\Large Upper bound")

        self.play(Write(title))
        self.play(FadeOut(title))


        seed(1)

        e = Ellipse(width=8, height=5,color=WHITE)

        text = Tex("$G$")
        text.shift(UP * 2 + RIGHT * 3.2)

        self.play(Write(e), Write(text))

        vertices = [i for i in range(10)] + ['9']

        edges = [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (8, 4), (8, 7), (9, 7), (0, 9), (8, '9'), (3, '9'), (4,8)]

        s = 0.3

        lt = {
                1: [(32.7448099360117  -37.5)*s, (24.434327797192754-20.85)*s, 0],
                2: [(30.06934351228568 -37.5)*s, (18.314489982954107-20.85)*s, 0],
                3: [(34.424961294659475-37.5)*s, (18.154452377859204-20.85)*s, 0],
                4: [(38.167198471557086-37.5)*s, (19.72097026586286 -20.85)*s, 0],
                5: [(40.08183144578378 -37.5)*s, (23.144101947056036-20.85)*s, 0],
                6: [(40.25588898889529 -37.5)*s, (26.799310352397896-20.85)*s, 0],
                7: [(43.201193299423025-37.5)*s, (16.591257981420444-20.85)*s, 0],
                8: [(40.16886021733954 -37.5)*s, (15.630618002742203-20.85)*s, 0],
                9: [(45.201193299423025-37.5)*s, (19.200000000000000-20.85)*s, 0],
                0: [(46.201193299423025-37.5)*s, (22.591257981420444-20.85)*s, 0],
                '9': [(37.16886021733954 -37.5)*s, (14.630618002742203-20.85)*s, 0],
                }

        g = Graph(vertices, edges, layout=lt, labels=True, layout_scale=0.2)

        # YUCK!!!!
        for i in g._labels:
            g._labels[i].scale(0)

        replace = Tex("$x$").move_to(g._labels[1]).set_color(BLACK)
        replace2 = Tex("$y$").move_to(g._labels[2]).set_color(BLACK)

        self.play(
                Write(g.vertices[1]),
                Write(g.vertices[2]),
                Write(g.edges[(1, 2)]),
                FadeIn(replace),
                FadeIn(replace2),
                )

        a = Circle(radius=0.07, fill_opacity=1, color=RED)
        a.next_to(g.vertices[1], UP * 0.7)
        b = Circle(radius=0.07, fill_opacity=1, color=RED)
        b.next_to(g.vertices[2], UP * 0.7)
        self.play(FadeIn(a))
        self.play(FadeIn(b))

        visuallyChangeColor(self, [(g.edges[(1, 2)], RED)])

        self.play(
                g.edges[(1, 2)].animate.set_color(WHITE),
                b.animate.set_color(PINK)
                )

        g.edges[(1, 3)].set_color(PINK),

        self.play(
                Write(g.vertices[3]),
                Write(g.edges[(1, 3)]),
                )

        c = Circle(radius=0.07, fill_opacity=1, color=BLUE)
        c.next_to(g.vertices[3], UP * 0.7)
        self.play(FadeIn(c))

        g.edges[(1, 4)].set_color(BLUE),
        g.edges[(1, 5)].set_color(GREEN),

        d = Circle(radius=0.07, fill_opacity=1, color=GREEN)
        d.next_to(g.vertices[4], UP * 0.7)

        e = Tex("?").scale(0.5)
        e.next_to(g.vertices[5], UP * 0.7)

        self.play(
                Write(g.vertices[4]),
                Write(g.edges[(1, 4)]),
                FadeIn(d),
                )

        self.play(
                Write(g.vertices[5]),
                Write(g.edges[(1, 5)]),
                FadeIn(e),
                )

        ee = Circle(radius=0.07, fill_opacity=1, color=RED)
        ee.next_to(g.vertices[5], UP * 0.7)

        case1 = Tex("\Large Case I")
        case1.shift(UP * 2.7 + LEFT * 4.8)

        self.play(
                Write(case1)
                )

        self.play(
                Transform(e, ee),
                )

        visuallyChangeColor(self, [
            (a, GREEN),
            (e, GREEN),
            (g.edges[(1, 5)], RED),
            ])

        visuallyChangeColor(self, [
            (a, BLUE),
            (d, BLUE),
            (g.edges[(1, 4)], GREEN),
            ])

        visuallyChangeColor(self, [
            (a, PINK),
            (c, PINK),
            (g.edges[(1, 3)], BLUE),
            ])

        visuallyChangeColor(self, [
            (a, GRAY),
            (b, GRAY),
            (g.edges[(1, 2)], PINK),
            ])

        eee = Tex("?").scale(0.5)
        eee.next_to(g.vertices[5], UP * 0.7)

        self.play(
                a.animate.set_color(RED),
                b.animate.set_color(PINK),
                c.animate.set_color(BLUE),
                d.animate.set_color(GREEN),
                Transform(e, eee),
                g.edges[(1, 2)].animate.set_color(WHITE),
                g.edges[(1, 3)].animate.set_color(PINK),
                g.edges[(1, 4)].animate.set_color(BLUE),
                g.edges[(1, 5)].animate.set_color(GREEN),
                )

        case2 = Tex("\Large I")
        case2.next_to(case1, RIGHT * 0.2)


        self.play(
            Write(case2)
        )

        ee.set_color(BLUE)
        self.play(
            Transform(e, ee),
        )


        self.play(
            Indicate(e),
            Indicate(g.edges[(1, 4)]),
        )

        replace3 = Tex("$u$").move_to(g._labels[5]).set_color(BLACK)
        replace4 = Tex("$v$").move_to(g._labels[4]).set_color(BLACK)

        g.edges[(8, 4)].set_color(RED)
        g.edges[(8, 7)].set_color(BLUE)
        g.edges[(9, 7)].set_color(RED)
        g.edges[(0, 9)].set_color(BLUE)

        self.play(
                FadeIn(replace3),
                FadeIn(replace4),
                )

        f = Circle(radius=0.07, fill_opacity=1, color=RED)
        f.next_to(g.vertices[0], UP * 0.7)

        replace5 = Tex("$w$").move_to(g._labels[3]).set_color(BLACK)

        # SUBCASE
        g.edges[(3, '9')].set_color(RED)
        g.edges[(8, '9')].set_color(BLUE)
        g.edges[(4, 8)].set_color(RED)
        self.play(
            FadeIn(replace5),
            FadeIn(g.edges[(3, '9')]),
            FadeIn(g.edges[(4, 8)]),
            FadeIn(g.edges[(8, '9')]),
            FadeIn(g.vertices[8]),
            FadeIn(g.vertices['9']),
            )

        visuallyChangeColor(self, [
                (g.edges[(1, 4)], RED), 
                (g.edges[(3, '9')], BLUE), 
                (g.edges[(8, '9')], RED), 
                (g.edges[(4, 8)], BLUE),
                (c, RED),
                (a, BLUE),
                ]
                )

        visuallyChangeColor(self, [ (g.edges[(1, 5)], BLUE), (a, GREEN), (e, GREEN), ])
        visuallyChangeColor(self, [ (g.edges[(1, 4)], GREEN), (a, RED), (d, RED), ])
        visuallyChangeColor(self, [ (g.edges[(1, 3)], RED), (a, PINK), (c, PINK), ])
        visuallyChangeColor(self, [ (g.edges[(1, 2)], PINK), (a, GRAY), (b, GRAY), ])

        # RESTORE
        self.play(
                a.animate.set_color(RED),
                b.animate.set_color(PINK),
                c.animate.set_color(BLUE),
                d.animate.set_color(GREEN),
                e.animate.set_color(BLUE),
                g.edges[(1, 2)].animate.set_color(WHITE),
                g.edges[(1, 3)].animate.set_color(PINK),
                g.edges[(1, 4)].animate.set_color(BLUE),
                g.edges[(1, 5)].animate.set_color(GREEN),
                FadeOut(g.edges[(3, '9')]),
                FadeOut(g.edges[(8, '9')]),
                FadeOut(g.edges[(4, 8)]),
                FadeOut(g.vertices[8]),
                FadeOut(g.vertices['9']),
                )

        g.edges[(4, 8)].set_color(RED)

        self.play(
                FadeIn(g.vertices[8]),
                FadeIn(g.vertices[7]),
                FadeIn(g.edges[(8, 7)]),
                FadeIn(g.edges[(9, 7)]),
                FadeIn(g.edges[(0, 9)]),
                FadeIn(g.edges[(4, 8)]),
                FadeIn(g.vertices[9]),
                FadeIn(g.vertices[0]),
                FadeIn(f),
                )

        visuallyChangeColor(self, [
                (g.edges[(1, 4)], RED), 
                (g.edges[(8, 4)], BLUE), 
                (g.edges[(8, 7)], RED),
                (g.edges[(9, 7)], BLUE),
                (g.edges[(0, 9)], RED),
                (g.edges[(0, 9)], RED),
                (a, BLUE),
                (f, BLUE),]
                )

        visuallyChangeColor(self, [
                (g.edges[(1, 3)], BLUE), 
                (a, PINK),
                (c, PINK),]
                )

        visuallyChangeColor(self, [
                (g.edges[(1, 2)], PINK), 
                (a, GRAY),
                (b, GRAY),]
                )

        self.play(
                Indicate(g.vertices[4]), 
                Indicate(g.vertices[7]), 
                Indicate(g.vertices[8]), 
                Indicate(g.vertices[9]),
                )

        self.play(
                Indicate(g.vertices[1]), 
                )

        self.play(
                Indicate(g.vertices[0]), 
                )


class Outro(Scene):
    def construct(self):
        g = Graph([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [(0, 11), (0, 10), (0, 16), (0, 6), (1, 18), (1, 5), (1, 11), (1, 8), (1, 10), (2, 9), (2, 15), (3, 13), (3, 19), (3, 12), (3, 18), (3, 8), (4, 17), (4, 13), (4, 19), (5, 7), (5, 10), (5, 15), (5, 8), (6, 11), (6, 10), (6, 16), (7, 9), (7, 15), (8, 18), (8, 11), (8, 10), (9, 15), (10, 11), (10, 16), (11, 16), (13, 17), (13, 19), (17, 19)], layout='circular', layout_scale=3)
        self.play(Write(g))
        self.play(
            g.edges[(0, 11)].animate.set_color(YELLOW),
            g.edges[(0, 10)].animate.set_color(GREEN),
            g.edges[(0, 16)].animate.set_color(RED),
            g.edges[(0, 6)].animate.set_color(PINK),
            g.edges[(1, 18)].animate.set_color(PINK),
            g.edges[(1, 5)].animate.set_color(GRAY),
            g.edges[(1, 11)].animate.set_color(GREEN),
            g.edges[(1, 8)].animate.set_color(ORANGE),
            g.edges[(1, 10)].animate.set_color(RED),
            g.edges[(2, 9)].animate.set_color(PINK),
            g.edges[(2, 15)].animate.set_color(BLUE),
            g.edges[(3, 13)].animate.set_color(PINK),
            g.edges[(3, 19)].animate.set_color(RED),
            g.edges[(3, 12)].animate.set_color(BLUE),
            g.edges[(3, 18)].animate.set_color(ORANGE),
            g.edges[(3, 8)].animate.set_color(GRAY),
            g.edges[(4, 17)].animate.set_color(PINK),
            g.edges[(4, 13)].animate.set_color(BLUE),
            g.edges[(4, 19)].animate.set_color(RED),
            g.edges[(5, 7)].animate.set_color(BLUE),
            g.edges[(5, 10)].animate.set_color(ORANGE),
            g.edges[(5, 15)].animate.set_color(RED),
            g.edges[(5, 8)].animate.set_color(YELLOW),
            g.edges[(6, 11)].animate.set_color(RED),
            g.edges[(6, 10)].animate.set_color(YELLOW),
            g.edges[(6, 16)].animate.set_color(GRAY),
            g.edges[(7, 9)].animate.set_color(RED),
            g.edges[(7, 15)].animate.set_color(YELLOW),
            g.edges[(8, 18)].animate.set_color(GREEN),
            g.edges[(8, 11)].animate.set_color(BLUE),
            g.edges[(8, 10)].animate.set_color(PINK),
            g.edges[(9, 15)].animate.set_color(GRAY),
            g.edges[(10, 11)].animate.set_color(GRAY),
            g.edges[(10, 16)].animate.set_color(BLUE),
            g.edges[(11, 16)].animate.set_color(PINK),
            g.edges[(13, 17)].animate.set_color(GRAY),
            g.edges[(13, 19)].animate.set_color(RED),
            g.edges[(17, 19)].animate.set_color(RED),
            )
        self.play(Write(g), rate_func=lambda t: smooth(1-t))
        self.remove(g)

        g = Graph([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29], [(0, 2), (0, 24), (0, 11), (1, 17), (2, 27), (2, 15), (2, 24), (3, 13), (3, 24), (3, 11), (3, 26), (4, 9), (4, 12), (4, 29), (4, 16), (5, 10), (5, 19), (5, 18), (5, 15), (5, 27), (6, 8), (6, 23), (6, 7), (6, 25), (7, 19), (8, 23), (8, 25), (9, 25), (9, 12), (10, 18), (10, 15), (10, 27), (10, 17), (10, 19), (11, 26), (11, 13), (11, 24), (13, 26), (13, 24), (14, 28), (14, 21), (14, 20), (15, 27), (15, 18), (16, 29), (17, 18), (18, 19), (18, 27), (19, 27), (20, 29), (20, 28), (20, 21), (21, 28), (21, 26), (23, 25), (24, 26), (28, 29)], layout='circular', layout_scale=3)
        self.play(Write(g))
        self.play(
            g.edges[(0, 2)].animate.set_color(YELLOW),
            g.edges[(0, 24)].animate.set_color(PINK),
            g.edges[(0, 11)].animate.set_color(GREEN),
            g.edges[(1, 17)].animate.set_color(GRAY),
            g.edges[(2, 27)].animate.set_color(GREEN),
            g.edges[(2, 15)].animate.set_color(GRAY),
            g.edges[(2, 24)].animate.set_color(BLUE),
            g.edges[(3, 13)].animate.set_color(PINK),
            g.edges[(3, 24)].animate.set_color(GREEN),
            g.edges[(3, 11)].animate.set_color(GRAY),
            g.edges[(3, 26)].animate.set_color(RED),
            g.edges[(4, 9)].animate.set_color(BLUE),
            g.edges[(4, 12)].animate.set_color(GREEN),
            g.edges[(4, 29)].animate.set_color(RED),
            g.edges[(4, 16)].animate.set_color(YELLOW),
            g.edges[(5, 10)].animate.set_color(PINK),
            g.edges[(5, 19)].animate.set_color(RED),
            g.edges[(5, 18)].animate.set_color(YELLOW),
            g.edges[(5, 15)].animate.set_color(GREEN),
            g.edges[(5, 27)].animate.set_color(GRAY),
            g.edges[(6, 8)].animate.set_color(YELLOW),
            g.edges[(6, 23)].animate.set_color(RED),
            g.edges[(6, 7)].animate.set_color(GRAY),
            g.edges[(6, 25)].animate.set_color(PINK),
            g.edges[(7, 19)].animate.set_color(BLUE),
            g.edges[(8, 23)].animate.set_color(BLUE),
            g.edges[(8, 25)].animate.set_color(GREEN),
            g.edges[(9, 25)].animate.set_color(YELLOW),
            g.edges[(9, 12)].animate.set_color(GRAY),
            g.edges[(10, 18)].animate.set_color(GRAY),
            g.edges[(10, 15)].animate.set_color(RED),
            g.edges[(10, 27)].animate.set_color(BLUE),
            g.edges[(10, 17)].animate.set_color(YELLOW),
            g.edges[(10, 19)].animate.set_color(GREEN),
            g.edges[(11, 26)].animate.set_color(PINK),
            g.edges[(11, 13)].animate.set_color(BLUE),
            g.edges[(11, 24)].animate.set_color(YELLOW),
            g.edges[(13, 26)].animate.set_color(GREEN),
            g.edges[(13, 24)].animate.set_color(RED),
            g.edges[(14, 28)].animate.set_color(BLUE),
            g.edges[(14, 21)].animate.set_color(GRAY),
            g.edges[(14, 20)].animate.set_color(YELLOW),
            g.edges[(15, 27)].animate.set_color(PINK),
            g.edges[(15, 18)].animate.set_color(BLUE),
            g.edges[(16, 29)].animate.set_color(RED),
            g.edges[(17, 18)].animate.set_color(GREEN),
            g.edges[(18, 19)].animate.set_color(PINK),
            g.edges[(18, 27)].animate.set_color(RED),
            g.edges[(19, 27)].animate.set_color(YELLOW),
            g.edges[(20, 29)].animate.set_color(RED),
            g.edges[(20, 28)].animate.set_color(PINK),
            g.edges[(20, 21)].animate.set_color(RED),
            g.edges[(21, 28)].animate.set_color(GREEN),
            g.edges[(21, 26)].animate.set_color(YELLOW),
            g.edges[(23, 25)].animate.set_color(GRAY),
            g.edges[(24, 26)].animate.set_color(GRAY),
            g.edges[(28, 29)].animate.set_color(RED),
            )
        self.play(Write(g), rate_func=lambda t: smooth(1-t))
        self.remove(g)

        g = Graph([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [(0, 23), (0, 9), (0, 36), (0, 47), (0, 22), (0, 6), (1, 29), (2, 27), (2, 24), (2, 8), (2, 26), (2, 3), (2, 18), (3, 24), (3, 8), (3, 44), (3, 5), (3, 18), (4, 48), (4, 33), (4, 14), (5, 44), (6, 47), (6, 22), (6, 23), (7, 17), (7, 35), (7, 21), (7, 41), (7, 25), (7, 36), (7, 22), (8, 27), (8, 38), (8, 24), (8, 42), (8, 26), (9, 35), (9, 10), (9, 30), (9, 23), (9, 41), (9, 20), (9, 22), (10, 20), (10, 30), (10, 18), (10, 41), (11, 37), (12, 13), (12, 31), (12, 15), (12, 39), (12, 32), (13, 15), (13, 39), (13, 32), (13, 31), (14, 33), (14, 48), (14, 45), (15, 39), (15, 32), (15, 16), (15, 31), (15, 28), (16, 31), (16, 28), (16, 39), (17, 21), (17, 41), (17, 43), (17, 36), (17, 35), (18, 30), (18, 41), (18, 20), (19, 32), (19, 44), (19, 30), (20, 40), (20, 30), (20, 41), (21, 34), (21, 43), (21, 27), (21, 26), (22, 35), (22, 23), (22, 36), (22, 47), (23, 47), (24, 42), (24, 26), (24, 27), (25, 36), (25, 33), (25, 35), (25, 48), (26, 43), (26, 27), (26, 38), (27, 43), (27, 38), (28, 39), (28, 31), (28, 49), (30, 41), (31, 39), (31, 32), (33, 36), (33, 48), (34, 43), (35, 41), (35, 36), (36, 48), (37, 49)], layout='circular', layout_scale=3)
        self.play(Write(g))
        self.play(
            g.edges[(0, 23)].animate.set_color(ORANGE),
            g.edges[(0, 9)].animate.set_color(RED),
            g.edges[(0, 36)].animate.set_color(GRAY),
            g.edges[(0, 47)].animate.set_color(WHITE),
            g.edges[(0, 22)].animate.set_color(GREEN),
            g.edges[(0, 6)].animate.set_color(YELLOW),
            g.edges[(1, 29)].animate.set_color(RED),
            g.edges[(2, 27)].animate.set_color(YELLOW),
            g.edges[(2, 24)].animate.set_color(BLUE),
            g.edges[(2, 8)].animate.set_color(WHITE),
            g.edges[(2, 26)].animate.set_color(ORANGE),
            g.edges[(2, 3)].animate.set_color(GREEN),
            g.edges[(2, 18)].animate.set_color(PINK),
            g.edges[(3, 24)].animate.set_color(PINK),
            g.edges[(3, 8)].animate.set_color(ORANGE),
            g.edges[(3, 44)].animate.set_color(GRAY),
            g.edges[(3, 5)].animate.set_color(RED),
            g.edges[(3, 18)].animate.set_color(BLUE),
            g.edges[(4, 48)].animate.set_color(WHITE),
            g.edges[(4, 33)].animate.set_color(BLUE),
            g.edges[(4, 14)].animate.set_color(ORANGE),
            g.edges[(5, 44)].animate.set_color(BLUE),
            g.edges[(6, 47)].animate.set_color(ORANGE),
            g.edges[(6, 22)].animate.set_color(GRAY),
            g.edges[(6, 23)].animate.set_color(GREEN),
            g.edges[(7, 17)].animate.set_color(ORANGE),
            g.edges[(7, 35)].animate.set_color(GREEN),
            g.edges[(7, 21)].animate.set_color(RED),
            g.edges[(7, 41)].animate.set_color(BLUE),
            g.edges[(7, 25)].animate.set_color(GRAY),
            g.edges[(7, 36)].animate.set_color(PINK),
            g.edges[(7, 22)].animate.set_color(YELLOW),
            g.edges[(8, 27)].animate.set_color(GRAY),
            g.edges[(8, 38)].animate.set_color(PINK),
            g.edges[(8, 24)].animate.set_color(GREEN),
            g.edges[(8, 42)].animate.set_color(BLUE),
            g.edges[(8, 26)].animate.set_color(RED),
            g.edges[(9, 35)].animate.set_color(BLUE),
            g.edges[(9, 10)].animate.set_color(YELLOW),
            g.edges[(9, 30)].animate.set_color(WHITE),
            g.edges[(9, 23)].animate.set_color(PINK),
            g.edges[(9, 41)].animate.set_color(GRAY),
            g.edges[(9, 20)].animate.set_color(GREEN),
            g.edges[(9, 22)].animate.set_color(ORANGE),
            g.edges[(10, 20)].animate.set_color(GRAY),
            g.edges[(10, 30)].animate.set_color(PINK),
            g.edges[(10, 18)].animate.set_color(GREEN),
            g.edges[(10, 41)].animate.set_color(ORANGE),
            g.edges[(11, 37)].animate.set_color(RED),
            g.edges[(12, 13)].animate.set_color(GREEN),
            g.edges[(12, 31)].animate.set_color(BLUE),
            g.edges[(12, 15)].animate.set_color(PINK),
            g.edges[(12, 39)].animate.set_color(RED),
            g.edges[(12, 32)].animate.set_color(ORANGE),
            g.edges[(13, 15)].animate.set_color(BLUE),
            g.edges[(13, 39)].animate.set_color(PINK),
            g.edges[(13, 32)].animate.set_color(WHITE),
            g.edges[(13, 31)].animate.set_color(RED),
            g.edges[(14, 33)].animate.set_color(YELLOW),
            g.edges[(14, 48)].animate.set_color(PINK),
            g.edges[(14, 45)].animate.set_color(RED),
            g.edges[(15, 39)].animate.set_color(GRAY),
            g.edges[(15, 32)].animate.set_color(RED),
            g.edges[(15, 16)].animate.set_color(ORANGE),
            g.edges[(15, 31)].animate.set_color(YELLOW),
            g.edges[(15, 28)].animate.set_color(WHITE),
            g.edges[(16, 31)].animate.set_color(WHITE),
            g.edges[(16, 28)].animate.set_color(GREEN),
            g.edges[(16, 39)].animate.set_color(BLUE),
            g.edges[(17, 21)].animate.set_color(YELLOW),
            g.edges[(17, 41)].animate.set_color(WHITE),
            g.edges[(17, 43)].animate.set_color(RED),
            g.edges[(17, 36)].animate.set_color(BLUE),
            g.edges[(17, 35)].animate.set_color(GRAY),
            g.edges[(18, 30)].animate.set_color(GRAY),
            g.edges[(18, 41)].animate.set_color(YELLOW),
            g.edges[(18, 20)].animate.set_color(ORANGE),
            g.edges[(19, 32)].animate.set_color(YELLOW),
            g.edges[(19, 44)].animate.set_color(PINK),
            g.edges[(19, 30)].animate.set_color(BLUE),
            g.edges[(20, 40)].animate.set_color(WHITE),
            g.edges[(20, 30)].animate.set_color(YELLOW),
            g.edges[(20, 41)].animate.set_color(PINK),
            g.edges[(21, 34)].animate.set_color(PINK),
            g.edges[(21, 43)].animate.set_color(ORANGE),
            g.edges[(21, 27)].animate.set_color(BLUE),
            g.edges[(21, 26)].animate.set_color(WHITE),
            g.edges[(22, 35)].animate.set_color(PINK),
            g.edges[(22, 23)].animate.set_color(RED),
            g.edges[(22, 36)].animate.set_color(WHITE),
            g.edges[(22, 47)].animate.set_color(BLUE),
            g.edges[(23, 47)].animate.set_color(GRAY),
            g.edges[(24, 42)].animate.set_color(YELLOW),
            g.edges[(24, 26)].animate.set_color(GRAY),
            g.edges[(24, 27)].animate.set_color(RED),
            g.edges[(25, 36)].animate.set_color(ORANGE),
            g.edges[(25, 33)].animate.set_color(GREEN),
            g.edges[(25, 35)].animate.set_color(WHITE),
            g.edges[(25, 48)].animate.set_color(RED),
            g.edges[(26, 43)].animate.set_color(YELLOW),
            g.edges[(26, 27)].animate.set_color(PINK),
            g.edges[(26, 38)].animate.set_color(BLUE),
            g.edges[(27, 43)].animate.set_color(WHITE),
            g.edges[(27, 38)].animate.set_color(GREEN),
            g.edges[(28, 39)].animate.set_color(YELLOW),
            g.edges[(28, 31)].animate.set_color(PINK),
            g.edges[(28, 49)].animate.set_color(RED),
            g.edges[(30, 41)].animate.set_color(GREEN),
            g.edges[(31, 39)].animate.set_color(ORANGE),
            g.edges[(31, 32)].animate.set_color(GRAY),
            g.edges[(33, 36)].animate.set_color(RED),
            g.edges[(33, 48)].animate.set_color(ORANGE),
            g.edges[(34, 43)].animate.set_color(BLUE),
            g.edges[(35, 41)].animate.set_color(RED),
            g.edges[(35, 36)].animate.set_color(YELLOW),
            g.edges[(36, 48)].animate.set_color(GREEN),
            g.edges[(37, 49)].animate.set_color(RED),
            )
        self.play(Write(g), rate_func=lambda t: smooth(1-t))
        self.remove(g)


class Thumbnail(MovingCameraScene):
    def construct(self):
        self.next_section(skip_animations=True)

        petersen=nx.petersen_graph()
        #tutte=nx.tutte_graph()
        complete=nx.complete_graph(8)

        #A = Graph.from_networkx(petersen, layout="spring", layout_scale=2).shift(UP * 1.5 + LEFT * 3)
        #B = Graph.from_networkx(tutte, layout="spring", layout_scale=2.5).rotate(PI / 4).shift(DOWN * 2)
        C = Graph.from_networkx(complete, layout="circular", layout_scale=1.5).shift(UP * 1.5 + RIGHT * 3)

        vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        edges = [(1, 2),
                 (1, 6),
                 (1, 5),
                 (2, 3),
                 (2, 7),
                 (3, 8),
                 (3, 4),
                 (4, 5),
                 (4, 9),
                 (5, 10),
                 (6, 8),
                 (6, 9),
                 (7, 9),
                 (7, 10),
                 (8, 10),
                 ]
        lt = {
            1: Dot().shift(UP).get_center(),
            2: Dot().shift(UP).rotate_about_origin(2 * PI / 5).get_center(),
            3: Dot().shift(UP).rotate_about_origin(2 * PI / 5 * 2).get_center(),
            4: Dot().shift(UP).rotate_about_origin(2 * PI / 5 * 3).get_center(),
            5: Dot().shift(UP).rotate_about_origin(2 * PI / 5 * 4).get_center(),
            6: Dot().shift(UP * 0.5).get_center(),
            7: Dot().shift(UP * 0.5).rotate_about_origin(2 * PI / 5).get_center(),
            8: Dot().shift(UP * 0.5).rotate_about_origin(2 * PI / 5 * 2).get_center(),
            9: Dot().shift(UP * 0.5).rotate_about_origin(2 * PI / 5 * 3).get_center(),
            10: Dot().shift(UP * 0.5).rotate_about_origin(2 * PI / 5 * 4).get_center(),
        }
        A = Graph(vertices, edges, layout=lt, layout_scale=3).scale(1.5)

        self.play(
                Write(A),
                Write(C),
                )

        self.play(
                    A.edges[(1, 2) ].animate.set_color(YELLOW),
                    A.edges[(1, 6) ].animate.set_color(BLUE),
                    A.edges[(1, 5) ].animate.set_color(ORANGE),
                    A.edges[(2, 3) ].animate.set_color(GREEN),
                    A.edges[(2, 7) ].animate.set_color(RED),
                    A.edges[(3, 8) ].animate.set_color(ORANGE),
                    A.edges[(3, 4) ].animate.set_color(BLUE),
                    A.edges[(4, 5) ].animate.set_color(RED),
                    A.edges[(4, 9) ].animate.set_color(YELLOW),
                    A.edges[(5, 10)].animate.set_color(GREEN),
                    A.edges[(6, 8) ].animate.set_color(RED),
                    A.edges[(6, 9) ].animate.set_color(GREEN),
                    A.edges[(7, 9) ].animate.set_color(ORANGE),
                    A.edges[(7, 10)].animate.set_color(BLUE),
                    A.edges[(8, 10)].animate.set_color(YELLOW),
                    C.edges[(0, 1)].animate.set_color(RED),
                    C.edges[(0, 2)].animate.set_color(GREEN),
                    C.edges[(0, 3)].animate.set_color(BLUE),
                    C.edges[(0, 4)].animate.set_color(ORANGE),
                    C.edges[(0, 5)].animate.set_color(PINK),
                    C.edges[(0, 6)].animate.set_color(WHITE),
                    C.edges[(0, 7)].animate.set_color(GRAY),
                    C.edges[(1, 2)].animate.set_color(WHITE),
                    C.edges[(1, 3)].animate.set_color(GREEN),
                    C.edges[(1, 4)].animate.set_color(GRAY),
                    C.edges[(1, 5)].animate.set_color(ORANGE),
                    C.edges[(1, 6)].animate.set_color(BLUE),
                    C.edges[(1, 7)].animate.set_color(PINK),
                    C.edges[(2, 3)].animate.set_color(ORANGE),
                    C.edges[(2, 4)].animate.set_color(PINK),
                    C.edges[(2, 5)].animate.set_color(BLUE),
                    C.edges[(2, 6)].animate.set_color(GRAY),
                    C.edges[(2, 7)].animate.set_color(RED),
                    C.edges[(3, 4)].animate.set_color(RED),
                    C.edges[(3, 5)].animate.set_color(GRAY),
                    C.edges[(3, 6)].animate.set_color(PINK),
                    C.edges[(3, 7)].animate.set_color(WHITE),
                    C.edges[(4, 5)].animate.set_color(WHITE),
                    C.edges[(4, 6)].animate.set_color(GREEN),
                    C.edges[(4, 7)].animate.set_color(BLUE),
                    C.edges[(5, 6)].animate.set_color(RED),
                    C.edges[(5, 7)].animate.set_color(GREEN),
                    C.edges[(6, 7)].animate.set_color(ORANGE),
                    )

        self.next_section()

        g = Group(A, C).arrange(buff=1.2).move_to(ORIGIN)

        a = Tex("Vizing's Theorem").scale(2).next_to(g, UP, buff=0.8)
        self.add(a)

        fg = Group(a, g)

        self.camera.frame.move_to(fg).set_height(fg.get_height() * 1.4)


        self.wait()


