from manim import *

class ObjectText(Scene):
  def construct(self):
    text = Text("Hi")
    text.set_color_by_gradient(WHITE, BLUE)
    
    text1 = Text("My name is Favian")
    text1.set_color_by_gradient(WHITE, BLUE)
    
    circle = Circle(radius=1.5, color=BLUE).set_fill(BLUE, opacity=0.5)
    
    # circle to text
    self.play(Create(circle))
    
    self.play(circle.animate.rotate(PI/2).shift(UP*1))
    self.wait(0.25)
    
    self.play(ReplacementTransform(circle, text, runtime=1))
    
    # text to text1
    self.play(text.animate.shift(DOWN*1), runtime=0.1)
    self.wait(0.25)
    
    self.play(text.animate.shift(UP*1), runtime=0.1)
    self.wait(0.25)
    
    self.play(ReplacementTransform(text, text1), runtime=0.25)
    self.play(FadeOut(text1, runtime=0.5))