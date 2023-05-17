# ----------------------------------------------------------------------
# Name:        matchit
# Purpose:     Implement a single player matching game
#
# Author(s): Timothy Phan and Ibrahim Dobashi
# ----------------------------------------------------------------------
"""
A single player matching game.

usage: matchit.py [-h] [-f] {blue,green,magenta} [image_folder]
positional arguments:
  {blue,green,magenta}  What color would you like for the player?
  image_folder          What folder contains the game images?

optional arguments:
  -h, --help            show this help message and exit
  -f, --fast            fast or slow game?
"""
import tkinter
import os
import random
import argparse


class MatchGame(object):
    """
    GUI Game class for a matching game.

    Arguments:
    parent: the root window object
    player_color (string): the color to be used for the matched tiles
    folder (string) the folder containing the images for the game
    delay (integer) how many milliseconds to wait before flipping a tile

    Attributes:
    Please list ALL the instance variables here
    """

    # Add your class variables if needed here - square size, etc...)
    score = 100
    square_size = 100
    folder_images = []
    flip_counter = 1
    match_counter = 0
    tags_map = {}

    def __init__(self, parent, player_color, folder, delay):

        parent.title('Match it!')
        self.color = player_color
        self.delay = delay

        # Create the restart button widget python matchit.py blue SJSUimages
        # Create a canvas widget
        # Create a label widget for the score and end of game messages
        # Create any additional instance variable you need for the game
        # Call the restart method to finish the initialization
        # take out the pass statement and enter your code

        for filename in os.listdir(folder):
            _, ext = os.path.splitext(filename)
            if ext == ".gif":
                self.folder_images.append(filename)

        self.image_names = 2 * self.folder_images
        self.image_dict = {image_file: tkinter.PhotoImage(
            file=os.path.join(f"./{folder}", image_file)) for
            image_file in
            self.folder_images}

        self.restart_btn = tkinter.Button(parent, text="Restart", width=20,
                                          command=self.restart)
        self.restart_btn.grid()

        self.canvas = tkinter.Canvas(parent, width=400, height=400)
        i = 1
        for row in range(4):
            for col in range(4):
                x1 = col * self.square_size
                y1 = row * self.square_size
                x2 = x1 + self.square_size
                y2 = y1 + self.square_size
                self.canvas.create_rectangle(x1, y1, x2, y2,
                                             fill="yellow",
                                             outline="black",
                                             tags=(f'img{i}', 'tiles'))

                i += 1

        self.canvas.bind("<Button-1>", self.flip)
        self.canvas.grid()
        self.game_over = tkinter.Label(parent, text="", width=30)
        self.game_over.grid()
        self.score_label = tkinter.Label(parent, text=f"Score:{self.score}",
                                         width=30)
        self.score_label.grid()
        self.total_tries = tkinter.Label(parent, text="", width=30)
        self.total_tries.grid()
        self.restart()

    def restart(self):
        """
        This method is invoked when player clicks on the RESTART button.
        It should also be called from __init__ to initialize the game.
        It shuffles and reassigns the images and resets the GUI and the
        score.
        :return: None
        """
        self.canvas.bind("<Button-1>", self.flip)
        self.canvas.delete('images')
        self.canvas.dtag('first')
        self.canvas.dtag('second')
        self.canvas.itemconfigure('tiles', fill='yellow')
        random.shuffle(self.image_names)

        self.score = 100
        self.game_over.config(text="")
        self.score_label.config(text=f"Score:{self.score}")
        self.total_tries.config(text="")
        self.flip_counter = 0
        self.match_counter = 0

    def flip(self, event):
        """
        This method is invoked when the user clicks on a square.
        It implements the basic controls of the game.
        :param event: event (Event object) describing the click event
        :return: None
        """

        self.tags_map = {f'img{i + 1}': self.image_names[i] for i in
                         range(len(self.image_names))}

        current_tags = self.canvas.gettags(tkinter.CURRENT)

        x1, y1, x2, y2 = self.canvas.coords(current_tags[0])
        if (self.canvas.type(
                tkinter.CURRENT) == 'rectangle') and self.canvas.itemcget(
            tkinter.CURRENT, 'fill') == 'yellow':
            self.canvas.create_image(x1 +
                                     self.square_size / 2, y1 +
                                     self.square_size / 2,
                                     image=self.image_dict[
                                         self.tags_map[current_tags[0]]],
                                     tag=(
                                         f'img{1}',
                                         self.tags_map[current_tags[0]],
                                         'images'))

            if not self.canvas.gettags('first'):
                self.canvas.addtag_withtag('first', current_tags[0])
            else:
                self.canvas.addtag_withtag('second', current_tags[0])
                self.canvas.after(self.delay, self.hide)
                self.canvas.unbind("<Button-1>")

    def hide(self):
        """
        This method is called after a delay to hide the two tiles that
        were flipped.  The method will also change the tile color to the
        user specified color if there is a match.
        :return: None
        """
        self.canvas.delete(self.tags_map[self.canvas.gettags('first')[0]])
        self.canvas.delete(self.tags_map[self.canvas.gettags('second')[0]])
        if (self.canvas.type('first') == 'rectangle') and self.tags_map[
            self.canvas.gettags('first')[0]] == self.tags_map[
            self.canvas.gettags('second')[0]]:
            self.canvas.itemconfigure('first', fill=self.color)
            self.canvas.itemconfigure('second', fill=self.color)
            self.match_counter += 1

        if self.flip_counter >= 13:
            self.score -= 10

        self.canvas.dtag('first')
        self.canvas.dtag('second')
        self.flip_counter += 1
        self.score_label.config(text=f"Score:{self.score}")
        self.canvas.bind("<Button-1>", self.flip)

        if self.match_counter == 8:
            self.game_over.config(text="Game over!")
            self.total_tries.config(
                text=f"Number of tries: {self.flip_counter}")

    # Enter your additional method definitions below
    # Make sure they are indented inside the MatchGame class
    # Make sure you include docstrings for all the methods.

    # Enter any function definitions here to get and validate the
    # command line arguments.  Include docstrings.


def valid_folder(image_folder):
    """
    Checks if the user's image folder is valid
    :param image_folder: string
    :return: string
    """
    if not os.path.isdir(image_folder):
        raise argparse.ArgumentTypeError(f"{image_folder} is not a valid "
                                         f"folder")
    else:
        image_files = [filename for filename in os.listdir(image_folder) if
                       os.path.splitext(filename)[1] == ".gif"]
        if len(image_files) < 8:
            raise argparse.ArgumentTypeError(
                f"{image_folder} must contain at least 8 gif "
                f"images")
    return image_folder


def get_arguments():
    """
    Parse and validate the command line arguments.
    :return: tuple containing the player color (string), the image
    folder (string) and the fast option (boolean)
    """
    # take out the pass statement and enter your code

    parser = argparse.ArgumentParser()
    parser.add_argument("color", help="What color would you like for the "
                                      "player?",
                        choices=["blue", "green", "magenta"])

    parser.add_argument("image_folder", type=valid_folder, help="What folder "
                                                                "contains the "
                                                                "game "
                                                                "images?",
                        nargs="?",
                        default="images")

    parser.add_argument("-f", "--fast", help="Fast or slow game?",
                        action="store_true")

    arguments = parser.parse_args()
    color = arguments.color
    image_folder = arguments.image_folder
    fast = arguments.fast

    return color, image_folder, fast


def main():
    # Retrieve and validate the command line arguments using argparse
    # Instantiate a root window
    # Instantiate a MatchGame object with the correct arguments
    # Enter the main event loop
    # take out the pass statement and enter your code

    color, folder, fast = get_arguments()

    root = tkinter.Tk()
    match = MatchGame(root, color, folder, fast)
    if fast:
        match.delay = 1000
    else:
        match.delay = 3000
    root.mainloop()


if __name__ == '__main__':
    main()
