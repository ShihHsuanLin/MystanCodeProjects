"""
File: babygraphics.py
Name: Shih Hsuan Lin
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    x_coordinate = GRAPH_MARGIN_SIZE+year_index*(width-2*GRAPH_MARGIN_SIZE)/len(YEARS)
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    for year_index in range(len(YEARS)):
        x_coordinate = get_x_coordinate(CANVAS_WIDTH, year_index)
        canvas.create_line(x_coordinate, 0, x_coordinate, CANVAS_HEIGHT)
        canvas.create_text(x_coordinate+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[year_index], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #

    for name_index in range(len(lookup_names)):
        lookup_name = lookup_names[name_index]
        start_x_coordinate = start_y_coordinate = 0
        for year_index in range(len(YEARS)):
            if year_index == 0:
                start_x_coordinate = get_x_coordinate(CANVAS_WIDTH, year_index)
                if str(YEARS[year_index]) in name_data[lookup_name]:
                    start_y_coordinate = re_scale(int(name_data[lookup_name][str(YEARS[year_index])]))
                else:
                    start_y_coordinate = re_scale(MAX_RANK)
            else:
                end_x_coordinate = get_x_coordinate(CANVAS_WIDTH, year_index)
                if str(YEARS[year_index]) in name_data[lookup_name]:
                    end_y_coordinate = re_scale(int(name_data[lookup_name][str(YEARS[year_index])]))
                else:
                    end_y_coordinate = re_scale(MAX_RANK)
                canvas.create_line(start_x_coordinate, start_y_coordinate, end_x_coordinate, end_y_coordinate, width=LINE_WIDTH, fill=COLORS[name_index % len(COLORS)])
                start_x_coordinate, start_y_coordinate = end_x_coordinate, end_y_coordinate
            if str(YEARS[year_index]) in name_data[lookup_name]:
                rank = name_data[lookup_name][str(YEARS[year_index])]
            else:
                rank = '*'
            canvas.create_text(start_x_coordinate+TEXT_DX, start_y_coordinate, text=lookup_name+' '+rank, anchor=tkinter.SW, fill=COLORS[name_index % len(COLORS)])


def re_scale(y_coordinate):
    return (y_coordinate-1)*(CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE)/(MAX_RANK-1)+GRAPH_MARGIN_SIZE


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
