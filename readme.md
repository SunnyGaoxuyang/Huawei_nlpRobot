工程环境:
    Python版本:2.7.11
    操作系统: Win8.1
    集成开发环境: PyCharm 4.5.2

python 包及其版本:
    jieba (0.38)
    gensim(0.12.4)
    然而其他的依赖包你应该装好,包括numpy等重要的包
    如果出现gensim报错的话很大可能是numpy和scipy的安装方式有误,请重新安装,这也从另一方面说明你的包在安装的时候有问题

文件层次:
    nlp
      |-- reply_lib 用于存放回复库的文件夹
      |     |-- alpha.txt 测试版本使用的回复文件(由text_processing_script.py处理alpha的内容物得到的)
      |     |-- beta.txt 融合素材文本1
      |     |-- gamma.txt 融合素材文本2
      |     |-- delta.txt 融合素材文本3
      |
      |-- jieba_cut.py 面向输入语句,使用jieba分词库进行处理
      |-- synonym.py 利用google的gensim查询一个词的近义词
      |-- main.py 工程的主函数
      |-- text_processing_script.py 用于处理alpha内容物的脚本,本身并不是工程结构的一部分
      |-- alpha 高旭阳的聊天机器人语料库,其下的文件目录省略

作者相关:
    姓名: 高旭阳
    github: SunnyGaoxuyang
    单位: UESTC
    联系方式: QQ-1064803638-折桂

最新更新信息:
    2016/5/4 进行了局部try的改写,使得在调试的过程中能看见错误