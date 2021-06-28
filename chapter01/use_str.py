
def format_str():
    """ 格式化字符串 """
    name = '张三'
    age = 18
    print('您的名字是：%s' % name)
    num = 333.333
    print('您的编号是：%.4f' % num)
    num2 = 66
    print('编码是：%04d' % num2)

    t = (1, 2, 3, 4, 5)
    print('元组是：%s' % str(t))

    print('姓名:%(name)s  年龄：%(age)d' % {'name': name, 'age': age})


def format_str_2():
    print('欢迎 {0}{1}{0}'.format('张三', '666'))
    d = {
        'name': '李四',
        'age': '18'
    }
    print('姓名：{name},年龄：{age}'.format(**d))
    point = ((2, 3), (4, 5))
    print('坐标：{0[0][0]}:{0[1][1]}'.format(point))

    user = User('王五', 20)
    print(user)


class User(object):
    def __init__(self, username, age):
        self.username = username
        self.age = age

    def show_user(self):
        return '用户名：{self.username} 年龄：{self.age}'.format(self=self)

    def __str__(self):
        return self.show_user()


if __name__ == '__main__':
    format_str()
    format_str_2()
