from ConfigObj import ConfigObj

class Map:
	def __init__(self):
		map = 0
		tiles = 0
		tsm = 0
		aliases = 0
		metadata = 0
		Tiles = 0
		
	def loadTileset(self, f):
		# load the map file
		self.tsm = ConfigObj(f)
		
		# construct the tiles array for use later
		self.tiles = self.tsm['tileset']
		
		# load map array
		self.map = self.tsm['map']['tiles'].split()
		
		# fill up the alias array
		self.aliases = []
		for i in self.tiles:
			self.aliases[i[alias]] = i['tile'])
			
		# load explicit map metadata
		self.metadata = [self.tsm['map']['width'], self.tsm['map']['height'], self.tsm['map']['scale'], self.tsm['map']['size']]
		
	def buildMap(self):
		# create the tile entities that will make up the map
		Tiles = []
		for i in self.map:
			for a in self.aliases:
				if a.keys()
			Tiles.append(Tile(self.tiles[])
		