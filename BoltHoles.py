
print( "Welcome to Tonys Basic Bolt Hole G-Code Creator")
print("This program will create G-code for peck drilling a series of bolt holes based on the parameters you input. Please follow the prompts to input the necessary parameters.")      

ToolNo = input("What tool number are you using? ") 
WrkOfset = input("What is the work offset? ") 
SpdleRpm = input("What is the spindle RPM? ") 

XPos = input("What is the X position of the centre of the bolt holes? ") 
XPos = float(XPos)

YPos = input("What is the Y position of the centre of the bolt holes? ") 
YPos = float(YPos)

ZRapid = input("What is the rapid Z position? ") 
ZRapid = float(ZRapid)

Peck = input("What is the Z peck size? ")
Peck = float(Peck)

ZDepth = input("Drill Depth in Z? ") 
ZDepth = float(ZDepth) 

pcd = input("What is the PCD of the bolt holes")
pcd = float(pcd)

Noholes = input("How many holes?")
Noholes = int(Noholes)

Feedrate = input("What is the feedrate? ") 
Feedrate = float(Feedrate)



print("Generating G-code...") 
print("M97 P8000") 
print("M05") 
print("T" + ToolNo + " M06")  
print("M03 P" + SpdleRpm) 
print("G" + WrkOfset) 
print("G40") 
print("G98 G17") 
print("G00 X" + str(XPos) + " Y" + str(YPos))
print("G" + WrkOfset + " G00 Z" + str(ZRapid) + " G43 " + ToolNo + " M08") 
print("G83 Z-" + str(ZDepth) + " R" + str(ZRapid) + " Q" + str(Peck) + " F" + str(Feedrate) + " L0")
print("G70 I" + str(pcd/2) + " J0 L" + str(Noholes))
print("G80")
print("G00 Z" + str(ZRapid) + " M09")
print("M05")
print("M97 P8000")
print("M30")


print("N8000") 
print("G00 G90 G99 G97 M09") 
print("G53 G00 G40 Z0") 
print("G53 G00 G40 X0 Y0") 
print("M01") 
print("M99") 