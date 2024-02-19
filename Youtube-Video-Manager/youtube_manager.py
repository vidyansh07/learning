import json
def load_data():
        try:
            with open('youtube.txt', 'r') as file:
                return json.load(file)
        except json.JSONDecodeError as e:
            print("ErrorDecodeError Json :" ,e)
            return None
        except FileNotFoundError:
            return []
        
def save_data_helper(vidoes):
    with open('youtube.txt', 'w') as file :
        json.dump(vidoes, file)
        
def list_all_videos(videos):
    for index, video in enumerate(videos, start=1): 
        print(f"{index}.")

def add_videos(videos):
    name = input("Enter vidoe Name : ")
    time = input("Enter vidoe time : ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_videos(videos):
    pass

def delete_videos(videos):
    pass

def exit_app():
    pass

def main():
    videos = load_data()

    while True:
        print("\n Youtube Manager")
        print("\n 1. List Your favourite videos ")
        print("\n 2. Add a youtube video")
        print("\n 3. update a youtube video details")
        print("\n 4. Delete a youtube video ")
        print("\n 5. exit the app")
        user_choice = input("Enter your choice :")
        print(videos)
        
        match user_choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_videos(videos)
            case "3":
                update_videos(videos)
            case "4":
                delete_videos(videos)
            case "5":
                break
            case _:
                print("Plese select write value")
                
if __name__ == "__main__":
    main()