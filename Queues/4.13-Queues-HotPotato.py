from queue import Queue

def play_hot_potato(names, num):
    q = Queue()
    for name in names:
        q.enqueue(name)

    while q.size() > 1:
        for i in range(num):
            q.enqueue(q.dequeue())
        q.dequeue()

    return q.dequeue()


def main():
    print(play_hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7)) # expected winner: Susan

if __name__ == '__main__':
    main()