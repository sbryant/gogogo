#!/usr/bin/env python
import sys
from gogogo import BoardState
from gogogo.game import Game
from optparse import OptionParser

def options_arguments_and_parser():
    parser = OptionParser()
    parser.add_option("-n", "--name", dest="name",
                  help="NAME of a game", metavar="NAME")
    (options, args) = parser.parse_args()
    return options, args, parser

def main(name, x=None, y=None, **options):
    game = Game(name)
    print "Game:", game
    try:
        if options.get('skip', False): game.skip()
        elif (x is not None and y is not None): game.move(int(x), int(y))
    except Exception, e:
        print "== Your input is nonsensical: ", str(e)
        print " = I'll allow it"

    game.board.dump_board()
    if game.board.game_over:
        print "Game over:", game.scores()
        print "Winner:", game.winner() or "Tie"
    else:
        print "Next:", game.who()

def fail(code=None, msg=None, e=None):
    print "CATASTROFIC ERROR!"

    if msg is not None: sys.stderr.write("Error: {0}\n".format(msg))
    if e is not None: sys.stderr.write("Error: {0}\n".format(str(e)))

    if code is not None: exit(code)

if __name__ == "__main__":
    options, args, parser = options_arguments_and_parser()
    options = options.__dict__
    try: main(name, *args, **options)
    except Exception, e:
        parser.error("OH SHTI: {0}".format(str(e)))
        fail(1, "main() failed", e)
