import mcp

io = mcp.MCP23017()

# controls some output pins
outPins = list(range(0,8))
nextVals = {}
for pinNum in outPins:
    io.setup(pinNum, mcp.OUT)
    nextVals[pinNum] = True
io.output_pins(nextVals)

# monitors and prints some input pins
inPins = list(range(7,2, -1)) + list(range(8,13))
for pinNum in inPins:
    io.setup(pinNum, mcp.IN)
while True:
    print([ 1 if val else 0 for val in io.input_pins(inPins)])
