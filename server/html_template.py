
class HTML_Template:



	def __init__(self, template_path):
		template_file = open(template_path, 'r')
		self.html = template_file.read()


	def generate_html(self):
		return self.html