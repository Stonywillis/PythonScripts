
print( "Welcome to Tonys Basic Interpolation G-Code Creator")
print("This program will create G-code for Interpolating a hole, or Thread Milling based on the parameters you input. Please follow the prompts to input the necessary parameters.")      

ToolNo = input("What tool number are you using? ") 
ToolDia = input("What is the tool diameter? ") 
ToolDia = float(ToolDia)
ToolRad = (ToolDia/2)
ToolRad = float(ToolRad)

WrkOfset = input("What is the work offset? ") 
SpdleRpm = input("What is the spindle RPM? ") 

XPos = input("What is the X position of the hole or thread centre? ") 
XPos = float(XPos)

YPos = input("What is the Y position of the hole or thread centre? ") 
YPos = float(YPos)

ZRapid = input("What is the rapid Z position? ") 
ZRapid = float(ZRapid)
ZStart = input("What is the starting Z position? ") 
ZStart = float(ZStart)

ZCut = input("What is the Z cut increment or thread pitch? ")
ZCut = float(ZCut)
Nosteps = input("How many steps, or threads? ") 
Nosteps = int(Nosteps) 

Diam = input("What is the diameter of the hole or thread? ") 
Diam = float(Diam)
Rad = (Diam/2)
Rad = float(Rad)

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
print("G00 X" + str(XPos) + " Y" + str(YPos) + "(All XY movements in sub-program are incremental.)")
print("G" + WrkOfset + " G00 Z" + str(ZRapid) + " G43 " + ToolNo + " M08") 
print("G01 Z" + str(ZStart) + " F" + str(Feedrate/2))
print("M97 P401") 
print("(For multiple holes add more XY positions and re-run Sub-program here.)")
print("G00 Z" + str(ZRapid + 20) + " M09")
print("M05")
print("M97 P8000")
print("M30")

print("N401")
print("G90 G01 Z" + str(ZStart) + " F" + str(Feedrate/2))
print("G91 G01 X" + str(Rad - ToolRad) + " F" + str(Feedrate/2))
print("G91 G02 Z-" + str(ZCut) + " I-" + str(Rad - ToolRad) + " F" + str(Feedrate) + " L" + str(Nosteps))
print("(For a bottom finish hole, use this line --  G02 I-" + str(Rad - ToolRad) + ")")
print("G91 G01 X-" + str(Rad - ToolRad) + " F" + str(Feedrate/2))
print("G90 G01 Z" + str(ZStart))
print("G00 Z" + str(ZRapid))
print("M99")


print("N8000") 
print("G00 G90 G99 G97 M09") 
print("G53 G00 G40 Z0") 
print("G53 G00 G40 X0 Y0") 
print("M01") 
print("M99") 