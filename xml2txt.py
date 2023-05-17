import xml.etree.ElementTree as ET

# 解析 XML 文件
tree = ET.parse('strings.xml')

# 获取根元素
root = tree.getroot()

valueString = ""
# 遍历根元素下的所有子元素
for string in root.findall('./string'):
    # 获取字符串名和值
    name = string.get('name')
    value = string.text
    
    # 输出字符串名和值
    # print(f'{value}')
    
    valueString += f'{value},'

print(valueString)