from manimlib import *

class SquareMove(Scene):

    def construct(self):
        s = Square(stroke_color =  BLUE_E)
        s.set_style(fill_color=BLUE_C,
                    fill_opacity=0.35,
                    stroke_width=5,
                    stroke_opacity=1)
                 
        self.play(Write(s, run_time = 3))

        self.wait(2)

        self.play(
            s.shift,2*RIGHT, 
            run_time = 3
        )
        self.wait(2)

        self.play(
            s.shift, 1*UP,
            run_time = 2
        )
        self.wait(2)



class SquareRotation(Scene):

    def construct(self):
        s = Square(stroke_color =  BLUE_E)
        s.set_style(fill_color=BLUE_C,
                    fill_opacity=0.35,
                    stroke_width=5,
                    stroke_opacity=1)
                 
        self.play(Write(s, run_time = 3))

        self.wait(2)

        self.play(
            s.rotate, 180, 
            run_time = 3
        )
        self.wait(2)

class SquareRotationUpdater(Scene):

    def construct(self):
        s = Square(stroke_color =  BLUE_E)
        s.set_style(fill_color=BLUE_C,
                    fill_opacity=0.35,
                    stroke_width=5,
                    stroke_opacity=1)
                 
        self.play(Write(s, run_time = 3))

        self.wait(2)

        s.add_updater(lambda m, dt: m.rotate(10*dt))

        self.wait(10)

class SquareAnimAsUpdater(Scene):

    def construct(self):
        s = Square(stroke_color =  BLUE_E)
        s.set_style(fill_color=BLUE_C,
                    fill_opacity=0.35,
                    stroke_width=5,
                    stroke_opacity=1)
                 
        self.play(Write(s, run_time = 3))

        self.wait(2)

        anim = turn_animation_into_updater(
            ApplyMethod(s.shift, 2*RIGHT, run_time = 2.2),
            cycle = True
            )
            
        self.wait(10)
        self.remove(anim)

        self.wait(2)

        s2 = Square(stroke_color =  RED_E)
        s2.set_style(fill_color=RED_C,
                    fill_opacity=0.35,
                    stroke_width=5,
                    stroke_opacity=1)
                 
        
        self.add(s2)
        
        anim2 = turn_animation_into_updater(
            ShowCreation(s2,run_time = 2),
            cycle = True            
        )

        self.wait(10)


class CircleUpdater(Scene):

    def construct(self):


        c = Circle(radius = 2,fill_color = BLUE, stroke_color =  BLUE_E,opacity = 0.6)
        c.set_style(fill_color=BLUE_C,
                    fill_opacity=0.35,
                    stroke_width=5,
                    stroke_opacity=1)


        self.play(Write(c, run_time = 3))
        

        self.wait(2)

        self.radius_tracker = ValueTracker(2)

        # Update circle. Animate
        c.add_updater(
            lambda m,dt: self.update_circle(c,self.radius_tracker.get_value())
            )

        self.play(
            self.radius_tracker.set_value, 0.1,
            run_time = 5)

        self.wait(2)

        self.play(
            self.radius_tracker.set_value, 3,
            run_time = 3.5)
        self.wait(2)


    
    def update_circle(self,circle,radius):
        """
        circle: manim circle
        radius: float
            new radius of circle

        """
        
        new_circle = Circle(radius =radius)
        new_circle.match_style(circle)

        circle.become(new_circle)















class AnimCircle(Scene):

    def construct(self):

        self.radius = 2
        self.c = Circle(radius =self.radius ,fill_color = BLUE, stroke_color =  BLUE_E,opacity = 0.6)
        self.c.set_style(fill_color=BLUE_C,
                    fill_opacity=0.35,
                    stroke_width=5,
                    stroke_opacity=1)


        self.play(Write(self.c, run_time = 3))
        

        self.wait(2)

        # Update circle. Animate
        self.c.add_updater(
            lambda m,dt: self.update_circle()
            )

        self.wait(10)


    
    def update_circle(self):
        """
        dt: float 
            change in scale of current circle
        circle: manim circle

        """

        self.radius  = (self.radius + 0.01) % 3 

        if self.radius < 0.1:
            self.radius  = 0.1
       
        new_circle = Circle(radius = self.radius)
        new_circle.match_style(self.c)

        self.c.become(new_circle)