from manim import *

class helloMom(scene):
    def construct(self):
        text = Text("Hello Mom")
        self.play(Write(text))
        self.wait(2)
        self.play(FadeOut(text))
        self.wait(1)