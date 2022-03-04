from hang_man import HangMan
import sys

def main():
    argv = sys.argv[1:]
    if len(argv) == 0:
        raise Exception("Usage: python {} [<file> ...]".format(sys.argv[0]))
    
    game = HangMan(argv)
    game.start()

if __name__ == "__main__":
    main()