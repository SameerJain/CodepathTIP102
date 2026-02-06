class problem_1:
    def welcome(self):
        print("Welcome to The Hundred Acre Wood!")

    def test_1(self):
        print("Expected: ")
        self.welcome()


class problem_2:
    def greeting(self, name):
        print(f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin")

    def test_1(self):
        self.greeting("Michael")

    def test_2(self):
        self.greeting("Christopher Robin")


class problem_3:
    def print_catchphrase(self, character):
        phrase_list = {
            "Pooh": "Oh bother!",
            "Tigger": "TTFN: Ta-ta for now!",
            "Eeyore": "Thanks for noticing me.",
            "Christopher Robin": "Silly old bear.",
        }
        return (
            print(phrase_list[character])
            if character in phrase_list
            else print(f"Sorry! I don't know {character}'s catchphrase!")
        )

    def tests(self):
        self.print_catchphrase("Pooh")
        self.print_catchphrase("Piglet")


class problem_4:
    def get_item(self, items, x):
        item_idxs = len(items) - 1
        if item_idxs < x:
            return None
        return items[x]

    def tests(self):
        items = ["piglet", "pooh", "roo", "rabbit"]
        x = 2
        print(self.get_item(items, x))

        items = ["piglet", "pooh", "roo", "rabbit"]
        x = 5
        print(self.get_item(items, x))

# Time Complexity: O(N)
# Space Complexity: O(N)

print("Hello")


class problem_5:
    def sum_honey(hunny_jars):
        pass

class problem_6:
    def count_tails(animal_tails):
        pass   

class problem_7:
    
