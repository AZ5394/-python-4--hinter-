# coding:utf-8
# @Author:AZ5394
# GitHub:github.com/AZ5394

import sqlite3, random, time

with sqlite3.connect('database.db') as conn:
	c = conn.cursor()
	c.execute('select word,paraphrase from dictionary')
	words = c.fetchall()

	while True:
		rand = random.randint(0, len(words))
		print(f'\r{words[rand][0]}--------{words[rand][1]}', end='')
		time.sleep(1)

