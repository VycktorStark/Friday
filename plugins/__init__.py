__all__ = ['plugins_']
def plugins_():
		global plugins
		plugins = []
		import os, re
		curPath = os.path.dirname(os.path.realpath(__file__))
		pluginFiles = []
		advanced = [curPath + "/advanced/" + f for f in os.listdir(curPath + "/advanced") if re.search('^.+\.py$', f)]
		pluginFiles += advanced
		utility = [curPath + "/utility/" + f for f in os.listdir(curPath + "/utility") if re.search('^.+\.py$', f)]
		pluginFiles += utility
		entertainment = [curPath + "/entertainment/" + f for f in os.listdir(curPath + "/entertainment") if re.search('^.+\.py$', f)]
		pluginFiles += entertainment
		for file in pluginFiles:
			values = {}
			with open(file, encoding='utf-8') as f:
				code = compile(f.read(), file, 'exec')
				exec(code, values)
			plugins.append(values['plugin'])
		return
