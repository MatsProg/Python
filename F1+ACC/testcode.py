from START import *
import winsound

class overlay():
	def __init__(self):
		self.ex = Example()
		self.ex.bits()
		self.RPM = ex.RPM
		winsound.PlaySound("C:\Program Files (x86)\FreePIE\pylib\alarm.wav", winsound.SND_FILENAME)
	def RPM1(self):
		if self.RPM > self.RPMsound:
			winsound.PlaySound("C:\Program Files (x86)\FreePIE\pylib\alarm.wav", winsound.SND_FILENAME)