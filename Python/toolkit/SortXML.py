#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lxml import etree

def sort_xml_fields_by_top(input_file, output_file):
    """
    读取 XML 文件，并按 Fields 中元素的 Top 属性重新排列，然后输出到新的 XML 文件。

    Args:
        input_file (str): 输入 XML 文件路径。
        output_file (str): 输出 XML 文件路径。
    """
    try:
        # 解析 XML 文件
        tree = etree.parse(input_file)     
        root = tree.getroot()
            
        # 找到 Fields 元素
        fields = root.find('.//Fields')

        if fields is not None:
            # 获取 Fields 中的所有 Field 元素
            field_elements = list(fields)

            # Field 元素 按照属性的数值大小排序 , 先按 Top 升序，再按 Left 升序排序
            sorted_fields = sorted(field_elements, key=lambda field: (int(field.get('Top')), int(field.get('Left'))))            

            # 清空 Fields 元素并添加排序后的 Field 元素
            fields[:] = sorted_fields
            
        tree.write(output_file, encoding='utf-8', xml_declaration=True)
            
    except etree.ParseError as e:
        print(f"XML 解析错误: {e}")
    except FileNotFoundError:
        print(f"文件未找到: {input_file}")
    except Exception as e:
        print(f"发生错误: {e}")



# 示例用法
input_xml_file = 'BIPSmartForm.xml' #输入xml的文件名
output_xml_file = 'output.xml' #输出xml的文件名

sort_xml_fields_by_top(input_xml_file, output_xml_file)
        
    