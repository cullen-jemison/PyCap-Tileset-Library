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

def loadBase():
	import PycapRes
	global PCR
	PCR = PycapRes

def init():
	map = TS.Map()
	map.loadTileset("Res\\Tilesets\\Tileset.tsm")
	print map.getTiles()

def update( delta ):
	PC.markDirty()

def draw():
	pass
