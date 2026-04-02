print("Welcome to Tony's Basic Rectangle Pocket G-Code Creator")
print("This program will create G-code for a simple rectangular pocket based on the parameters you input.")

def fmt(v):
    return f"{v:.2f}"

# --- Input Parameters ---
ToolNo = input("What tool number are you using? ")
ToolDia = input("What is the tool diameter? ")
ToolDia = float(ToolDia)
ToolRad = (ToolDia / 2)
ToolRad = float(ToolRad)

WrkOfset = input("What is the work offset? ")
SpdleRpm = input("What is the spindle RPM? ")

XPos = input("What is the X position of the pocket centre? ")
XPos = float(XPos)

YPos = input("What is the Y position of the pocket centre? ")
YPos = float(YPos)

ZRapid = input("What is the rapid Z position? ")
ZRapid = float(ZRapid)
ZStart = input("What is the starting Z position? ")
ZStart = float(ZStart)

TZCut = input("What is the Z cut increment? ")
TZCut = float(TZCut)
ZDepth = input("What is the total depth of the pocket? ")
ZDepth = float(ZDepth)

Nosteps = ZDepth / TZCut
Nosteps = int(Nosteps)

ZCut = ZDepth / Nosteps
ZCut = float(ZCut)

XDist = input("What is the X distance of the pocket? ")
XDist = float(XDist)

YDist = input("What is the Y distance of the pocket? ")
YDist = float(YDist)

StepOver = input("What is the stepover as a percentage of tool diameter (e.g., 50 for 50%)? ")
StepOver = float(StepOver) / 100 * ToolDia

Feedrate = input("What is the feedrate? ")
Feedrate = float(Feedrate)

# --- Calculate Values ---
Xcut = ((XDist / 2)-ToolRad)
Xcutl = float(Xcut)

Ycut = ((YDist / 2)-ToolRad)
Ycutl = float(Ycut)

if Xcut > Ycut:
    SideStep = Xcut/StepOver
    Xcis = Xcut/SideStep
    Ycis = Ycut/SideStep
        
if Ycut > Xcut:
    SideStep = Ycut/StepOver
    Ycis = Ycut/SideStep
    Xcis = Xcut/SideStep

Xcis = float(Xcis)
Ycis = float(Ycis)
SideStep = int(SideStep)


# --- G-Code Generation ---
print("Generating G-code...")
print("\n%")  # Program Start
print("M97 P8000")
print("M05")
print("T" + ToolNo + " M06")
print("M03 S" + SpdleRpm)  # Corrected to use 'S' for spindle speed
print("G" + WrkOfset)
print("G40")
print("G98 G17")

# --- Initial Rapid Move ---
print("G00 X" + str(XPos + StepOver) + " Y" + str(YPos))
print("G" + WrkOfset + " G00 Z" + str(ZRapid) + " G43 H" + str(ToolNo) + " M08")  # Added H offset
print("G01 Z" + str(ZStart) + " F" + str(Feedrate / 2))
print("G91 G02 I-" + str(StepOver) + " Z-" + str(ZCut/2) + " L" + str(2*Nosteps) + " F" + str(Feedrate / 2))
print("G02 I-" + str(StepOver)) 
print("G90 G01 X" + str(XPos))
print("G01 Z" + str(ZStart) + " F" + str(Feedrate))
print("M97 P701 L" + str(Nosteps))
print("G00 z" + str(ZRapid) + " M09")
print("M05")
print("M97 P8000")
print("M30")

# --- Pocketing Subroutine ---
print("\nN701")
print(f"G91 G01 Z-{fmt(ZCut)} F{fmt(Feedrate / 2)}")
print("F" + str(Feedrate))
print("G90")

for i in range(1, SideStep + 1):
    x_step = Xcis * i
    y_step = Ycis * i

    print(f"G01 X{fmt(XPos + x_step)}")
    print(f"G01 Y{fmt(YPos - y_step)}")
    print(f"G01 X{fmt(XPos - x_step)}")
    print(f"G01 Y{fmt(YPos + y_step)}")
    print(f"G01 X{fmt(XPos + x_step)}")
    print(f"G01 Y{fmt(YPos)}")
    
print("G90 G01 X" + str(XPos) + " Y" + str(YPos))
print("M99") #End of Subroutine

# --- Program End Subroutine ---
print("\nN8000")
print("G00 G90 M09")
print("G53 G00 G40 Z0")
print("G53 G00 G40 X0 Y0")
print("M01")
print("M99")
print("%")  # Program End