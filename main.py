# name: str = input('Enter your name: ')
# print(f'WITAJ {name}')
data_of_users: list = [
    {'name': 'Julia', 'surname': 'Szklarzewska', 'posts': 5, 'location': 'Hajnówka'},
    {'name': 'Norbert', 'surname': 'Szeliga', 'posts': 15, 'location': 'Rzeszów'},
    {'name': 'Kacper', 'surname': 'Wójcik', 'posts': 20, 'location': 'Legnica'},
    {'name': 'Sebastian', 'surname': 'Dudek', 'posts': 100, 'location': 'Siedlce'},
]
print(f'Witaj {data_of_users[0]["name"]}')


def read(users: list) -> None:
    """
    show users from a list
    :param users: a list of users
    :return: None
    """
    for user in users[1:]:
        print(f'twój znajomy:  {user['name']}, opublikował: {user['posts']} postów')


# read(data_of_users)

def add_user(users: list) -> None:
    """
    add a user to a users list
    :param users: 
    :return: 
    """""

    name: str = input('Enter your name:')
    surname: str = input('Enter your surname:')
    posts: int = int(input('Enter number of your posts:'))
    location: str = input('Enter your location:')
    new_user: dict = {'name': name, 'surname': surname, 'posts': posts, 'location': location}
    users.append(new_user)


# add_user(data_of_users)
#
def delete_user(users: list) -> None:
    name: str = input('Enter a name of the user to remove:')
    for user in users:
        if user['name'] == name:
            users.remove(user)


#     read(data_of_users)
#
# delete_user(data_of_users)
def update_user(users: list) -> None:
    name: str = input("Enter a name of the user to update: ")
    for user in users:
        if user['name'] == name:
            new_name: str = input('Enter a new name of the user:')
            user['name'] = new_name
            new_surname: str = input('Enter a new surname of the user:')
            user['surname'] = new_surname
            new_posts: int = int(input('Enter a new number of posts of the user:'))
            user['posts'] = new_posts
            new_location: str = input('Enter a new location of the user:')
            user['location'] = new_location

update_user(data_of_users)
read(data_of_users)

