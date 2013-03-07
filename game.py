# Template pycap game v1.0
# Written by Farbs

appIni = {	"mCompanyName"		: "CompanyNameGoesHere",
		"mFullCompanyName"	: "CompanyNameGoesHere",
		"mProdName"		: "Pycap Template Game",
		"mProductVersion"	: "1.0",
		"mTitle"			: "Pycap Template Game v1.0",
		"mRegKey"			: "PycapTest",
		"mWidth"			: 800,
		"mHeight"			: 600,
		"mAutoEnable3D"	: 1,
		"mVSyncUpdates"	: 1 }

import Pycap as PC
PCR = None
import tile as TS

KEYLEFT		= 65
KEYRIGHT	= 68
KEYUP		= 87
KEYDOWN		= 83

leftDown = 0
rightDown = 0
upDown = 0
downDown = 0

scrollX = 100
scrollY = 100

def loadBase():
	import PycapRes
	global PCR
	PCR = PycapRes

def init():
	global map
	map = TS.Map("Res\\Tilesets\\Tileset.tsm")
	map.buildMap()

def update( delta ):
	global scrollX
	global scrollY
	
	PC.markDirty()
	
	scrollX += (rightDown - leftDown) * 2
	scrollY += (downDown - upDown) * 2
	
	map.update(delta, scrollX, scrollY)

def draw():
	PC.setColour(255, 255, 255, 255)
	PC.fillRect(0, 0, 800, 600)
	map.draw()
	
def keyDown(key):
	if key == KEYLEFT:
		global leftDown
		leftDown = 1
	elif key == KEYRIGHT:
		global rightDown
		rightDown = 1
	elif key == KEYUP:
		global upDown
		upDown = 1
	elif key == KEYDOWN:
		global downDown
		downDown = 1 

def keyUp(key):
        if key == KEYLEFT:
		global leftDown
		leftDown = 0
	elif key == KEYRIGHT:
		global rightDown
		rightDown = 0
	elif key == KEYUP:
		global upDown
		upDown = 0
	elif key == KEYDOWN:
		global downDown
		downDown = 0
