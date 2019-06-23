# 【预备任务】
## 学习了tensorflow的安装方式，配置好了相关环境
## 学习了tensorflow的语法基础
    使用图(graphs)来表示计算任务、在被称之为会话(Session)的上下文(context)中执行图、使用tensor表示数据、通过变量(Variable)维护状态；使用feed和fetch为任意的操作赋值或者从其中获取数据。
## 关注NLP基础技术、NLP核心技术、NLP+的介绍


# 【Task1 数据集探索 (2 days)】
## 数据集
    数据集：中、英文数据集各一份
    中文数据集：THUCNews
    THUCNews数据子集：https://pan.baidu.com/s/1hugrfRu 密码：qfud
    英文数据集：IMDB数据集 Sentiment Analysis
    
## 影评文本分类
    IMDB数据集下载和探索参考TensorFlow官方教程|TensorFlow科赛 - Kesci.com

## CNN字符级中文文本分类
    THUCNews数据集下载和探索
    参考博客中的数据集部分和预处理部分：CNN字符级中文文本分类-基于TensorFlow实现 - 一蓑烟雨 - CSDN博客
    参考代码：text-classification-cnn-rnn/cnews_loader.py 
    
## 学习召回率、准确率、ROC曲线、AUC、PR曲线这些基本概念
    参考1：机器学习之类别不平衡问题 (2) —— ROC和PR曲线_慕课手记
    
    
## 影评文本分类实验代码：
https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/keras/basic_text_classification.ipynb#scrollTo=RnKvHWW4-lkW