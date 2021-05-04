This is a Terminal Widget Library, including Terminal Progresbar

import piconsole

prg = piconsole.ProgressBar(piconsole.ProgressBar.default)
for x in range(100):
    prg.draw(x)

