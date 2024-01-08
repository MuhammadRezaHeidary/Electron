
import eel
import mpld3
from matplotlib import pyplot as plt, patches
import math
import os
import ctypes

eel.init("eel")

@eel.expose                         # Expose this function to Javascript
def plot_partitioner(BL,BH,SL,SH):

    big_sheet_length_cm = BL
    big_sheet_height_cm = BH

    sheet_length_cm = SL
    sheet_height_cm = SH

    plt.rcParams["figure.figsize"] = [big_sheet_length_cm/15, big_sheet_height_cm/15]
    plt.rcParams["figure.autolayout"] = True
    fig = plt.figure("PCB Sheet Partitioner")
    ax = fig.add_subplot(111)

    div_mat = [[math.floor(big_sheet_length_cm/sheet_length_cm), math.floor(big_sheet_height_cm/sheet_height_cm)],[math.floor(big_sheet_length_cm/sheet_height_cm), math.floor(big_sheet_height_cm/sheet_length_cm)]]
    rect_length = 0
    rect_height = 0
    n_rect_length = 0
    n_rect_height = 0

    if (div_mat[0][0]*div_mat[0][1] >= div_mat[1][0]*div_mat[1][1]):
        rect_length = sheet_length_cm
        rect_height = sheet_height_cm
        n_rect_length = div_mat[0][0]
        n_rect_height = div_mat[0][1]
    else:
        rect_length = sheet_height_cm
        rect_height = sheet_length_cm
        n_rect_length = div_mat[1][0]
        n_rect_height = div_mat[1][1]


    big_sheet_rect = patches.Rectangle((0, 0), big_sheet_length_cm, big_sheet_height_cm, edgecolor='black', facecolor="#B26F31", linewidth=1)
    ax.add_patch(big_sheet_rect)

    for i in range(n_rect_length):
        for j in range(n_rect_height):
            rect = patches.Rectangle((i*rect_length, j*rect_height), rect_length, rect_height, edgecolor='black', facecolor="#ffffbb", linewidth=1)
            ax.add_patch(rect)


    sheet_error = ((big_sheet_length_cm*big_sheet_height_cm - rect_length*rect_height*n_rect_length*n_rect_height)/(big_sheet_length_cm*big_sheet_height_cm))*100;

    plt.xlim([0, big_sheet_length_cm])
    plt.ylim([0, big_sheet_height_cm])
    plt.xlabel(big_sheet_length_cm,
              fontsize='20',
              color='black')
    plt.ylabel(big_sheet_height_cm,
              fontsize='20',
              color='black')
    plt.title(f'Sheet = {n_rect_length}*{n_rect_height} ({rect_length}cm*{rect_height}cm)___ Error = {"{:.2f}".format(sheet_error)}%',
              fontsize='14',
              color='black')


    html_str = mpld3.fig_to_html(fig)
    Html_file= open("./eel/figure.html","w")
    Html_file.seek(0)
    Html_file.truncate()
    Html_file.write(html_str)
    Html_file.close()
    Html_file = open("./eel/figure.html", "a")
    Html_file.write("""<link rel="stylesheet" href="styles.css">""")
    Html_file.close()
    plt.figure().clear()
    plt.close()
    plt.cla()
    plt.clf()


user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[screen_w, screen_h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]

# open in default system browser
eel.start("index.html", mode='default',
                        host='localhost',
                        port=20975,
                        block=True,
                        size=(screen_w, screen_h),
                        position=(0,0),
                        disable_cache=True,
                        cmdline_args=['--browser-startup-dialog',
                        '--incognito', '--no-experiments'])
