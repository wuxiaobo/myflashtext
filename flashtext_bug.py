# -*- coding: utf-8 -*-
'''
@Time    : 2021/7/30 6:53 PM
@Author  : 武晓波
@File    : flashtext_bug.py
'''



from MyFlashtext import MyFlashtext
from flashtext import KeywordProcessor

print('flashtext 查找英文字符串')
keyword_processor = KeywordProcessor()
keyword_processor.add_keyword('Big Apple', 'New York')
keyword_processor.add_keyword('Bay Area')
keywords_found1 = keyword_processor.extract_keywords('I love Big Apple and Bay Area.')
print(keywords_found1)

# 存在bug
print('flashtext在中文字符串匹配存在的问题')
keyword_processor.add_keyword('北京')
keyword_processor.add_keyword('欢迎')
keyword_processor.add_keyword('你')
keywords_found2=keyword_processor.extract_keywords('北京欢迎你')
print('flashtext匹配中文字符串:',keywords_found2)
keyword_processor.add_keyword('打call')
keyword_processor.add_keyword('奥运会')
keywords_found3=keyword_processor.extract_keywords('我为在参加东京2021奥运会的中国运动员all打call.')
print('flashtext匹配中英文混合字符串:',keywords_found3)
print('改进之后.......')

myflash_text = MyFlashtext()
myflash_text.add_keyword('Big Apple', 'New York')
myflash_text.add_keyword('Bay Area')
keywords_found_update_1 = myflash_text.extract_keywords('I love Big Apple and Bay Area.')
print('MyFlashtext匹配英文字符串:',keywords_found_update_1)

myflash_text.add_keyword('北京')
myflash_text.add_keyword('欢迎')
myflash_text.add_keyword('你')
keywords_found_update_2 = myflash_text.extract_keywords('北京欢迎你')
print('MyFlashtext匹配英文字符串:',keywords_found_update_2)

myflash_text.add_keyword('打call')
myflash_text.add_keyword('奥运会')
keywords_found_update_3 = myflash_text.extract_keywords('我为在参加东京2021奥运会的中国运动员all打call.')
print('MyFlashtext匹配中英数字混合文字符串:',keywords_found_update_3)




