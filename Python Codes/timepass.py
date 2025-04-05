from manim import *
from math import *

# class GraphSpeedControl(Scene):
#     def construct(self):
#         axes = Axes(x_range=[-5, 5], y_range=[-5, 5])
#         graph = axes.plot(lambda x: 0.1 * (x**3), color=BLUE)

#         # Linear speed
#         self.play(Create(graph, run_time=2, rate_func=linear), run_time = 2)
#         self.wait(1)

#         # Smooth speed
#         self.play(Create(graph, run_time=2, rate_func=smooth), run_time = 2)
#         self.wait(1)

#         # Rush into speed
#         self.play(Create(graph, run_time=2, rate_func=rush_into), run_time = 2)
#         self.wait(1)

# class WritingMathFunction(Scene):
#     def construct(self):
#         function = MathTex(r"N = N_0e^{-\lambda t}")
#         self.wait()
#         self.play(Write(function),run_time = 2)
#         self.wait()
#         

# class CartesianAxis(Scene):
#     def construct(self):
#         axes = Axes(
#             x_range=[-5, 5, 1],
#             y_range=[-5, 5, 1],
#             x_length=10,
#             y_length=10,
#             axis_config={
#                 "tips": False,
#                 "include_numbers": True,
#                 "numbers_to_exclude": [0],
#                 "font_size": 24,   
#             },
#         )
#         axes.shift(LEFT * 3 + DOWN * 2)
#         self.play(Create(axes), run_time=10)
#         self.wait(1)

class Circle_Demonstrating_Sin_Cos_Curves(Scene):

    def construct(self):

        circle = Circle(
            radius = 1, 
            color = BLUE, 
            fill_opacity = 0.1,
            stroke_width = 6
        )

        dot1 = Dot(
            point = ORIGIN,
            radius = 0.1,
            color = RED,
        ).move_to(circle)

        axis = Axes(
            x_range=[-2*pi, 2*pi + pi/2, pi/2],
            y_range=[-2, 2, 1],
            x_length = 5,
            y_length = 5
        )

        sin = axis.plot(
            lambda x: np.sin(x),
            x_range = [0,2*pi],
            color = YELLOW,
            stroke_width = 3
        )

        dot2 = Dot(
            point = ORIGIN,
            radius = 0.08,
            color = RED,
        ).move_to(sin.get_start())

        circle.shift(LEFT * 5)
        axis.shift(RIGHT * 2)
        sin.shift(RIGHT * 2)

        self.play(DrawBorderThenFill(circle), Create(axis),  run_time = 2)
        self.play(
            MoveAlongPath(dot1, circle, run_time = 5, rate_func = smooth),
            MoveAlongPath(dot2, sin, run_time = 5, rate_func = smooth),
            Create(sin, run_time = 5, rate_func = smooth),

        )
        self.wait(2)