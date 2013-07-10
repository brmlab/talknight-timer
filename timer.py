
from __future__ import print_function

def args(argv):
    import argparse
    parser = argparse.ArgumentParser(description='TalkNight timer.', epilog='example: %(prog)s --first 1200 --other 600 600 600')
    parser.add_argument('--first', nargs=1, default=[1200], metavar='<secs>', help='specify first time limit')
    parser.add_argument('--other', nargs='+', default=[600,600,600], metavar='<secs>', help='specify next time limit(s).')
    return parser.parse_args(argv)

def wait(seconds):
    from time import sleep
    print('Waiting for %d minutes..'%(seconds/60)) 
    sleep(seconds)

if __name__ == '__main__':
    from sys import argv
    import mpylayer
    from itertools import chain, imap
    a = args(argv[1:])
    p = mpylayer.MPlayerControl()

    while True:
        p.loadfile('test.mp3')
        if raw_input('Do you hear the voice? ') == 'y':
            break

    p.loadfile('start.mp3')
    intervals = map(int,chain(a.first,a.other))
    end = False
    for t in intervals[:-1]:
        wait(t)

        p.loadfile('expired.mp3')
        
        i = raw_input('Can continue? ')

        if i == 'y':
            # continue
            print('Yeah, can continue')
            p.loadfile('continue.mp3')
        else:
            end = True
            break
    
    if not end:
        wait(intervals[-1])
    
    # finish in 2 minutes
    p.loadfile('finish.mp3')
    wait(120) # some dealy for mplayer
    print('Done')
        


