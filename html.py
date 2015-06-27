#!/usr/bin/env python
# -*- coding=utf-8 -*-

"""
html get name,id and phone
use module re to find phone number and Id number
file name such as "xxx-----3702...902.html"
@auther: zhuangyw
"""

import os
import re
import sys
import shutil

city_name = sys.argv[1:]
if len(city_name) > 1:
    pass
else:
    city_name = ['������', '�Ϻ���', '�����', '������', 'ʯ��ׯ��', '̫ԭ��', '���ͺ�����',
                 '��ɽ��', '��ͬ��', '��ͷ��',
                 '�ػʵ���', '��Ȫ��', '�ں���', '������', '������', '�����',
                 '��̨��', '������', '���ױ�����', '������', '˷����', 'ͨ����', '�żҿ���',
                 '������', '�����첼��', '�е���', '������', '������˹��', '������', '������',
                 '�����׶���', '�ȷ���', '�ٷ���', '��ˮ��', '�˳���', '��������', '������',
                 '������', '���������', '������', '������', 'ĵ������', '��ƽ��', '��ɽ��',
                 '��ľ˹��', '��Դ��', '��˳��', '������', 'ͨ����', '��Ϫ��', '������',
                 '��ɽ��', '������', '������', '�׳���', '������', '�׸���', '��ԭ��',
                 'Ӫ����', '˫Ѽɽ��', '������', '��̨����', '������', '�绯��', '�̽���',
                 '�ں���', '������', '������', '��«����', '�Ͼ���', '������', '�Ϸ���',
                 '������', '�ϲ���', '������', '������', '������', '�ߺ���', '������',
                 '������', '�ൺ��', '������', '������', '������', 'Ȫ����', '�˴���',
                 '�Ͳ���', '������', '������', '������', '������', '������', '��ׯ��',
                 '������', '������', '����ɽ��', '������', '������', '��Ӫ��', '��ͨ��',
                 '������', '������', '������', '������', '��̨��', '���Ƹ���', '����',
                 'ͭ����', '������', '�Ž���', 'Ϋ����', '������', '������', '������',
                 '��ƽ��', '��������', '������', '�γ���', '̨����', '��ɽ��', '������',
                 'Ƽ����', '̩����', '������', '��ˮ��', '������', '������', '������',
                 '����', '��ɽ��', '������', 'ӥ̶��', '������', '̩����', '������',
                 '������', '��Ǩ��', '������', '������', '������', '�ĳ���', '������',
                 '������', '������', '������', '������', '֣����', '�人��', '��ɳ��',
                 '������', '��ʯ��', '������', '������', 'ʮ����', '��̶��', '������',
                 '������', '������', '������', '�˲���', '������', 'ƽ��ɽ��', '������',
                 '������', '������', '������', '�żҽ���', '������', '������', '������',
                 '�����', '�Ƹ���', '������', '������', 'Т����', '¦����', '�����',
                 '������', '������', '����Ͽ��', '������', '������', '�ױ���', '������',
                 '�ܿ���', 'פ������', '������', '������', '��Դ��', '������', '������',
                 '������', '������', '������', '������', '�麣��', '������', '��ͷ��',
                 '������', '��ɽ��', '������', '�ع���', '������', 'տ����', '������',
                 '������', '�����', '������', '������', 'ï����', '������', '������',
                 '��ɫ��', '÷����', '�ӳ���', '��β��', '������', '��Դ��', '���Ǹ���',
                 '������', '��Զ��', '��ݸ��', '��ɽ��', '������', '������', '�Ƹ���',
                 '�ɶ���', '������', '������', '������', '������', '����ˮ��', '��ͨ��',
                 '�Թ���', '������', '������', '��֦����', '��˳��', '��Ϫ��', '������',
                 '�ն���', '������', '��ɽ��', '��Ԫ��', '������', '������', '�ٲ���',
                 '�ڽ���', '��ɽ��', '������', '�˱���', '�ϳ���', '������', '�Ű���',
                 '�㰲��', '������', 'üɽ��', '������', '������', '������', '������',
                 '��³ľ����', '������', '��������', 'ʯ��ɽ��', '����������', '������',
                 '�����', '������', 'ͭ����', '������', '��ԭ��', 'μ����', '��ˮ��',
                 '������', '������', '��Ȫ��', '������', '��Ҵ��', '������', '������',
                 '�Ӱ���', '������', '������', '¤����', 'ƽ����', '������',
                 '����', '�Ϻ�', '���', '����', 'ʯ��ׯ', '̫ԭ', '���ͺ���',
                 '��ɽ', '��ͬ', '��ͷ',
                 '�ػʵ�', '��Ȫ', '�ں�', '����', '����', '���',
                 '��̨', '����', '���ױ���', '����', '˷��', 'ͨ��', '�żҿ�',
                 '����', '�����첼', '�е�', '����', '������˹', '����', '����',
                 '�����׶�', '�ȷ�', '�ٷ�', '��ˮ', '�˳�', '������', '����',
                 '����', '�������', '����', '����', 'ĵ����', '��ƽ', '��ɽ',
                 '��ľ˹', '��Դ', '��˳', '����', 'ͨ��', '��Ϫ', '����',
                 '��ɽ', '����', '����', '�׳�', '����', '�׸�', '��ԭ',
                 'Ӫ��', '˫Ѽɽ', '����', '��̨��', '����', '�绯', '�̽�',
                 '�ں�', '����', '����', '��«��', '�Ͼ�', '����', '�Ϸ�',
                 '����', '�ϲ�', '����', '����', '����', '�ߺ�', '����',
                 '����', '�ൺ', '����', '����', '����', 'Ȫ��', '�˴�',
                 '�Ͳ�', '����', '����', '����', '����', '����', '��ׯ',
                 '����', '����', '����ɽ', '����', '����', '��Ӫ', '��ͨ',
                 '����', '����', '����', '����', '��̨', '���Ƹ�', '��',
                 'ͭ��', '����', '�Ž�', 'Ϋ��', '����', '����', '����',
                 '��ƽ', '������', '����', '�γ�', '̨��', '��ɽ', '����',
                 'Ƽ��', '̩��', '����', '��ˮ', '����', '����', '����',
                 '��', '��ɽ', '����', 'ӥ̶', '����', '̩��', '����',
                 '����', '��Ǩ', '����', '����', '����', '�ĳ�', '����',
                 '����', '����', '����', '����', '֣��', '�人', '��ɳ',
                 '����', '��ʯ', '����', '����', 'ʮ��', '��̶', '����',
                 '����', '����', '����', '�˲�', '����', 'ƽ��ɽ', '����',
                 '����', '����', '����', '�żҽ�', '����', '����', '����',
                 '���', '�Ƹ�', '����', '����', 'Т��', '¦��', '���',
                 '����', '����', '����Ͽ', '����', '����', '�ױ�', '����',
                 '�ܿ�', 'פ����', '����', '����', '��Դ', '����', '����',
                 '����', '����', '����', '����', '�麣', '����', '��ͷ',
                 '����', '��ɽ', '����', '�ع�', '����', 'տ��', '����',
                 '����', '���', '����', '����', 'ï��', '����', '����',
                 '��ɫ', '÷��', '�ӳ�', '��β', '����', '��Դ', '���Ǹ�',
                 '����', '��Զ', '��ݸ', '��ɽ', '����', '����', '�Ƹ�',
                 '�ɶ�', '����', '����', '����', '����', '����ˮ', '��ͨ',
                 '�Թ�', '����', '����', '��֦��', '��˳', '��Ϫ', '����',
                 '�ն�', '����', '��ɽ', '��Ԫ', '����', '����', '�ٲ�',
                 '�ڽ�', '��ɽ', '����', '�˱�', '�ϳ�', '����', '�Ű�',
                 '�㰲', '����', 'üɽ', '����', '����', '����', '����',
                 '��³ľ��', '����', '������', 'ʯ��ɽ', '��������', '����',
                 '���', '����', 'ͭ��', '����', '��ԭ', 'μ��', '��ˮ',
                 '����', '����', '��Ȫ', '����', '��Ҵ', '����', '����',
                 '�Ӱ�', '����', '����', '¤��', 'ƽ��', '����']

nu = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-']

curFile = []

curPath = os.getcwd()
dstPath = curPath + os.sep + '������'
for allFile in os.walk(curPath):
    for fileName in allFile[2]:
        if '������' not in allFile[0]:
            if 'δ��ȡ' not in allFile[0]:
                if '����' not in allFile[0]:
                    curFile.append(allFile[0] + os.sep + fileName)
# curFile = os.listdir(curPath)
result = open('result.txt', 'w')
result.write('����,����֤,�绰,����\n')
curNum = 0
findNum = 0
failNum = 0
jiheNum = 0
weitiqu = 0
fenleijieguo = 0
sumNum = len(curFile)
try:
    os.mkdir('δ��ȡ')
except:
    pass
try:
    os.mkdir('����')
except:
    pass
try:
    os.mkdir('������')
except:
    pass
for files in curFile:
    curNum = curNum + 1
    print str(curNum) + '/' + str(sumNum) + '\r',
    flag = 0
    contains = (files.find('.htm') >= 0)  # and(files.find('-') >= 0)
    if contains:
        i = 0
        tempFile = os.path.split(files)[1]
        while (not(tempFile[i] in nu)) and (tempFile[i] != '.'):
            i = i + 1
        Id = re.search(r'\d{17}[\dX]', tempFile)
        File = open(files)
        lines = File.readlines()
        if len(lines) > 394:
            if flag == 0:
                m = re.search(r'>1\d{10}<', lines[245])
                if m:
                    flag = 1
                    phone = m.group(0)[1:-1]
            if flag == 0:
                for line in lines:
                    m = re.search(r'>1\d{10}<', line)
                    if m:
                        flag = 1
                        phone = m.group(0)[1:-1]
                    if flag == 1:
                        for c in city_name:
                            if c in line:
                                flag = 2
                                city = c
                                break
                        if flag == 2:
                            break
                    if flag == 2:
                        break
            else:
                for line in lines[270], lines[273], lines[378], lines[393]:
                    for c in city_name:
                        if c in line:
                            if flag == 1:
                                city = c
                                flag = 2
                                break
                    if flag == 2:
                        break
            if flag == 2:
                result.write(tempFile[:i] + ",")
                if Id:
                    result.write(Id.group(0) + ",")
                else:
                    result.write(",")
                result.write(phone + ",")
                result.write(city + "\n")
                findNum = findNum + 1
                try:
                    os.mkdir(dstPath + os.sep + city)
                except:
                    pass
                try:
                    shutil.copy(files, dstPath + os.sep + city)
                except:
                    # os.remove(files)
                    failNum = failNum + 1
                    fenleijieguo = fenleijieguo + 1
        File.close()
        if flag == 0:
            try:
                shutil.copy(files, 'δ��ȡ')
            except:
                # os.remove(files)
                failNum = failNum + 1
                weitiqu = weitiqu + 1
        try:
            shutil.move(files, '����')
        except:
            pass
            failNum = failNum + 1
            jiheNum = jiheNum + 1

result.close()

print '������ϣ�'
print '��' + str(sumNum) + '��html�ļ����ɹ���ȡ' + str(curNum) + '���ļ�'
print '����' + str(failNum) + '���ļ��ظ����ƶ�ʧ��'
print '����' + str(fenleijieguo) + '���ļ��ڷ��������ظ�',
print str(weitiqu) + '���ļ���δ��ȡ���ظ�',
print str(jiheNum) + '���ļ��ڼ������ظ�'


def delete_gap_dir(di):
    if os.path.isdir(di):
        for d in os.listdir(di):
            delete_gap_dir(di + os.sep + d)

        if not os.listdir(di):
            os.rmdir(di)
            print('�Ƴ���Ŀ¼: ' + di)
print '������������Ƴ���Ŀ¼'
os.system('pause')

delete_gap_dir(curPath)