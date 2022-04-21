# 🥑Avocado: The Text Cleaner
An app on mac to help you remove unwanted spaces and wrong symbols with one click when organizing paragraph with both Chinese and English.

# 🥑Avocado：一个文本清洁工具
## 功能列表
1. 对所有文本：
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
2. 对纯数字文本：
  - 清除数字中的空格
  - 将全角数字转为半角数字
3. 对中文（和数字混排）：
  - 去除某些符号及空格：“*”、“#”、“^”、“～”、“~”
  - 修改一些排版中常见的符号错误：
    - 替换两个连续中文句号（。。）为一个句号（。）
    - 替换三个连续中文句号（。。。）为一个中文省略号（……）
  - 将中文和数字混排中的全角数字转为半角数字，不改变标点的全半角情况
  - 给中文和数字的临近字符中间增加空格
  - 将常用英文标点转换为中文标点：（,.;:!?[]()<>）➡️（，。；：！？【】（）《》）
4. 对英文（和数字混排）：
  - 将全角英文和全角数字转为半角英文和半角数字
  - 将文段中的中文标点转换为英文标点（，。；：！？【】（）《》）➡️（,.;:!?[]()<>）
  - 给英文和数字的临近字符中间增加空格
  - 替换两个连续空格为一个空格
5. 对中英（和数字）混排文本：识别中英文字符，对中英文文段分别处理，再合成一个总文段进行集中处理。标点默认使用原文标点，整体语境以中文为主。
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
### 基本用法
1. 复制需要清理的文段
2. 在menubar中点击“Start Avocado”
3. 粘贴至需要插入文段的位置
### 设置快捷键
- 由于rumps包无法在menubar app中增加原生快捷键，此处推荐使用Apple Script模拟屏幕点击为Avocado增加快捷键。
- 注意⚠️：
  1. 第一个点击可以使用系统命令，第二个点击必须使用屏幕坐标。
  2. 两次点击的命令中间必须使用特殊命令行绕过Apple Script两次动作间间隔5秒的设置。
     - 下图为没有插入特殊命令的情况：
     
     ![avatar](https://raw.githubusercontent.com/Ryan-the-hito/Avocado/main/image/CleanShot%202022-04-16%20at%2002.51.10.gif)
  
     - 下图为插入特殊命令之后的情况：
  
     ![avatar](https://raw.githubusercontent.com/Ryan-the-hito/Avocado/main/image/CleanShot%202022-04-16%20at%2003.06.21.gif)
  3. 建议将脚本放在第三方软件如Alfred中使用，使用原生的Automator会对每一个需要使用的软件请求Accessibility权限，使用Alfred后一次授权可以避免此情况。
     ![avatar](https://raw.githubusercontent.com/Ryan-the-hito/Avocado/main/image/CleanShot%202022-04-21%20at%2017.14.03%402x.png)
- 以下为可以使用的Apple Script（或从Release中下载Alfred workflow）：
  ```applescript
  on run
  	tell application "System Events" to tell process "Avocado"
		  ignoring application responses
			  click menu bar item "🥑" of menu bar 1 of application process "Avocado" of application "System Events"
		  end ignoring
	  end tell
	  delay 0.1
	  do shell script "killall System\\ Events"
	
	  tell application "System Events"
		  click at {1200, 40}
	  end tell
  end run
  ```
- 将{1200， 40}中的坐标替换为使用者电脑中“Start Avocado”的坐标即可（可使用系统自带的截图功能，将光标放到对应位置，查看目标位置的坐标）。
### 使用情景
- 可适应阅读文献、读书摘抄、浏览页面摘抄等多个场景
- 推荐与OCR软件和文本格式清除软件（清除字体颜色粗细字号的软件）配合使用：OCR软件有如TextSniper、白描、TReX等，清除文字格式软件有如Get Plain Text、Pure Paste等
  
  ![avatar](https://raw.githubusercontent.com/Ryan-the-hito/Avocado/main/image/CleanShot%202022-04-21%20at%2017.01.16.gif)

### 不能用来做什么？（请使用软件清理文段之后多瞅一眼，检查清理情况是否符合需求）
- 不能用来100%清除排版上的错误
- 不能检测由于语义而产生的引号误用
- 不能检测拼写错误等词法错误
- 不能排除语法错误
### 中英文排版规范和标点符号使用规范参见：
- [中文技术文档写作风格指南](https://zh-style-guide.readthedocs.io/zh_CN/latest/index.html)
- [中文文档中英文混写混排规范](https://www.lzc256.com/archives/552/#toc_5)
## 未来改进与版本历史
### 未来改进
- 优化核心表达，解决不当删除的bug（极少出现）
- 可能考虑文件读取和导出
- 考虑支持日语和韩语
- 考虑转为Swift
### 版本历史
- 
