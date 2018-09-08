# coding=utf-8
import pandas as pd
import sys


def xlsx_to_csv_pd(ifile, ofile):
    data_xls = pd.read_excel(ifile, index_col=0)
    data_xls.to_csv(ofile, encoding='utf-8')


if __name__ == '__main__':
	infile = sys.argv[1]
	outfile = sys.argv[2]
	xlsx_to_csv_pd(infile, outfile)
