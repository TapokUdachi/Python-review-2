import json


def show_options():
    print("Your options")
    for name, result in options.items():
        print(name, "->", result)


def show_description():
    print("-------------------------------")
    if description == -1:
        print("No description yet")
    else:
        print(description)
    print("-------------------------------")


def preview():
    show_description()
    show_options()


def change_description():
    global description
    if description != -1:
        print("Description already exists, overwrite it? (y/n)")
        while True:
            ans = input()
            if ans == "y" or ans == "yes":
                break
            elif ans == "n" or ans == "no":
                return
            print("unknown command")
    print("Set new description")
    description = input()


def add_option():
    global options
    print("assign a new option")
    print("assign the name")
    name = input()
    if name in options.keys():
        print("This option alreaddy exists, overwrite?(y/n)")
        while True:
            ans = input()
            if ans == "y" or ans == "yes":
                break
            elif ans == "n" or ans == "no":
                return
            print("unknown command")
    print("assign the result")
    path = input()
    options.update([(name, path)])


def delete_option():
    print("which option should be deleted?")
    ans = input()
    # удаление через перехват исключений


print("Enter file name")
name = input()
with open(name, "w") as cur_scen:
    description = -1
    options = {}
    while True:
        print("enter command (type help for more info)")
        cmd = input()
        # if cmd = "help":
        #    give_help()
        if cmd == "preview":
            preview()
        elif cmd == "edesc":
            change_description()
        elif cmd == "sdesc":
            show_description()
        elif cmd == "+option":
            add_option()
        elif cmd == "options":
            show_options()
        elif cmd == "-option":
            delete_option()
        elif cmd == "beep":
            print("boop")
        elif cmd == "save":
            json.dump((description, options), cur_scen)
            break
        elif cmd == "delete":
            print("Выйти без сохранения?")
            while True:
                ans = input()
                if ans == "y" or ans == "yes":
                    exit()
                elif ans == "n" or ans == "no":
                    break
                print("unknown command")
        else:
            print("unknown command")
            print("type help for list of commands")
