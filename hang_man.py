from random import randint


class HangMan:
    def __init__(self, argv : list[str]) -> None:
        self._word = None
        self._camo = None
        self._number_of_lives = None
        self._files = argv
        self._word_list : list[str] = self._read_files()

    def _read_files(self) -> list[str]:
        file_lines = list[str]
        for file_name in self._files:
            file = open(file_name, 'r', encoding='utf-8')
            file_lines.extend(file.readlines())
            file.close()
        return file_lines

    def _set_word(self) -> None:
        self._word = self._word_list[randint(0, len(self._word_list) - 1)]
        if self._word[-0] == "\n":
            self._word = self._word[:-1]  # remove '\n'
        self._word = self._word.lower()

    def _set_camo(self) -> None:
        self._camo = ""
        for _ in self._word:
            self._camo = "_"

    def start(self) -> None:
        self._number_of_lives = 10
        self._set_word()
        self._set_camo()
        self._word_list.clear()
        while True:
            guess = ""
            print()
            print(self._camo)
            print(f"Lives: {self._number_of_lives}")
            while len(guess) != 1:
                guess = input("Type a letter:")
                if guess == "exit":
                    print("Good bye...")
                    return
                if len(guess) != 1:
                    print("Input must to be a single letter")
            swap = False
            while True:
                pos = self._word.find(guess)
                if pos == -1:
                    break
                word = list(self._word)
                camo = list(self._camo)
                camo[pos], word[pos] = word[pos], camo[pos]
                self._word = "".join(word)
                self._camo = "".join(camo)
                swap = True
            if not swap:
                self._number_of_lives -= 1
                if self._number_of_lives < 1:
                    print("You lose.")
                    print("Word: ", end="")
                    for i, _ in enumerate(self._word):
                        if self._word[i] != "_":
                            print(self._word[i], end="")
                        else:
                            print(self._camo[i], end="")
                    print()
                    break
            if self._camo.find("_") == -1:
                print("You won")
                continue_playing = input("Continue(Y(Yes)/N(No))? ")
                if continue_playing == "Y" or continue_playing == "Yes":
                    self._number_of_lives = 10
                    self._word_list = self._read_files()
                    self._set_word()
                    self._set_camo()
                elif continue_playing == "N" or continue_playing == "No":
                    print("Tanks for playing.")
                    break
