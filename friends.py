users =[
    { "id":0, "name": "Hero" },
    { "id":1, "name": "Dunn" },
    { "id":2, "name": "Sue" },
    { "id":3, "name": "Chi" },
    { "id":4, "name": "Thor" },
    { "id":5, "name": "Clive" },
    { "id":6, "name": "Hicks" },
    { "id":7, "name": "Devin" },
    { "id":8, "name": "Kate" },
    { "id":9, "name": "Klein" }    
]

friendship = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (6, 8),
    (7, 8),
    (8, 9)
]

def num_friends(user):
    '''
    Find number of friends for a given user
    '''
    count = 0;
    for a,b in friendship:
        if a==user.get("id"):
            count += 1
    #print(user.get("name")+ ' has '+str(count)+ ' friends')
    return count

def sort_by_num_friends():
    '''README.md
    Sort from "most friends" to "least friends"
    '''
    global users
    users = sorted(users,key=lambda x:num_friends(x),reverse=True)
    print("");
    print("List from most friends to least friends:")
    for a in users:
        print(a.get('name') + ' has '+ str(num_friends(a))+' friends')

print('Hero has '+str(num_friends({ "id":0, "name": "Hero" }))+' friends')

sort_by_num_friends()
