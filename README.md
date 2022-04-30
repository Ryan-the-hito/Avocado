# 🥑Avocado: A Text Tool for Better Typesetting <br />一个文本排版与清理工具

An app on mac to help you remove unwanted spaces and wrong symbols with one click when organizing paragraph with both Chinese and English.

Avocado 是一个在 macOS 上运行的小软件，它可以一键清理中英文文本（尤其是混排文本）中那些非语义的排版错误。当你打开它时，它会在任务栏（menubar）中运作，十分简洁明了。最重要的是，它是全局性的，不会受限于任何一个特定的软件，可随取随用。
## 功能列表
**1. 对所有文本：**
  - 清除不必要的记号：
    - 换行符
    - 段落标记
    - 用中括号、大括号、六角括号标注的引用内容（括号中为纯数字则会被识别为引用标记），如“[1]”、“{2}”、“〔3〕”、“﹝4﹞”
    - 上述情况中括号内出现空格也会被识别为引用标记
    - 中括号、大括号、六角括号表示引用标记且相互混用的情况，如“[1〕”、“﹝2}”、“[3〕”、“﹝4〕”
    - 带圈数字等引用符号（0-50）和黑底带圈数字（0-20），如“🄋”、“①”、“㊿”、“⓿”；
    - 圆圈符号和商标符号“◎”、“®”
    - 单独的单双直引号（'）（"）
  - 纠正错误标点：
    - 替换一组奇怪的引号（〝〞）为正常的弯引号（“”）
    - 替换角分符号（′）为弯引号（’）
    - 替换角秒符号（″）为弯引号（”）
    - 替换两个同向单引号（‘‘”）为前后弯双引号（“”）
    - 替换两个同向单引号（“’’）为前后弯双引号（“”）
    - 替换前后两个单引号（‘‘’’）为一组双引号（“”）
    - 两个同向双引号（““”）去掉一个<前>，结果为（“”）
    - 两个同向双引号（“””）去掉一个<后>，结果为（“”）
    - 两组双引号（““””）变成一组双引号（“”）
    - 前直单引号后弯双引号（'”）改为前后弯双引号（“”）
    - 前直双引号后弯双引号（"”）改为前后弯双引号（“”）
    - 前弯双引号后直单引号（“'）改为前后弯双引号（“”）
    - 前弯双引号后直双引号（“"）改为前后弯双引号（“”）
    - 替换成对的直双引号（""）为成对的弯双引号（“”）
    - 替换成对的直单引号（''）为成对的弯单引号（“”）

**2. 对纯数字文本：**
  - 清除数字中的空格
  - 将全角数字转为半角数字

**3. 对中文（和数字混排）：**
  - 去除某些符号及空格：“*”、“#”、“^”、“～”、“~”
  - 修改一些排版中常见的符号错误：
    - 替换两个连续中文句号（。。）为一个句号（。）
    - 替换三个连续中文句号（。。。）为一个中文省略号（……）
  - 将中文和数字混排中的全角数字转为半角数字，不改变标点的全半角情况
  - 给中文和数字的临近字符中间增加空格
  - 将常用英文标点转换为中文标点：（,.;:!?[]()<>）➡️（，。；：！？【】（）《》）

**4. 对英文（和数字混排）：**
  - 将全角英文和全角数字转为半角英文和半角数字
  - 将文段中的中文标点转换为英文标点（，。；：！？【】（）《》）➡️（,.;:!?[]()<>）
  - 给英文和数字的临近字符中间增加空格
  - 替换两个连续空格为一个空格

**5. 对中英（和数字）混排文本：识别中英文字符，对中英文文段分别处理，再合成一个总文段进行集中处理。标点默认使用原文标点，整体语境以中文为主。**
  - 对中文：
    - 去除某些符号及空格：“*”、“#”、“^”、“～”、“~”
    - 修改一些排版中常见的符号错误：
      - 替换两个连续中文句号（。。）为一个句号（。）
      - 替换三个连续中文句号（。。。）为一个中文省略号（……）
    - 将常用英文标点转换为中文标点：（,.;:!?[]()<>）➡️（，。；：！？【】（）《》）
  - 对英文：将全角英文转为半角英文，不改变符号的全半角
  - 对数字：将全角数字转为半角数字，不改变符号的全半角
  - 对总文段：
    - 将所有括号转为中文括号（默认为中文语境引用英文文段）
    - 清除括号内外的空格
    - 给中英数三种字符两两相邻的符号之间插入空格
    - 替换两个连续空格为一个空格
## 用法介绍
### 软件安装
1. 从右边的 Release 页面里面下载第一个压缩包；
2. 解压之后将 app 文件拖放到“应用程序”（Application）文件夹内；
3. 从启动器（Launchpad）中点击启动，可以设为开机自启，目前软件运行时，程序坞（Dock）中会一直显示应用图标；
4. 有可能需要进入系统设置开启辅助功能的权限。（如果需要应该会有弹窗，或主动进入系统设置中手动添加也可）
5. 如果遇到报警 Alert，请转到“系统设置”（System Preferences）-“安全和隐私”（Security & Privacy）-“通用”（General）面板，选择信任该软件并打开。
### 基本用法
1. 复制需要清理的文段
2. 在 menubar 中点击“Start Avocado”
3. 粘贴至需要插入文段的位置
### 设置快捷键
- 由于 rumps 包无法在 menubar app 中增加原生快捷键，此处推荐使用 Apple Script 模拟屏幕点击，再给此脚本增加快捷键。
- 注意⚠️：
  1. 第一个点击可以使用系统命令（v1.5.0之后不建议使用系统命令，两个都用屏幕坐标即可），第二个点击必须使用屏幕坐标。
  2. 两次点击的命令中间必须使用特殊命令行绕过 Apple Script 两次动作间间隔 5 秒的设置。
     - 下图为没有插入特殊命令的情况：
     
     ![avatar](https://raw.githubusercontent.com/Ryan-the-hito/Avocado/main/image/CleanShot%202022-04-16%20at%2002.51.10.gif)
  
     - 下图为插入特殊命令之后的情况：
  
     ![avatar](https://raw.githubusercontent.com/Ryan-the-hito/Avocado/main/image/CleanShot%202022-04-16%20at%2003.06.21.gif)
  
  3. 建议将脚本放在第三方软件如 Alfred 中使用，使用原生的 Automator 会对每一个需要使用的软件请求 Accessibility 权限，使用 Alfred 后一次授权可以避免此情况。
  
     ![avatar](https://raw.githubusercontent.com/Ryan-the-hito/Avocado/main/image/CleanShot%202022-04-21%20at%2017.14.03%402x.png)
     
- 以下为可以使用的 Apple Script（或从 Release 中下载 Alfred workflow）（v1.5.0及之后）：
  ```applescript
  on run
  	tell application "System Events" to tell process "Avocado"
		  ignoring application responses
			  click at {1177, 11}
		  end ignoring
	  end tell
	  delay 0.1
	  do shell script "killall System\\ Events"
	
	  tell application "System Events"
		  click at {1200, 40}
	  end tell
  end run
  ```
- 将{1177, 11}和{1200， 40}中的坐标替换为使用者电脑中“Start Avocado”的坐标（可使用系统自带的截图功能，将光标放到对应位置，查看目标位置的坐标）。
- 最后为这个脚本设置触发快捷键，如（opt+A）
### 软件更新
1. 从 Github 的 Release 页面上下载最新的版本；
2. 将下载到本地的软件拖入“应用程序”（Application）文件夹，跳出窗口，选择覆盖原来的应用文件。
### 使用情景
- 可适应阅读文献、读书摘抄、浏览页面摘抄等多个场景。
- 可以用来检查自己写的一段话里面有没有排版问题，并一键纠正（有引用的情况除外）。
- 推荐与 OCR 软件和文本格式清除软件（清除字体的颜色、粗细、字号的软件）配合使用：OCR 软件有 TextSniper、白描、TReX 等，清除文字格式软件有 Get Plain Text、Pure Paste 等。
  
  ![avatar](https://raw.githubusercontent.com/Ryan-the-hito/Avocado/main/image/CleanShot%202022-04-21%20at%2017.01.16.gif)

### 不能用来做什么？（请使用软件清理文段之后多瞅一眼，检查清理情况是否符合需求）
- 不能用来 100% 清除排版上的错误
- 不能检测由于语义而产生的引号误用
- 不能检测拼写错误等词法错误
- 不能排除语法错误
### 中英文排版规范和标点符号使用规范参见：
- [标点符号用法-中华人民共和国教育部](http://www.moe.gov.cn/ewebeditor/uploadfile/2015/01/13/20150113091548267.pdf)
- [中文技术文档写作风格指南](https://zh-style-guide.readthedocs.io/zh_CN/latest/index.html)
- [中文文档中英文混写混排规范](https://www.lzc256.com/archives/552/#toc_5)
- [中文文案排版指北](https://github.com/sparanoid/chinese-copywriting-guidelines)
- [简易中文简繁转换](https://github.com/gumblex/zhconv)
## 未来改进与版本历史
### 未来改进
- [x] 优化核心表达，解决不当删除的bug（极少出现）
- [ ] ~~可能考虑文件读取和导出
- [ ] 考虑支持日语和韩语
- [ ] ~~考虑转为 Swift
- [ ] 主页说明增加效果图示
- [x] 软件内增加说明窗口
- [ ] ~~在 Swift 文件窗口的基础上增加选项实现更高客制化水平
- [x] 百分号之后、度数符号之后增加空格，之前删去空格。人民币和美元符号之前增加空格，如果是标点则不加空格。
- [x] 提供客制化替换文本的功能
- [ ] ~~提供对英文文本和单位相连的时候去掉空格的支持
- [ ] 隐藏 dock 图标
- [ ] 内置更新提示
- [x] 重构软件架构
- [x] 将清除换行的功能从原软件中变为可选项
- [x] 增加对繁体字和简体字相互转换的支持
- [x] 软件启动的时候不要把每个窗口都打开
### 版本历史
#### v1.5.2（2022-4-30）
1-增加对繁体字和简体字相互转换的支持（⬆️未来改进）；

2-给菜单增加分割线，更加美观。

#### v1.5.1（2022-4-29）
1-新增“保留断行”（Avocado with Line Breaks）功能（⬆️未来改进）；

2-对窗口内元素位置进行了细微改动，更加美观；

3-bug fix：不会一打开软件就弹出窗口了（⬆️未来改进）。

#### v1.5.0（2022-4-29）
1-重构软件框架，更换 rumps 模块为 PyQt6（⬆️未来改进）；

2-增加了客制化替换文本的功能（⬆️未来改进）；

3-更新了 Alfred workflow。

#### v1.4.3（2022-4-26）
1-更换了 menu bar 中的图标；

2-为菜单栏增加了分隔；

3-更新了 Alfred workflow。

#### v1.4.2（2022-4-24）
1-重构了默认清理的代码块；

2-bug fix：中英数混排的情况中，解决括号不成对的问题，在“（）”的基础上新增对“【】”和“《》”的支持，以中文括号为主；

3-bug fix：解决中英数混排不当删除的问题（⬆️未来改进），增加对中英数字符之间间隔四位标点的情况的分割；

4-bug fix：在中英数混排前并未消除英文星号“*”导致标点重复的问题；

5-新增 About 按键（软件说明窗口）（⬆️未来改进）；

6-新增功能：在百分号之后、度数符号之后增加空格，之前删去空格；人民币和美元符号之前增加空格。（若货币符号前有其他符号则不增加空格）（⬆️未来改进）

#### v1.4.1（2022-4-21）
1-bug fix：如果引用符号中存在空格（如“[3 ]”）则无法准确清除的情况；

2-精简带圈数字的代码，新增对黑底带圈数字（0-20）的支持，可一键清除；

3-新增纯数字代码块，可对纯数字文段进行清理，将数字段落中的空格去除，同时将所有全角数字转化为半角数字；

4-精简混排代码块，支持将混排（中数、英数、中英、中英数）中的全角英文字符和全角数字字符转为对应的半角字符。（其中中数混排以中文标点为主，英数混排将以英文标点为主，中英和中英数混排以原文标点和中文标点为主）。

#### v1.3.1（2022-4-20）
1-细化了删除中括号中数字的正则表达式，只有中括号中是纯数字才会被删除；

2-bug fix：纯中文和纯英文文本中，遇见数字的时候没有插入空格的情况；

3-中括号和六角括号混用的引用标记可被识别删除，如“〔3]”。

#### v1.3.0（2022-4-19）
增加了“中英数三种字符紧挨着的时候增加空格”的功能。

#### v1.2.0（2022-4-9）
1-简化了清除上标（[]、{}和两种六角括号）的代码；

2-将中英混排之后因为分块错误带来的英文括号全部换成中文括号；

3-将中英混排带来的括号前后的空格全部消除。

#### v.1.1.0（2022-4-6）
替换装入剪贴板的模块为pyperclip，避免出现乱码。
