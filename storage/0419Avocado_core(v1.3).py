#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- encoding:UTF-8 -*-
# coding=utf-8
# coding:utf-8

# 功能介绍：对所有中文的字符串，将其中的英文字符转换为中文字符，去掉不必要的空格；对英文字符串，将其中的中文字符转换为英文字符，保留空格；对中英混排的字符串，分别处理。由此简化文段，方便复制粘贴。

# import pyautogui
# import time
import pyperclip
import re
import os
import rumps
import io
import sys
# from pynput.keyboard import Listener

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding="utf-8")
os.path.join(os.path.dirname(sys.argv[0]), "Avocado.db")

class Avocado(object):
    def __init__(self):
        self.config = {
            "app_name": "Avocado",
            "start": "Start Avocado",
        }
        self.app = rumps.App(self.config["app_name"])
        self.set_up_menu()
        self.start_button = rumps.MenuItem(title=self.config["start"], callback=self.start_app)
        self.app.menu = [self.start_button]

    def set_up_menu(self):
        self.app.title = "🥑"

    def start_app(self, sender):
        if sender.title.lower().startswith("start"):
            sender.title = self.config["start"]
            self.app.start = True
            # 从剪贴板导入待转换文本
            a = pyperclip.paste()

            # 【共同块】不管是全中文/全英文/中英混排，都需要清除的不规范的符号与排版
            # 清除文档排版符号
            a = a.replace('\t', '')
            a = a.replace('\r', '')
            a = a.replace('\n', '')

            # 清除连续空格（如连续两个和三个空格）
            a = a.replace('  ', ' ')
            a = a.replace('   ', ' ')

            # 清除那些引用标记，如圈圈数字和方括号引用，将两个连续空格变为一个空格
            a = re.sub(r"\{.*?\}|\[.*?\]|\〔.*?\〕|\﹝.*?\﹞", "", a)
            a = a.replace('◎', '')
            a = a.replace('®', '')
            a = a.replace('①', '')
            a = a.replace('②', '')
            a = a.replace('③', '')
            a = a.replace('④', '')
            a = a.replace('⑤', '')
            a = a.replace('⑥', '')
            a = a.replace('⑦', '')
            a = a.replace('⑧', '')
            a = a.replace('⑨', '')
            a = a.replace('⑩', '')
            a = a.replace('⑪', '')
            a = a.replace('⑫', '')
            a = a.replace('⑬', '')
            a = a.replace('⑭', '')
            a = a.replace('⑮', '')
            a = a.replace('⑯', '')
            a = a.replace('⑰', '')
            a = a.replace('⑱', '')
            a = a.replace('⑲', '')
            a = a.replace('⑳', '')
            a = a.replace('㉑', '')
            a = a.replace('㉒', '')
            a = a.replace('㉓', '')
            a = a.replace('㉔', '')
            a = a.replace('㉕', '')
            a = a.replace('㉖', '')
            a = a.replace('㉗', '')
            a = a.replace('㉘', '')
            a = a.replace('㉙', '')
            a = a.replace('㉚', '')
            a = a.replace('㉛', '')
            a = a.replace('㉜', '')
            a = a.replace('㉝', '')
            a = a.replace('㉞', '')
            a = a.replace('㉟', '')
            a = a.replace('㊱', '')
            a = a.replace('㊲', '')
            a = a.replace('㊳', '')
            a = a.replace('㊴', '')
            a = a.replace('㊵', '')
            a = a.replace('㊶', '')
            a = a.replace('㊷', '')
            a = a.replace('㊸', '')
            a = a.replace('㊹', '')
            a = a.replace('㊺', '')
            a = a.replace('㊻', '')
            a = a.replace('㊼', '')
            a = a.replace('㊽', '')
            a = a.replace('㊾', '')
            a = a.replace('㊿', '')

            # 错误标点纠正：将奇怪的弯引号换为正常的弯引号，为下面执行弯引号与直引号的清除提供条件
            a = a.replace('〞', '”')
            a = a.replace('〝', '“')

            # 错误标点纠正：将角分符号（′）替换为弯引号（若需要使用角分符号则不运行此条）
            a = a.replace('′', "’")
            # 错误标点纠正：将角秒符号（″）替换为弯引号（若需要使用角秒符号则不运行此条）
            a = a.replace('″', '”')

            # 错误标点纠正1（两个同向单引号变成一个双引号<前>，改为前后弯双引号）
            pattern = re.compile(r'‘‘(.*?)”')
            result = pattern.findall(a)
            for i in result:
                a = a.replace('‘‘{}”'.format(i), '“{}”'.format(i))

            # 错误标点纠正2（两个同向单引号变成一个双引号<后>，改为前后弯双引号）
            p1 = r"(?<=“).+?(?=’’)"
            pattern1 = re.compile(p1)
            result = pattern1.findall(a)
            for i in result:
                a = a.replace('“{}’’'.format(i), '“{}”'.format(i))

            # 错误标点纠正3（前后两个单引号变成一组双引号）
            pattern = re.compile(r'‘‘(.*?)’’')
            result = pattern.findall(a)
            for i in result:
                a = a.replace('‘‘{}’’'.format(i), '“{}”'.format(i))

            # 错误标点纠正4（两个同向双引号去掉一个<前>）
            pattern = re.compile(r'““(.*?)”')
            result = pattern.findall(a)
            for i in result:
                a = a.replace('““{}”'.format(i), '“{}”'.format(i))

            # 错误标点纠正5（两个同向双引号去掉一个<后>）
            p1 = r"(?<=“).+?(?=””)"
            pattern1 = re.compile(p1)
            result = pattern1.findall(a)
            for i in result:
                a = a.replace('“{}””'.format(i), '“{}”'.format(i))

            # 错误标点纠正6（两组双引号变成一组双引号）
            pattern = re.compile(r'““(.*?)””')
            result = pattern.findall(a)
            for i in result:
                a = a.replace('““{}””'.format(i), '“{}”'.format(i))

            # 错误标点纠正7（前直单引号<前>，后弯双引号<后>，改为前后弯双引号）
            pattern = re.compile(r"'(.*?)”")
            result = pattern.findall(a)
            for i in result:
                a = a.replace("'{}”".format(i), '“{}”'.format(i))

            # 错误标点纠正8（前直双引号<前>，后弯双引号<后>，改为前后弯双引号）
            pattern = re.compile(r'"(.*?)”')
            result = pattern.findall(a)
            for i in result:
                a = a.replace('"{}”'.format(i), '“{}”'.format(i))

            # 错误标点纠正9（前弯双引号<前>，后直单引号<后>，改为前后弯双引号）
            p1 = r"(?<=“).+?(?=')"
            pattern1 = re.compile(p1)
            result = pattern1.findall(a)
            for i in result:
                a = a.replace("“{}'".format(i), '“{}”'.format(i))

            # 错误标点纠正10（前弯双引号<前>，后直双引号<后>，改为前后弯双引号）
            p1 = r'(?<=“).+?(?=")'
            pattern1 = re.compile(p1)
            result = pattern1.findall(a)
            for i in result:
                a = a.replace('“{}"'.format(i), '“{}”'.format(i))

            # 将成对的直双引号改为成对的弯双引号
            pattern = re.compile(r'"(.*?)"')
            result = pattern.findall(a)
            for i in result:
                a = a.replace('"{}"'.format(i), '“{}”'.format(i))

            # 将成对的直单引号改为成对的弯单引号
            pattern = re.compile(r"'(.*?)'")
            result = pattern.findall(a)
            for i in result:
                a = a.replace("'{}'".format(i), "‘{}’".format(i))

            # 对文段进行再次多余部分的清洗
            # 错误标点纠正1（两个同向单引号变成一个双引号<前>，改为前后弯双引号）
            pattern = re.compile(r'‘‘(.*?)”')
            result = pattern.findall(a)
            for i in result:
                a = a.replace('‘‘{}”'.format(i), '“{}”'.format(i))

            # 错误标点纠正2（两个同向单引号变成一个双引号<后>，改为前后弯双引号）
            p1 = r"(?<=“).+?(?=’’)"
            pattern1 = re.compile(p1)
            result = pattern1.findall(a)
            for i in result:
                a = a.replace('“{}’’'.format(i), '“{}”'.format(i))

            # 错误标点纠正3（前后两个单引号变成一组双引号）
            pattern = re.compile(r'‘‘(.*?)’’')
            result = pattern.findall(a)
            for i in result:
                a = a.replace('‘‘{}’’'.format(i), '“{}”'.format(i))

            # 错误标点纠正4（两个同向双引号去掉一个<前>）
            pattern = re.compile(r'““(.*?)”')
            result = pattern.findall(a)
            for i in result:
                a = a.replace('““{}”'.format(i), '“{}”'.format(i))

            # 错误标点纠正5（两个同向双引号去掉一个<后>）
            p1 = r"(?<=“).+?(?=””)"
            pattern1 = re.compile(p1)
            result = pattern1.findall(a)
            for i in result:
                a = a.replace('“{}””'.format(i), '“{}”'.format(i))

            # 错误标点纠正6（两组双引号变成一组双引号）
            pattern = re.compile(r'““(.*?)””')
            result = pattern.findall(a)
            for i in result:
                a = a.replace('““{}””'.format(i), '“{}”'.format(i))

            # 将单独的单双直引号替换为空(清除剩余的直引号)
            a = a.replace("'", '')
            a = a.replace('"', '')

            # 【判断块】判断文段是全中文、全英文还是中英混排。
            def containenglish(str0):  # 判断是否包含英文字母
                import re
                return bool(re.search('[a-zA-Z]', str0))

            def is_contain_chinese(check_str):  # 判断是否包含中文字
                for ch in check_str:
                    if u'\u4e00' <= ch <= u'\u9fff':
                        return True
                return False

            def is_contain_num(str0):  # 判断是否包含数字
                import re
                return bool(re.search('[0-9]', str0))

            if containenglish(str(a)) == False and is_contain_chinese(str(a)) == True:
                # 【全中块】
                # 去除不必要的中英文符号及空格
                a = a.replace('*', '')
                a = a.replace(' ', '')
                a = a.replace('#', '')
                a = a.replace('^', '')
                a = a.replace('~', '')
                a = a.replace('～', '')

                # 修改一些排版中常见的符号错误
                a = a.replace('。。', '。')
                a = a.replace('。。。', '……')

                # 将常用英文标点转换为中文标点
                def E_trans_to_C(string):
                    E_pun = u',.;:!?[]()<>'
                    C_pun = u'，。；：！？【】（）《》'
                    table = {ord(f): ord(t) for f, t in zip(E_pun, C_pun)}
                    return string.translate(table)

                a = E_trans_to_C(str(a))

                # 【导出块】将转换后的内容装到剪贴板中
                # os.system("echo '%s' | pbcopy" % a)
                pyperclip.copy(a)
            elif containenglish(str(a)) == True and is_contain_chinese(str(a)) == False:
                # 【全英块】将文段中的中文符号转换为英文符号
                def C_trans_to_E(string):
                    E_pun = u',.;:!?[]()<>'
                    C_pun = u'，。；：！？【】（）《》'
                    table = {ord(f): ord(t) for f, t in zip(C_pun, E_pun)}
                    return string.translate(table)

                a = C_trans_to_E(str(a))
                a = a.replace('  ', ' ')

                # 【导出块】将转换后的内容装到剪贴板中
                # os.system("echo '%s' | pbcopy" % a)
                pyperclip.copy(a)
            elif containenglish(str(a)) and is_contain_chinese(str(a)) or \
                    is_contain_chinese(str(a)) and is_contain_num(str(a)) or \
                    is_contain_num(str(a)) and containenglish(str(a)) or \
                    containenglish(str(a)) and is_contain_chinese(str(a)) and is_contain_num(str(a)):
                # 【中英混排块】识别中英文字符，对英文字符保留空格，对中文字符去掉空格。两段内的标点按照各自的要求修改。
                def find_this(q, i):
                    result = q[i]
                    return result

                def find_pre(q, i):
                    result = q[i - 1]
                    return result

                def find_next(q, i):
                    result = q[i + 1]
                    return result

                def find_pre2(q, i):
                    result = q[i - 2]
                    return result

                def find_next2(q, i):
                    result = q[i + 2]
                    return result

                # 首先来一遍此一后一的精准筛查
                i = 0
                while i >= 0 and i < len(a) - 1:
                    if is_contain_chinese(str(find_this(a, i))) and containenglish(str(find_next(a, i))):  # 从中文转英文
                        a = list(a)
                        a.insert(i + 1, '*')
                        a = ''.join(a)
                        # print(a)
                        i = i + 1
                        continue
                    if is_contain_chinese(str(find_this(a, i))) and is_contain_num(str(find_next(a, i))):  # 从中文转数字
                        a = list(a)
                        a.insert(i + 1, '*')
                        a = ''.join(a)
                        # print(a)
                        i = i + 1
                        continue
                    if is_contain_chinese(str(find_next(a, i))) and is_contain_num(str(find_this(a, i))):  # 从数字转中文
                        a = list(a)
                        a.insert(i + 1, '*')
                        a = ''.join(a)
                        # print(a)
                        i = i + 1
                        continue
                    if is_contain_num(str(find_this(a, i))) and containenglish(str(find_next(a, i))):  # 从数字转英文
                        a = list(a)
                        a.insert(i + 1, '*')
                        a = ''.join(a)
                        # print(a)
                        i = i + 1
                        continue
                    if is_contain_num(str(find_next(a, i))) and containenglish(str(find_this(a, i))):  # 从英文转数字
                        a = list(a)
                        a.insert(i + 1, '*')
                        a = ''.join(a)
                        # print(a)
                        i = i + 1
                        continue
                    if is_contain_chinese(str(find_next(a, i))) and containenglish(str(find_this(a, i))):  # 从英文转中文
                        a = list(a)
                        a.insert(i + 1, '*')
                        a = ''.join(a)
                        # print(a)
                        i = i + 1
                        continue
                    else:
                        i = i + 1
                        continue

                # 再进行前一后一的插入
                i = 1
                while i > 0 and i < len(a) - 1:
                    if is_contain_chinese(str(find_pre(a, i))) and containenglish(str(find_next(a, i))):  # 从中文转英文
                        a = list(a)
                        a.insert(i + 1, '*')
                        a = ''.join(a)
                        # print(a)
                        i = i + 1
                        continue
                    if is_contain_chinese(str(find_pre(a, i))) and is_contain_num(str(find_next(a, i))):  # 从中文转数字
                        a = list(a)
                        a.insert(i + 1, '*')
                        a = ''.join(a)
                        # print(a)
                        i = i + 1
                        continue
                    if is_contain_chinese(str(find_next(a, i))) and is_contain_num(str(find_pre(a, i))):  # 从数字转中文
                        a = list(a)
                        a.insert(i + 1, '*')
                        a = ''.join(a)
                        # print(a)
                        i = i + 1
                        continue
                    if is_contain_num(str(find_pre(a, i))) and containenglish(str(find_next(a, i))):  # 从数字转英文
                        a = list(a)
                        a.insert(i + 1, '*')
                        a = ''.join(a)
                        # print(a)
                        i = i + 1
                        continue
                    if is_contain_num(str(find_next(a, i))) and containenglish(str(find_pre(a, i))):  # 从英文转数字
                        a = list(a)
                        a.insert(i + 1, '*')
                        a = ''.join(a)
                        # print(a)
                        i = i + 1
                        continue
                    if is_contain_chinese(str(find_next(a, i))) and containenglish(str(find_pre(a, i))):  # 从英文转中文
                        a = list(a)
                        a.insert(i + 1, '*')
                        a = ''.join(a)
                        # print(a)
                        i = i + 1
                        continue
                    else:
                        i = i + 1
                        continue

                # 这里试切分为列表，如果列表元素中存在多种字符存在，则运行加一字符即下面这段代码（前一后二）。
                i = 1
                while i > 0 and i < len(a) - 2:
                    if is_contain_chinese(str(find_pre(a, i))) and containenglish(str(find_next2(a, i))):  # 从中文转英文
                        a = list(a)
                        a.insert(i + 2, '*')
                        a = ''.join(a)
                        # print(a)
                        i = i + 1
                        continue
                    if is_contain_chinese(str(find_pre(a, i))) and is_contain_num(str(find_next2(a, i))):  # 从中文转数字
                        a = list(a)
                        a.insert(i + 2, '*')
                        a = ''.join(a)
                        # print(a)
                        i = i + 1
                        continue
                    if is_contain_chinese(str(find_next2(a, i))) and is_contain_num(str(find_pre(a, i))):  # 从数字转中文
                        a = list(a)
                        a.insert(i + 2, '*')
                        a = ''.join(a)
                        # print(a)
                        i = i + 1
                        continue
                    if is_contain_num(str(find_pre(a, i))) and containenglish(str(find_next2(a, i))):  # 从数字转英文
                        a = list(a)
                        a.insert(i + 2, '*')
                        a = ''.join(a)
                        # print(a)
                        i = i + 1
                        continue
                    if is_contain_num(str(find_next2(a, i))) and containenglish(str(find_pre(a, i))):  # 从英文转数字
                        a = list(a)
                        a.insert(i + 2, '*')
                        a = ''.join(a)
                        # print(a)
                        i = i + 1
                        continue
                    if is_contain_chinese(str(find_next2(a, i))) and containenglish(str(find_pre(a, i))):  # 从英文转中文
                        a = list(a)
                        a.insert(i + 2, '*')
                        a = ''.join(a)
                        # print(a)
                        i = i + 1
                        continue
                    else:
                        i = i + 1
                        continue

                # 再检查，如果还存在两种字符（中英数），则运行下一段代码（前二后二）
                i = 1
                while i > 0 and i < len(a) - 2:
                    if is_contain_chinese(str(find_pre2(a, i))) and containenglish(str(find_next2(a, i))):  # 从中文转英文
                        a = list(a)
                        a.insert(i + 2, '*')
                        a = ''.join(a)
                        # print(a)
                        i = i + 1
                        continue
                    if is_contain_chinese(str(find_pre2(a, i))) and is_contain_num(str(find_next2(a, i))):  # 从中文转数字
                        a = list(a)
                        a.insert(i + 2, '*')
                        a = ''.join(a)
                        # print(a)
                        i = i + 1
                        continue
                    if is_contain_chinese(str(find_next2(a, i))) and is_contain_num(str(find_pre2(a, i))):  # 从数字转中文
                        a = list(a)
                        a.insert(i + 2, '*')
                        a = ''.join(a)
                        # print(a)
                        i = i + 1
                        continue
                    if is_contain_num(str(find_pre2(a, i))) and containenglish(str(find_next2(a, i))):  # 从数字转英文
                        a = list(a)
                        a.insert(i + 2, '*')
                        a = ''.join(a)
                        # print(a)
                        i = i + 1
                        continue
                    if is_contain_num(str(find_next2(a, i))) and containenglish(str(find_pre2(a, i))):  # 从英文转数字
                        a = list(a)
                        a.insert(i + 2, '*')
                        a = ''.join(a)
                        # print(a)
                        i = i + 1
                        continue
                    if is_contain_chinese(str(find_next2(a, i))) and containenglish(str(find_pre2(a, i))):  # 从英文转中文
                        a = list(a)
                        a.insert(i + 2, '*')
                        a = ''.join(a)
                        # print(a)
                        i = i + 1
                        continue
                    else:
                        i = i + 1
                        continue

                # 将多个*号替换成一个*，四颗星号说明转换点中间没有加空格。
                a = a.replace('****', "*")
                a = a.replace('***', "*")
                a = a.replace("**", "*")

                # 转换为三个列表（考虑在每个星号之后打上顺序，这样成为了列表后每个元素有一个代码i☆。最后可以还原，考虑是数字、字母还是符号。以及这样会带来数字单列表的问题：不，其实只需要两个就够了中+数字/英+数字。）
                b = a.split('*')
                i = 0
                while i >= 0 and i <= len(b) - 1:
                    b[i] = str(i + 1), '☆', b[i], '*'
                    b[i] = ''.join(b[i])
                    i = i + 1
                    continue

                b_ch = []  # 中文+数字
                for i in range(len(b)):
                    b_ch.append(b[i])
                c_en = []  # 英文+数字
                for i in range(len(b)):
                    c_en.append(b[i])
                d_nu = []
                for i in range(len(b)):
                    d_nu.append(b[i])

                # 读取列表元素中#之后的元素？不知道是不是可以定义出来（要定义的函数，不要单的）
                def qingli(k, i):
                    x = k[i]
                    z = x.index("☆") + 1
                    y = x[z: len(x)]
                    return y

                # 或者这里还需要再在每个元素前面增加index值，或者再创造出一个列表，专门记录对应的值
                n = 0
                while n <= len(b_ch) - 1:
                    if containenglish(str(qingli(b_ch, n))) or is_contain_num(str(qingli(b_ch, n))):
                        del b_ch[n]
                        n = n
                        continue
                    else:
                        n = n + 1
                        continue

                n = 0
                while n <= len(c_en) - 1:
                    if is_contain_chinese(str(qingli(c_en, n))) or is_contain_num(str(qingli(c_en, n))):
                        del c_en[n]
                        n = n
                        continue
                    else:
                        n = n + 1
                        continue

                n = 0
                while n <= len(d_nu) - 1:
                    if is_contain_chinese(str(qingli(d_nu, n))) or containenglish(str(qingli(d_nu, n))):
                        del d_nu[n]
                        n = n
                        continue
                    else:
                        n = n + 1
                        continue

                # 【对中文处理】
                zh = ''.join(b_ch)
                # 去除不必要的中英文符号及空格
                zh = zh.replace(' ', '')
                zh = zh.replace('#', '')
                zh = zh.replace('^', '')
                zh = zh.replace('~', '')
                zh = zh.replace('～', '')

                # 修改一些排版中常见的符号错误
                zh = zh.replace('。。', '。')
                zh = zh.replace('。。。', '……')

                # 将常用英文标点转换为中文标点
                def E_trans_to_C(string):
                    E_pun = u',.;:!?[]()<>'
                    C_pun = u'，。；：！？【】（）《》'
                    table = {ord(f): ord(t) for f, t in zip(E_pun, C_pun)}
                    return string.translate(table)

                zh = E_trans_to_C(str(zh))

                # 合成待整合的中文列表
                zh_he = zh.split('*')

                # 【对英文处理】
                en = ''.join(c_en)
                en_he = en.split('*')

                # 【对数字处理】
                shu = ''.join(d_nu)
                shu_he = shu.split('*')

                # 合在一起，存在大于10的数变成小于2的问题。
                he = zh_he + en_he + shu_he

                # 清掉空以及前面的顺序符号
                n = 0
                while n >= 0 and n <= len(he) - 1:
                    if he[n] == '':
                        he.remove('')
                        continue
                    else:
                        n = n + 1
                        continue

                he.sort(key=lambda x: int(x.split('☆')[0]))

                m = 0
                while m >= 0 and m <= len(he) - 1:
                    f = he[m]
                    g = f.index('☆') + 1
                    h = f[g: len(f)]
                    he[m] = h
                    m = m + 1

                # 将列表转化为字符串相连，并且在中英数交错的位置插入空格（暂时先使用空连结，因为有些带符号不一定准）
                zhong = ''.join(he)

                # 将因为分块不当带来的括号问题清除
                zhong = zhong.replace('(', '（')
                zhong = zhong.replace(')', '）')

                # 清除因为分块不当带来的括号内外的空格
                zhong = list(zhong)
                i = 0
                while i >= 0 and i < len(zhong) - 1:
                    if zhong[i] == '（':
                        if zhong[i - 1] == ' ':
                            del zhong[i - 1]
                            continue
                        else:
                            i = i + 1
                            continue
                    if zhong[i] == '）':
                        if zhong[i - 1] == ' ':
                            del zhong[i - 1]
                            continue
                        else:
                            i = i + 1
                            continue
                    else:
                        i = i + 1
                        continue

                i = 0
                while i >= 0 and i < len(zhong) - 1:
                    if zhong[i] == '（':
                        if zhong[i + 1] == ' ':
                            del zhong[i + 1]
                            continue
                        else:
                            i = i + 1
                            continue
                    if zhong[i] == '）':
                        if zhong[i + 1] == ' ':
                            del zhong[i + 1]
                            continue
                        else:
                            i = i + 1
                            continue
                    else:
                        i = i + 1
                        continue

                zhong = ''.join(zhong)

                # 给中英数三者相邻的文本插入空格
                i = 0
                while i >= 0 and i < len(zhong) - 1:
                    if is_contain_chinese(str(find_this(zhong, i))) and containenglish(str(find_next(zhong, i))):  # 从中文转英文
                        zhong = list(zhong)
                        zhong.insert(i + 1, ' ')
                        zhong = ''.join(zhong)
                        i = i + 1
                        continue
                    if is_contain_chinese(str(find_this(zhong, i))) and is_contain_num(str(find_next(zhong, i))):  # 从中文转数字
                        zhong = list(zhong)
                        zhong.insert(i + 1, ' ')
                        zhong = ''.join(zhong)
                        i = i + 1
                        continue
                    if is_contain_chinese(str(find_next(zhong, i))) and is_contain_num(str(find_this(zhong, i))):  # 从数字转中文
                        zhong = list(zhong)
                        zhong.insert(i + 1, ' ')
                        zhong = ''.join(zhong)
                        i = i + 1
                        continue
                    if is_contain_num(str(find_this(zhong, i))) and containenglish(str(find_next(zhong, i))):  # 从数字转英文
                        zhong = list(zhong)
                        zhong.insert(i + 1, ' ')
                        zhong = ''.join(zhong)
                        i = i + 1
                        continue
                    if is_contain_num(str(find_next(zhong, i))) and containenglish(str(find_this(zhong, i))):  # 从英文转数字
                        zhong = list(zhong)
                        zhong.insert(i + 1, ' ')
                        zhong = ''.join(zhong)
                        i = i + 1
                        continue
                    if is_contain_chinese(str(find_next(zhong, i))) and containenglish(str(find_this(zhong, i))):  # 从英文转中文
                        zhong = list(zhong)
                        zhong.insert(i + 1, ' ')
                        zhong = ''.join(zhong)
                        i = i + 1
                        continue
                    else:
                        i = i + 1
                        continue

                # 清除连续空格
                zhong = zhong.replace('  ', ' ')

                # 【导出块】将转换后的内容装到剪贴板中
                # os.system("echo '%s' | pbcopy" % zhong)
                pyperclip.copy(zhong)

    def run(self):
        self.app.run()

if __name__ == '__main__':
    app = Avocado()
    app.run()

# 测试文段3
# 另一方面，六十年代出现大量新的微电子产品，使传统设计思想感到困惑。
# 电子元件微型化使用户难以搞情许多产品到底是 怎么一回事，而且这些产品的功能不能通过电子器件外形表现出来，
# 它们象一个“黑區子“。人们使用这些产品时，面临的最大问 题是无法从产品的外部形式来了解它的内部功能。
# “外形”设计怎么“跟随功能””？许多人开始探索新的设计理论，有人提出“外形跟 随美学"，有人提出“外形跟随成本”。
# 还需要增加中英数空格的功能。
