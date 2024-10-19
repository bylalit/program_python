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
    
    


# import requests

# def user_api():
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
#         username, country = user_api()
#         print(f"Username: {username} \nCountry: {country}")
#     except Exception as e:
#         print(f"Error: {str(e)}")
        
# if __name__ == "__main__":
#     main()
    
    

import requests

def api_user():
    url = "https://api.freeapi.app/api/v1/public/stocks/stock/random"
    response = requests.get(url)
    data = response.json()
    
    if data["success"] and "data" in data:
        # print(data)
        # print(data["data"])
        
        stock_data = data["data"]
        username = stock_data["Name"]
        date = stock_data["ListingDate"]
        return username, date  #stock_data
    else:
        raise Exception("Failed to featch user data.")
    
def main():
    try:
        username, date = api_user()  #stock_data
        print()
        print(f"Stock Name: {username} \nListing Date: {date}") #\nStorck data: {stock_data}
        print()
    except Exception as e:
        print(f"Error: {str(e)}")
        
if  __name__ == "__main__":
    main()

    