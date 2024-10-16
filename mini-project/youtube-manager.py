# x = ('Masala', 'lomen', 'Ginger')
# y = enumerate(x)
# print(x)
# print(y)
# print(list(y))

import json


def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)


def list_all_videos(videos):
    print("\n")
    print('*' * 50)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    print('*' * 50)
    print("\n")

def add_videos(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_videos(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update: "))
    if 1 <= index <= len(index):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        videos[index-1] = {'name':name, 'time': time}
        save_data_helper(videos)
    else:
        print("Invalid index seleted")
    
def delete_videos(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be delete: "))
    if 1 <= index <= len(index):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid videos index seleted")
    
    
def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | choose a option ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube videos detailes ")
        print("4. Delete a youtube videos ")
        print("5. Exit the app ")
        choice = input("Enter your choice: ")
        print(videos)
        
        
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_videos(videos)
            case '3':
                update_videos(videos)
            case '4':
                delete_videos(videos)
            case '5':
                break
            case _:
                print("Invalid Choice")
                
if __name__ == "__main__":
    main()
    