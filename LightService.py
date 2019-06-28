from pybleno import *
from SwitchCharacteristic import *

class LightService(BlenoPrimaryService):
	def __init__(self):
		BlenoPrimaryService.__init__(self, {
			'uuid': 'ff10',
			'characteristics': [
				SwitchCharacteristic()
			]})
