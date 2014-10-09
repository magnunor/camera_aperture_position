import matplotlib.pyplot as plt
from camera_position_tools import SquareObject, CircleObject

#Everything in relation to HR camera coordinate system

#There are two different objects: CircleObject and SquareObject
#CircleObject has the input: 
#Center position, tuple. For example: (10,-5)
#Radius, number. For example: 312
#Label, string. For example "Beam stopper"
#color, string. For example "Red" (this is optional)
#
#SquareObject
#Center position, tuple. For example: (10,-5)
#sideSize, number. Length of sides in the square. For example 42
#label, string. For example "Beam stopper"
#rotation, number. Counter-clockwise rotation. For example, 30. (this is optional)
#color, string. For example "Red". (this is optional)

BeamStopper = CircleObject((-3,-32),133./2, "Beam stopper", color="blue")
GifAperture1 = CircleObject((7.38,-43.57),298.87/2, "GIF 5mm aperture", color="red")
GifAperture2 = CircleObject((7.62,-43.80),148.35/2, "GIF 2.5mm aperture", color="brown")
GHAADFInnerRadius = CircleObject((25.67,-30.94),484.1/2, "Gatan HAADF inner", color="purple")
GADFInnerRadius = CircleObject((13.52,-28.70),294.4/2, "Gatan ADF inner", color="cyan")
HRcamera = SquareObject((0,0), 2024, "TopHR camera", color="black")
GIFcamera = SquareObject((8.56,-43.8), 337.7, "GIF Imaging aperture", rotation=5.0, color="yellow")

object_list = (
        BeamStopper, 
        HRcamera, 
        GifAperture1, 
        GifAperture2,
        GHAADFInnerRadius,
        GADFInnerRadius,
        GIFcamera)
    
fig, ax = plt.subplots(figsize=(10,10))

for an_object in object_list:
    if an_object.__class__.__name__ == 'CircleObject':
        ax.add_patch(an_object.patch)
    if an_object.__class__.__name__ == 'SquareObject':
        ax.add_patch(an_object.patch)
ax.legend()

ax.set_ylim(-1100,1100)
ax.set_xlim(-1100,1100)
ax.set_axis_off()
fig.tight_layout()
fig.savefig("camera_overview.png", dpi=300)
