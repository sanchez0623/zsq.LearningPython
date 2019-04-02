# 1级合成6级宝石 是自己合划算，还是直接买划算

# 合成过程需要消耗 金，钻石，体力

# 规则
# 1:购买1级石，消耗金和钻石
# 2:1-》3，消耗0.39金，10体力，12个1级石
# 3:3-》4，消耗0.897金，10体力，16个1级石，成功概率48.78%
# 4:4-》6，消耗19.75金，10体力，12个4级石
'''
    购买1级
'''
l1_buy_gold = 0.75
l1_bug_diamond = 8
'''
    1合3
'''
l1_to_l3 = 12
l1_to_l3_gold = 0.39
l1_to_l3_vit = 10
'''
    3合4
'''
l3_to_l4 = 16
l3_to_l4_gold = 0.897
l3_to_l4_vit = 10
l3_to_l4_rate = 0.4878  # 成功概率，失败的话，金和石都被扣除，但不扣除体力
'''
    4合6
'''
l4_to_l6 = 12
l4_to_l6_gold = 19.75
l4_to_l6_vit = 10

# 一个6级石，750金
# 一个钻石，0.05金
# 一个体力，1金

diamond = 0.05

l1 = l1_buy_gold + l1_bug_diamond * diamond
print('购买一颗1级石头花费' + str(l1) + '金')
l3 = l1 * l1_to_l3 + l1_to_l3_gold + l1_to_l3_vit
print('升级一颗3级石头花费' + str(l3) + '金')
l4_suc = (l3 + (l1 * l3_to_l4 + l3_to_l4_gold + l3_to_l4_vit) * l3_to_l4_rate)
l4_fail = (l3+(l1 * l3_to_l4 + l3_to_l4_gold) * (1 - l3_to_l4_rate))
l4 = l4_suc + l4_fail
print('升级一颗4级石头花费' + str(l4) + '金')
l6 = l4 * l4_to_l6 + l4_to_l6_gold + l4_to_l6_vit
print('升级一颗6级石头花费' + str(l6) + '金')

print(l6)