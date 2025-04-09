from manim import *

class CreateShapes(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)
        self.play(Create(circle, run_time=2))
        self.play(FadeOut(circle, run_time=1))
        
        self.wait(0.5)
        
        triangle = Triangle()
        triangle.set_fill(BLUE, opacity=0.5)
        self.play(Create(triangle, run_time=2))
        self.play(FadeOut(triangle, run_time=1))
        
        self.wait(1.5)