import os

def create_folder(folder_name):
    try:
        os.mkdir(folder_name)
        print(f"'{folder_name}' 폴더를 성공적으로 생성하였습니다.")
    except FileExistsError:
        print(f"'{folder_name}' 폴더가 이미 존재합니다.")
    except Exception as e:
        print(f"폴더 생성 중 오류가 발생했습니다: {e}")
        
def create_folder_array(folder_names):
    for name in folder_names:
        create_folder(name)