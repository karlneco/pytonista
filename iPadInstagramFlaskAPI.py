from flask import Flask

class InstaApi(object):
	app = Flask('insta_api')
	
	def __init__(self):
		pass
		
	@staticmethod
	@app.route('/ping', methods=['GET'])	
	def ping():
		return "pong"
		
	def run(self, debug=False, port=8080):
		self.app.run(port=port, debug=debug)
		
if __name__ == '__main__':
	app = Insta"Api()
	app.run()
