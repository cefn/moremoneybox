from time import sleep
import scanplayer
import mcp

io = mcp.MCP23017()
# monitors and prints some input pins
inPins = [8,9,0,1,2,3,4,5,6,7]
for pinNum in inPins:
    io.setup(pinNum, mcp.IN)

print(io.input_pins(inPins))

print("Loading Tracks")
player = scanplayer.ScanPlayer()
availableFolders = list(player.tracks.keys())

slotTriggered = None
print("Monitoring slots")
while True:
    if not player.playing():
        slotTriggered = None
    slotsUncovered = io.input_pins(inPins)
    if False in slotsUncovered:
        firstCovered = slotsUncovered.index(False)
        if firstCovered != slotTriggered:
            slotTriggered = firstCovered
            print("{} inserted".format(firstCovered))
            if slotTriggered in player.tracks:
                print("{} playing".format(firstCovered))
                player.playFolder(slotTriggered)