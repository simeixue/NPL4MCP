0916: 根据tool的名字能够获得完整的implementation
所以下面这种函数名改变的情况找不到：
在找tool的implementation的时候，代码是去找函数名为：qdrant-find的函数体，而实际的实现是find(find_foo = find)
![alt text](image.png)