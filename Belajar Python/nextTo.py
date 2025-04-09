from manim import *

class nextTo(Scene):
  def construct(self):
      circle = Circle()
      circle.set_fill(BLUE, opacity=0.5)
    
      triangle = Triangle()
      triangle.set_fill(BLUE, opacity=0.5)
      
      square = Square()
      square.set_fill(BLUE, opacity=0.5)
      
      triangle.next_to(circle, RIGHT, buff=0.5)
      square.next_to(circle, LEFT, buff=0.5)
      self.play(Create(circle), Create(square), Create(triangle), runtime=1.25)
      self.play(FadeOut(circle, square, triangle), runtime=1)