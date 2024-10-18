# import requests

# def feacth_api_user():
#     url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
#     response = requests.get(url)
#     data = response.json()
    
#     if data["success"] and "data" in data:
#         user_data = data["data"]
#         username = user_data["login"]["username"]
#         country = user_data["location"]["country"]
#         return username, country
#     else:
#         raise Exception("failed to fecth user data")
    
# def main():
#     try:
#         username, country = feacth_api_user()
#         print(f"Username: {username} \nCountry: {country}")
#     except Exception as e:
#         print(f"Error: {str(e)}")

# if __name__ == "__main__":
#     main()
    
    


import requests

def user_api():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()
    
    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username, country
    else:
        raise Exception("failed to fecth user data")
    
def main():
    try:
        username, country = user_api()
        print(f"Username: {username} \nCountry: {country}")
    except Exception as e:
        print(f"Error: {str(e)}")
        
if __name__ == "__main__":
    main()
    
    