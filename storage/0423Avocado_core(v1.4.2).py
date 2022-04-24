#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- encoding:UTF-8 -*-
# coding=utf-8
# coding:utf-8


# 功能介绍：对纯中文文本，将其中的英文字符转换为中文字符，去掉不必要的符号；对纯英文文本，将其中的中文字符转换为英文字符，保留空格；对中英混排的文本，分别处理。由此简化文段，方便复制粘贴。


import pyperclip
import re
import rumps


def default_clean(a):
    # 【共同块】不管是全中文/全英文/中英混排，都需要清除的不规范的符号与排版
    # 清除文档排版符号
    a = a.replace('\t', '')
    a = a.replace('\r', '')
    a = a.replace('\n', '')

    # 清除连续空格（如连续两个和三个空格）
    a = a.replace('  ', ' ')
    a = a.replace('   ', ' ')

    # 清除那些引用标记（括号内为纯数字），如圈圈数字和方括号引用，同时由于方括号和六角括号混用较多，清理前后不搭的情况中的引用符号
    a = re.sub(r"\{(\s)*\d+\s*?\}|\[(\s)*\d+\s*?\]|\〔(\s)*\d+\s*?\〕|\﹝(\s)*\d+\s*?\﹞", "", a)
    a = re.sub(r"\[(\s)*\d+\s*?\〕|\[(\s)*\d+\s*?\﹞|\〔(\s)*\d+\s*?\]\
                |\〔(\s)*\d+\s*?\﹞|\﹝(\s)*\d+\s*?\]|\﹝(\s)*\d+\s*?\〕", "", a)
    a = re.sub(u'\u24EA|[\u2460-\u2473]|[\u3251-\u325F]|[\u32B1-\u32BF]|[\u2776-\u277F]|\u24FF|[\u24EB-\u24F4]',
               "", a)
    a = a.replace('◎', '')
    a = a.replace('®', '')
    a = a.replace('*', '')

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
        return bool(re.search('[a-zA-Zａ-ｚＡ-Ｚ]', str0))

    def is_contain_chinese(check_str):  # 判断是否包含中文字
        for ch in check_str:
            if u'\u4e00' <= ch <= u'\u9fff':
                return True
        return False

    def is_contain_num(str0):  # 判断是否包含数字
        import re
        return bool(re.search('[0-9０-９]', str0))

    def is_contain_symbol(keyword):
        if re.search(r"\W", keyword):
            return True
        else:
            return False

    if is_contain_num(str(a)) and not containenglish(str(a)) and not is_contain_chinese(str(a)):
        # 【全数块】清除数字中的空格，将全角数字转为半角数字
        a = a.replace(' ', '')

        def is_Qnumber(uchar):
            """判断一个unicode是否是全角数字"""
            if uchar >= u'\uff10' and uchar <= u'\uff19':
                return True
            else:
                return False

        def Q2B(uchar):
            """单个字符 全角转半角"""
            inside_code = ord(uchar)
            if inside_code == 0x3000:
                inside_code = 0x0020
            else:
                inside_code -= 0xfee0
            if inside_code < 0x0020 or inside_code > 0x7e:  # 转完之后不是半角字符返回原来的字符
                return uchar
            return chr(inside_code)

        def stringpartQ2B(ustring):
            """把字符串中数字全角转半角"""
            return "".join(
                [Q2B(uchar) if is_Qnumber(uchar) else uchar for uchar in ustring])

        a = stringpartQ2B(a)

        # 对全数字文段的货币符号、百分号和度数这三个符号进行专门处理
        i = 0
        while i <= len(a) - 1:
            if a[i] == '¥' and not is_contain_symbol(str(a[i - 1])):
                a = list(a)
                a.insert(i, ' ')
                a = ''.join(a)
                i = i + 2
                continue
            if a[i] == '$' and not is_contain_symbol(str(a[i - 1])):
                a = list(a)
                a.insert(i, ' ')
                a = ''.join(a)
                i = i + 2
                continue
            if a[i] == "%":
                if a[i - 1] == ' ':
                    a = list(a)
                    del a[i - 1]
                    a = ''.join(a)
                    i = i - 1
                    continue
                else:
                    a = list(a)
                    a.insert(i + 1, ' ')
                    a = ''.join(a)
                    i = i + 2
                    continue
            if a[i] == "°":
                if a[i - 1] == ' ':
                    a = list(a)
                    del a[i - 1]
                    a = ''.join(a)
                    i = i - 1
                    continue
                else:
                    a = list(a)
                    a.insert(i + 1, ' ')
                    a = ''.join(a)
                    i = i + 2
                    continue
            else:
                i = i + 1
                continue

        a = a.replace(' ', '')
        return a

    elif not containenglish(str(a)) and is_contain_chinese(str(a)):
        # 【中（数）块】
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

        # 将中文和数字混排中的全角数字转为半角数字，不改变标点的全半角情况
        def is_Qnumber(uchar):
            """判断一个unicode是否是全角数字"""
            if uchar >= u'\uff10' and uchar <= u'\uff19':
                return True
            else:
                return False

        def Q2B(uchar):
            """单个字符 全角转半角"""
            inside_code = ord(uchar)
            if inside_code == 0x3000:
                inside_code = 0x0020
            else:
                inside_code -= 0xfee0
            if inside_code < 0x0020 or inside_code > 0x7e:  # 转完之后不是半角字符返回原来的字符
                return uchar
            return chr(inside_code)

        def stringpartQ2B(ustring):
            """把字符串中数字全角转半角"""
            return "".join(
                [Q2B(uchar) if is_Qnumber(uchar) else uchar for uchar in ustring])

        a = stringpartQ2B(a)

        # 给中文和数字的混排增加空格
        def find_this(q, i):
            result = q[i]
            return result

        def find_next(q, i):
            result = q[i + 1]
            return result

        i = 0
        while i >= 0 and i < len(a) - 1:
            if is_contain_chinese(str(find_this(a, i))) and is_contain_num(str(find_next(a, i))):  # 从中文转数字
                a = list(a)
                a.insert(i + 1, ' ')
                a = ''.join(a)
                i = i + 1
                continue
            if is_contain_chinese(str(find_next(a, i))) and is_contain_num(str(find_this(a, i))):  # 从数字转中文
                a = list(a)
                a.insert(i + 1, ' ')
                a = ''.join(a)
                i = i + 1
                continue
            else:
                i = i + 1
                continue

        # 将常用英文标点转换为中文标点
        def E_trans_to_C(string):
            E_pun = u',.;:!?[]()<>'
            C_pun = u'，。；：！？【】（）《》'
            table = {ord(f): ord(t) for f, t in zip(E_pun, C_pun)}
            return string.translate(table)

        a = E_trans_to_C(str(a))

        # 对特殊数字符号进行处理
        i = 0
        while i <= len(a) - 1:
            if a[i] == '¥' and not is_contain_symbol(str(a[i - 1])):
                a = list(a)
                a.insert(i, ' ')
                a = ''.join(a)
                i = i + 2
                continue
            if a[i] == '$' and not is_contain_symbol(str(a[i - 1])):
                a = list(a)
                a.insert(i, ' ')
                a = ''.join(a)
                i = i + 2
                continue
            if a[i] == "%":
                if a[i - 1] == ' ':
                    a = list(a)
                    del a[i - 1]
                    a = ''.join(a)
                    i = i - 1
                    continue
                else:
                    a = list(a)
                    a.insert(i + 1, ' ')
                    a = ''.join(a)
                    i = i + 2
                    continue
            if a[i] == "°":
                if a[i - 1] == ' ':
                    a = list(a)
                    del a[i - 1]
                    a = ''.join(a)
                    i = i - 1
                    continue
                else:
                    a = list(a)
                    a.insert(i + 1, ' ')
                    a = ''.join(a)
                    i = i + 2
                    continue
            else:
                i = i + 1
                continue

        a = a.replace('  ', ' ')
        return a

    elif containenglish(str(a)) and not is_contain_chinese(str(a)):
        # 【英（数）块】给英文和数字混排的情况增加空格
        def find_this(q, i):
            result = q[i]
            return result

        def find_next(q, i):
            result = q[i + 1]
            return result

        i = 0
        while i >= 0 and i < len(a) - 1:
            if is_contain_num(str(find_this(a, i))) and containenglish(str(find_next(a, i))):  # 从数字转英文
                a = list(a)
                a.insert(i + 1, ' ')
                a = ''.join(a)
                i = i + 1
                continue
            if is_contain_num(str(find_next(a, i))) and containenglish(str(find_this(a, i))):  # 从英文转数字
                a = list(a)
                a.insert(i + 1, ' ')
                a = ''.join(a)
                i = i + 1
                continue
            else:
                i = i + 1
                continue

        # 将全角英文字符和数字转为半角英文和半角数字
        def is_Qnumber(uchar):
            """判断一个unicode是否是全角数字"""
            if uchar >= u'\uff10' and uchar <= u'\uff19':
                return True
            else:
                return False

        def is_Qalphabet(uchar):
            """判断一个unicode是否是全角英文字母"""
            if (uchar >= u'\uff21' and uchar <= u'\uff3a') or (uchar >= u'\uff41' and uchar <= u'\uff5a'):
                return True
            else:
                return False

        def Q2B(uchar):
            """单个字符 全角转半角"""
            inside_code = ord(uchar)
            if inside_code == 0x3000:
                inside_code = 0x0020
            else:
                inside_code -= 0xfee0
            if inside_code < 0x0020 or inside_code > 0x7e:  # 转完之后不是半角字符返回原来的字符
                return uchar
            return chr(inside_code)

        def stringpartQ2B(ustring):
            """把字符串中字母和数字全角转半角"""
            return "".join(
                [Q2B(uchar) if is_Qnumber(uchar) or is_Qalphabet(uchar) else uchar for uchar in ustring])

        a = stringpartQ2B(a)

        # 将文段中的中文符号转换为英文符号
        def C_trans_to_E(string):
            E_pun = u',.;:!?[]()<>'
            C_pun = u'，。；：！？【】（）《》'
            table = {ord(f): ord(t) for f, t in zip(C_pun, E_pun)}
            return string.translate(table)

        a = C_trans_to_E(str(a))

        # 对全数字文段的货币符号、百分号和度数这三个符号进行专门处理
        i = 0
        while i <= len(a) - 1:
            if a[i] == '¥' and not is_contain_symbol(str(a[i - 1])):
                a = list(a)
                a.insert(i, ' ')
                a = ''.join(a)
                i = i + 2
                continue
            if a[i] == '$' and not is_contain_symbol(str(a[i - 1])):
                a = list(a)
                a.insert(i, ' ')
                a = ''.join(a)
                i = i + 2
                continue
            if a[i] == "%":
                if a[i - 1] == ' ':
                    a = list(a)
                    del a[i - 1]
                    a = ''.join(a)
                    i = i - 1
                    continue
                else:
                    a = list(a)
                    a.insert(i + 1, ' ')
                    a = ''.join(a)
                    i = i + 2
                    continue
            if a[i] == "°":
                if a[i - 1] == ' ':
                    a = list(a)
                    del a[i - 1]
                    a = ''.join(a)
                    i = i - 1
                    continue
                else:
                    a = list(a)
                    a.insert(i + 1, ' ')
                    a = ''.join(a)
                    i = i + 2
                    continue
            else:
                i = i + 1
                continue

        a = a.replace('  ', ' ')
        return a

    elif containenglish(str(a)) and is_contain_chinese(str(a)) or \
            containenglish(str(a)) and is_contain_chinese(str(a)) and is_contain_num(str(a)):
        # 【中英（数）混排块】识别中英文字符，对英文字符保留空格，对中文字符去掉空格。标点默认使用原文标点，以中文为主（默认使用情况为在中文中引用英文）。
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

        def find_next3(q, i):
            result = q[i + 3]
            return result

        # 首先来一遍此一后一的精准筛查
        i = 0
        while i >= 0 and i < len(a) - 1:
            if is_contain_chinese(str(find_this(a, i))) and containenglish(str(find_next(a, i))):  # 从中文转英文
                a = list(a)
                a.insert(i + 1, '*')
                a = ''.join(a)
                i = i + 1
                continue
            if is_contain_chinese(str(find_this(a, i))) and is_contain_num(str(find_next(a, i))):  # 从中文转数字
                a = list(a)
                a.insert(i + 1, '*')
                a = ''.join(a)
                i = i + 1
                continue
            if is_contain_chinese(str(find_next(a, i))) and is_contain_num(str(find_this(a, i))):  # 从数字转中文
                a = list(a)
                a.insert(i + 1, '*')
                a = ''.join(a)
                i = i + 1
                continue
            if is_contain_num(str(find_this(a, i))) and containenglish(str(find_next(a, i))):  # 从数字转英文
                a = list(a)
                a.insert(i + 1, '*')
                a = ''.join(a)
                i = i + 1
                continue
            if is_contain_num(str(find_next(a, i))) and containenglish(str(find_this(a, i))):  # 从英文转数字
                a = list(a)
                a.insert(i + 1, '*')
                a = ''.join(a)
                i = i + 1
                continue
            if is_contain_chinese(str(find_next(a, i))) and containenglish(str(find_this(a, i))):  # 从英文转中文
                a = list(a)
                a.insert(i + 1, '*')
                a = ''.join(a)
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
                i = i + 1
                continue
            if is_contain_chinese(str(find_pre(a, i))) and is_contain_num(str(find_next(a, i))):  # 从中文转数字
                a = list(a)
                a.insert(i + 1, '*')
                a = ''.join(a)
                i = i + 1
                continue
            if is_contain_chinese(str(find_next(a, i))) and is_contain_num(str(find_pre(a, i))):  # 从数字转中文
                a = list(a)
                a.insert(i + 1, '*')
                a = ''.join(a)
                i = i + 1
                continue
            if is_contain_num(str(find_pre(a, i))) and containenglish(str(find_next(a, i))):  # 从数字转英文
                a = list(a)
                a.insert(i + 1, '*')
                a = ''.join(a)
                i = i + 1
                continue
            if is_contain_num(str(find_next(a, i))) and containenglish(str(find_pre(a, i))):  # 从英文转数字
                a = list(a)
                a.insert(i + 1, '*')
                a = ''.join(a)
                i = i + 1
                continue
            if is_contain_chinese(str(find_next(a, i))) and containenglish(str(find_pre(a, i))):  # 从英文转中文
                a = list(a)
                a.insert(i + 1, '*')
                a = ''.join(a)
                i = i + 1
                continue
            else:
                i = i + 1
                continue

        # 进行前一后二的筛查
        i = 1
        while i > 0 and i < len(a) - 2:
            if is_contain_chinese(str(find_pre(a, i))) and containenglish(str(find_next2(a, i))):  # 从中文转英文
                a = list(a)
                a.insert(i + 2, '*')
                a = ''.join(a)
                i = i + 1
                continue
            if is_contain_chinese(str(find_pre(a, i))) and is_contain_num(str(find_next2(a, i))):  # 从中文转数字
                a = list(a)
                a.insert(i + 2, '*')
                a = ''.join(a)
                i = i + 1
                continue
            if is_contain_chinese(str(find_next2(a, i))) and is_contain_num(str(find_pre(a, i))):  # 从数字转中文
                a = list(a)
                a.insert(i + 2, '*')
                a = ''.join(a)
                i = i + 1
                continue
            if is_contain_num(str(find_pre(a, i))) and containenglish(str(find_next2(a, i))):  # 从数字转英文
                a = list(a)
                a.insert(i + 2, '*')
                a = ''.join(a)
                i = i + 1
                continue
            if is_contain_num(str(find_next2(a, i))) and containenglish(str(find_pre(a, i))):  # 从英文转数字
                a = list(a)
                a.insert(i + 2, '*')
                a = ''.join(a)
                i = i + 1
                continue
            if is_contain_chinese(str(find_next2(a, i))) and containenglish(str(find_pre(a, i))):  # 从英文转中文
                a = list(a)
                a.insert(i + 2, '*')
                a = ''.join(a)
                i = i + 1
                continue
            else:
                i = i + 1
                continue

        # 再进行前二后二的筛查
        i = 1
        while i > 0 and i < len(a) - 2:
            if is_contain_chinese(str(find_pre2(a, i))) and containenglish(str(find_next2(a, i))):  # 从中文转英文
                a = list(a)
                a.insert(i + 2, '*')
                a = ''.join(a)
                i = i + 1
                continue
            if is_contain_chinese(str(find_pre2(a, i))) and is_contain_num(str(find_next2(a, i))):  # 从中文转数字
                a = list(a)
                a.insert(i + 2, '*')
                a = ''.join(a)
                i = i + 1
                continue
            if is_contain_chinese(str(find_next2(a, i))) and is_contain_num(str(find_pre2(a, i))):  # 从数字转中文
                a = list(a)
                a.insert(i + 2, '*')
                a = ''.join(a)
                i = i + 1
                continue
            if is_contain_num(str(find_pre2(a, i))) and containenglish(str(find_next2(a, i))):  # 从数字转英文
                a = list(a)
                a.insert(i + 2, '*')
                a = ''.join(a)
                i = i + 1
                continue
            if is_contain_num(str(find_next2(a, i))) and containenglish(str(find_pre2(a, i))):  # 从英文转数字
                a = list(a)
                a.insert(i + 2, '*')
                a = ''.join(a)
                i = i + 1
                continue
            if is_contain_chinese(str(find_next2(a, i))) and containenglish(str(find_pre2(a, i))):  # 从英文转中文
                a = list(a)
                a.insert(i + 2, '*')
                a = ''.join(a)
                i = i + 1
                continue
            else:
                i = i + 1
                continue

        # 最后进行一次前二后三的检查，这个比较少见，只在「武力⋯⋯”(1974」这个情况中存在
        i = 1
        while i > 0 and i < len(a) - 3:
            if is_contain_chinese(str(find_pre2(a, i))) and containenglish(str(find_next3(a, i))):  # 从中文转英文
                a = list(a)
                a.insert(i + 3, '*')
                a = ''.join(a)
                i = i + 1
                continue
            if is_contain_chinese(str(find_pre2(a, i))) and is_contain_num(str(find_next3(a, i))):  # 从中文转数字
                a = list(a)
                a.insert(i + 3, '*')
                a = ''.join(a)
                i = i + 1
                continue
            if is_contain_chinese(str(find_next3(a, i))) and is_contain_num(str(find_pre2(a, i))):  # 从数字转中文
                a = list(a)
                a.insert(i + 3, '*')
                a = ''.join(a)
                i = i + 1
                continue
            if is_contain_num(str(find_pre2(a, i))) and containenglish(str(find_next3(a, i))):  # 从数字转英文
                a = list(a)
                a.insert(i + 3, '*')
                a = ''.join(a)
                i = i + 1
                continue
            if is_contain_num(str(find_next3(a, i))) and containenglish(str(find_pre2(a, i))):  # 从英文转数字
                a = list(a)
                a.insert(i + 3, '*')
                a = ''.join(a)
                i = i + 1
                continue
            if is_contain_chinese(str(find_next3(a, i))) and containenglish(str(find_pre2(a, i))):  # 从英文转中文
                a = list(a)
                a.insert(i + 3, '*')
                a = ''.join(a)
                i = i + 1
                continue
            else:
                i = i + 1
                continue

        # 将多个*号替换成一个*。
        a = a.replace('*****', "*")
        a = a.replace('****', "*")
        a = a.replace('***', "*")
        a = a.replace("**", "*")

        # 转换为三个列表（考虑在每个星号之后打上顺序，这样成为了列表后每个元素有一个代码i☆
        b = a.split('*')
        i = 0
        while i >= 0 and i <= len(b) - 1:
            b[i] = str(i + 1), '☆', b[i], '*'
            b[i] = ''.join(b[i])
            i = i + 1
            continue

        b_ch = []  # 中文（待清理）
        for i in range(len(b)):
            b_ch.append(b[i])
        c_en = []  # 英文（待清理）
        for i in range(len(b)):
            c_en.append(b[i])
        d_nu = []  # 数字（待清理）
        for i in range(len(b)):
            d_nu.append(b[i])

        # 读取列表元素中☆之后的元素，定义一个函数
        def qingli(k, i):
            x = k[i]
            z = x.index("☆") + 1
            y = x[z: len(x)]
            return y

        # 执行清理
        n = 0
        while n <= len(b_ch) - 1:
            if containenglish(str(qingli(b_ch, n))) or is_contain_num(str(qingli(b_ch, n))):
                del b_ch[n]  # 中文，除掉英文和数字
                n = n
                continue
            else:
                n = n + 1
                continue

        n = 0
        while n <= len(c_en) - 1:
            if is_contain_chinese(str(qingli(c_en, n))) or is_contain_num(str(qingli(c_en, n))):
                del c_en[n]  # 英文，除掉中文和数字
                n = n
                continue
            else:
                n = n + 1
                continue

        n = 0
        while n <= len(d_nu) - 1:
            if is_contain_chinese(str(qingli(d_nu, n))) or containenglish(str(qingli(d_nu, n))):
                del d_nu[n]  # 数字，除掉中文和英文
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

        def Q2B(uchar):
            """单个字符 全角转半角"""
            inside_code = ord(uchar)
            if inside_code == 0x3000:
                inside_code = 0x0020
            else:
                inside_code -= 0xfee0
            if inside_code < 0x0020 or inside_code > 0x7e:  # 转完之后不是半角字符返回原来的字符
                return uchar
            return chr(inside_code)

        # 【对英文处理】将全角英文字母转为半角英文字母，不改变符号的全半角
        en = ''.join(c_en)

        def is_Qalphabet(uchar):
            """判断一个unicode是否是全角英文字母"""
            if (uchar >= u'\uff21' and uchar <= u'\uff3a') or (uchar >= u'\uff41' and uchar <= u'\uff5a'):
                return True
            else:
                return False

        def stringpartQ2B(ustring):
            """把字符串中字母全角转半角"""
            return "".join([Q2B(uchar) if is_Qalphabet(uchar) else uchar for uchar in ustring])
        en = stringpartQ2B(en)

        en_he = en.split('*')

        # 【对数字处理】将全角数字转为半角数字，不改变符号的全半角
        shu = ''.join(d_nu)

        def is_Qnumber(uchar):
            """判断一个unicode是否是全角数字"""
            if uchar >= u'\uff10' and uchar <= u'\uff19':
                return True
            else:
                return False

        def stringpartQ2B(ustring):
            """把字符串中数字全角转半角"""
            return "".join(
                [Q2B(uchar) if is_Qnumber(uchar) else uchar for uchar in ustring])
        shu = stringpartQ2B(shu)

        shu_he = shu.split('*')

        # 合在一起（存在大于10的数变成小于2的问题，后面解决）
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

        # 将列表转化为字符串相连，这里本可以转化成空格，但是这样会因为分割点问题产生问题，故先整体以"空"合并
        zhong = ''.join(he)

        # 解决因为分块不当带来的括号问题（当括号分到英文块的时候没有被处理到），此处默认全部换成中文括号
        zhong = zhong.replace('(', '（')
        zhong = zhong.replace(')', '）')
        zhong = zhong.replace('[', '【')
        zhong = zhong.replace(']', '】')
        zhong = zhong.replace('<', '《')
        zhong = zhong.replace('>', '》')

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

        # 给中英数三者相邻的文本插入空格，给特定的单位符号前后增减空格（注意，如果是探索，不能等号，如果是全局修改，必须<=）
        i = 0
        while i <= len(zhong) - 1:
            if zhong[i] == '¥' and not is_contain_symbol(str(zhong[i - 1])):
                zhong = list(zhong)
                zhong.insert(i, ' ')
                zhong = ''.join(zhong)
                i = i + 2
                continue
            if zhong[i] == '$' and not is_contain_symbol(str(zhong[i - 1])):
                zhong = list(zhong)
                zhong.insert(i, ' ')
                zhong = ''.join(zhong)
                i = i + 2
                continue
            if zhong[i] == "%":
                if zhong[i - 1] == ' ':
                    zhong = list(zhong)
                    del zhong[i - 1]
                    zhong = ''.join(zhong)
                    i = i - 1
                    continue
                else:
                    zhong = list(zhong)
                    zhong.insert(i + 1, ' ')
                    zhong = ''.join(zhong)
                    i = i + 2
                    continue
            if zhong[i] == "°":
                if zhong[i - 1] == ' ':
                    zhong = list(zhong)
                    del zhong[i - 1]
                    zhong = ''.join(zhong)
                    i = i - 1
                    continue
                else:
                    zhong = list(zhong)
                    zhong.insert(i + 1, ' ')
                    zhong = ''.join(zhong)
                    i = i + 2
                    continue
            else:
                i = i + 1
                continue

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
        return zhong


class AvocadoApp(rumps.App):
    @rumps.clicked("Start Avocado")
    def start_app(self, sender):
        if sender.title.lower().startswith("start"):
            # 从剪贴板导入待转换文本
            a = pyperclip.paste()
            # 【导出块】将转换后的内容装到剪贴板中
            pyperclip.copy(default_clean(a))

    @rumps.clicked("About")
    def prefs(self, _):
        rumps.alert(title='About', message='''
                    🥑
                    Avocado_v1.4.2
                    
                    This app is open-sourced. 
                    Please do not use it for business.
                    本软件开源，
                    请勿用于商业用途。
                    
                    ---
                    
                    Author: 
                    Ryan-the-hito
                    
                    Github: 
                    https://github.com/Ryan-the-hito/Avocado
                    
                    Contact: 
                    dpye2hmpivcwqrvg@hideaddress.net''', ok='Got it!')

if __name__ == "__main__":
    AvocadoApp("🥑").run()
