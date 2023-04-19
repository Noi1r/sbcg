import os
import argparse
# windows版jenv 实现 java版本管理

def list_all_java_version():
    with open('./version.txt','r',encoding='utf-8') as f:
        for line in f:
            print(line.strip())

def add_java_version(path,version):
    instru = 'setx ' + 'JAVA' + version + '_HOME ' + '"' + path + '"' +' /m'
    with open('./version.txt','w+',encoding='utf-8') as f:
        f.write(path + ' ' + str(version) + '\n')
    os.system(instru)

# def set_java_version(version):
#     exist = False
#     with open('./version.txt','r',encoding='utf-8') as f:
#         for line in f:
#             if line == '':
#                 print('version not exist')
#                 return
#             l = line.split()
#             # print(l)
#             if l[-1] == version:
#                 exist = True
#                 # path = ' '.join(l[:-2])
#     if exist:
#         instru = 'set ' + 'JAVA' + '_HOME ' + '"' + '%JAVA' + version + '_HOME%' + '"'
#         print(instru)
#         os.system(instru)
#     else:
#         print('version not exist')

def show_current_version():
    instru = 'echo %JAVA_HOME%'
    os.system(instru)

def set_global_version(version):
    exist = False
    with open('./version.txt','r',encoding='utf-8') as f:
        for line in f:
            if line == '':
                print('version not exist')
                return
            l = line.split()
            # print(l)
            if l[-1] == version:
                exist = True
    if exist:
        instru = 'setx ' + 'JAVA' + '_HOME ' + '"' + '%JAVA' + version + '_HOME%' + '"'+' /m'
        os.system(instru)
    else:
        print('version not exist')

def initial():
    instru0 = r'setx CLASSPATH %JAVA_HOME%\lib;%JAVA_HOME%\lib\tools.jar /m'
    instru1 = r'setx PATH %JAVA_HOME%\bin;%PATH% /m'
    instru3 = r'setx PATH %JAVA_HOME%\jre\bin;%PATH% /m'
    if not os.path.exists('./version.txt'):
        with open('./intial.txt','w+',encoding='utf-8') as f:
            f.write('initial')
        os.system(instru1)
        os.system(instru3)
        os.system(instru0)
    else:
        print('already initial')
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                    prog='sbcg.py',
                    description='A program can help you to manage java version',
                    epilog='Have fun with it!')
    parser.add_argument('-i', '--initial', action='store_true', help='Initial the program')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
    parser.add_argument('-l', '--list', action='store_true', help='list all java version')
    parser.add_argument('-s', '--set', action='store', help='set java version')
    parser.add_argument('-c', '--current', action='store_true', help='show current java version')
    # parser.add_argument('-g', '--globall', action='store_true', help='set global java version')
    parser.add_argument('-a', '--add', action='store', help='add java version')
    parser.add_argument('--vvv', action='store', help='java version')
    args = parser.parse_args()

    if args.initial:
        print('initial')
        initial()
    if args.list:
        print('list all java version')
        list_all_java_version()
    if args.set:
        print('set java version')
        set_global_version(args.set)
    if args.current:
        print('show current java version')
        show_current_version()
    if args.add:
        if args.vvv:
            print('add java version')
            add_java_version(args.add,args.vvv)
        else:
            print('please input java version')
    
    