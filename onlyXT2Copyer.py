import os
import os.path
import datetime
#import time
import shutil
#from distutils.dir_util import copy_tree


def main():
    filename = input("ファイル名を入力してください>>")
    #元のファイルのパス
    path = "E:/DCIM/" + filename
    files = os.listdir(path)
    #コピー先のファイルのパス
    copypath = "C:/Users/Owner/Pictures/Camera Roll/2021"

    box_dir = list()
    box_dir = []

    print("コピーしています。")

    for i in files:
        #1ファイルずつ読み込んで、指定フォルダに移動

        filepath = path + "/" + i
        #print(filepath)


        #ファイルパスの作成日時を返す関数
        #dtime = datetime.datetime.fromtimestamp(os.path.getctime(filepath))
        dtime = datetime.datetime.fromtimestamp(os.stat(filepath).st_ctime)

        #print(dtime)

        #dtimeをdatetimeからstrに型変換する

        tstr = dtime.strftime('%Y-%m-%d')

        if not os.path.exists(copypath + "/" + tstr) :
            #ディレクトリを作成、重複する場合はスキップする。
            os.mkdir(copypath + "/" + tstr)
            os.mkdir(copypath + "/" + tstr + '/RAW')
            os.mkdir(copypath + "/" + tstr + '/JPEG')
            #os.mkdir(copypath + "/" + tstr + '/MOVIE')

        """
        if tstr not in box_dir:
            #ディレクトリを作成、重複する場合はスキップする。
            os.mkdir(copypath + "/" + tstr)
            os.mkdir(copypath + "/" + tstr + '/RAW')
            os.mkdir(copypath + "/" + tstr + '/JPEG')

            #box_dirリストに日付を格納する
            box_dir.append(tstr)
        """
        #print("tstr")
        #print(tstr)
        #print(type(box_dir[0]))
        #print("box_dir")
        #print(box_dir)
        #ファイルの拡張子の判断
        root, ext = os.path.splitext(path + '/' + i)

        if ext == ".RAF" :
            #SDカードから作成したフォルダにファイルをコピー
            #copy2で作成日などのメタ情報もコピー
            shutil.copy2(filepath, copypath + "/"  + tstr + '/RAW')
        elif ext == ".JPG" :
            shutil.copy2(filepath, copypath + "/"  + tstr + '/JPEG')
        elif ext == ".MP4" :
            shutil.copy2(filepath, copypath + "/"  + tstr + '/MOVIE')

        
        #shutil.copy2(filepath,copypath + "/"  + tstr + '/XT2')
        #shutil.copy2(filepath, copypath + "/"  + tstr)

    print("コピーが完了しました")
    """    
    for i in box_dir:
        #ファイル名に適当な名前をつける
        in_name = input(i +"の名前をつけてください")
        os.rename ("./" + i, "./" + i + "_" + in_name)
    """
    

if __name__ == "__main__":
    main()