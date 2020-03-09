

class Request:



	def __init__(self, byte_request):
		self.source = byte_request.decode("utf-8").split("\n")
		
		if self.source[0][0:3] == "GET":
			self.type = "GET"

		self.url = self.source[0].split(" ")[1]			# Gets the url to be loaded