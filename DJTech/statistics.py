from xlrd import open_workbook
import openpyxl
import sys
import os


def write_xls(workdata, name):
    workbook = openpyxl.load_workbook(name)
    sheet = workbook.active  # 获取当前活跃的sheet,默认是第一个sheet
    sheet.append(workdata)  # 在最后追加一行数据
    workbook.save(name)


def read_xls(filename, collect_excel, week):
    content = {filename: []}
    workbook = open_workbook(filename)
    for table in workbook.sheets():
        rows = table.nrows
        for i in range(2, rows):
            row_value = table.row_values(i)[:5]
            if row_value[0] and week in row_value:
                content[filename].append(row_value)
                write_xls(row_value, collect_excel)
    return content


if __name__ == '__main__':
    now_week = sys.argv[1]
    all_dir = sys.argv[2]
    collect_excel = sys.argv[3]
    for efile in os.listdir(all_dir):
        data = read_xls(all_dir + "\\" + efile, collect_excel, now_week)
        print(data)
