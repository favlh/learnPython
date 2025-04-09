from manim import *

class SquareToCircle(Scene):
    def construct(self):
        triangle = Triangle()
        triangle.set_fill(PINK, opacity=0.5)

        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)
        circle.rotate(PI / 4)

        self.play(Create(circle))
        self.play(Transform(circle, triangle))
        self.play(FadeOut(circle))
        
        self.wait(0.5)