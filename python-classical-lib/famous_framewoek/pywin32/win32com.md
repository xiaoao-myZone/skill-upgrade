COM(Component Object Model)组件对象模型
·COM是使用或发布对象的一种技术，不管执行它的是什么语言
·COM允许对象在不知道其他对象的情况下与之通信，甚至连对方的运行语言也不需要知道
·COM处理接口和对象，将对象与实现进行了明确的区分，接口定义了对象如何使用，
  对象用来实现接口的定义的功能。

COM的典型接口——IDispatch，允许COM对象在脚本环境中使用，比如VB和python

在COM中class和python中相似，对象是类的实例，创建一个新的对象，必须有正确的类被定为并使用

类在登记簿中以一个唯一的但是复杂的代码，CLSID(class ID)，和一个不复杂但是不一定唯一的
  ProgID（program ID）代码标识

··类、对象、接口之间的关系

每个COM对象可以定义自己的属性与方法

生成CLSID的方法
import pythoncom
pythoncom.CreateGuid()
Guid = Globally Unique Identifiers

·借口可以继承和扩展，IUnknown是所有接口的基础

·类提供对象与一系列接口，至少两个，一个是IUnknown

·ProgID是一个描述对象的字符串，创建对象一般用ProgID，而不是CLSID，但是ProgID不是唯一的，注意冲突

·COM支持接口的方法，但是不支持属性，并且不支持使用比C++更高级的语言运行
  但是COM定义了IDispatch接口的方法可以实现更高级语言的运行，它允许对象公开模型
  在用户需要方法与属性时确定他们，而不需要预定义

·Python与COM之间的接口由两部分组成：pythoncom与为win32com
  前者主要负责将原始的COM接口公开给python，对于许多标准COM接口，有python对象可以公开它们
  后者通过pythoncom提供额外的功能，win32com.client支持客户端(调用接口)，
  win32com.server支持服务端(执行接口)

·自动化对象就是通过IDispatch公开方法和属性的COM对象

·makepy:对Excel对象模型的所有引用都使用makepy生成的早期绑定功能。

·前绑与后绑，大概就是前绑一次性将属性和方法都给了python，而后绑则是一直与python互动

·enumerations枚举
