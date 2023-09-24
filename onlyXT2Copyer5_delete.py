# -*- coding: utf-8 -*-

import os
import os.path
import datetime
import shutil

def main():

    #元のファイルのパス
    if os.path.exists("/Volumes/NO NAME/DCIM"):
        dirpath = "/Volumes/NO NAME/DCIM/"
    if os.path.exists("/Volumes/SD CARD01/DCIM"):
        dirpath = "/Volumes/SD CARD01/DCIM/"
    if os.path.exists("/Volumes/Untitled/DCIM"):
        dirpath = "/Volumes/Untitled/DCIM/"    
    dirfiles = os.listdir(dirpath)
    
    #コピー先のファイルのパス
    copypath = "/Users/owner/Pictures/Camera Roll"

    print("コピーしています。")

    #ファイルのコピーを行う
    for j in dirfiles:

        path = dirpath + j
        files = os.listdir(path)

        for i in files:
            #1ファイルずつ読み込んで、指定フォルダに移動

            filepath = path + "/" + i

            #ファイルパスの作成日時を返す関数
            dtime = datetime.datetime.fromtimestamp(os.stat(filepath).st_mtime)

            yeartime = dtime.strftime('%Y')
            monthtime = dtime.strftime('%m')
            
            if not os.path.exists(copypath + "/" + yeartime):
                os.mkdir(copypath + "/" + yeartime)
                
            copypath_prime = copypath + "/" + yeartime
            
            if not os.path.exists(copypath_prime + "/" + yeartime + "-" + monthtime):
                os.mkdir(copypath_prime + "/" + yeartime + "-" + monthtime)

            YMtime = yeartime + "-" + monthtime

            
            #dtimeをdatetimeからstrに型変換する

            tstr = dtime.strftime('%Y-%m-%d')
            copypath2 = copypath_prime + "/" + YMtime
            #print(tstr)

            if not os.path.exists(copypath2 + "/" + tstr) :
                #ディレクトリを作成、重複する場合はスキップする。
                os.mkdir(copypath2 + "/" + tstr)
                os.mkdir(copypath2 + "/" + tstr + '/MOV')
                os.mkdir(copypath2 + "/" + tstr + '/RAW')
                os.mkdir(copypath2 + "/" + tstr + '/JPEG')
                
  
            #ファイルの拡張子の判断
            root, ext = os.path.splitext(path + '/' + i)
            RAWjudge = ext == ".RAF" or ext == ".CR2" or ext == ".CRW" or ext == ".NEF" or ext == ".NRW" or ext == ".ARW" or ext == ".SR2" or ext == ".SRF" or ext == ".ORF" or ext == ".RW2" or ext == ".RAF" or ext == ".DNG" or ext == ".PEF" or ext == ".BAY" or ext == ".RWL" or ext == ".X3F"
            if RAWjudge:
                #SDカードから作成したフォルダにファイルをコピー
                #copy2で作成日などのメタ情報もコピー
                shutil.copy2(filepath, copypath2 + "/"  + tstr + '/RAW')
            #jpegの表記ゆれに対応
            elif ext == ".JPG" or ext == ".jpg" or ext == ".JPEG" or ext == ".jpeg" :
                shutil.copy2(filepath, copypath2 + "/"  + tstr + '/JPEG')
            elif ext == ".MOV" or ext == ".MP4" :
                shutil.copy2(filepath, copypath2 + "/"  + tstr + '/MOV')

             
        # #ファイルの削除を行う
        for j in dirfiles:

            path = dirpath + j
            files = os.listdir(path)

            for i in files:
                #1ファイルずつ削除を行う。

                filepath = path + "/" + i

                os.remove(filepath) 

    print("コピーが完了しました")
    

if __name__ == "__main__":
    main()