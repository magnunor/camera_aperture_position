import matplotlib.pyplot as plt
from camera_position_tools import RectangleObject, CircleObject

#Everything in relation to HR camera coordinate system
#Positive x and y is in the top right quadrant, negative x and positive y is in the right quadrant

#There are two different objects: CircleObject and RectangleObject
#CircleObject has the input: 
#Center position, tuple. For example: (10,-5)
#Radius, number. For example: 312
#Label, string. For example "Beam stopper"
#color, string. For example "Red" (this is optional)

#RectangleObject
#Center position, tuple. For example: (10,-5)
#sideSize1, number. Length of one of the sides in the square. For example 42
#sideSize2, number. Length of the other side in the square. For example 60
#label, string. For example "Beam stopper"
#rotation, number. Counter-clockwise rotation in degrees. For example, 30. (this is optional)
#color, string. For example "Red". (this is optional)

BeamStopper = CircleObject((-100.,15.), 150., "Beam stopper", color="blue")
GifAperture1 = CircleObject((-50.,50), 90., "GIF 2.5 mm aperture", color="red")
GifAperture2 = CircleObject((-50,50), 180, "GIF 5 mm aperture", color="brown")
GADFInnerRadius = CircleObject((-50,50), 220, "Gatan ADF inner", color="cyan")
GHAADFInnerRadius = CircleObject((-50,50), 400, "Gatan HAADF inner", color="purple")
HRcamera = RectangleObject((0,0), 4000, 2000, "Orius camera", color="black")
GIFcamera = RectangleObject((-50, 50), 500, 500, "GIF Imaging aperture", rotation=110.0, color="yellow")
JADFInnerRadius = CircleObject((0.0,0.0), 800, "Jeol ADF inner", color="darkorchid")

object_list = (
        BeamStopper, 
        HRcamera, 
        GifAperture1, 
        GifAperture2,
        GHAADFInnerRadius,
        GADFInnerRadius,
        GIFcamera,
        JADFInnerRadius)
    
fig, ax = plt.subplots(figsize=(10,10))

for an_object in object_list:
    ax.add_patch(an_object.patch)
#ax.set_position([0.0,0.0,0.5,0.8])
#ax.legend(loc='center left', bbox_to_anchor=(0.0,0.0))
ax.legend()
ax.set_ylim(-2100,2100)
ax.set_xlim(-2100,2100)
ax.set_axis_off()
fig.tight_layout()
fig.savefig("camera_overview.pdf")#, dpi=300)
