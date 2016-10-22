# coding:utf-8
import time

time_a = time.time()
sstring = '#' * 15
print sstring.ljust(20) * 4

# a = '戊辰辛酉壬申癸卯' + '甲子' + '丙申'   #cnxuan
# a = '丁卯戊申丁酉辛丑' + '乙巳' + '丙申'   #cao zhi yong
# a = '戊戌甲寅丁卯丙午' + '' + ''   #zhou en lai
a = '辛卯庚寅丙戌乙未' + '' + ''
a1 = ''
a2 = ''
a3 = ''
line1 = lambda s: [s[i:i + 3] for i in range(len(s)) if i % 6 == 0]
line2 = lambda s: [s[i:i + 3] for i in range(len(s)) if (i + 3) % 6 == 0]
for u in line1(a):
    a1 = a1 + u.ljust(21)
for u in line2(a):
    a2 = a2 + u.ljust(21)
print a1
print a2
b = '癸甲乙丙丁戊己庚辛壬'
c = '亥子丑寅卯辰巳午未申酉戌'
f1 = '金金水水木木火火土土金金水水木木'
f2 = '庚辛壬癸甲乙丙丁戊己庚辛壬癸甲乙'
g3 = '比劫食伤才财杀官卪印'
g4 = '兄姐岳奶父妻儿女爷母'
j1 = '猪鼠牛虎兔龙蛇马羊猴鸡狗'
j2 = '十冬腊正二三四五六七八九'
e = {
    '亥': '壬甲',
    '子': '癸',
    '丑': '己癸辛',
    '寅': '甲丙戊',
    '卯': '乙',
    '辰': '戊乙癸',
    '巳': '丙戊庚',
    '午': '丁己',
    '未': '己乙丁',
    '申': '庚戊壬',
    '酉': '辛',
    '戌': '戊辛丁',
}
for u in line2(a):
    a3 = a3 + e[u].ljust(22)
print a3
d = {
    '辰库': '水',
    '未库': '木',
    '丑库': '金',
    '戌库': '火',

    '甲己': '甲己 合土,中正之合',
    '乙庚': '乙庚 合金,仁义之合',
    '丙辛': '丙辛 合水,威制之合',
    '丁壬': '丁壬 合木,淫匿之合',
    '戊癸': '戊癸 合火,无情之合',

    '寅卯辰': '寅卯辰 三会木',
    '巳午未': '巳午未 三会火',
    '申酉戌': '申酉戌 三会金',
    '亥子丑': '亥子丑 三会水',

    '寅午戌': '寅午戌 三合火',
    '巳酉丑': '巳酉丑 三合金',
    '申子辰': '申子辰 三合水',
    '亥卯未': '亥卯未 三合木',

    '寅午': '寅午 半三合火',
    '寅戌': '寅戌 拱局',
    '巳酉': '巳酉 半三合金',
    '午戌': '午戌 半三合火',
    '酉丑': '酉丑 半三合金',
    '申子': '申子 半三合水',
    '卯未': '卯未 半三合木',
    '子辰': '子辰 半三合水',
    '亥卯': '亥卯 半三合木',

    '子丑': '子丑 六合土',
    '寅亥': '寅亥 六合木',
    '卯戌': '卯戌 六合火',
    '辰酉': '辰酉 六合金',
    '午未': '午未 六合火',
    '巳酉': '巳酉 六合水',

    '寅丑': '寅丑 支藏人元',
    '卯申': '卯申 支藏人元',
    '午亥': '午亥 支藏人元',

    '子午': '子午 六冲',
    '丑未': '丑未 六冲',
    '寅申': '寅申 六冲',
    '卯酉': '卯酉 六冲',
    '辰戌': '辰戌 六冲',
    '巳亥': '巳亥 六冲',

    '子未': '子未 六害',
    '丑午': '丑午 六害',
    '寅巳': '寅巳 六害',
    '卯辰': '卯辰 六害',
    '酉戌': '酉戌 六害',
    '申亥': '申亥 六害',

    '子酉': '子酉 破,职能部门不为你服务',
    '卯午': '卯午 破,职能部门不为你服务',
    '辰丑': '辰丑 破,同行内部矛盾',
    '未戌': '未戌 破,同行内部矛盾',
    '寅亥': '寅亥 破,隐蔽的小矛盾',
    '巳申': '巳申 破,隐蔽的小矛盾',

    '辰辰': '辰辰 自刑',
    '午午': '午午 自刑',
    '酉酉': '酉酉 自刑',
    '亥亥': '亥亥 自刑',
    '子卯': '子卯 相刑',
    '寅巳申': '寅巳申 相刑',
    '丑未戌': '丑未戌相刑',
}

vert1 = lambda s: [s[i:i + 3] for i in range(len(s)) if i % 3 == 0]
for u in d:
    if len(set(vert1(u))) == len(set(vert1(u)) & set(vert1(a))):
        print d[u]

print '#' * 20
time_b = time.time()
print 'cost = ' + str(time_b - time_a)
