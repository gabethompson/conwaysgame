import argparse
import numpy
import matplotlib.pyplot as plot
import matplotlib.animation as anim

randval = [255, 0]

def randSeed(size, rate):
    return numpy.random.choice(randval, size*size, p=[rate, (1-rate)]).reshape(size, size)
    

def tick(time, image, board, size):
    nextboard = board.copy()
    for x in range(size):
        for y in range(size):
            neighbors = int( ( board[(x-1)%size, (y-1)%size] + board[x, (y-1)%size] + board[(x+1)%size, (y-1)%size] +
                              board[(x-1)%size, y] + board[(x+1)%size, y] +
                              board[(x-1)%size, (y+1)%size] + board[x, (y+1)%size] + board[(x+1)%size, (y+1)%size] ) / 255 )

            if board[x,y] == 255:
                if (neighbors > 3 or neighbors < 2): nextboard[x,y] = 0

            else:
                if neighbors == 3: nextboard[x,y] = 255
    image.set_data(nextboard)
    board[:] = nextboard[:]
    return image

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('--size', dest='size', required=False)
    parser.add_argument('--ticklen', dest='time', required=False)
    parser.add_argument('--rate', dest='rate', required=False)

    args = parser.parse_args()

    size = 100
    if args.size and int(args.size) > 10: size = int(args.size)

    time = 50
    if args.time: time = int(args.time)

    rate = 0.2
    if args.rate and int(args.rate) > 0 and int(args.rate) < 1: rate = float(args.rate)

    board = numpy.array([])
    board = randSeed(size, rate)

    figure, ax = plot.subplots()
    image = ax.imshow(board, interpolation = 'nearest')
    animation = anim.FuncAnimation(figure, tick, fargs=(image, board, size), frames = 10, interval = time, save_count = 50)

    plot.show()

if __name__ == '__main__':
    main()
