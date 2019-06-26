# TF-IDF原理
TF-IDF(Term Frequency-Inverse Document Frequency, 词频-逆文件频率)是一种用于资讯检索与资讯探勘的常用加权技术。

TF-IDF是一种统计方法，用以评估一字词对于一个文件集或一个语料库中的其中一份文件的重要程度。字词的重要性随着它在文件中出现的次数成正比增加，但同时会随着它在语料库中出现的频率成反比下降。

总结： 一个词语在一篇文章中出现次数越多, 同时在所有文档中出现次数越少, 越能够代表该文章的主题。
算法权重的设计必须满足：一个词预测主题的能力越强，权重越大，反之，权重越小。



## 词频

- 词频 (term frequency, TF) 指的是某一个给定的词语在该文件中出现的次数。这个数字通常会被归一化(一般是词频除以文章总词数), 以防止它偏向长的文件。（同一个词语在长文件里可能会比短文件有更高的词频，而不管该词语重要与否。）

- 词频公式：

​       $TF_w = \frac{在某一类中词条w出现的次数}{该类中所有的词条数目}$



## 逆向文件频率

- 逆向文件频率 (inverse document frequency, IDF) 的主要思想是：如果包含词条t的文档越少, IDF越大，则说明词条具有很好的类别区分能力。某一特定词语的IDF，可以由总文件数目除以包含该词语之文件的数目，再将得到的商取对数得到。

​      $IDF = log(\frac{语料库的文档总数}{包含词条w的文档数+1}), 分母之所以要加1，是为了避免分母为0$

- 某一特定文件内的高词语频率，以及该词语在整个文件集合中的低文件频率，可以产生出高权重的TF-IDF。因此，TF-IDF倾向于过滤掉常见的词语，保留重要的词语。 

   $TF-IDF = TF * IDF$



## TF_IDF小结

TF-IDF是非常常用的文本挖掘预处理基本步骤，但是如果预处理中使用了Hash Trick，则一般就无法使用TF-IDF了，因为Hash Trick后我们已经无法得到哈希后的各特征的IDF的值。使用了IF-IDF并标准化以后，我们就可以使用各个文本的词特征向量作为文本的特征，进行分类或者聚类分析。

当然TF-IDF不光可以用于文本挖掘，在信息检索等很多领域都有使用。因此值得好好的理解这个方法的思想。



## 相关应用

[TF-IDF与余弦相似性的应用（一）：自动提取关键词](http://www.ruanyifeng.com/blog/2013/03/tf-idf.html)
[TF-IDF与余弦相似性的应用（二）：找出相似文章](http://www.ruanyifeng.com/blog/2013/03/cosine_similarity.html)



# 词袋模型

词袋模型假设我们不考虑文本中词与词之间的上下文关系，仅仅只考虑所有词的权重。而权重与词在文本中出现的频率有关。
词袋模型首先会进行分词，在分词之后，通过统计每个词在文本中出现的次数，我们就可以得到该文本基于词的特征，如果将各个文本样本的这些词与对应的词频放在一起，就是我们常说的向量化。向量化完毕后一般也会使用 TF-IDF 进行特征的权重修正，再将特征进行标准化。 再进行一些其他的特征工程后，就可以将数据带入机器学习模型中计算。
词袋模型的三部曲：分词（tokenizing），统计修订词特征值（counting）与标准化（normalizing)。
词袋模型有很大的局限性，因为它仅仅考虑了词频，没有考虑上下文的关系，因此会丢失一部分文本的语义。
在词袋模型统计词频的时候，可以使用 sklearn 中的 CountVectorizer 来完成。

词袋模型同样有以下缺点：
- 词向量化后，词与词之间是有大小关系的，不一定词出现的越多，权重越大。
- 词与词之间是没有顺序关系的。


词频向量化，文本矩阵化，使用词袋模型，以TF-IDF特征值为权重

参考来源：
[文本数据预处理](https://blog.csdn.net/m0_37324740/article/details/79411651)


# 点互信息和互信息

## 点互信息PMI

点互信息PMI到点互信息PMI(Pointwise Mutual Information)这个指标来衡量两个事物之间的相关性（比如两个词）。

其原理很简单，公式如下：

![img](https://img-blog.csdn.net/20170603000958939?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxMzcxMDI2NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

在概率论中，我们知道，如果x跟y不相关，则p(x,y)=p(x)p(y)。二者相关性越大，则p(x, y)就相比于p(x)p(y)越大。用后面的式子可能更好理解，在y出现的情况下x出现的条件概率p(x|y)除以x本身出现的概率p(x)，自然就表示x跟y的相关程度。

举个自然语言处理中的例子来说，我们想衡量like这个词的极性（正向情感还是负向情感）。我们可以预先挑选一些正向情感的词，比如good。然后我们算like跟good的PMI。



## 互信息MI

点互信息PMI其实就是从信息论里面的互信息这个概念里面衍生出来的。  

互信息即：

![img](https://img-blog.csdn.net/20170603000903771?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxMzcxMDI2NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

其衡量的是两个随机变量之间的相关性，即一个随机变量中包含的关于另一个随机变量的信息量。所谓的随机变量，即随机试验结果的量的表示，可以简单理解为按照一个概率分布进行取值的变量，比如随机抽查的一个人的身高就是一个随机变量。

可以看出，互信息其实就是对X和Y的所有可能的取值情况的点互信息PMI的加权和。因此，点互信息这个名字还是很形象的。



## sklearn编程

```
from sklearn import metrics as mr
mr.mutual_info_score(label,x)
```


## 参考来源

https://blog.csdn.net/zrc199021/article/details/53728499

https://www.cnblogs.com/pinard/p/6693230.html

[信息熵，条件熵，互信息的通俗理解](https://blog.csdn.net/ranghanqiao5058/article/details/78458815)

[互信息](https://www.cnblogs.com/gatherstars/p/6004075.html)

[sklearn：点互信息和互信息](https://blog.csdn.net/u013710265/article/details/72848755)



# https://baijiahao.baidu.com/s?id=1604074325918456186&wfr=spider&for=pc


使用第二步生成的特征矩阵，利用互信息进行特征筛选