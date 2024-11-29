# coding:utf-8
# @Author:AZ5394
# GitHub:github.com/AZ5394
import requests
import re
from bs4 import BeautifulSoup
import words_operation
import data_operation

# 爬取单词
# 目标网页URL
url = "https://www.eol.cn/html/en/cetwords/cet4.shtml"

# 发送GET请求
response = requests.get(url)
response.raise_for_status()  # 确保请求成功

# 使用BeautifulSoup解析网页内容
soup = BeautifulSoup(response.content.decode(), 'html.parser')
word_soup = soup.find('div', class_='main')

# 处理提取的单词，例如打印或保存到文件
num_write = 0
words = []
repeat_words = []

with open('dictionary.txt', 'w', encoding='utf - 8') as file:
    for p_element in word_soup.findAll('p'):
        text = p_element.get_text().strip()
        if not text.strip():  # 跳过空行
            continue
        # 用正则表达式提取单词
        word = re.findall(r'\b\w+\b', text)
        # 防止重复的单词写入
        print(word)
        if word[0] in words:
            repeat_words.append(word[0])
            continue
        num_write += 1
        words.append(word[0])

        file.write(f'{text}\n')

print("写入的行数:", num_write) # 实际上并不匹配
print(repeat_words)
print(f'重复的单词有{len(repeat_words)}个') # 实际上并不匹配

# 这里不知道为什么打印的行数和写出的行数不匹配,写入的行数还是有重复的单词,所以写了remove_repeat_word去重


# txt文本操作
words_operation.remove_repeat_word()
words_operation.find_mistakes('cet4-words.txt')



