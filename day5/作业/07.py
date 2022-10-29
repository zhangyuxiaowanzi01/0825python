"""
开发敏感词语过滤程序，提示用户输入内容，如果用户输入的内容中包含特殊的字符：
如 "手枪"等，将内容替换为 *
"""
msg = input('输入内容：')
sensitive_words = ['小可爱', '小宝贝', '你好']
for word in sensitive_words:
    msg = msg.replace(word, len(word) * '*')

print(msg)