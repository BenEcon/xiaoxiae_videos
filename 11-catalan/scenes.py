from utilities import *


class StarsExample(Scene):
    def construct(self):
        trees = VGroup(*BinaryTree.generate_binary_trees(3)).arrange(buff=0.8)

        self.play(AnimationGroup(*[Write(t) for t in trees], lag_ratio=0.1))

        stars_animations = []
        for t in trees:
            StarUtilities.add_stars_to_graph(t)
            stars_animations.append(CreateStars(t))

        self.play(*stars_animations)

        #self.play(ChangeStars(trees[2], 5))

        self.play(*[FadeOut(t) for t in trees])


class BuildStarsExample(Scene):
    def construct(self):
        tree = BinaryTree.generate_binary_trees(7)[72]

        self.play(Write(tree))

        StarUtilities.add_stars_to_graph(tree)

        self.play(CreateStars(tree))

        for i in range(2):
            self.play(*RemoveHighestStar(tree))


class DyckPathExamplesNew(MovingCameraScene):
    def construct(self):
        self.next_section()

        dyck_paths = Tex(r"Dyck Paths").scale(2)

        self.play(Write(dyck_paths))

        good_paths = VGroup(
            DyckPath([1, -1, 1, 1, -1, 1, -1, -1]),
            DyckPath([1, 1, 1, -1, -1, -1, 1, -1]),
        ).arrange(buff=1.5).shift(DOWN)

        good_paths[0].align_to(good_paths[1], DOWN)

        self.play(
            AnimationGroup(
                dyck_paths.animate.shift(UP * 1.25),
                AnimationGroup(*[Write(p) for p in good_paths], lag_ratio=0.3),
                lag_ratio=0.5,
            )
        )

        #self.play(
        #    good_paths.animate.arrange(DOWN, buff=0.54).move_to(LEFT * 3 + DOWN * 0.7),
        #    dyck_paths.animate.move_to(LEFT * 3 + UP * 1.5),
        #    run_time=1.25
        #)

        return

        bad_paths = VGroup(
            DyckPath([-1, 1, 1, -1, 1, -1]),
            DyckPath(list(reversed([-1, -1, 1, 1, 1, -1, -1]))),
            DyckPath([1, 1, -1, 1]),
        ).arrange(DOWN, buff=0.35).move_to(RIGHT * 3 + UP * 0.7)

        self.play(AnimationGroup(*[Write(p) for p in bad_paths], lag_ratio=0.1))

        cross = Tex(r"$\times$").next_to(bad_paths, DOWN, buff=0.7).scale(2).set_color(RED)

        self.play(FadeIn(cross, shift=DOWN * 0.2))

        self.next_section()

        featured_path = good_paths[0]

        # transition
        self.play(
            self.camera.frame.animate.move_to(featured_path).set_width(featured_path.width * 1.5),
            FadeOut(good_paths[1]),
            FadeOut(good_paths[2]),
            FadeOut(bad_paths),
            FadeOut(cross),
            FadeOut(dyck_paths),
        )

        self.play(
            AnimationGroup(
            *list(map(lambda x: AnimationGroup(*x), zip(
                [featured_path.path.edges[(u, v)].animate.set_color(GREEN if featured_path.deltas[u] == 1 else RED)
                  for (u, v) in featured_path.path.edges],
                [Flash(
                    featured_path.path.edges[(u, v)],
                    line_width=0.04, flash_radius=0.05, line_stroke_width=1, line_length=0.04,
                    color=(GREEN if featured_path.deltas[u] == 1 else RED)
                    )
                  for (u, v) in featured_path.path.edges],
                ))),
            lag_ratio=0.05,
            )
        )


class DyckPathExamples(MovingCameraScene):
    def construct(self):
        self.next_section()

        good_paths = VGroup(
            DyckPath([1, -1, 1, 1, -1, 1, -1, -1]),
            DyckPath([1, 1, 1, -1, -1, -1, 1, -1]),
            DyckPath([1, -1, 1, -1, 1, -1]),
        ).arrange()

        good_paths[0].shift(UP)
        good_paths[1].shift(DOWN)
        good_paths[2].shift(UP)

        self.play(AnimationGroup(*[Write(p) for p in good_paths], lag_ratio=0.1))

        # animate arrange paths in a slightly better-looking order
        good_paths = VGroup(good_paths[0], good_paths[2], good_paths[1])

        self.play(good_paths.animate.arrange(DOWN, buff=0.54).move_to(LEFT * 3 + DOWN * 0.7), run_time=1.25)

        dyck_paths = Tex(r"Dyck Paths").next_to(good_paths, UP, buff=0.7)

        self.play(Write(dyck_paths))

        bad_paths = VGroup(
            DyckPath([-1, 1, 1, -1, 1, -1]),
            DyckPath(list(reversed([-1, -1, 1, 1, 1, -1, -1]))),
            DyckPath([1, 1, -1, 1]),
        ).arrange(DOWN, buff=0.35).move_to(RIGHT * 3 + DOWN * 0.7)

        self.play(AnimationGroup(*[Write(p) for p in bad_paths], lag_ratio=0.1))

        cross = Tex(r"$\times$").next_to(bad_paths, UP, buff=0.7).scale(2).set_color(RED)

        self.play(FadeIn(cross, shift=UP * 0.2))

        self.next_section()

        featured_path = good_paths[0]

        # transition
        self.play(
            self.camera.frame.animate.move_to(featured_path).set_width(featured_path.width * 1.5),
            FadeOut(good_paths[1]),
            FadeOut(good_paths[2]),
            FadeOut(bad_paths),
            FadeOut(cross),
            FadeOut(dyck_paths),
        )

        self.play(
            AnimationGroup(
            *list(map(lambda x: AnimationGroup(*x), zip(
                [featured_path.path.edges[(u, v)].animate.set_color(GREEN if featured_path.deltas[u] == 1 else RED)
                  for (u, v) in featured_path.path.edges],
                [Flash(
                    featured_path.path.edges[(u, v)],
                    line_width=0.04, flash_radius=0.05, line_stroke_width=1, line_length=0.04,
                    color=(GREEN if featured_path.deltas[u] == 1 else RED)
                    )
                  for (u, v) in featured_path.path.edges],
                ))),
            lag_ratio=0.05,
            )
        )



class AllDyckPaths(Scene):
    def construct(self):
        dp = [
            VGroup(*DyckPath.generate_dyck_paths(1)).arrange_in_grid(cols=1).set_width(1),
            VGroup(*DyckPath.generate_dyck_paths(2)).arrange_in_grid(cols=1).set_width(1.2),
            VGroup(*DyckPath.generate_dyck_paths(3)).arrange_in_grid(cols=1).set_width(1.5),
            VGroup(*DyckPath.generate_dyck_paths(4)).arrange_in_grid(cols=2).set_width(2.4),
        ]

        table = Table(
            [dp],
            element_to_mobject = lambda x: x,
            row_labels=[VGroup(Tex("Dyck"), Tex("Paths")).arrange(DOWN)],
            col_labels=[Tex("1"), Tex("2"), Tex("5"), Tex("14")],
            v_buff=0.4, h_buff=0.65,
            top_left_entry=Tex("$C_n$"),
            include_outer_lines=True,
        )

        table.remove(*table.get_vertical_lines())

        self.play(
            FadeIn(table.get_entries()),
            AnimationGroup(
                Write(table.get_horizontal_lines()[0]),
                Write(table.get_horizontal_lines()[2]),
                Write(table.get_horizontal_lines()[1]),
                lag_ratio=0.25,
            ),
        )


class FullBinaryTreeExample(MovingCameraScene):
    def construct(self):
        text = Tex("Full Binary Tree").scale(4.60)
        tree = FullBinaryTree.generate_binary_trees(6)[50]

        self.camera.frame.set_width(text.width * 1.5)

        self.play(Write(text))

        points = text[0][5].get_subpaths()[1]

        avg = points[0]
        for i in points[1:]:
            avg += i
        avg /= len(points)

        diff = tree.vertices[""].get_center() - avg
        tree.shift(-diff).shift(LEFT * 0.02)

        self.add(tree.vertices[""])

        self.play(
            self.camera.frame.animate.move_to(tree.vertices[""]).scale(1/4),
            FadeOut(text),
        )

        show_first = [
            tree.vertices["l"], tree.vertices["r"],
            tree.edges[("", "l")], tree.edges[("", "r")],
        ]

        self.play(
            AnimationGroup(
                self.camera.frame.animate.shift(DOWN * 0.5),
                AnimationGroup(
                    *[Write(a) for a in show_first],
                    lag_ratio=0.1,
                ),
                lag_ratio=0.3,
            )
        )

        self.play(
            AnimationGroup(
                self.camera.frame.animate.move_to(tree).set_height(tree.height * 1.5),
                AnimationGroup(
                    *[Write(a)
                        for a in list(tree.vertices.values()) + list(tree.edges.values())
                        if a not in show_first + [tree.vertices[""]]],
                    lag_ratio=0.1,
                    run_time=1.5,
                ),
                lag_ratio=0.3,
            )
        )


class DyckToBinary(MovingCameraScene):

    def construct(self):
        dpath = DyckPath([1, -1, 1, 1, -1, -1, 1, 1, 1, -1, 1, -1, -1, -1])

        self.camera.frame.set_width(dpath.width * 1.3)

        self.play(Write(dpath, run_time=1.5))

        all_paths = VGroup(dpath)

        anim, todo = dpath.get_last_hill_animations()

        self.play(anim)

        todo()

        def parallel_animate_subpath_creation(paths: List[DyckPath], all_paths, scale, vertices, edges):
            return_paths = []

            path_tuples = []

            for path in paths:

                if len(path.deltas) == 0:
                    continue

                l_path, r_path = path.get_left_right_subpaths(scale)

                vertices.append(l_path)
                vertices.append(r_path)
                edges.append((path, l_path))
                edges.append((path, r_path))

                return_paths.append(l_path)
                return_paths.append(r_path)

                self.bring_to_back(l_path)
                l_pathcopy = l_path.copy().next_to(path, DOWN, buff=0.5).align_to(path, LEFT).scale(0.85)
                l_path.fade(1)

                self.bring_to_back(r_path)
                r_pathcopy = r_path.copy().next_to(path, DOWN, buff=0.5).align_to(path, RIGHT).scale(0.85)
                r_path.fade(1)

                if l_pathcopy.height > r_pathcopy.height:
                    r_pathcopy.align_to(l_pathcopy, DOWN)
                else:
                    l_pathcopy.align_to(r_pathcopy, DOWN)

                all_paths.add(l_pathcopy)
                all_paths.add(r_pathcopy)

                path_tuples.append((l_path, r_path, l_pathcopy, r_pathcopy))

            self.play(
                *[Transform(lp, lpc) for lp, rp, lpc, rpc in path_tuples],
                *[Transform(rp, rpc) for lp, rp, lpc, rpc in path_tuples],
                self.camera.frame.animate.move_to(all_paths).set_height(max(self.camera.frame.height, all_paths.height * 1.25)),
            )

            hill_anims = [lp.get_last_hill_animations() for lp, rp, lpc, rpc in path_tuples] + [rp.get_last_hill_animations() for lp, rp, lpc, rpc in path_tuples]

            self.play(*[a for (a, _) in hill_anims])

            for _, todo in hill_anims:
                todo()

            for lp, rp, lpc, rpc in path_tuples:
                all_paths.remove(lpc)
                all_paths.remove(rpc)
                all_paths.add(lp)
                all_paths.add(rp)

            return return_paths

        vertices = [dpath]
        edges = []

        paths = parallel_animate_subpath_creation([dpath], all_paths, 1          , vertices, edges)
        paths = parallel_animate_subpath_creation(paths, all_paths, 1 * 0.85 ** 1, vertices, edges)
        paths = parallel_animate_subpath_creation(paths, all_paths, 1 * 0.85 ** 2, vertices, edges)
        paths = parallel_animate_subpath_creation(paths, all_paths, 1 * 0.85 ** 3, vertices, edges)

        g = Graph([id(v) for v in vertices], [(id(u), id(v)) for u, v in edges])

        for path in all_paths:
            g.vertices[id(path)].move_to(path).align_to(path, DOWN)

        self.play(
            *[
            FadeTransform(path, g.vertices[id(path)])
            for path in all_paths
            ],
            self.camera.frame.animate.move_to(VGroup(*list(g.vertices.values()))).set_height(VGroup(*list(g.vertices.values())).height * 1.5),
            run_time=1.5,
        )

        for path in all_paths:
            g.remove(g.vertices[id(path)])

        self.play(
            Write(g, run_time=2)
        )


class ExpressionExample(Scene):
    def construct(self):
        expression = Tex(r"$(7+16) \times ((9 - 3) / 2)$").scale(2)

        self.play(Write(expression, run_time=0.75))

        self.play(
            AnimationGroup(
                AnimationGroup(
                    expression[0][0].animate.fade(1),
                    expression[0][5].animate.fade(1),
                    expression[0][7].animate.fade(1),
                    expression[0][15].animate.fade(1),
                ),
                AnimationGroup(
                    expression[0][1:5].animate.set_color(RED),
                    Circumscribe(expression[0][1:5], color=RED),
                    expression[0][8:15].animate.set_color(BLUE),
                    Circumscribe(expression[0][8:15], color=BLUE),
                ),
                lag_ratio=0.5,
            )
        )


class TriangulatedPolygonExample(Scene):
    def construct(self):
        p = VGroup(*LinedPolygon.generate_triangulated_polygons(7)).arrange_in_grid(rows=5).scale(0.5)

        self.play(Write(p))
