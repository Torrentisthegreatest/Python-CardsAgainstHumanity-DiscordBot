#Don't be an idiot! Change these values!
class Config():
	maxplayerspergame = 0
	maxnumberofgames = 0
	def __init__(self):
		#Change Presence
		self.prestype = 0
		self.prestext = ""
		#Do Not Change
		for i in range(self.maxnumberofgames):
			self.gamenum.append(i)


config = Config()
