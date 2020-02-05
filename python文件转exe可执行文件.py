import os
import PythonMagick
import shutil
import zipfile

#获得遍历目录的所有文件和子目录的文件路径
def get_all_files(dir):
    files_ = []
    list = os.listdir(dir)
    for i in range(0, len(list)):
        path = os.path.join(dir, list[i])
        if os.path.isdir(path):
            files_.extend(get_all_files(path))
        if os.path.isfile(path):
            files_.append(path)
    return files_

#压缩包主体
def yasuobao(zhutiwenjian):
    print("成功进入压缩包程序，正在执行下一步.......")
    f = zipfile.ZipFile('{}.zip'.format(zhutiwenjian), 'w', zipfile.ZIP_STORED)
    f.write('./{}\\build'.format(zhutiwenjian))
    for i in get_all_files('./{}\\build'.format(zhutiwenjian)):
        f.write('./{}'.format(i))
    print("主要文件已导入压缩包，正在执行下一步........")
    for gao in os.listdir(zhutiwenjian):
        if gao.find('.')>-1:
            f.write('./{}\\{}'.format(zhutiwenjian,gao))
        else:
            pass
    print("可执行文件已导入压缩包，正在完成最后的工作........")
    print("压缩包已生成，正在执行下一步..........")

#程序介绍模块
def txt():
    w=open('程序介绍（必看）.txt','w')
    w.write('*******************************************\n')
    w.write('*******************************************\n')
    w.write('请将您所写的程序功能和各种介绍写到此文本\n')
    w.write('以此方便发给别人\n')
    w.write('如不需要可以直接忽略删除文本\n')
    w.write('感谢你用宝贵的时间来看完本字段，有缘再见\n')
    w.write('*******************************************\n')
    w.write('*******************************************\n')


print("*" * 100)
print("本脚本用的打包方法是pyinstaller")
print("欢迎进入python代码文件变为可执行文件脚本，本程序将自动把需要的组件下载好")
print("将自动检测是否安装所需组件")
print("本程序将默认自动帮你更新pip也可以选择不更新安装")
print("*"*100)

#pip自动更新模块
try:
    pip = int(input("是否选择退出，填写数字0为退出(注：按任意键默认自动更新)："))
    if pip==0:
        print("已退出pip自动更新")
        print("*" * 100)
    else:
        pass
except:
    print(os.system("pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip"))
    print("pip命令传输完成")
    print("请自行查看pip是否更新成功")
    print("*"*100)

#ico文件生成
def shengchengicowenjian(yuantupianwenjian):
    w1=yuantupianwenjian#列表:所有的文件名字
    # tupiandaxiao = 0
    zidong = []
    liebiaoxin = []
    # img=''
    jishu=1
    while True:
        print("*"*100)
        print("(1)16x16")
        print("(2)32x32")
        print("(3)64x64")
        print("(4)128x128")
        print("(5)256x256")
        print("*"*100)
        try:
            tupiandaxiao = eval(input("请输入尺寸大小括号里面对应的数字："))
        except:
            print("请输入正确的数字，请重新输入")
            continue
        for nn in w1:
            img = PythonMagick.Image(nn)# 原有的图片文件
            if tupiandaxiao==1:
                img.sample('16x16')  # ico文件图片大小
                mingzi=0
                try:
                    print("="*100)
                    print("按任意键为默认,将自动设为不是,不是为系统生成名字")
                    mingzi=eval(input("是否修改生成ico文件名字（1）为是（0）为不是（注意：填数字）："))
                    print("=" * 100)
                except:
                    pass
                if mingzi==1:
                    while True:
                        try:
                            print("只输入文件名字不用输入后缀")
                            mingzicunshu=input("请输入新的ico文件名字：")
                            while True:
                                if os.path.exists(mingzicunshu):
                                    print("文件名字已存在，请重新输入")
                                    continue
                                else:
                                    img.write('{}.ico'.format(mingzicunshu))# 生成的文件名字
                                    print("文件已生成")
                                    zidong.append('{}.ico'.format(mingzicunshu))
                                    liebiaoxin.append('{}.ico'.format(mingzicunshu))
                                    break
                            break
                        except:
                            print("输入错误，请重新输入")
                            continue
                else:
                    img.write('image_16x16_{}.ico'.format(jishu))
                    print("文件已生成")
                    liebiaoxin.append('image_16x16_{}.ico'.format(jishu))
                    zidong.append('image_16x16_{}.ico'.format(jishu))
                    jishu+=1
            elif tupiandaxiao==2:
                img.sample('32x32')  # ico文件图片大小
                mingzi=0
                try:
                    print("默认为不是,不是为系统生成名字")
                    mingzi = eval(input("是否修改生成ico文件名字（1）为是（0）为不是（注意：填数字）："))
                except:
                    pass
                if mingzi == 1:
                    while True:
                        try:
                            print("只输入文件名字不用输入后缀")
                            mingzicunshu = input("请输入新的ico文件名字：")
                            while True:
                                if os.path.exists(mingzicunshu):
                                    print("文件名字已存在，请重新输入")
                                    continue
                                else:
                                    img.write('{}.ico'.format(mingzicunshu))  # 生成的文件名字
                                    print("文件已生成")
                                    liebiaoxin.append('{}.ico'.format(mingzicunshu))
                                    zidong.append('{}.ico'.format(mingzicunshu))
                                    break
                            break
                        except:
                            print("文件输入错误，请重新输入")
                            continue

                else:
                    img.write('image_32x32_{}.ico'.format(jishu))
                    print("文件已生成")
                    liebiaoxin.append('image_32x32_{}.ico'.format(jishu))
                    zidong.append('image_32x32_{}.ico'.format(jishu))
                    jishu+=1
            elif tupiandaxiao==3:
                img.sample('64x64')  # ico文件图片大小
                mingzi=0
                try:
                    print("默认为不是,不是为系统生成名字")
                    mingzi = eval(input("是否修改生成ico文件名字（1）为是（0）为不是（注意：填数字）："))
                except:
                    pass
                if mingzi == 1:
                    while True:
                        try:
                            print("只输入文件名字不用输入后缀")
                            mingzicunshu = input("请输入新的ico文件名字：")
                            if os.path.exists(mingzicunshu):
                                print("文件名字已存在，请重新输入")
                                continue
                            else:
                                img.write('{}.ico'.format(mingzicunshu))  # 生成的文件名字
                                print("文件已生成")
                                liebiaoxin.append('{}.ico'.format(mingzicunshu))
                                zidong.append('{}.ico'.format(mingzicunshu))
                                break
                        except:
                            print("文件输入错误，请重新输入")
                            continue
                else:
                    img.write('image_64x64_{}.ico'.format(jishu))
                    print("文件已生成")
                    liebiaoxin.append('image_64x64_{}.ico'.format(jishu))
                    zidong.append('image_64x64_{}.ico'.format(jishu))
                    jishu+=1
            elif tupiandaxiao==4:
                img.sample('128x128')  # ico文件图片大小
                mingzi=0
                try:
                    print("默认为不是,不是为系统生成名字")
                    mingzi = eval(input("是否修改生成ico文件名字（1）为是（0）为不是（注意：填数字）："))
                except:
                    pass
                if mingzi == 1:
                    while True:
                        try:
                            print("只输入文件名字不用输入后缀")
                            mingzicunshu = input("请输入新的ico文件名字：")
                            if os.path.exists(mingzicunshu):
                                print("文件名字已存在，请重新输入")
                                continue
                            else:
                                img.write('{}.ico'.format(mingzicunshu))  # 生成的文件名字
                                print("文件已生成")
                                liebiaoxin.append('{}.ico'.format(mingzicunshu))
                                zidong.append('{}.ico'.format(mingzicunshu))
                                break
                        except:
                            print("文件输入错误，请重新输入")
                            continue
                else:
                    img.write('image_128x128_{}.ico'.format(jishu))
                    print("文件已生成")
                    liebiaoxin.append('image_128x128_{}.ico'.format(jishu))
                    zidong.append('image_128x128_{}.ico'.format(jishu))
                    jishu+=1
            elif tupiandaxiao==5:
                img.sample('256x256')  # ico文件图片大小
                mingzi=0
                try:
                    print("默认为不是,不是为系统生成名字")
                    mingzi = eval(input("是否修改生成ico文件名字（1）为是（0）为不是（注意：填数字）："))
                except:
                    pass
                if mingzi == 1:
                    while True:
                        try:
                            print("只输入文件名字不用输入后缀")
                            mingzicunshu = input("请输入新的ico文件名字：")
                            if os.path.exists(mingzicunshu):
                                print("文件名字已存在，请重新输入")
                            else:
                                img.write('{}.ico'.format(mingzicunshu))  # 生成的文件名字
                                print("文件已生成")
                                liebiaoxin.append('{}.ico'.format(mingzicunshu))
                                zidong.append('{}.ico'.format(mingzicunshu))
                                break
                        except:
                            print("文件输入错误，请重新输入")
                            continue
                else:
                    img.write('image_256x256_{}.ico'.format(jishu))
                    print("文件已生成")
                    liebiaoxin.append('image_256x256_{}.ico'.format(jishu))
                    zidong.append('image_256x256_{}.ico'.format(jishu))
                    jishu+=1
            else:
                print("输入错误，请输入尺寸大小括号里面对应的数字")
                print("请重新输入")
        break
    return liebiaoxin,zidong



#移动文件
def wenjianyidong(yidongdewenjian,yidongdedifang):
    try:
        if os.path.exists(yidongdewenjian):
            if os.path.exists(yidongdedifang):
                shutil.move(yidongdewenjian, yidongdedifang)# 第一个参数是要移动的文件，第二个文件是移动的地方
            else:
                print("移至的目录不存在")
                print("请检查路径是否准确")
        else:
            print("要移动的文件不存在")
            print("请检查文件路径是否准确")
    except:
        print("错误，请重新检查")

#整理文件
def zhuanhua(wenjianmingzi):
    rongqi=wenjianmingzi
    os.makedirs(rongqi)
    print("已创建文件夹，正在下一步执行......")
    shutil.move('./build','./{}'.format(rongqi))#第一个参数是要移动的文件，第二个文件是移动的地方
    shutil.move('./dist','./{}'.format(rongqi))
    wenjianmulu=os.listdir('./{}\\build\\{}'.format(rongqi,rongqi))
    for i in wenjianmulu:
        shutil.move('./{}\\build\\{}\\{}'.format(rongqi,rongqi,i),'./{}\\build'.format(rongqi))
    shutil.move('./{}.spec'.format(rongqi),'./{}\\build'.format(rongqi))
    shutil.move('./程序介绍（必看）.txt','./{}'.format(rongqi))
    shutil.move('./{}\\dist\\{}.exe'.format(rongqi,rongqi),'./{}'.format(rongqi))
    print("移动完成，正在下一步执行......")
    shutil.rmtree('./{}\\dist'.format(rongqi))#删除文件夹
    shutil.rmtree('./{}\\build\\{}'.format(rongqi,rongqi))
    print("删除文件夹完成，正在执行下一步......")




#删除文件
def wenjianshanchu(wenjianshanchude):
    if os.path.exists(wenjianshanchude):
        shutil.rmtree(wenjianshanchude)  # 删除文件夹
    else:
        print("要删除的文件不存在")
        print("请检查文件路径")

mokuan=os.popen("pip list").read().lower()
mokuan1=mokuan.find("pyinstaller")
mokuan2=len("pyinstaller")+mokuan1+1
mokuan3=''
for i in range(mokuan1,mokuan2-1):
    mokuan3+=mokuan[i]

print("正在环境检测中......")
if mokuan1==-1:
    os.system("pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyinstaller")
elif mokuan3=='pyinstaller':
    print("环境检测成功，您已经安装所需的组件")

    py=".py"
    ico=".ico"

    while True:
        try:
            print("="*100)
            print("（1）正常执行(注：一个python文件用这个)")
            print("（2）换可执行文件的图片，(注：换可执行文件图标，文件格式要为ico)不要dos命令框(注意：没有GUI界面不要选择这个)")
            print("（3）正常执行，不要dos命令框(注意：没有GUI界面不要选择这个)")
            print("（4）换可执行文件的图片，正常执行")
            print("（5）有主程序用到的额外python文件")
            print("（6）换可执行文件的图片，有主程序用到的额外python文件")
            print("（7）生成ico图片程序")
            print("（8）退出")
            print("="*100)
            tupian=0
            try:
                tupian = int(input("请输入以上的要选择的数字："))
            except:
                print("输入错误，请输入正确服务所对应的数字")
                print("请重新输入")
                continue
            if tupian == 1:
                while True:
                    print("请输入文件名字，不用输入文件后缀")
                    print("=" * 100)
                    wenjia1=''
                    try:
                        wenjia1=input("请输入主执行的python文件名字:")
                    except:
                        print("输入文件错误，请重新输入")
                        continue
                    yang="{}{}".format(wenjia1,py)
                    if os.path.exists(yang):
                        zheng=os.path.realpath(yang)
                        for i in zheng:
                            if i==' ':
                                print("路径错误，不允许路径有空格")
                                continue
                            else:
                                pass
                        os.system('pyinstaller -F {}'.format(zheng))
                        print("*" * 100)
                        print("*" * 100)
                        print("正常执行，转化成功")
                        txt()
                        zhuanhua(wenjia1)
                        yasuobao(wenjia1)
                        print("*"*45+"已成功完成所有任务"+"*"*45)
                        break
                    else:
                        print("请把python文件放到脚本同目录下")
                        print("请重新输入")

            elif tupian==2:
                while True:
                    print("请输入文件名字，不用输入文件后缀")
                    print("=" * 100)
                    wenjia2=''
                    try:
                        wenjia2=input("请输入主执行的python文件名字:")
                    except:
                        print("输入文件错误，请重新输入")
                        continue
                    yang="{}{}".format(wenjia2,py)
                    tu=''
                    zidong = ''
                    icoweizhicunshu = ''
                    if os.path.exists(yang):
                        while True:
                            wenjiantu=''
                            try:
                                icoweizhi=zidong.find('.ico')
                                for i in range(icoweizhi,icoweizhi+4):
                                    icoweizhicunshu+="{}".format(zidong[i])
                            except:
                                try:
                                    wenjiantu = input("请输入ico文件名字：")
                                except:
                                    print("ico文件输入错误，请重新输入")
                                    continue
                                tu = "{}{}".format(wenjiantu, ico)
                            if icoweizhicunshu=='.ico':
                                tu="{}".format(zidong)
                            if os.path.exists(tu):
                                break
                            else:
                                print("="*100)
                                print("ico文件名字错误或者不存在")
                                print("请检查文件格式或是否在同一个目录")
                                print("是否跳转ico自动生成程序?（1）为是（0）为不是")
                                print("按任意键为默认，默认为不是")
                                print("="*100)
                                try:
                                    tiaozhuan=int(input("请输入数字："))
                                    print("=" * 100)
                                    if tiaozhuan==1:
                                        while True:
                                            try:
                                                wenjiantu2=input("请输入原图片文件(注：需要加文件后缀)：")
                                                if os.path.exists(wenjiantu2):
                                                    zizidongdong=shengchengicowenjian(wenjiantu2.split())
                                                    for zidongg in zizidongdong[1]:
                                                        zidong=zidongg
                                                    break
                                                else:
                                                    print("文件不存在，请重新输入")
                                                    continue
                                            except:
                                                print("文件输入错误，请重新输入")
                                                continue
                                    else:
                                        print("请重新输入")
                                        print("=" * 100)
                                except:
                                    print("请重新输入")
                                    print("=" * 100)
                    else:
                        print("="*100)
                        print("主执行python文件找不到")
                        print("请检查目录是否存在或者检查是否在同级目录里")
                        print("请重新输入")
                        print("="*100)
                        continue
                    wang=os.path.realpath(yang)
                    zheng=os.path.realpath(tu)
                    for i in zheng,wang:
                        if i==' ':
                            print("路径错误，不允许路径有空格")
                            continue
                        else:
                            pass
                    os.system("pyinstaller -F -i {} -w {}".format(tu,yang))
                    print("*" * 100)
                    print("*" * 100)
                    print("正常执行，成功")
                    shutil.move('./{}'.format(zidong),'./build')
                    print("ico文件已移动成功，正在执行下一步.....")
                    txt()
                    zhuanhua(wenjia2)
                    yasuobao(wenjia2)
                    print("*" * 45 + "已成功完成所有任务" + "*" * 45)
                    break

            elif tupian==3:
                while True:
                    print("请输入文件名字，不用输入文件后缀")
                    print("=" * 100)
                    wenjia3=''
                    try:
                        wenjia3=input("请输入主执行的python文件名字：")
                    except:
                        print("文件输入错误，请重新输入")
                        continue
                    yang="{}{}".format(wenjia3,py)
                    if os.path.exists(yang):
                        wang=os.path.realpath(yang)
                        for i in wang:
                            if i==' ':
                                print("路径错误，不允许路径有空格")
                                continue
                            else:
                                pass
                        os.system("pyinstaller -F -w {}".format(wang))
                        print("*" * 100)
                        print("*" * 100)
                        print("正常执行，成功")
                        txt()
                        zhuanhua(wenjia3)
                        yasuobao(wenjia3)
                        print("*" * 45 + "已成功完成所有任务" + "*" * 45)
                        break
                    else:
                        print("请把python文件放到脚本同目录下")
                        print("请重新输入")

            elif tupian==4:
                while True:
                    print("请输入文件名字，不用输入文件后缀")
                    print("=" * 100)
                    wenjia4=''
                    try:
                        wenjia4=input("请输入主执行的python文件名字:")
                    except:
                        print("文件输入错误，请重新输入")
                    yang="{}{}".format(wenjia4,py)
                    tu=''
                    zidong = ''
                    zidongcunshu = ''
                    if os.path.exists(yang):

                        while True:
                            wenjiantu1=''
                            try:
                                icoweizhi = zidong.find('.ico')
                                for i in range(icoweizhi, icoweizhi + 4):
                                    zidongcunshu += "{}".format(zidong[i])
                            except:
                                try:
                                    wenjiantu1 = input("请输入ico文件名字：")
                                except:
                                    print("ico文件输入错误，请重新输入")
                                    continue
                                tu = "{}{}".format(wenjiantu1, ico)
                            if zidongcunshu=='.ico':
                                tu="{}".format(zidong)
                            if os.path.exists(tu):
                                break
                            else:
                                print("="*100)
                                print("ico文件名字错误或者不存在")
                                print("请检查文件格式或是否在同一个目录")
                                print("是否跳转ico自动生成程序?（1）为是（0）为不是")
                                print("按任意键为默认，默认为不是")
                                print("="*100)
                                try:
                                    tiaozhuan1=eval(input("请输入数字："))
                                    print("=" * 100)
                                    if tiaozhuan1==1:
                                        while True:
                                            try:
                                                wenjiantu3=input("请输入原图片文件(注：需要加文件后缀)：")
                                                if os.path.exists(wenjiantu3):
                                                    pass
                                                else:
                                                    print("文件输入错误，请重新输入")
                                                    continue
                                                wang=shengchengicowenjian(wenjiantu3.split())
                                                for www in wang[1]:
                                                    zidong+=www
                                                break
                                            except:
                                                print("文件输入错误，请重新输入")
                                                continue
                                    else:
                                        print("请重新输入")
                                        print("=" * 100)
                                except:
                                    print("请重新输入")
                                    print("=" * 100)
                    else:
                        print("="*100)
                        print("主执行python文件找不到")
                        print("请检查目录是否存在或者检查是否在同级目录里")
                        print("请重新输入")
                        print("=" * 100)
                        continue
                    wang=os.path.realpath(yang)
                    zheng=os.path.realpath(tu)
                    for i in zheng,wang:
                        if i==' ':
                            print("路径错误，不允许路径有空格")
                            continue
                        else:
                            pass
                    os.system('pyinstaller -F -i {} {}'.format(tu,yang))
                    print("*" * 100)
                    print("*" * 100)
                    print("正常执行，成功")
                    print("换图片成功")
                    shutil.move('./{}'.format(zidong), './build')
                    print("ico文件已移动成功，正在执行下一步.....")
                    txt()
                    zhuanhua(wenjia4)
                    yasuobao(wenjia4)
                    print("*" * 45 + "已成功完成所有任务" + "*" * 45)
                    break

            elif tupian==5:
                while True:
                    a=0
                    print("请输入文件名字，不用输入文件后缀")
                    print("=" * 100)
                    wenjia5=''
                    try:
                        wenjia5=input("请输入主执行python文件名字：")
                    except:
                        print("文件输入错误，请重新输入")
                        continue
                    yang="{}{}".format(wenjia5,py)
                    if os.path.exists(yang):
                        while True:
                            shuzi=0
                            try:
                                shuzi=int(input("请输入需要加入几个文件（数字）："))
                                break
                            except:
                                print("输入数字错误，请重新输入")
                                continue
                        liebiao=[]
                        liebiao1=[]
                        w = ''
                        z = ''
                        for i in range(shuzi):
                            while True:
                                wenjia6=''
                                try:
                                    wenjia6=input("请输入附加python文件名字：")
                                    break
                                except:
                                    print("文件输入错误，请重新输入")
                                    continue
                            yang1="{}{}".format(wenjia6,py)
                            if os.path.exists(yang1):
                                liebiao.append(yang1)
                                for x in liebiao:
                                    w += "-p {} ".format(os.path.realpath(x))
                                    z += "--hidden-import {} ".format(x[:-3])
                                    liebiao1.append(os.path.realpath(x))
                            else:
                                print("请把脚本或者python文件放到同级目录下")
                                print("附加python文件不存在，请从新输入")
                                a+=1
                                while True:
                                    if a>0:
                                        while True:
                                            wenjia6=''
                                            try:
                                                wenjia6 = input("请输入附加python文件名字：")
                                                break
                                            except:
                                                print("文件输入错误，请重新输入")
                                                continue
                                        yang1 = "{}{}".format(wenjia6, py)
                                        if os.path.exists(yang1):
                                            liebiao.append(yang1)
                                            for x in liebiao:
                                                w += "-p {} ".format(os.path.realpath(x))
                                                z += "--hidden-import {} ".format(x[:-3])
                                                liebiao1.append(os.path.realpath(x))
                                            break
                                        else:
                                            print("请把脚本或者python文件放到同级目录下")
                                            print("附加python文件不存在，请从新输入")
                        lujing=os.path.realpath(yang)
                        for n in lujing,liebiao1:
                            if n==' ':
                                print("路径错误，不允许路径有空格")
                                continue
                            else:
                                pass
                        os.system("pyinstaller -F {} {} {}".format(lujing,w,z))
                        print("*" * 100)
                        print("*" * 100)
                        print("执行成功")
                        txt()
                        zhuanhua(wenjia5)
                        yasuobao(wenjia5)
                        print("*" * 45 + "已成功完成所有任务" + "*" * 45)
                        break
                    else:
                        print("主文件不存在")
                        print("请重新输入")

            elif tupian==6:
                zi=''
                ji=''
                pp=[]
                we=[]
                while True:
                    print("请输入文件名字，不用输入文件后缀")
                    print("=" * 100)
                    wenjia7=''
                    try:
                        wenjia7=input("请输入主执行的python文件名字：")
                    except:
                        print("文件输入错误，请重新输入")
                        continue
                    yang="{}{}".format(wenjia7,py)
                    tupian1=''
                    zidong = ''
                    zidongcunshu = ''
                    if os.path.exists(yang):
                        while True:
                            wenjiantupian1=''
                            try:
                                icoweizhi = zidong.find('.ico')
                                for i in range(icoweizhi, icoweizhi + 4):
                                    zidongcunshu += "{}".format(zidong[i])
                            except:
                                try:
                                    wenjiantupian1=input("请输入图片文件名字：")
                                except:
                                    print("输入图片文件错误，请重新输入")
                                    continue
                                tupian1="{}{}".format(wenjiantupian1,ico)
                            if zidongcunshu=='.ico':
                                tupian1="{}".format(zidong)
                            if os.path.exists(tupian1):
                                break
                            else:
                                print("="*100)
                                print("ico文件名字错误或者不存在")
                                print("请检查文件格式或是否在同一个目录")
                                print("是否跳转ico生成程序?（1）为是（0）为不是")
                                print("按任意键为默认，默认为不是")
                                print("="*100)
                                try:
                                    tiaozhuan2 = eval(input("请输入数字："))
                                    print("=" * 100)
                                    if tiaozhuan2 == 1:
                                        while True:
                                            try:
                                                wenjiantu4 = input("请输入原图片文件(注：需要加文件后缀)：")
                                                if os.path.exists(wenjiantu4):
                                                    pass
                                                else:
                                                    print("文件输入错误，请重新输入")
                                                    continue
                                                wang11=shengchengicowenjian(wenjiantu4.split())
                                                for www1 in wang11[1]:
                                                    zidong+=www1
                                                break
                                            except:
                                                print("文件输入错误，请重新输入")
                                                continue
                                    else:
                                        print("请重新输入")
                                        print("=" * 100)
                                except:
                                    print("请重新输入")
                                    print("=" * 100)
                    else:
                        print("="*100)
                        print("主执行python文件找不到")
                        print("请检查目录是否存在或者检查是否在同级目录里")
                        print("请重新输入")
                        print("="*100)
                        continue
                    a=0
                    while True:
                        try:
                            a=int(input("输入多少个额外文件（输入数字）："))
                            break
                        except:
                            print("数字输入错误，请重新输入")
                            continue
                    for i in range(a):
                        while True:
                            wenjia8=''
                            try:
                                wenjia8=input("请输入附加python文件名字：")
                                if os.path.exists("{}{}".format(wenjia8,py)):
                                    break
                                else:
                                    print("没有这个文件，请检查过后重新输入")
                                    continue

                            except:
                                print("输入文件名字错误，请重新输入")
                                continue
                        wang="{}{}".format(wenjia8,py)
                        if os.path.exists(wang):
                            pp.append(wang)
                        else:
                            print("没有找到附加python文件")
                            print("请把脚本或者python文件放到同级目录下")

                        for x in pp:
                            zi+='-p {} '.format(os.path.realpath(x))
                            ji+='--hidden-import {} '.format(x[:-3])
                            we.append(os.path.realpath(x))
                        for n in we:
                            if n == ' ':
                                print("路径错误，不允许路径有空格")
                                continue
                            else:
                                pass
                    os.system('pyinstaller -F -i {} {} {} {}'.format(tupian1,yang,zi,ji))
                    print("*"*100)
                    print("*" * 100)
                    print("执行成功")
                    shutil.move('./{}'.format(zidong), './build')
                    print("ico文件已移动成功，正在执行下一步.....")
                    txt()
                    zhuanhua(wenjia7)
                    yasuobao(wenjia7)
                    print("*" * 45 + "已成功完成所有任务" + "*" * 45)
                    break

            elif tupian==7:
                while True:
                    print("="*100)
                    print("（1）单个ico生成（需要单个原图片文件）")
                    print("（2）多个ico生成（需要多个原图片文件）")
                    print("（3）退出ico程序进入主菜单")
                    print("输入服务的对于括号里的数字")
                    print("="*100)

                    dongge=0
                    try:
                        dongge=int(input("请输入你要选择的服务（填数字）："))
                        print("="*100)
                    except:
                        print("选择服务错误，请重新输入")
                        continue

                    mulu=0
                    if dongge==1:
                        while True:
                            shengchengico = ''
                            mulu2=''
                            mulu1=0
                            try:
                                while True:
                                    shengchengico=input("请输入原图片文件名字（注：需要加后缀）：")
                                    if os.path.exists(shengchengico):
                                        break
                                    else:
                                        print("=" * 100)
                                        print("文件不存在或文件名字或文件后缀错误")
                                        print("请检查文件和脚本是否在同一个目录")
                                        print("请检查文件文件和后缀")
                                        print("=" * 100)
                                        print("是否返回主菜单（1）为是（0）为不是（2）返回ico菜单")
                                        print("按任意键默认为不是")
                                        try:
                                            mulu2 = int(input("请输入数字："))
                                            break
                                        except:
                                            continue
                                if mulu2==1:
                                    break
                                elif mulu2==2:
                                    break
                                elif mulu2==0:
                                    continue
                            except:
                                print("输入原文件图片文件错误，请检查文件名字后缀和文件路径")
                                print("请重新输入")
                                continue
                            shengchengicowenjian(shengchengico.split())
                            break
                        if mulu2==1:
                            break

                    elif dongge==2:
                        tupianliebiao=[]

                        a=1
                        while True:
                            tuichu = 0
                            tushuzi = 0
                            tuichu1=0
                            try:
                                tushuzi=int(input("请输入总共有多少个原图文件（填数字）"))
                                if tushuzi==0:
                                    print("数字不能等于小于零，请输入大于一的数字")
                                    continue
                                break
                            except:
                                print("输入错误，填总原图文件数量，请重新输入")
                                continue
                        for i in range(tushuzi):
                            print("*"*100)
                            print("请一个一个文件输入，不要直接全部文件输入")
                            while True:
                                tuwenjian=''
                                try:
                                    tuwenjian=input("请输入原图文件（加文件后缀）：")
                                    if os.path.exists(tuwenjian):
                                        print("图片文件成功导入程序数据库")
                                        break
                                    else:
                                        print("=" * 100)
                                        print("文件不存在或文件名字或文件后缀错误")
                                        print("请检查文件和脚本是否在同一个目录")
                                        print("请检查文件文件和后缀")
                                        print("=" * 100)
                                        try:
                                            print("是否返回主菜单（1）为是（0）为不是（2）为ico菜单")
                                            print("按任意键默认为不是")
                                            tuichu = int(input("请输入数字："))
                                            if tuichu == 1:
                                                break
                                            elif tuichu==2:
                                                break
                                            else:
                                                print("请重新输入")
                                                continue
                                        except:
                                            continue
                                except:
                                    print("输入文件错误，请检查一下，请重新输入")
                                    continue
                            if tuichu==1:
                                break
                            elif tuichu==2:
                                break
                            tupianliebiao.append(tuwenjian)
                        if tuichu==2:
                            continue
                        elif tuichu==1:
                            break
                        while True:
                            if os.path.exists('ico图片'):
                                break
                            else:
                                os.makedirs('ico图片')
                        liebiaoxin1=shengchengicowenjian(tupianliebiao)
                        for zxc in liebiaoxin1[0]:
                            wenjianyidong('./{}'.format(zxc),'./ico图片')
                            print("="*100)
                            print("第{}张已成功转移到文件夹中".format(a))
                            print("第{}张已转化成功".format(a))
                            a+=1
                    elif dongge==3:
                        break

            elif tupian==8:
                break
        except:
            print("程序错误，重新启动中.....")
            print("程序重新启动完成")
    print("="*100)
    print("感谢使用")
    input("按任意键退出")
    print("=" * 100)
else:
    print("没有组件请安装")