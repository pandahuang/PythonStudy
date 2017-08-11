# -*-coding:utf-8-*-

'''
First Stage...
'''
# 1.input output
# print "Please Input Your Name:"
# Name = raw_input()
# print "%s,Welcome to Python!"%(Name)

# 2.not to transform
# print r'\\\n\\\\'

# encode decode
# print '中文'.decode('utf-8')

# 列表生成式的两层循环
# print [m+n for m in range(1,10) for n in range(11,20)]
# import os
# print [d for d in os.listdir('.')]

# 对dict按key排序，升序，降序
# dict = {2:'b',1:'a',4:'d',3:'c'}
# print sorted(dict.items(), key=lambda d:d[0])
# print sorted(dict.items(), key=lambda d:d[1])
# print sorted(dict.items(), key=lambda d:d[0], reverse = True)

# 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self
# class Hero(object):
# 	__hero_level = 1
# 	def __init__(self, hero_name, hero_property, hero_skill):
# 		self.hero_name = hero_name
# 		self.hero_property = hero_property
# 		self.hero_skill = hero_skill
#
# 	def print_hero(self):
# 		print "hero name is:%s"%(self.hero_name)
# 		print "hero property is:%s"%(self.hero_property)
# 		print "hero skill is:%s"%(self.hero_skill)
# 		print "hero level is:%d"%(self.__hero_level)
# 	def level_up(self):
# 		self.__hero_level += 1
# 	def set_level(self, lvl):
# 		self.__hero_level = lvl
# 	def get_level(self):
# 		return self.__hero_level
#
#
# if __name__ == "__main__":
#     sevn = Hero("sevn", "strength", ["strom hamer", "devision", "hoo", "god like"])
#     sevn.print_hero()
#     sevn.level_up()
#     sevn.print_hero()
#     sevn.set_level(25)
#     sevn.print_hero()

# 多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，因为Dog、Cat、Tortoise……都是Animal类型，然后，按照Animal类型进行操作即可。由于Animal类型有run()方法，因此，传入的任意类型，只要是Animal类或者子类，就会自动调用实际类型的run()方法，这就是多态的意思

# type()函数
# isinstance()函数
# dir()函数获得一个对象的所有属性和方法

# python允许给一个类或者实例动态绑定属性和方法(使用MethodType())，__slots__可以限制可添加的属性
# @property，python的内置装饰器，负责把一个方法变成属性调用的
# class Student(object):

#     @property
#     def birth(self):
#         return self._birth

#     @birth.setter
#     def birth(self, value):
#         self._birth = value

#     @property
#     def age(self):
#         return 2014 - self._birth

# python允许多重继承，需要给某个类加入额外功能时可以通过多重继承实现，这种设计成为Mixin
# 定制类__str__,__repr__,__iter__,getitem__,__getatrr__,__call__
# type函数可用于直接创建类
# def fn(self, name='world'):  # 先定义函数
#     print('Hello, %s.' % name)
#
#
# Hello = type('Hello', (object,), dict(hello=fn))  # 创建Hello class

# Python GUI
# from Tkinter import *
# import tkMessageBox
#
#
# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()
#
#     def createWidgets(self):
#         self.helloLabel = Label(self, text="Hello World!")
#         self.helloLabel.pack()
#         self.quitButton = Button(self, text="Quit", command=self.quit)
#         self.quitButton.pack()
#         self.nameInput = Entry(self)
#         self.nameInput.pack()
#         self.alertButton = Button(self, text="hello", command=self.hello)
#         self.alertButton.pack()
#
#     def hello(self):
#         name = self.nameInput.get() or "World!"
#         tkMessageBox.showinfo("Message", "Hello %s" % name)
#
#
# if __name__ == "__main__":
#     app = Application()
#     app.master.title("hello world!")
#     app.mainloop()

# Python TCP client
# import socket
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(("www.sina.com.cn", 80))
# s.send("GET / HTTP/1/1\r\nHost: www.sina.com.cn\r \nConnection: close\r\n\r\n")
#
# buffer = []
# while True:
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
# data = "".join(buffer)
#
# s.close()
#
# header, html = data.split("\r\n\r\n", 1)
# print len(data)

# Python TCP server
# import threading
# import socket
# import time
#
#
# def tcplink(sock, addr):
#     print "Accept new connection from %s:%s" % addr
#     sock.send("Welcome!")
#     while True:
#         data = sock.recv(1024)
#         time.sleep(1)
#         if data == "exit" or not data:
#             break
#         sock.send("Hello, %s" % data)
#     sock.close()
#     print "Connection from %s:%s closed." % addr
#
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(("127.0.0.1", 9998))
# s.listen(5)
# print "Waiting for connection.."
#
# while True:
#     sock, addr = s.accept()
#     t = threading.Thread(target=tcplink, args=(sock, addr))
#     t.start()

# Python TCP client
# client.py
# import socket
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(("127.0.0.1", 9998))
# print s.recv(1024)
# for data in ["Cheney", "Panda", "Olivia"]:
#     s.send(data)
#     print s.recv(1024)
# s.send("exit")
# s.close()

# Connect MySQL database
# import mysql.connector
#
# conn = mysql.connector.connect(user="root", password="password", database="test", use_unicode=True)
# cursor = conn.cursor()
# cursor.execute("create table user (id varchar(20) primary key, name varchar(20))")
# cursor.execute("insert into user (id, name) values (%s, %s)", ['1', 'Cheney'])
# print cursor.rowcount
# conn.commit()
# cursor.close()
#
# cursor = conn.cursor()
# cursor.execute("select * from user where id = %s", ('1',))
# values = cursor.fetchall()
# print values
# cursor.close()
# conn.close()

# Python Web Application
# WSGI Server
# from wsgiref.simple_server import make_server
# from web_app import application
#
# httpd = make_server("", 8000, application)
# print "Servering HTTP on port 8000..."
# httpd.serve_forever()

# web_app.py
# def application(environ, start_response):
#     start_response("200 OK", [("Content-Type", "text/html")])
#     return "<h1>Hello, %s!</h1>" % (environ["PATH_INFO"][1:] or "web")

# ==================================================================================================

'''
Second Stage...
'''

'''
1.必选参数
2.默认参数
3.可变参数
4.关键字参数
'''


def param_pass(*param1):
    for param in param1:
        print param


# param_pass(1,2,3)
# num = [1,2,3]
# param_pass(*num)

def param_pass_multi(name, age, school='TJU', *info, **hobits):
    print name, age, school
    print info
    print hobits


# param_pass_multi(1,2,*num, sport='Basket')

'''`
匿名函数
'''
f = lambda x, y: x * x + y * y
# print f(2,3)

'''
返回函数
函数闭包
'''


def str2num(str_in):
    def trans():
        return int(str_in)

    return trans


# f = str2num('2')
# print f()
# print f.__name__

'''
装饰器:在不改变代码原有结构的情况下，为某段代码动态添加新的功能，这种方法叫做装饰器
decorator是一个返回函数的高阶函数，它接收一个函数作为参数，并且返回一个函数
如果装饰器本身需要传入参数，就需要在装饰器外层再套一个函数，该函数接收装饰器要用的参数，返回装饰器本身
'''
import datetime
import functools


def log(func):
    @functools.wraps(func)  # 需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错
    def wrapper():
        print 'host name is Yixiang Huang.'
        # func()
        return func()  # 返回这个函数，其实跟执行这个函数是同样的作用

    return wrapper


def log_text(text):
    def log(func):
        @functools.wraps(func)
        def wrapper():
            print 'host name is %s' % text
            func()

        return wrapper

    return log


@log
@log_text('Panda')
def now():
    print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S');


# now = log(now)
# now = log_text('Panda')(now)
# now()
# print now.__name__

'''
面向对象 OOP
访问限制
继承和多态
使用@property
多重继承
定制类
'''


# 面向对象 OOP 定义一个类的语法
class Student(object):
    def __init__(self, name, age, gender, score):
        self.name = name
        self.age = age
        # 访问限制
        self.gender = gender  # public
        self.__score = score  # private

    def show_info(self):
        print 'My name is %s.' % self.name
        print 'I\'m %d years old.' % self.age
        print 'And, I\'m a %s' % self.gender


# Student('Lina', 16, 'girl', 59).show_info()

'''
面向对象
	1.@property，对于Class中的属性，一般有两种赋值和获取的方式，一个是直接通过类或实例加.调用，
	一种是通get和set方法。前者方便使用但是无法进行验证数据合法性等操作，后者可以验证但是使用麻烦。
	@property的方法可以同时兼顾二者。
'''


class Hero(object):
    # hero_name = ''
    def __init__(self, name, level, gift):
        self.hero_name = name
        self.__hero_level = level
        self.__hero_gift = gift

    def set_level(self, level):
        if not isinstance(level, int):
            raise ValueError('Your input must be an integer.')
        elif level < 1 or level > 25:
            raise ValueError('Your input must between [1, 25]')
        else:
            self.__hero_level = level

    def get_level(self):
        return self.__hero_level

    @property
    def hero_gift(self):
        return self.__hero_gift

    @hero_gift.setter
    def hero_gift(self, gift):
        if not isinstance(gift, str):
            raise ValueError('Your input must be a string.')
        else:
            self.__hero_gift = gift


# hero = Hero('AXE', 16, 'Attack')
# print hero.hero_name
# # print hero.__hero_level
# # hero.set_level('25')
# hero.set_level(25)
# print hero.get_level()
# print hero.hero_gift
# # hero.hero_gift = 7
# hero.hero_gift = 'Defense'
# print hero.hero_gift

# 继承和多态
class Animal(object):
    def run(self):
        print 'Animal is running...'


class Cat(Animal):
    def run(self):
        print 'Cat is running...'

    def meow(self):
        print 'Cat is mewing...'


class Dog(Animal):
    def run(self):
        print 'Dog is running...'

    def bark(self):
        print 'Dog is barking...'


# cat = Cat()
# dog = Dog()
# def run_twice(animal):
# 	animal.run()
# 	animal.run()
# run_twice(cat)

# 使用@property
# done

# 多重继承
'''
面向对象
	1.多重继承：多重继承的两种方式
		a.主线层次单一继承
		b.如需扩展额外功能，实现多重继承
'''


class Animal(object):
    pass


class Mammal(Animal):
    pass


class Bird(Animal):
    pass


class lion(Mammal):
    pass


class sparrow(Bird):
    pass


class Runnable(object):
    def run(self):
        print "Running..."


class Flyable(object):
    def fly(self):
        print "Flying..."


class elephant(Mammal, Runnable):
    pass


class eagle(Bird, Flyable):
    pass


# elephant_alex = elephant()
# elephant_alex.run()
# eagle_allen = eagle()
# eagle_allen.fly()

# 定制类
'''
面向对象
	1.定制类：可以用于定制class内部的一些功能
		a.__str__() 通过print类实例，可以打印class信息
		b.__repr__() 直接使用实例，不用print，也能打印出class信息
		c.__iter__() 实现__iter__()方法，再实现一个next()函数，可以让class作用于
		循环，通过调用class的next方法进行循环
		d.__getitem__() 可以通过下标的方式使用class，获取class内部信息
		e.__getattr__() 可以获取类的方法和属性，用于判断该类是否拥有某个方法或属性
'''

'''
异常处理
	1.try...except...finally...
	2.raise
	3.如果想要打开一个文件，可以尝试添加IOError
	4.在刚开始Import的时候可以尝试加入ImportError
	5.遍历字典的时候，可以尝试加入KeyError
	6.参数传递的时候，可以考虑使用TypeError
	7.ValueError
'''
# import logging
# infos = [('huangyixiang', 25), ('zhangqige', '24'), (55, 18), (35, '16')]
# def info_verify(infos):
# 	for name, age in infos:
# 		try:
# 			print 'My name is %s, I am %d years old.'%(name, age)
# 		except TypeError, e:
# 			print e
# 			logging.exception(e)
# 			continue
# 		finally:
# 			print 'Shanghai'
# info_verify(infos)

# try:
# 	print total
# except NameError, e:
# 	print e
# total = 0
# for num in range(10):
# 	total += num
# print total

'''
单元测试
	1.import unittest
	2.创建一个Test类，根据要测试的类来命名，该类要继承unittest.TestCase类
	3.setUp()方法和tearDown()方法在测试开始和测试结束时执行
	4.多种断言方式：assertEquals(),assertTrue(),with self.assertRaises(KeyError)
	5.以test开头的方法被默认为测试方法，不以test开头的方法测试时不会被执行
	6.运行单元测试的两种方法：
		1）在测试类Python文件的main函数中写入：unittest.main()
		2）命令行运行python -m unittest mydict_test
'''


class Dict(dict):
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


import unittest


class TestDict(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEquals(d.a, 1)
        self.assertEquals(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEquals(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEquals(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty


# if __name__=='__main__':
# 	unittest.main()

'''
序列化pickling,serialization
反序列化unpickling
把变量从内存中变成可存储或传输的过程称之为序列化
	1.使用Python内置pickle和cPickle模块
		1)使用pickle.dumps()方法将对象序列化成str，对应使用pickle.dumps()方法将str转回对象
		2）使用pickle.dump()方法将对象序列化并保存到本地文件，对应使用pickle.dump()方法从本地文件中读取序列化对象
		3）Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python彼此都
			不兼容，因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。
	2.如果想要序列化成一种通用的格式，可以使用xml和json格式，最常用的是json格式，使用json模块进行序列化操作
		1）如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为JSON，
			因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，
			并且比XML更快，而且可以直接在Web页面中读取，非常方便。
		2）json.dumps()方法返回一个str，json.loads()方法将json的str转回对象
		3）json也同样有json.dump()方法和对应的json.load()方法
		4）有一点需要注意，就是反序列化得到的所有字符串对象默认都是unicode而不是str。由于JSON标准规定JSON编码是UTF-8，
			所以我们总是能正确地在Python的str或unicode与JSON的字符串之间转换
	3.使用json模块进行高级序列化操作，将class实例序列化
		1)使用自定义方法告诉json如何将class实例序列化
		2）class都有__dict__属性，利用dafault=lambda obj:obj.__dict__的方法将class实例序列化
	4.from sklearn.externals import joblib 可以用来保存训练好的机器学习模型
		1）http://www.jianshu.com/p/113f33ab6f31
'''
# cPickle，pickle
# try:
# 	import cPickle as pickle
# except ImportError:
# 	import pickle
# dict_info = dict(name='Bob', age=20, score=88)
# dict_info_dump = pickle.dumps(dict_info)
# dict_info1 = pickle.loads(dict_info_dump)
# print dict_info1
# f = open('dump.txt', 'wb')
# pickle.dump(dict_info, f)
# f.close()
# f = open('dump.txt', 'rb')
# dict_info2 = pickle.load(f)
# f.close()
# print dict_info2

# import json
# d = dict(name='Bob', age=20, score=88)
# print json.dumps(d)
# json_str = '{"age": 20, "score": 88, "name": "Bob"}'
# print json.loads(json_str)

# student_lina = Student('Lina', 16, 'girl', 59)
# def student2json(student):
# 	return {'name':student.name, 'age':student.age, 'gender':student.gender, '_Student__score':student._Student__score}
# print json.dumps(student_lina, default=student2json)
# student_lina_json = json.dumps(student_lina, default=lambda obj:obj.__dict__)
# student_lina_copy = json.loads(student_lina_json)
# ?can not use function?
# student_lina_copy.show_info()

'''
 常用内建模块
 	1.collections
 	2.hashlib
 	3.itertools
'''
# namedtuple
from collections import namedtuple

Circle = namedtuple('Circle', ['x', 'y', 'r'])
circle = Circle(3, 4, 5)
# print 'The centre of a circle is ({x}, {y}), the radius is {r}'.format(x=circle.x, y=circle.y, r=circle.r)

# deque
from collections import deque

q = deque([1, 'a', 2, 'b', 3])
# print q
# q.append('c')
# print q
# q.appendleft('.')
# q.appendleft(0)
# print q
# q.popleft()
# print q

# defaultdict = dict.setdefault()
from collections import defaultdict

f = lambda: 'Key is not exist!'
dedict = defaultdict(f)
dedict['Panda'] = 'Huang Yixiang'
# print dedict['Panda']
# print dedict['Will']

# OrderedDict
from collections import OrderedDict

od = OrderedDict()
od.setdefault('enjoy', 'Miheng Hu')
od['Panda'] = 'Yixiang Huang'
od['Oujiba'] = 'Fan Ouyang'
od['shaoye'] = 'Feng Shi'
# for k in ['Panda', 'Oujiba', 'shaoye', 'enjoy', 'Falin']:
# 	print od.get(k)
names = ['Panda', 'Ouyang', 'Feng', 'Ouyang', 'Feng', 'Feng']
dnames = {}
for name in names:
    dnames[name] = dnames.setdefault(name, 0) + 1
# print dnames

# Counter
from collections import Counter

name_counter = Counter()
for name in names:
    name_counter[name] += 1
# print name_counter

# haslib:摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。
# 摘要算法之所以能指出数据是否被篡改过，就是因为摘要函数是一个单向函数，计算f(data)很容易，但通过digest反推data却非常困难。
import hashlib

# MD5是最常见的摘要算法，速度很快，生成结果是固定的128
md5 = hashlib.md5()
md5.update('huangyixiang')
# print md5.hexdigest()
md5_1 = hashlib.md5()
md5_1.update('huangyixiang')
# print md5_1.hexdigest()
# SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。
sha1 = hashlib.sha1()
sha1.update('huangyixiang')
# print sha1.hexdigest()

# itertools
import itertools

nums = itertools.count(0, 2)
for n in nums:
    # print n
    if n == 30:
        break
cycle_ABC = itertools.cycle('ABC')
repeat_A = itertools.repeat('A', 10)
# print repeat_A
for s in itertools.chain('Huang', 'Yi', 'Xiang'):
    # print s
    pass
for key, group in itertools.groupby('WilliW'):
    # print key, list(group)
    pass
for x in itertools.imap(lambda x, y: x * y, [10, 20, 30], [1, 2, 3]):  # print imap is an object
    # print x
    pass
for x in map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]):  # print map is an instance
    # print x
    pass

'''
正则表达式 
'''

'''
多进程
'''
from multiprocessing import Process, Pool, Queue
import os, time, random


def func_printer(sent):
    print os.getpid(), sent


def run():
    print os.getpid()
    child_process = Process(target=func_printer, args=(raw_input(),))
    child_process.start()
    child_process.join()
    print 'END'


# if __name__ == '__main__':
#     run()


def run_again(name):
    start = time.time()
    time.sleep(random.random() * 3)
    print os.getpid(), name


# if __name__ == '__main__':
#     print os.getpid()
#     pool = Pool()
#     for i in range(5):
#         pool.apply_async(run_again, args=(raw_input(),))
#     pool.close()
#     pool.join()  # 使用join()方法前必须要先调用close()方法

# 进程间通信
def write_queue(queue, info):
    queue.put(info)


# if __name__ == '__main__':
#     queue = Queue()
#     for i in range(5):
#         p = Process(target=write_queue, args=(queue, i))
#         p.start()
#     p.join()
#     for i in range(queue.qsize()):
#         print queue.get(), queue.qsize()

'''
多线程:启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行
	多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，
	互不影响，而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线
	程修改，因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。
	1.lock.acquire()
	2.lock.release()
'''
import threading


def thread_printer(num):
    print 'thread %s is printing %d' % (threading.current_thread().name, num)
    time.sleep(random.random())


def thread_printer_pro(num):
    print 'thread %s is printing %d' % (threading.current_thread().name, num * num)
    time.sleep(random.random())


# print 'Current thread is %s' % threading.current_thread().name
# for i in range(10):
#     t = threading.Thread(target=thread_printer, args=(i,), name='ChildThreadOne')
#     t.start()
#     t.join()
# for i in range(10):
#     t = threading.Thread(target=thread_printer_pro, args=(i,), name='ChildThreadTwo')
#     t.start()
#     t.join()

# lock
balance = 0
lock = threading.Lock()


def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(100000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()
            # change_it(n)


#
# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print balance

'''
网络编程TCP/IP
'''

'''
数据库访问MySQL
'''
