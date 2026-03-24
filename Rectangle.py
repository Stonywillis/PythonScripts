
print( "Welcome to Tonys Basic Rectangle G-Code Creator")
print("This program will create G-code for a simple rectangle based on the parameters you input. Please follow the prompts to input the necessary parameters.")      

ToolNo = input("What tool number are you using? ") 
ToolDia = input("What is the tool diameter? ") 
ToolDia = float(ToolDia)
ToolRad = (ToolDia/2)
ToolRad = float(ToolRad)

WrkOfset = input("What is the work offset? ") 
SpdleRpm = input("What is the spindle RPM? ") 

XPos = input("What is the X position of the rectangle centre? ") 
XPos = float(XPos)

YPos = input("What is the Y position of the rectangle centre? ") 
YPos = float(YPos)

ZRapid = input("What is the rapid Z position? ") 
ZRapid = float(ZRapid)
ZStart = input("What is the starting Z position? ") 
ZStart = float(ZStart)

ZCut = input("What is the Z cut increment? ")
ZCut = float(ZCut)
Nosteps = input("How many steps? ") 
Nosteps = int(Nosteps) 

XDist = input("What is the X distance of the rectangle? ") 
XDist = float(XDist)

Xcut = (XDist/2)
Xcutl = float(Xcut)

YDist = input("What is the Y distance of the rectangle? ") 
YDist = float(YDist)

Ycut = (YDist/2)
Ycutl = float(Ycut)

ConRad = input("What is the corner radius? ")
ConRad = float(ConRad)

LeadIn = input("What is the lead in radius? ")
LeadIn = float(LeadIn)  

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
print("G00 X" + str(XPos - LeadIn) + " Y" + str(Ycutl + ToolRad + LeadIn))
print("G" + WrkOfset + " G00 Z" + str(ZRapid) + " G43 " + ToolNo + " M08") 
print("G01 Z" + str(ZStart) + " F" + str(Feedrate/2))
print("M97 P301 L" + str(Nosteps))
print("G01 Z" + str(ZStart) + " F" + str(Feedrate/2))
print("G00 z" + str(ZRapid) + " M09")
print("M05")
print("M97 P8000")
print("M30")

print("N301") 
print("G91 G01 Z-" + str(ZCut) + " F" + str(Feedrate/2))
print("G90 G03 X" + str(XPos) + " Y" + str(Ycutl + ToolRad) + " R" + str(LeadIn) + " F" + str(Feedrate))
print("G01 X" + str(Xcutl - ConRad))
print("G02 X" + str(Xcutl + ToolRad) + " Y" + str(Ycutl - ConRad) + " R" + str(ToolRad + ConRad))
print("G01 Y-" + str(Ycutl - ConRad))
print("G02 X" + str(Xcutl - ConRad) + " Y-" + str(Ycutl + ToolRad) + " R" + str(ToolRad + ConRad))
print("G01 X-" + str(Xcutl - ConRad))
print("G02 X-" + str(Xcutl + ToolRad) + " Y-" + str(Ycutl - ConRad) + " R" + str(ToolRad + ConRad))
print("G01 Y" + str(Ycutl - ConRad))
print("G02 X-" + str(Xcutl - ConRad) + " Y" + str(Ycutl + ToolRad) + " R" + str(ToolRad + ConRad))
print("G01 X" + str(XPos))
print("G03 X" + str(XPos + LeadIn) + " Y" + str(Ycutl + ToolRad + LeadIn) + " R" + str(LeadIn))
print("G01 X" + str(XPos - LeadIn))
print("M99")

print("N8000") 
print("G00 G90 G99 G97 M09") 
print("G53 G00 G40 Z0") 
print("G53 G00 G40 X0 Y0") 
print("M01") 
print("M99") 