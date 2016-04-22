import sqlite3, datetime

db_file="maindb.db"

class CTCPhotoDB:
	def __init__(self):
		self.conn=sqlite3.connect(db_file)
		self.cursor=self.conn.cursor()

	def createTables(self):
		cmds=['''
		CREATE TABLE IF NOT EXISTS photos(
			ID PRIMARY KEY,
			file_name CHAR(50),
			set_id INT,
			order_in_set INT,
			hosted_url CHAR(255),
			hosted_id CHAR(15),
			refering_url CHAR(125),
			last_updated DATETIME,
			synced TINYINT
		);
		''',
		'''
		CREATE TABLE IF NOT EXISTS sets(
			set_id PRIMARY KEY,
			name CHAR(125)
		);
		''']

		for cmd in cmds:
			self.cursor.execute(cmd)

	def addSet(self, pack):
		ipt=self.updatedInput({"set_id":"","name":""},pack)
		cmd='''
		INSERT OR IGNORE INTO sets VALUES
		('{set_id}','{name}')
		'''.format(**ipt)

		#print cmd

		self.cursor.execute(cmd)

	def addPhoto(self,pack):
		basePack={
			"ID":"",
			"file_name":"",
			"set_id":"",
			"order_in_set":-1,
			"hosted_url":"",
			"hosted_id":"",
			"refering_url":"",
			"last_updated":datetime.datetime.now(),
			"synced":0
		}
		ipt=self.updatedInput(basePack,pack)
		cmd='''
		INSERT OR IGNORE INTO photos VALUES
		('{ID}','{file_name}','{set_id}',{order_in_set},'{hosted_url}','{hosted_id}','{refering_url}','{last_updated}',{synced})
		'''.format(**ipt)

		#print cmd

		self.cursor.execute(cmd)

	def commit(self):
		self.conn.commit()

	def updatedInput(self, base, newData):
		keys=base.keys()
		base.update(newData)
		res={k:base[k] for k in base if k in keys}
		return res


if __name__=="__main__":
	query=CTCPhotoDB()
	query.createTables()
	query.commit()
	#query.addSet({"set_id":"234125","name":"Bla"})
	#query.addSet({"name":"world"})
	'''
	query.addPhoto({
			"ID":"1234",
			"file_name":"PIC01242",
			"set_id":"1214253",
			"order_in_set":3,
		})
	'''