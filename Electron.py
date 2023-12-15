from matplotlib import pyplot as plt, patches

big_sheet_length_cm = 120
big_sheet_height_cm = 100

sheet_length_cm = 30
sheet_height_cm = 20

plt.rcParams["figure.figsize"] = [big_sheet_length_cm/20, big_sheet_height_cm/20]
plt.rcParams["figure.autolayout"] = True
fig = plt.figure("PCB Sheet Partitioner")
ax = fig.add_subplot(111)
rectangle1 = patches.Rectangle((0, 0), sheet_length_cm, sheet_height_cm, edgecolor='black', facecolor="#ffffbb", linewidth=1)
rectangle2 = patches.Rectangle((0, sheet_height_cm), sheet_length_cm, sheet_height_cm, edgecolor='black', facecolor="#ffffbb", linewidth=1)
rectangle3 = patches.Rectangle((sheet_length_cm, 0), sheet_length_cm, sheet_height_cm, edgecolor='black', facecolor="#ffffbb", linewidth=1)
rectangle4 = patches.Rectangle((sheet_length_cm, sheet_height_cm), sheet_length_cm, sheet_height_cm, edgecolor='black', facecolor="#ffffbb", linewidth=1)
rectangle5 = patches.Rectangle((40, 60), sheet_length_cm, sheet_height_cm, edgecolor='black', facecolor="#ffffbb", linewidth=1)


ax.add_patch(rectangle1)
ax.add_patch(rectangle2)
ax.add_patch(rectangle3)
ax.add_patch(rectangle4)
ax.add_patch(rectangle5)

plt.xlim([0, big_sheet_length_cm])
plt.ylim([0, big_sheet_height_cm])
plt.show()
