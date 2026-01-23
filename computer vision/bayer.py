from matplotlib.pylab import mat


GRGB_Mat = [[120, 200, 130],
       [100, 150, 110],
       [125, 105, 220]]

def get_rgb_mat(mat, pattern='GRGB'):
    row_pattern11 = pattern[0] # G
    row_pattern12 = pattern[1] # R
    row_pattern21 = pattern[2] # G
    row_pattern22 = pattern[3] # B
    R = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
    G = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
    B = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
    col_map = {'R': R, 'G': G, 'B': B}

    for i in range(len(mat)):
          for j in range(len(mat[0])):
              if i % 2 == 0:
                     if j % 2 == 0:
                            col_map[row_pattern11][i][j] = mat[i][j]
                     else:
                            col_map[row_pattern12][i][j] = mat[i][j]
              else:
                     if j % 2 == 0:
                            col_map[row_pattern22][i][j] = mat[i][j]
                     else:
                            col_map[row_pattern21][i][j] = mat[i][j]
    return [R, G, B]

R, G, B = get_rgb_mat(GRGB_Mat)
print("R:", R)
print("G:", G)
print("B:", B)

def nearest_neighbor_interpolation(mat, pattern='GRGB'):
    R, G, B = get_rgb_mat(mat, pattern)
    height = len(mat)
    width = len(mat[0])
    RBG_mat = [[[0, 0, 0] for _ in range(width)] for _ in range(height)]

    for i in range(height):
        for j in range(width):
              if (i % 2 == 0) and (j % 2 == 0):
                     RBG_mat[i][j][0] = R[i][j]
                     RBG_mat[i][j][1] = G[i][j-1] if j-1 >= 0 else G[i][j+1]
                     RBG_mat[i][j][2] = B[i-1][j-1] if i-1 >= 0 and j-1 >= 0 else (B[i+1][j+1] if i+1 < height and j+1 < width else 0)
              elif (i % 2 == 0) and (j % 2 == 1):
                     RBG_mat[i][j][0] = R[i][j]
                     RBG_mat[i][j][1] = G[i][j]
                     RBG_mat[i][j][2] = B[i-1][j] if i-1 >= 0 else B[i+1][j]
              elif (i % 2 == 1) and (j % 2 == 0):
                     RBG_mat[i][j][0] = R[i][j]
                     RBG_mat[i][j][1] = G[i][j]
                     RBG_mat[i][j][2] = B[i][j]
              else:
                     RBG_mat[i][j][0] = R[i-1][j-1] if i-1 >= 0 and j-1 >= 0 else (R[i+1][j+1] if i+1 < height and j+1 < width else 0)
                     RBG_mat[i][j][1] = G[i][j-1] if j-1 >= 0 else G[i][j+1]
                     RBG_mat[i][j][2] = B[i][j]
    return RBG_mat