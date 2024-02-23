import createAPI

# create_folder_array를 사용하기 위한 기본적인 배열 
test_1 = ["mp4", "ts", "smi"]
# create_folder_map를 사용하기 위한 기본적인 딕셔너리(맵)
test_2 = {"mp4":"mp4", "ts":"ts", "smi":"smi"}

def main():
    # print("hello")
    createAPI.create_folder_array(test_1)
    # createAPI.create_folder_map(test_2)
    
    
if __name__ =='__main__':
    main()