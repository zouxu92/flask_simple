# -*- coding: utf-8 -*-
'''作项目启动文件'''
from blog import app

@app.route('/')
def hello_world():
	return "Hello World!"

if __name__ == '__main__':
	app.run(debug=True)