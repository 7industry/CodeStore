#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
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


def sort_sdd_files_in_directory(input_directory, output_directory):
    """
    逐个读取指定目录下所有的 XML 文件。

    Args:
        input_directory (str): 要读取 XML 文件的目录路径。
        output_directory (str): 输出 XML 文件的目录路径。
    """
    try:
        # 检查目录是否存在
        if not os.path.isdir(input_directory):
            print(f"错误：目录 '{input_directory}' 不存在。")
            return

        # 遍历目录中的所有文件和子目录
        for filename in os.listdir(input_directory):
            file_path = os.path.join(input_directory, filename)

            # 检查是否是文件且文件名以 .sdd 结尾（忽略大小写）
            if os.path.isfile(file_path) and filename.lower().endswith(".sdd"):
                print(f"正在读取文件: {file_path}")
                    
                # 输出xml的目录路径
                output_sdd_path = os.path.join(output_directory, filename) 

                sort_xml_fields_by_top(file_path, output_sdd_path)
                
    except Exception as e:
        print(f"遍历目录 '{directory_path}' 时发生错误: {e}")


if __name__ == "__main__":
    input_directory = "../files/in/"  # 将此路径替换为你的实际目录路径
    output_directory = "../files/out/"  # 将此路径替换为你的实际目录路径
    sort_sdd_files_in_directory(input_directory, output_directory)
    print("读取完成。")

    # 示例用法
    #input_xml_file = 'BIPSmartForm.xml' #输入xml的文件名
    #output_xml_file = 'output.xml' #输出xml的文件名
    #sort_xml_fields_by_top(input_xml_file, output_xml_file)
    
    