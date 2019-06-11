# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 15:11:41 2019

@author: gzy10
"""

#第三部分，人员删除

import os
import shutil

def delete_person(name):
    people = './people'
    if not os.path.exists(people):
        os.makedirs(people)
    
    index = 1
    person_all = []
    for (path, dirnames, filenames) in os.walk(people):
        for filename in filenames:
            if filename.endswith('.jpg'):
                person_all.append(filename)
                index += 1
    
    if 'person_'+name+'.jpg' in person_all:
        shutil.rmtree(name)
        shutil.rmtree('person_'+name)
        os.remove('people/person_'+name+'.jpg')
        print("删除完成！")
    else:
        print("所删成员不存在，请重新输入！")

def person_delete(option=0):
    name = input("请输入要删除的人员学号：")
    de_path = 'person_' + str(name)
    if not os.path.exists(de_path):
        print('要删除的人员不存在！')
        option = input("请选择重新输入或者退出（0:重新输入，1:退出）")
        if option == str(0):
            person_delete(option)
        elif option == str(1):
            option = 0
        else:
            print("输入非法！")
    if os.path.exists(de_path):
        delete_person(name)
            
person_delete()