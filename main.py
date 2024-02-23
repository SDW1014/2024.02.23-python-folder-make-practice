import createAPI

test_1 = ["mp4", "ts", "smi"]
test_2 = {"mp4":"mp4", "ts":"ts", "smi":"smi"}

def main():
    # print("hello")
    createAPI.create_folder_array(test_1)
    # createAPI.create_folder_map(test_2)
    
    
if __name__ =='__main__':
    main()