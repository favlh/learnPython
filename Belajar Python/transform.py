from manim import *

class TransformPy(Scene):
  def construct(self):
    teks1 = Text("Hello You're My ..")
    teks2 = Text("NIGGERS")
    teks3 = Text("Just Kidding (LOL ITS TRUE THO)")
    
    self.play(Write(teks1))
    self.wait(0.25)
    
    self.play(ReplacementTransform(teks1, teks2))
    self.wait(0.25)
    
    self.play(ReplacementTransform(teks2, teks3))
    self.wait(0.5)
    
# To make another scene, just copy the class and change the name
# and the text. You can also change the animation by changing the function