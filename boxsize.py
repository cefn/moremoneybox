from math import *
plyWidth = 6
cashWidth = 300
cashHeight = 240
cashDepth = 90
backHeight = 935
backWidth = 590
degToRad = 1.0 / 360.0 * 2.0 * pi 
faceAngle = 10.0 * degToRad # angle downwards of face - was 15
sideAngle = 26 * degToRad # angle outwards, (difference from normal right-angle of cabinet) 
faceBorders = plyWidth / cos(faceAngle) * 2.0
faceHeight = cashHeight + (tan(faceAngle) * cashDepth) + faceBorders
topTaper = (sin(faceAngle) * faceHeight)
boxDepth = faceHeight * cos(faceAngle)
sideWidth = boxDepth / cos(sideAngle)
sideTaper = sideWidth * sin(sideAngle)
sideBorders = plyWidth * cos(sideAngle) * 2.0
frontHeight = backHeight - topTaper
frontWidth = backWidth - (sideTaper * 2.0)
insetHeight = faceHeight - faceBorders
insetBackWidth = backWidth - sideBorders
insetFrontWidth = frontWidth - sideBorders
insetTaper = (insetBackWidth - insetFrontWidth) / 2
frontJointAngle = (45 * degToRad) - (sideAngle * 0.5)
backJointAngle = (45 * degToRad) + (sideAngle * 0.5)