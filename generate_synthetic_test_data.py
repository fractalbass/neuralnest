import numpy as np

height = 3
width = 3
cellw = 1


br = 0
bl = 0
mv = 0

f1 = open('./three_by_three_data.txt', 'a')

for bx in range(0, width - cellw + 1):
    basket_row = np.zeros(width)
    bl = bx
    br = bx + cellw - 1

    for cw in range(0, cellw):

        basket_row[bx + cw] = 1

    display_rows = np.zeros(width * (height - 1))
    for x in range(0, display_rows.size, width):
        for y in range(0, height):
            display_rows = np.zeros(width * (height - 1))
            display_rows[x + y] = 1
            mv = 0.0
            ex = (x+y) % width
            if bl > ex:
                mv = -1.0
            if br < ex:
                mv = 1.0

            full_display = np.append(display_rows, basket_row)
            full_row = np.append(full_display, mv)
            x_str = np.array2string(full_row).replace('\n', '').replace('[','').replace(']','').replace('. ',', ')

            print(x_str+"0")
            f1.write(x_str + "0\n")

            # print("ex={0}, br={1}, bl={2}, mv={3}".format(ex, br, bl, mv))
            # print("")
f1.close()
print("Done!")
