#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    hidden = dir(hidden_4)
    print(hidden)
    for i in range(len(hidden)):
        if hidden[i][0] != "_" and hidden[i][1] != "_":
            print(hidden[i])
