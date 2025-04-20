from manim import *

class DifferenceRotate(Scene):
  def construct(self):
    left_square = Square(color=RED, opacity=1,).shift(2 * LEFT) # left_square
    right_square = Square(color=WHITE, opacity=1,).shift(2 * RIGHT) # right_square
    
    self.play(
      left_square.animate.rotate(PI), # left_square animation
      
      AnimationGroup( # right_square animation
      Rotate(right_square, angle=PI),
      lag_ratio=0
      )
    )
    self.wait(0.5)