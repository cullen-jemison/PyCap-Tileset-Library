""" 
	Pycap Tileset Engine
	copyright (c) Cullen Jemison 2013
"""

from ConfigObj import ConfigObj
import Pycap as PC

class Map:
	def __init__(self, f):
		# load the map file
		tsm = ConfigObj(f)
		
		# construct the tiles dictionary
		self.tiles = tsm['tileset']
		
		# load map array
		self.map = tsm['map']['tiles'].split()
		
		# construct the alias dictionary
		tilenames = tsm['tileset'].keys() # obtain a list of tile names
		self.aliases = {}
		for i in tilenames:
			self.aliases[tsm['tileset'][i]['alias']] = i
			
		# load explicit map metadata
		self.metadata = tsm['map']
		del self.metadata['tiles']
		
	def buildMap(self):
		# create the tile entities that will make up the map
		self.Tiles = []
		for j in self.map:
			self.Tiles.append(Tile(self.tiles[self.aliases[j]]))
			
	def update(self, delta, sx, sy):
		# update all of the Tile locations from global scrolling variables
		column = 0
		row = 0
		for i in self.Tiles:
			i.update(delta, sx + int(self.metadata['size'])* row, sy + int(self.metadata['size']) * column, int(self.metadata['size']))
			row += 1
			if row > int(self.metadata['width'])-1:
				column += 1
				row = 0
			
	def draw(self):
		for i in self.Tiles:
			i.draw()
		
			
class Tile:
	def __init__(self, d):
		self.definition = d
		self.x = 0
		self.y = 0
		self.s = 5
		
	def update(self, delta, x, y, s):
		self.x = x
		self.y = y
		self.s = s
		
	def draw(self):
		if self.definition.has_key('image'):
			print "image tiles not yet supported"
		elif self.definition.has_key('color'):
			PC.setColour(TileColors[self.definition['color']]['red'], TileColors[self.definition['color']]['green'], TileColors[self.definition['color']]['blue'], 255)
			PC.fillRect(self.x, self.y, self.s, self.s)
		else:
			print "tile must have color or image attribute"
			
			
TileColors = {
	'black': {
		'red': 0,
		'green': 0,
		'blue': 0,
		},
	'white': {
		'red': 255,
		'green': 255,
		'blue': 255,
		},
	'red': {
		'red': 255,
		'green': 0,
		'blue': 0,
		},
	'green': {
		'red': 0,
		'green': 255,
		'blue': 0,
		},
	'blue': {
		'red': 0,
		'green': 0,
		'blue': 255,
		}
	}
	
		