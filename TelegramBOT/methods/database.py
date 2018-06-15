import psycopg2
class Conexao(object):
	_db=None;
	def __init__(self):
		self._db = psycopg2.connect(
		database = config.DATABASE['database'],
		user = config.DATABASE['user'],
		password = config.DATABASE['password'],
		host = config.DATABASE['host'],
		port = config.DATABASE['port']
	)
	def create(self, sql): #create table condition in database
				db = self._db
				cursor = db.cursor()
				cursor.execute(sql)
				db.commit()
				db.close()
	def delete(self, sql): #delete table condition in database
			db = self._db
			cursor = db.cursor()
			cursor.execute(sql)
			db.commit()
			db.close()
	def consult(self, sql): #query table condition in database
			cursor = self._db.cursor()
			cursor.execute(sql)
			return cursor.fetchall()
	def insert(self, sql): #insert table condition in database
			db = self._db
			cursor = db.cursor()
			cursor.execute(sql)
			db.commit()
			db.close()