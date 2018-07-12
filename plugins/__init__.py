__all__ = ['plugins_']
def values_plugin(path):
	import os, re, time
	pluginsFile = []
	curPath = os.path.dirname(os.path.realpath(__file__))
	_path = "/{}/".format(path)
	path_ = "/{}".format(path)
	updateTime = time.strftime('    - Date: %d/%m \n    - Time: %H:%M:%S', 
														 time.localtime(os.path.getatime((curPath + _path))))
	Files = [curPath + _path + f for f in os.listdir(curPath + path_) if re.search('^.+\.py$', f)]
	for files in Files:
		values = {}
		with open(files, encoding='utf-8') as file:
			code = compile(file.read(), files, 'exec')
			exec(code, values)
			pluginsFile.append(values['plugin'])
	return pluginsFile, updateTime
def plugins_():
		global plugins
		from langs import lang
		plugins = []
		global advanced, utility, entertainment
		advanced, update_advanced = values_plugin('advanced')
		plugins += advanced
		utility, update_utility = values_plugin('utility')
		plugins += utility
		entertainment, update_entertainment = values_plugin('entertainment')
		plugins += entertainment
		info = lang('info', 'plugin', sudo=True).format(
			infoplugins=len(plugins),
			infoutility=len(utility), 
			infoupdate_utility=update_utility,
			infoentertainment=len(entertainment), 
			infoupdate_entertainment=update_entertainment,
			infoadvanced=len(advanced), 
			infoupdate_advanced=update_advanced)
		return info
