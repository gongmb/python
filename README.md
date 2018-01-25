# python

安装PyUserInput可以轻松实现模拟鼠标点击，安装方法：
apt-get install python-pip
pip install pymouse
使用举例：
from pymouse import PyMouse
m = PyMouse()
m.position() #获取当前的鼠标坐标
m.move(x,y)
m.click(x,y) #模拟点击
m.press(x,y) #按下鼠标
m.release(x,y) #释放鼠标


{
   "code":   200 ,
   "data":  [
    {
       "code":   200 ,
       "content":   "gonbm" ,
       "dataId":   "5045125a-15a5-45f0-99e9-3c5c5bb6e69c" ,
       "msg":   "OK" ,
       "results":  [
        {
           "label":   "meaningless" ,
           "rate":   100 ,
           "scene":   "antispam" ,
           "suggestion":   "block"
        }
      ],
       "taskId":   "txt7$uKKwcBXJC5zMB3e@$Olf-1oisJf"
    }
  ],
   "msg":   "OK" ,
   "requestId":   "30E3CF1F-75D7-472B-A7F8-83968D7B555E"
}

##场景（scene）和分类（label）
+ 垃圾检测会结合行为、内容采用多维度、多种模型、多种检测手段对文本进行垃圾与否的识别，识别色情、广告、灌水、渉政、辱骂等风险。用户可以自定义敏感词，自定义关键词请前往云盾内容安全控制台添加.


##对应关系如下：

+ 场景(scene)中文名  场景（scene）	分类（label）	备注
+ 垃圾检测	        antispam	    normal	        正常文本
+ 垃圾检测	        antispam	    spam        	含垃圾信息
+ 垃圾检测           antispam	    ad	            广告
+ 垃圾检测	        antispam	    politics	    渉政
+ 垃圾检测           antispam	    terrorism	    暴恐
+ 垃圾检测	        antispam	    abuse	        辱骂
+ 垃圾检测           antispam	    porn	        色情
+ 垃圾检测           antispam	    flood	        灌水
+ 垃圾检测	         antispam	    contraband	    违禁
+ 垃圾检测           antispam	    customized	    自定义(比如命中自定义关键词)

##返回body中的Data字段是JSON数组，每一个元素有如下字段：​

###字段	类型	是否必须	说明
+ code	整形	必须	错误码，和http的status code一致
+ msg	字符串	必须	错误描述信息
+ dataId	字符串	可选	对应的请求中的dataId
+ taskId	字符串	必须	云盾内容安全服务器返回的唯一标识该检测任务的ID
+ content	字符串	可选	对应的请求中的content
+ results	数组	可选	当成功时（code == 200）,该结果的包含一个或多个元素。每个元素是个结构体。参见下表。

##上表results中包含的元素说明：​

###字段	类型	是否必须	说明
+ scene	字符串	必须	风险场景
+ suggestion	字符串	必须	建议用户处理，取值范围：[“pass”, “review”, “block”], pass:文本正常，review：需要人工审核，block：文本违规，可以直接删除或者做限制处理
+ label	字符串	必须	该文本的分类，取值范围参考1.1小节
+ rate	浮点数	必须	结果为该分类的概率；值越高，越趋于该分类；取值为[0.00-100.00], 分值仅供参考，您只需要关注label和suggestion的取值即可
+ extras	JSON对象	可选	附加信息，比如命中了您自定义的词库,返回词库code.该值将来可能会调整，建议不要在业务上进行依赖
+ details	数组	可选	命中风险的详细信息。参见下表