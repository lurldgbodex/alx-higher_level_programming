#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    all_names = dir(hidden_4)
    for names in range(0, len(all_names)):
        if all_names[names][0:2] != "__":
            print(all_names[names])
