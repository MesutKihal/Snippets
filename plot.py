import matplotlib.pyplot as mlp
import numpy

mlp.style.use('seaborn')
day_x = numpy.arange(1, 32, 1)
infected_y = numpy.array([503, 556, 515, 507, 532, 551, 571, 529, 536, 521, 498,
                          492, 495, 488, 477, 469, 450, 442, 419, 403, 411, 409,
                          401, 392, 398, 370, 391, 397, 387, 364, 348])



mlp.plot(day_x, infected_y, color='c')
mlp.title('Algeria Confirmed Cases in August')
mlp.xlabel('Days of the month')
mlp.ylabel('Confirmed Cases')
mlp.tight_layout()
mlp.show()
