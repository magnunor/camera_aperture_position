from matplotlib.path import Path
import matplotlib.patches as patches
from math import cos, sin, radians

class RectangleObject:
    def __init__(self, centerPosition, sideSize1, sideSize2, label, rotation=0.0, color='black'):
        self.sideSize1 = sideSize1
        self.sideSize2 = sideSize2
        self.label = label
        self.rotation = rotation
        self.centerPosition = centerPosition
        self.color = color
        self.calculate_object_position(
                sideSize1, sideSize2, centerPosition, rotation)
        self.patch = self.make_patch()

    def get_object_dimensions(self):
        side1 = ((self.x0-self.x1)**2+(self.y0-self.y1)**2)**0.5
        side2 = ((self.x1-self.x2)**2+(self.y1-self.y2)**2)**0.5
        side3 = ((self.x2-self.x3)**2+(self.y2-self.y3)**2)**0.5
        side4 = ((self.x3-self.x0)**2+(self.y3-self.y0)**2)**0.5
        return(side1,side2,side3,side4)

    def get_center_position(self):
        return((self.x0+self.x2)*0.5, (self.y0+self.y2)*0.5)

    def make_patch(self):
        verts = [
            (self.x0,self.y0),
            (self.x1,self.y1),
            (self.x2,self.y2),
            (self.x3,self.y3),
            (self.x0,self.y0)]

        codes = [Path.MOVETO,
            Path.LINETO,
            Path.LINETO,
            Path.LINETO,
            Path.CLOSEPOLY]

        label = [
                self.label,
                ". Center: ",
                str(self.centerPosition),
                ". Side length: ",
                str(self.sideSize1),
                "x",
                str(self.sideSize2),
                ". Rotation: ",
                str(self.rotation)]
        label = ''.join(label)

        path = Path(verts, codes)
        patch = patches.PathPatch(
                path, 
                lw=2,
                fill=False,
                color=self.color,
                label=label)
        return(patch)

    def calculate_object_position(self, sideSize1, sideSize2, centerPosition, rotation):
        #This can probably be done in a much more elegant way...
        temp_x0 = -sideSize1/2. 
        temp_y0 = -sideSize2/2.
        temp_x1 = -sideSize1/2. 
        temp_y1 = sideSize2/2.
        temp_x2 = sideSize1/2. 
        temp_y2 = sideSize2/2.
        temp_x3 = sideSize1/2. 
        temp_y3 = -sideSize2/2.

        x0 = temp_x0*cos(radians(rotation))-temp_y0*sin(radians(rotation))
        y0 = temp_x0*sin(radians(rotation))+temp_y0*cos(radians(rotation))
        x1 = temp_x1*cos(radians(rotation))-temp_y1*sin(radians(rotation))
        y1 = temp_x1*sin(radians(rotation))+temp_y1*cos(radians(rotation))
        x2 = temp_x2*cos(radians(rotation))-temp_y2*sin(radians(rotation))
        y2 = temp_x2*sin(radians(rotation))+temp_y2*cos(radians(rotation))
        x3 = temp_x3*cos(radians(rotation))-temp_y3*sin(radians(rotation))
        y3 = temp_x3*sin(radians(rotation))+temp_y3*cos(radians(rotation))

        x_center_pos = centerPosition[0]
        y_center_pos = centerPosition[1]

        self.x0 = x0 + x_center_pos
        self.y0 = y0 + y_center_pos
        self.x1 = x1 + x_center_pos
        self.y1 = y1 + y_center_pos
        self.x2 = x2 + x_center_pos
        self.y2 = y2 + y_center_pos
        self.x3 = x3 + x_center_pos
        self.y3 = y3 + y_center_pos

class CircleObject:
    def __init__(self, centerPosition, radius, label, color='black'):
        self.centerPosition = centerPosition
        self.radius = radius
        self.label = label
        self.color = color
        self.patch = self.make_patch()

    def make_patch(self):
        label = [
                self.label,
                ". Center: ",
                str(self.centerPosition),
                ". Radius: ",
                str(self.radius)]
        label = ''.join(label)
        circle = patches.Circle(
                self.centerPosition,
                self.radius,
                fill=False,
                edgecolor=self.color,
                label=label)
        return(circle)

