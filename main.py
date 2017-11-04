from utime import sleep_ms, ticks_ms, ticks_diff
import scanplayer
import mcp

io = mcp.MCP23017()
# monitors and prints some input pins
inPins = list(range(7,2, -1)) + list(range(8,13))
for pinNum in inPins:
    io.setup(pinNum, mcp.IN)

print(io.input_pins(inPins))

print("Loading Tracks")
#player = scanplayer.ScanPlayer() # implicitly volume=0.5
player = scanplayer.ScanPlayer(volume=1.0)
availableFolders = list(player.tracks.keys())

playtestfrequency = 16

def run():
	playtestcounter = 0
	slotTriggered = None
	print("Monitoring Slots")
	while True:
		if slotTriggered is not None and playtestcounter >= playtestfrequency:
			playtestcounter = 0
			if not player.playing():
				slotTriggered = None
		playtestcounter += 1
		
		slotsUncovered = io.input_pins(inPins)
		if False in slotsUncovered:
			firstCovered = slotsUncovered.index(False)
			if firstCovered != slotTriggered:
				slotTriggered = firstCovered
				print("{} coin".format(firstCovered))
				if slotTriggered in player.tracks:
					print("{} play".format(firstCovered))
					player.playNext(slotTriggered)

# workaround for scanplayer which resets volume
sleep_ms(2000) # TODO can this be removed? Belt and braces
player.awaitvolume()
player.volume(1.0) 

run()
