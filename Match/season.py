import re

# 季节匹配
def season_match(time):
    pattern = re.compile('[夏|冬|秋|春]')
    m = pattern.search(time)
    if m != None:
        season = m.group()
    return season