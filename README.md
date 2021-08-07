# myflashtext
快速的中文字符串匹配小工具
***
---


## 功能
基于 flashtext https://github.com/vi3k6i5/flashtext，对其不能匹配中文字符串进行了改进.

***
---
## demo 
运行 python3 flashtext_bug.py

### 1.flashtext 英文字符串的查找功能demo
```
from MyFlashtext import MyFlashtext
from flashtext import KeywordProcessor
print('flashtext 查找英文字符串')
keyword_processor = KeywordProcessor()
keyword_processor.add_keyword('Big Apple', 'New York')
keyword_processor.add_keyword('Bay Area')
keywords_found1 = keyword_processor.extract_keywords('I love Big Apple and Bay Area.')
print(keywords_found1)
# ['New York', 'Bay Area']
```
### 2.flashtext 中文字符串的查找存在bug demo
```
# 存在bug
print('flashtext在中文字符串匹配存在的问题')
keyword_processor.add_keyword('北京')
keyword_processor.add_keyword('欢迎')
keyword_processor.add_keyword('你')
keywords_found2=keyword_processor.extract_keywords('北京欢迎你')
print('flashtext匹配中文字符串:',keywords_found2)
#flashtext匹配中文字符串: ['北京', '你']
```

### 3.flashtext 中英文混合字符串的查bug demo

```
keyword_processor.add_keyword('打call')
keyword_processor.add_keyword('奥运会')
keywords_found3=keyword_processor.extract_keywords('我为在参加东京2021奥运会的中国运动员all打call.')
print('flashtext匹配中英文混合字符串:',keywords_found3)
#flashtext匹配中英文混合字符串: []
```

### 4.MyFlashtext 英文字符串的查找功能demo
```
print('改进之后.......')
myflash_text = MyFlashtext()
myflash_text.add_keyword('Big Apple', 'New York')
myflash_text.add_keyword('Bay Area')
keywords_found_update_1 = myflash_text.extract_keywords('I love Big Apple and Bay Area.')
print('MyFlashtext匹配英文字符串:',keywords_found_update_1)
#MyFlashtext匹配英文字符串: [{'word': 'New York', 'index': [7, 16]}, {'word': 'Bay Area', 'index': [21, 29]}]
```

### 5.MyFlashtext 中文字符串的查找功能demo
```
myflash_text.add_keyword('北京')
myflash_text.add_keyword('欢迎')
myflash_text.add_keyword('你')
keywords_found_update_2 = myflash_text.extract_keywords('北京欢迎你')
print('MyFlashtext匹配中文字符串:',keywords_found_update_2)
#MyFlashtext匹配中文字符串: [{'word': '北京', 'index': [0, 2]}, {'word': '欢迎', 'index': [2, 4]}, {'word': '你', 'index': [4, 5]}]
```

### 6.MyFlashtext 中文混合字符串的查找功能demo
```
myflash_text.add_keyword('打call')
myflash_text.add_keyword('奥运会')
keywords_found_update_3 = myflash_text.extract_keywords('我为在参加东京2021奥运会的中国运动员all打call.')
print('MyFlashtext匹配中英数字混合文字符串:',keywords_found_update_3)
# MyFlashtext匹配中英数字混合文字符串: [{'word': '奥运会', 'index': [11, 14]}, {'word': '打call', 'index': [23, 28]}]
```