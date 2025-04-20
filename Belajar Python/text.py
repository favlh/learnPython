from manim import *

class SceneMomAndDad(Scene):
  def construct(self):
    teks1 = Text("Hi Mom")
    self.play(Write(teks1))
    self.wait(0.25)

    teks2 = Text("Hi Dad")
    self.play(ReplacementTransform(teks1, teks2, runtime=0.75))
    self.wait(0.25)
    
    teks3 = Text("I Love You All!!")
    self.play(ReplacementTransform(teks2, teks3, runtime=0.75))
    self.play(FadeOut(teks3, runtime=0.25))
    
    teks4 = Text("May you be happy and healthy")
    teks4.set_color_by_gradient(RED, BLUE, GREEN)
    self.play(Write(teks4, runtime=0.75 ))
    self.play(FadeOut(teks4)) 