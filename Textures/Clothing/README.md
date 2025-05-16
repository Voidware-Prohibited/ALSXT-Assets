D RGB
Alpha

Hair
HairMask





Each Clothing Item should have at the minimum
DA - RGB: Diffuse A: Alpha
Mask - RGB: Color Mask, Alpha: Occlusion Mask
NDE - RB: Normal Map (Minus Blue Channel), B: Displacement, Alpha: ??
AORMS

BBDS

AORMSBBDS

R: Ambient Occulsion
G: Roughness
B: Metallic
A: Specular

R: Blood
G: Burn
B: Dirt
A: Spatter

R: Ambient Occulsion
G: Roughness
B: Metallic
C: Specular
M: Blood
Y: Burn
W: Dirt
A: Spatter

Optional

Emissive






Occlusion Mask
Defines where the Character Mesh will be occluded by the clothing. The Character Material can then make these sections invisible to prevent clipping. Optionally a Runtime Virtual Texture can combine all the Occlusion Masks into one.

Color Map
Defines the different materials or colors for the mesh. 

The following collors can be used: 
Red, Green, Blue, Cyan, Magenta, Yellow and White. 

The Clothing Master Material uses the ALSXT Material Function to access each color in the Color Mask.

Usage
Option 1: Use Color Map for 

Option 2: Use Color Map to define areaas for different in-game Materials

Importing into Unreal Engine

To optimize disk and memory usage and draw calls AO, Reflective, Metallic and Specular should be combined into a single channel packed texture TGA file called _MeshName_-AORMS.tga

R: Ambient Occulsion
G: Roughness
B: Metallic
C: Specular
M: Emissive
Y: Blood
W: Burn
A: Dirt

In-Game

Damage Levels