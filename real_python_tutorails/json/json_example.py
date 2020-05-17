

def keep(todo):
    is_complete = todo["completed"]
    has_max_count = str(todo["userId"]) in users
    return is_complete and has_max_count





if __name__ == "__main__":
    import json

    data = {
        "president": {
            "name": "Zaphod Beeblebrox",
            "species": "Betelgeusian"
        }
    }

    with open("data_file.json", "w") as write_file:
        json.dump(data, write_file)

    #dumping into variable to be used latter

    json_string = json.dumps(data)
    print(json_string)

    json_string = json.dumps(data, indent=4)
    print(json_string)

    #loading json objects

    blackjack_hand = (8, "Q")
    encoded_hand = json.dumps(blackjack_hand)
    decoded_hand = json.loads(encoded_hand)

    print(type(blackjack_hand))

    print(type(encoded_hand))

    assert type(blackjack_hand)  != type(encoded_hand)


    with open("data_file.json", "r") as read_file:
       data = json.load(read_file)
       print(data)


    #real time example

    import requests
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = json.loads(response.text)

    print(todos[:1])

   

    most_completed = dict()

    for d in todos:
        if d['completed'] :
            count = most_completed.get(d['userId'],0)
            count += 1
            most_completed[d['userId']] = count

    from operator import itemgetter        
    
    max_completed =  sorted( most_completed.items(), key = itemgetter(1))[-1]

    users = []
    for user, num_complete in most_completed.items():
        if num_complete == max_completed[1]:
            users.append(str(user))

   
    max_users = 'and'.join(users)        


    with open("filtered_data_file.json", "w") as data_file:
        filtered_todos = list(filter(keep, todos))
        json.dump(filtered_todos, data_file, indent =2)
    
