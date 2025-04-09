from manim import *

class HelloManim(Scene):
    def construct(self):
        text = Text("Hello, Mom!", font_size=72, color=BLUE)
        self.play(Write(text))
        self.wait(1)