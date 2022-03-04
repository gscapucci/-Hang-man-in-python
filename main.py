from hang_man import HangMan
import sys

def readFiles(argv):
    file_lines = list()
    for file_name in argv:
        file = open(file_name, 'r', encoding='utf-8')
        file_lines.extend(file.readlines())
        file.close()
    return file_lines

def main():
    argv = sys.argv[1:]
    if len(argv) == 0:
        raise Exception("Usage: python {} [<file> ...]".format(sys.argv[0]))
    else:
        words = readFiles(argv)
    game = HangMan()
    game.start(words)

if __name__ == "__main__":
    main()