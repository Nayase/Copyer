import os
import os.path
import datetime
import shutil



def main():

    #元のファイルのパス
    dirpath = "E:/DCIM"
    dirfiles = os.listdir(dirpath)
    
    #コピー先のファイルのパス
    copypath = "C:/Users/Owner/Pictures/Camera Roll/2021"

    

    print("コピーしています。")

    #ファイルのコピーを行う
    for j in dirfiles:

        path = "E:/DCIM/" + j
        files = os.listdir(path)

        for i in files:
            #1ファイルずつ読み込んで、指定フォルダに移動

            filepath = path + "/" + i

            #ファイルパスの作成日時を返す関数
            dtime = datetime.datetime.fromtimestamp(os.stat(filepath).st_mtime)

            yeartime = dtime.strftime('%Y')
            monthtime = dtime.strftime('%m')

            if not os.path.exists(copypath + "/" + yeartime + "-" + monthtime):
                os.mkdir(copypath + "/" + yeartime + "-" + monthtime)

            YMtime = yeartime + "-" + monthtime

            
            #dtimeをdatetimeからstrに型変換する

            tstr = dtime.strftime('%Y-%m-%d')
            copypath2 = copypath + "/" + YMtime
            #print(tstr)

            if not os.path.exists(copypath2 + "/" + tstr) :
                #ディレクトリを作成、重複する場合はスキップする。
                os.mkdir(copypath2 + "/" + tstr)
                os.mkdir(copypath2 + "/" + tstr + '/RAW')
                os.mkdir(copypath2 + "/" + tstr + '/JPEG')

            
            
            #ファイルの拡張子の判断
            root, ext = os.path.splitext(path + '/' + i)

            if ext == ".RAF" :
                #SDカードから作成したフォルダにファイルをコピー
                #copy2で作成日などのメタ情報もコピー
                shutil.copy2(filepath, copypath2 + "/"  + tstr + '/RAW')
            #jpegの表記ゆれに対応
            elif ext == ".JPG" or ext == ".jpg" or ext == ".JPEG" or ext == ".jpeg" :
                shutil.copy2(filepath, copypath2 + "/"  + tstr + '/JPEG')
                
    #ファイルの削除を行う
    for j in dirfiles:

        path = "E:/DCIM/" + j
        files = os.listdir(path)

        for i in files:
            #1ファイルずつ削除を行う。

            filepath = path + "/" + i

            os.remove(filepath)
         
    
            
    

    print("コピーが完了しました")
    

if __name__ == "__main__":
    main()