from manim import *
import numpy as np


class TrigTransformations(MovingCameraScene):
    def construct(self):
        phase_shift = ValueTracker(0)
        axes = Axes(
            x_range=[-2 * PI, 2 * PI, PI / 2],
            y_range=[-2, 2, 0.5],
            axis_config={"color": BLUE},
            x_axis_config={
                "include_numbers": False
            },
            y_axis_config={
                "include_numbers": True
            },
            tips=False
        )

        for (x, lbl) in [(-2, r"-2\pi"), (-1.5, r"-\frac{3}{2}\pi"), (-1, r"-\pi"), (-0.5, r"-\frac{1}{2}\pi"), (2, r"2\pi"), (1.5, r"\frac{3}{2}\pi"), (1, r"\pi"), (0.5, r"\frac{1}{2}\pi"), ]:
            axes.add(MathTex(lbl, font_size=27).next_to(axes.c2p(x * PI, 0), DOWN, buff=0.3))

        sg = axes.plot(lambda x: np.sin(x), x_range=[-2 * PI, 2 * PI])
        sg2 = axes.plot(lambda x: np.sin(x - phase_shift.get_value()), x_range=[-2 * PI, 2 * PI], color=YELLOW)

        phase_shift_text = always_redraw(lambda: Text(f"Phase Shift: {phase_shift.get_value():.2f}", font_size=24).to_edge(UP))
        self.add(phase_shift_text)

        self.play(Write(sg, run_time=2), Create(axes))

        self.wait(2)
        self.play(Transform(sg, sg2))

        self.play(phase_shift.animate.set_value(5), run_time=5, rate_func=linear)

        self.wait()

