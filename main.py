from manim import *
import random

class ExponentialGraph(Scene):

    a = 0
    b = 2
    c = 0

    def construct(self):
        self.create_func()

        ax = Axes(
            x_range=[-4, 4, 1],
            y_range=[-16, 16, 2],
            tips=False,
            axis_config={"include_numbers": True},
        )
        ax.stroke_opacity = 0.1

        # x_min must be > 0 because log is undefined at 0.
        exp_func = ax.plot(lambda x: self.function_exp(x), color=DARK_BLUE)

        self.add(ax)
        self.wait(0.5)
        self.play(Create(exp_func, run_time=2))
        self.wait(1)

        for i in range(-3, 4, 1):
            point = ax.coords_to_point(i, self.function_exp(i))
            dot = Dot(point, color=WHITE, fill_opacity=0.5, stroke_opacity=1, stroke_width=1.5, fill_color=GRAY, stroke_color=WHITE, radius=0.05)
            self.play(Create(dot))

            text = Tex(f"({i}, {round(self.function_exp(i), 2)})", color=YELLOW).scale(0.5).next_to(ax.c2p(i, self.function_exp(i)))
            self.play(Write(text))

            self.wait(0.5)

        # func = MathTex(rf'f(x) &= {self.a} * {self.b}^x + {self.c}').to_corner(UL)
        if self.a < 0:
            func = MathTex(rf'f(x) &= {self.a}({self.b}^x) + {self.c}').to_corner(DL)
        else:
            func = MathTex(rf'f(x) &= {self.a}({self.b}^x) + {self.c}').to_corner(DR)

        self.play(Write(func))
        self.wait(1)

    def function_exp(self, x) -> int | float:
        return (self.a * self.b**x) + self.c

    def create_func(self) -> None:
        while self.a == 0:  # a cannot be zero
            self.a = random.randint(-4, 4)

        self.b = random.randint(2, 5)
        self.c = random.randint(-10, 10)
