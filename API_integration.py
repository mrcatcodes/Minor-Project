import requests

def check_balance(user_id):

    response = requests.get(f"https://api.mobilebank.com/check_balance/{user_id}")
    
    if response.status_code == 200:
        return response.json()['balance']
    else:
        return "Error fetching balance."

# Example usage
user_balance = check_balance(123456)
print(f"User Balance: {user_balance}")
