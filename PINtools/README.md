# PIN tools

使用该脚本前，建议前往 [ipfs.io](https://ipfs.io) 稍微了解一些**必要**的知识点，如果你觉得你能都懂了，那就请继续往下看。

使用该脚本你可以快速的在你自建的本地IFPS节点pin住 i-Book.in 索引的全部资源，这将为其他人带来更快的连接速度，就像BT做种一样。当你全部pin下来之后，你在本地访问 i-Book.in 获取到的 Qmhash 就可以直接在本地节点下载，不需要从网上再次下载，理论上可以达到秒下的速度。

## 快速开始

### 必要环境：
```
Linux (目前仅测试了Ubuntu 16.04，求帮忙测试其他平台) 

Python3.7

大于100GB的储存空间
```
### 安装 ipfs-go
如果你需要自定义ipfs-go的储存位置，使用这个命令：
```
export IPFS_PATH="绝对路径"

```
使用以下代码安装的ipfs-go默认repo储存位置为`/root/.ipfs`。
```
wget https://dist.ipfs.io/go-ipfs/v0.4.23/go-ipfs_v0.4.23_linux-amd64.tar.gz && tar xvfz go-ipfs_v0.4.23_linux-amd64.tar.gz && cd go-ipfs/ && sudo ./install.sh && ipfs init
```
上述命令执行完毕将会返回一个类似的输出就说明安装好了：
```
generating 2048-bit RSA keypair...done
peer identity: QmTvSJEh3xarHMUj6uamQwnnvbYXH4vjttAehKjBvixxJH
to get started, enter:

        ipfs cat /ipfs/QmS4ustL54uo8FzR9455qaxZwuMiUhyvMcX9Ba8nUH4uVv/readme
```
启动ipfs-go：
```
ipfs daemon #& 可选，后台持续运行
```
如果需要后台持续运行，就在命令后面加上`&`。

### 安装 ipfshttpclient

```
pip3 install ipfshttpclient
```

## 使用 PIN tools

### 下载

如果你的网络OK，可以使用github，那就用下面这个脚本下载。
```
wget https://raw.githubusercontent.com/SaltyLeo/i-book.in/master/PINtools/pin_tools_BATE0.1.py
```
如果网络不OK，不能访问github，那就使用我备份到网站上的链接，内容都是一样的。
```
wget https://book.tstrs.me/tools/pin_tools_BATE0.1.py
```
### 使用

请在运行该脚本前确保已启动ipfs-go。使用以下命令运行脚本：
```
python3 pin_tools_BATE0.1.py
```
![](https://photo-1252237247.cos.ap-shanghai.myqcloud.com/20200417164014.png)
### pin文件

在上述界面输入1-19按回车后，脚本将自动下载本项目Qmhash文件夹内的list文件进行pin操作。出现下述界面即为正在进行pin操作种。耗时未知，但理论上人越多速度越快，建议配合使用screen放在后台运行，

![](https://photo-1252237247.cos.ap-shanghai.myqcloud.com/20200417162430.png)

## BUG反馈

如果发现任何bug，或其他使用上的问题，欢迎提issue反馈或到TG群组：[i-Book.in 讨论组](https://t.me/i_book_in) 反馈。

