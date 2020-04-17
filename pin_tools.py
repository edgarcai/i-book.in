# -*- coding: utf-8 -*-
import re
import os
import sys
import ipfshttpclient
client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001/http')

def ipfs_pin(num,count):
    filename = "%sGB-%sGB.json"%((int(num)-1)*100,int(num)*100)
    if os.path.exists("%s/%s"%(os.getcwd(),filename)) == True:
        os.system("rm %s/%s"%(os.getcwd(),filename))
    print('正在下载数据包，请稍后...')
    down = 'wget -q https://book.tstrs.me/hash/%s'%filename
    os.system(down)
    file = open(filename)
    linn_num = open('%s/%s'%(os.getcwd(),filename)).read()
    linn_num_count = linn_num.count('\n')
    print('数据包【%s】 共计%s个文件，约100GB。'%(num,linn_num_count))
    for line in file:
        ipfs_hash = line.replace('\n','') 
        client.pin.add(ipfs_hash)
        print('进度: '+'{:.2%}。'.format(int(count)/int(linn_num_count))+'正在pin第 %s 个文件。'%count)
        count = count +1

def choose_opt():
    print("""\n\n ██     ██████                     ██        ██         
░░     ░█░░░░██                   ░██       ░░          
 ██    ░█   ░██   ██████   ██████ ░██  ██    ██  ███████ 
░██ ███░██████   ██░░░░██ ██░░░░██░██ ██    ░██ ░██░░░██
░██░░░ ░█░░░░ ██░██   ░██░██   ░██░████     ░██ ░██  ░██
░██    ░█    ░██░██   ░██░██   ░██░██░██  ██░██ ░██  ░██
░██    ░███████ ░░██████ ░░██████ ░██░░██░██░██ ░██  ░██
░░     ░░░░░░░   ░░░░░░   ░░░░░░  ░░  ░░ ░░ ░░  ░░   ░░ 
\n-----------------------------------------------------------\ni-Book.in PIN_tools(BATE_0.1)\n\n目前i-Book.in的索引指向的资源数据大约为1.9TB，由无数热心网友齐心协力pin在互联网上。但随着使用的人越来越多，并且毫无顾忌地使用迅雷等其他多线程工具，数据的传输变得越来越慢。\n\n如果你愿意帮助大家，将数据扩散的更广(这将占用你的部分储存空间和宽带)，可以使用本工具，快速的pin住文件。你在本地节点pin住的文件将会加速你和其他人从IPFS网络获取数据的速度，理论上是内网宽带上限。\n\n为了方便大家pin，我们将其分割成19个大约100GB的hash list，储存在GitHub。本工具可以快速pin list文件。\n-----------------------------------------------------------\n\n【功能】：\n\n  [0]、退出脚本\n\n  [1-19]、pin文件 \n  输入1-19任意一个数字即可pin相应的数据包\n\n\n""")
    opt = input("请输入数字 : ")
    return opt

if __name__ == "__main__":
    opts = choose_opt()
    if opts.isdigit() == True:
        if int(opts)>=1 and int(opts) <=19:
            ipfs_pin(opts,1)
        elif int(opts) == 0:
            sys.exit()  
        else:
            print('输入错误，自动退出。')
            sys.exit() 
    else:
        print('输入错误，自动退出。')
        sys.exit() 

