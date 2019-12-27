# %%
# 字符串支持的方法
func_list = dir(str)
print(func_list)
# %%
# startswith
res1 = 'abc123'.startswith('ab')  # 字符串开头包含‘ab’时返回True，否则返回False
print(res1)  # res1 = True

# endswith
res2 = 'abc123'.endswith('3')  # 字符串结尾包含‘3’时返回True，否则返回False
print(res2)  # res2 = True

# %%
