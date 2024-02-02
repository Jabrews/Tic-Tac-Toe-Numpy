import numpy as np

rowTop = np.array([["a", "a", "a"],
                    ["-", "-", "-"],
                    ["-", "-", "-"]])
##########
rowMid = np.array([["-", "-", "-"],
                    ["a", "a", "a"],
                    ["-", "-", "-"]])
###########
rowBot = np.array([["-", "-", "-"],
                    ["-", "-", "-"],
                    ["a", "a", "a"]])
###########
colBot = np.array([["-", "-", "a"],
                    ["-", "-", "a"],
                    ["-", "-", "a"]])
##########
colMid = np.array([["-", "a", "-"],
                    ["-", "a", "-"],
                    ["-", "a", "-"]])
###########
colTop = np.array([["a", "-", "-"],
                    ["a", "-", "-"],
                    ["a", "-", "-"]])
###########
diaLeft = np.array([["a", "-", "-"],
                    ["-", "a", "-"],
                    ["-", "-", "a"]])
###########
diaRight = np.array([["-", "-", "a"],
                      ["-", "a", "-"],
                      ["a", "-", "-"]])

win_conditions = {
    "rowTop" : rowTop,
    "rowMid": rowMid,
    "rowBot": rowBot,
    "colTop": colTop,
    "colMid": colMid,
    "colBot": colBot,
    "diaLeft": diaLeft,
    "diaRight": diaRight
}