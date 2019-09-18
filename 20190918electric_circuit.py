import numpy as np
import matplotlib.pylab as plt


def main():
    prob1()
    prob2()


def prob1():
    E = 100 # V
    R = 1000 # ohm

    I = E/R # A
    print(I)


def prob2():
    Em = 100 # V
    f = 60 # Hz
    R = 1000 # ohm
    C = 10 * 10e-6 # F
    t = np.linspace(0, np.pi)

    E = Em * np.sin(2 * np.pi * f * t) # V
    I = E / (R + 1/(1j*2*np.pi*f*C)) # A
    abs_I = (Em / np.sqrt(2)) / np.abs(R + 1/(2*np.pi*f*C)) # A

    print(t)
    print(E)
    print(I)
    print(abs_I)

    plt.plot(t, E)
    plt.show()

if __name__ == '__main__':
    main()





