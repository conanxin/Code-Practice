说明：
=============

运行两个节点，包括本目录下的`simple_node.py`以及test目录下的`simple_node.py`，这两个目录下又分别有两个文件夹files1和files2，其中在files2中有一个test.txt文件。

在当前目录下运行
`python simple_node.py http://localhost:4242 files1 secret1`

在真正的程序中使用完整的机器名替换localhost，也可使用更复杂的密码代替secret1。

进入test目录，运行
`python simple_node.py http://localhost:4243 file2 secret2`


