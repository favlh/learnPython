from manim import *

class Animation(Scene):
  def construct(self):
      circle = Circle()
      triangle = Triangle()
      
      self.play(Create(triangle)) 
      self.play(triangle.animate.rotate(PI / 2))
      self.play(Transform(triangle, circle))
      self.play(
          triangle.animate.set_fill(RED, opacity=0.5).scale(1.5).shift(UP)
      )