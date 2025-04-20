from manim import *

class SquareToCircle(Scene):
    def construct(self):
        triangle = Triangle()
        triangle.set_fill(PINK, opacity=0.5)

        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)
        circle.rotate(PI / 4)
        
        square = Square()
        square.set_fill(PINK, opacity=0.5)

        self.play(Create(circle))
        self.play(ReplacementTransform(circle, triangle))
        self.play(ReplacementTransform(triangle, square))
        self.wait(0.5)