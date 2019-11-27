from models.client import Client

def create_client(email, password, f_name, l_name):
    new_client = Client(email, password, f_name, l_name)
    return new_client.save()

"""
def create_user(email, password, f_name, l_name):
    # 1. Check if email already exists in dB
    # 2. Hash the password
    pass

    # 3. Create the user object
    new_user = User(email, password, f_name, l_name)
    # 4. Save to the dBase
    return new_user.save()
"""