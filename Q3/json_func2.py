import json
from datetime import datetime

with open('Q3/invent_list.json') as json_read:
    data = json.load(json_read)

# Items on meeting room

def item_meet_room():
    room = 'Meeting Room'
    item_list = []
    for datas in data:
        if datas['placement']['name'] == room:
            item_list.append(datas['name'])
    print('These are items found in Meeting Room')
    for count, items in enumerate(item_list, 1):
        print(count, items)
    print()

item_meet_room()

# All electronic device

def find_elec():
    device = 'electronic'
    item_list = []
    for datas in data:
        if datas['type'] == device:
            item_list.append(datas['name'])
    print('These are electronic devices')
    for count, devices in enumerate(item_list, 1):
        print(count, devices)
    print()
    
find_elec()

# All Furniture 

def find_furniture():
    furniture = 'furniture'
    item_list = []
    for datas in data:
        if datas['type'] == furniture:
            item_list.append(datas['name'])
    print('These are furnitures')
    for count, furnitures in enumerate(item_list, 1):
        print(count, furnitures)
    print()

find_furniture()

# Items bought on 16 Januari 2020

def buy_date():
    date_mark = '2020-01-16'
    item_list = []
    for datas in data:
        date = datetime.fromtimestamp(datas['purchased_at'])
        date_string = datetime.strftime(date, '%Y-%m-%d')
        if date_mark == date_string:
            item_list.append(datas['name'])
    print('These are items bought on 16 Januari 2020')
    for count, items in enumerate(item_list, 1):
        print(count, items)
    print()

        

buy_date()

#Brown colored items

def items_brown():
    color = 'brown'
    item_list = []
    for datas in data:
        for tag in datas['tags']:
            if tag == color:
                item_list.append(datas['name'])
    print('These are items tagged with brown color')
    for count, items in enumerate(item_list, 1):
        print(count, items)
    print()

items_brown()