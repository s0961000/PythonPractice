"""

Provide a wrapper class around the existing map functionality to make sure
it is thread safe to add/modify any key value (which means no two threads can
modify the same key at once)

"""


class ThreadSafeMap:
    map = dict()
    set = set()

    def add(self, key, value):
        try:
            if key in self.set:
                # Key is already being modified, cannot add
                print("exiting")
                return None
            else:
                self.set.add(key)
            self.map[key] = value
        except Exception as e:
            print(e)
        finally:
            self.set.remove(key)

    def print(self):
        print(self.map)


if __name__ == "__main__":
    my_map = ThreadSafeMap()
    my_map.add("Key", "Value")
    my_map.print()
