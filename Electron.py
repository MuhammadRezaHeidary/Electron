from matplotlib import pyplot as plt, patches
import math

big_sheet_length_cm = 120
big_sheet_height_cm = 100

sheet_length_cm = 38
sheet_height_cm = 30

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
plt.title(f'Sheet = {n_rect_length}*{n_rect_height} ({rect_length}cm*{rect_height}cm)\nError = {"{:.2f}".format(sheet_error)}%',
          fontsize='14',
          color='black')

plt.show()
