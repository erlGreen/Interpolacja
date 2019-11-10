import matplotlib.pyplot as plt
import pandas as pd
from functions import *

file = ["ul. Dluga", "Mount Everest", "Wielki Kanion"]
for j in range(0, 3):
    for i in range(1, 5):
        data = pd.read_csv(file[j] + ".csv")
        distanceArray = data["Dystans (m)"]
        heightArray = data["Wysokość (m)"]
        subArraySequence = 2**i
        functionSequence = 10
        distanceSubArray = []
        heightSubArray = []
        for k in range(0, len(distanceArray), subArraySequence):
            distanceSubArray.append(distanceArray[k])
            heightSubArray.append(heightArray[k])
        xl, yl = lagrange(distanceSubArray, heightSubArray, functionSequence)
        xs, ys = splajn(distanceSubArray, heightSubArray, functionSequence)
        #plt.plot(distanceArray, heightArray, "b.", label="Faktyczny przekroj")
        plt.figure(figsize=(18,16))
        plt.subplot(4, 1, 1)
        plt.plot(xl, yl, "g-", label="Przekroj metoda interpolacji")
        plt.ylim(min(heightArray), max(heightArray))
        plt.legend()
        #plt.show()

        plt.subplot(4, 1, 2)
        #plt.plot(distanceArray, heightArray, "b.", label="Faktyczny przekroj")
        plt.plot(xs, ys, "r-", label="Przekroj metoda splajnow")
        plt.legend()
        #plt.show()

        plt.subplot(4, 1, 3)
        plt.plot(distanceSubArray, heightSubArray, "b.", label="Podzbior przekroju")
        plt.legend()

        plt.subplot(4, 1, 4)
        plt.plot(distanceArray, heightArray, "b.", label="Przekroj rzeczywisty")
        plt.legend()
        plt.suptitle(str(len(distanceSubArray)) + " z " + str(len(distanceArray)) + " punktow. Przekroj " + file[j])
        plt.gcf()
        plt.savefig(file[j] + "("+ str(len(distanceSubArray)) + ").png")
        plt.clf()