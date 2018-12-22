import main_match

user_id = '5ab0b251936aa2283c43783c'
url = 'https://detail.tmall.com/item.htm?spm=a230r.1.14.89.5d602e80XXX7nR&id=564553374880&ns=1&abbucket=19'
category1 = '上装'
category2 = '套头毛衣'

info = [user_id, url, category1, category2]


print(main_match.main_match(info))
