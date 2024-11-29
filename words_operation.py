# coding:utf-8
# @Author:AZ5394
# GitHub:github.com/AZ5394
import re

# 去重
def remove_repeat_word():
    all_words = []
    repeat_words = []
    with (open('dictionary.txt', 'rt', encoding='utf8') as file_read,
          open('cet4-words.txt', 'wt', encoding='utf8') as file_write):
        # 读取所有行

        for line in file_read:
            # 跳过空行
            line = line.strip()
            if not line:
                continue
            # 匹配单词
            word = re.findall(r'\b\w+\b', line)
            # 排查重复单词
            if word[0] in all_words:
                repeat_words.append(word[0])
                continue
            all_words.append(word[0])
            file_write.write(line+'\n')

    print(repeat_words)
    print(f'重复的单词有{len(repeat_words)}个')

# 由于爬取的网站个别单词开头是缺单词的,需要找出不完整的单词手动修改,这里可能有点难理解,可以先运行get-words,再运行reduplication,
# 再运行这个程序,去new.txt里找到对应行数就能明白了
# 不完整的单词分别是assport(应该为passport,少了p)ension(p后面多了空格)ecite(应该为recite,少了r)
# 运行完后需要手动修改,这个程序只是打印可能不完整的单词

# 通过上一轮循环单词的首字母和这轮循环单词首字母的ASCII码值进行比较
def find_mistakes(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        previous_letter = 'a'
        line_number = 0
        for line in file:
            line_number += 1
            word = line.strip()
            current_letter = word[0].lower()
            if current_letter < previous_letter:
                print(f"可能不完整的单词{line_number}: '{word}'")
            previous_letter = current_letter

