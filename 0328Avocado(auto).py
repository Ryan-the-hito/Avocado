#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- encoding:UTF-8 -*-
# coding=utf-8

# 功能介绍：对所有中文的字符串，将其中的英文字符转换为中文字符，去掉不必要的空格；对英文字符串，将其中的中文字符转换为英文字符，保留空格；对中英混排的字符串，分别处理。由此简化文段，方便复制粘贴。

# import pyautogui
# import time
import pyperclip
import re
import os
# import rumps
import io
import sys
from pynput.keyboard import Listener

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding="utf-8")
os.path.join(os.path.dirname(sys.argv[0]), "Avocado.db")


# 当监测到电脑按下这两个键的时候，读取剪贴板bug
def on_release(key):
    all_key.append(str(key))
    if 'Key.cmd' in all_key and "'c'" in all_key or 'Key.cmd' in all_key and "'C'" in all_key:
        # 【导入块】
        # 当电脑按下快捷键运行代码的时候，复制文档
        # pyautogui.keyDown('command')
        # pyautogui.keyDown('c')
        # time.sleep(.5)
        # pyautogui.keyUp('c')
        # pyautogui.keyUp('command')
        # time.sleep(.5)

        # 从剪贴板导入待转换文本
        a = pyperclip.paste()

        # 【共同块】不管是全中文/全英文/中英混排，都需要清除的不规范的符号与排版
        # 清除文档排版符号
        a = a.replace('\t', '')
        a = a.replace('\r', '')
        a = a.replace('\n', '')

        # 清除那些引用标记，如圈圈数字和方括号引用，将两个连续空格变为一个空格
        a = a.replace('  ', ' ')
        a = a.replace('[1]', '')
        a = a.replace('[2]', '')
        a = a.replace('[3]', '')
        a = a.replace('[4]', '')
        a = a.replace('[5]', '')
        a = a.replace('[6]', '')
        a = a.replace('[7]', '')
        a = a.replace('[8]', '')
        a = a.replace('[9]', '')
        a = a.replace('[10]', '')
        a = a.replace('[11]', '')
        a = a.replace('[12]', '')
        a = a.replace('[13]', '')
        a = a.replace('[14]', '')
        a = a.replace('[15]', '')
        a = a.replace('[16]', '')
        a = a.replace('[17]', '')
        a = a.replace('[18]', '')
        a = a.replace('[19]', '')
        a = a.replace('[20]', '')
        a = a.replace('[21]', '')
        a = a.replace('[22]', '')
        a = a.replace('[23]', '')
        a = a.replace('[24]', '')
        a = a.replace('[25]', '')
        a = a.replace('[26]', '')
        a = a.replace('[27]', '')
        a = a.replace('[28]', '')
        a = a.replace('[29]', '')
        a = a.replace('[30]', '')
        a = a.replace('[31]', '')
        a = a.replace('[32]', '')
        a = a.replace('[33]', '')
        a = a.replace('[34]', '')
        a = a.replace('[35]', '')
        a = a.replace('[36]', '')
        a = a.replace('[37]', '')
        a = a.replace('[38]', '')
        a = a.replace('[39]', '')
        a = a.replace('[40]', '')
        a = a.replace('[41]', '')
        a = a.replace('[42]', '')
        a = a.replace('[43]', '')
        a = a.replace('[44]', '')
        a = a.replace('[45]', '')
        a = a.replace('[46]', '')
        a = a.replace('[47]', '')
        a = a.replace('[48]', '')
        a = a.replace('[49]', '')
        a = a.replace('[50]', '')

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
        elif containenglish(str(a)) == True and is_contain_chinese(str(a)) == False:
            # 【全英块】将文段中的中文符号转换为英文符号
            def C_trans_to_E(string):
                E_pun = u',.;:!?[]()<>'
                C_pun = u'，。；：！？【】（）《》'
                table = {ord(f): ord(t) for f, t in zip(C_pun, E_pun)}
                return string.translate(table)

            a = C_trans_to_E(str(a))

        # 【中英混排块】识别中英文字符，对英文字符保留空格，对中文字符去掉空格。两段内的标点按照各自的要求修改。

        # 【数字板块】

        # 【导出块】将转换后的内容装到剪贴板中
        os.system("echo '%s' | pbcopy" % a)
        all_key.clear()

    if 'Key.esc' in all_key:
        return False


def start_listen():
    with Listener(on_release=on_release) as listener:
        listener.join()


if __name__ == '__main__':
    all_key = []
    start_listen()

# 测试文段3
# 另一方面，六十年代出现大量新的微电子产品，使传统设计思想感到困惑。
# 电子元件微型化使用户难以搞情许多产品到底是 怎么一回事，而且这些产品的功能不能通过电子器件外形表现出来，
# 它们象一个“黑區子“。人们使用这些产品时，面临的最大问 题是无法从产品的外部形式来了解它的内部功能。
# “外形”设计怎么“跟随功能””？许多人开始探索新的设计理论，有人提出“外形跟 随美学"，有人提出“外形跟随成本”。
