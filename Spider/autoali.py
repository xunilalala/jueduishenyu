"""快速入门"""
from aligo import Aligo

if __name__ == '__main__':
    ali = Aligo()
    
    user = ali.get_user()  # 获取用户信息
    print(user.user_name, user.nick_name, user.phone)  # 打印用户信息
    
    ll = ali.get_file_list()  # 获取网盘根目录文件列表
    for file in ll:  # 遍历文件列表
        print(file.file_id, file.name, file.type)  # 打印文件信息
