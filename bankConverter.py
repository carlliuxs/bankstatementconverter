import os
import pandas as pd

class BankConverter():
    def __init__(self,folder_path):
        self.folder_path = folder_path

    def list_csv_files(self):
        files = os.listdir(self.folder_path)
        files_path = []
        for file in files:
            file_path = os.path.join(self.folder_path,file)
            # print(os.path.splitext(file_path))
            if os.path.splitext(file_path)[-1] == '.csv':
                files_path.append(file_path)
        # print(len(files_path))
        # print(files_path)
        return files_path

    def review_one_file(self,num):
        files_path = self.list_csv_files()
        df = pd.read_csv(files_path[num])
        print(df)

    def merge_csv_files(self):
        files_path = self.list_csv_files()
        dfs = []
        for file_path in files_path:
            print(file_path)
            df = pd.read_csv(file_path)
            df["file"] = os.path.basename(file_path)
            dfs.append(df)
        exportDf = pd.concat(dfs)
        print(len(dfs))
        exportDf.to_csv(path_or_buf=os.path.join(self.folder_path,"combined.csv"),index=False)





if __name__ == '__main__':
    folder_path =r"文件夹路径"
    bank = BankConverter(folder_path=folder_path)
    # bank.list_csv_files()
    # bank.review_one_file(1)
    bank.merge_csv_files()
