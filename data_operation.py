# coding:utf-8
# @Author:AZ5394
# GitHub:github.com/AZ5394
import sqlite3

# 创建数据库及单词表
def create_database():
	with sqlite3.connect("database.db") as conn:
		cursor = conn.cursor()
		# 创建单词表
		cursor.execute("""
			CREATE TABLE IF NOT EXISTS dictionary(
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				word TEXT,
				paraphrase TEXT,
				isShow TEXT DEFAULT 'true',
				delete_button NULL
			);
		""")
# 添加单词和释义到单词表
def add_word():
	with sqlite3.connect('database.db') as conn, open('cet4-words.txt', 'rt', encoding='utf-8') as file:
		c = conn.cursor()
		# 添加单词和释义到单词表
		for line in file:
			word, paraphrase = line.strip().split(' ', 1)
			c.execute("INSERT INTO dictionary (word, paraphrase) VALUES (?, ?)", (word, paraphrase))


# 对单词进行排序
def sort_data():
	with sqlite3.connect("database.db") as conn:
		cursor = conn.cursor()
		# 创建单词表用于排序
		cursor.execute("""
	        CREATE TABLE IF NOT EXISTS sorted_table(
	            id INTEGER PRIMARY KEY AUTOINCREMENT,
	            word TEXT,
	            paraphrase TEXT,
	            isShow TEXT DEFAULT 'true',
	            delete_button NULL
	        );
	    """)
		# 从原单词表中插入数据到新单词表
		cursor.execute("""
	       INSERT INTO sorted_table(word, paraphrase)
	       SELECT word, paraphrase
	       FROM dictionary
	       ORDER BY LOWER(word) ASC;
	           """)
		# 删除原单词表
		cursor.execute("DROP TABLE dictionary;");
		# 把新单词表命名为原来的单词表
		cursor.execute("ALTER TABLE sorted_table RENAME TO dictionary;");


create_database()
add_word()
sort_data()