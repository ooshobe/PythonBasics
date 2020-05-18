import matplotlib.pyplot as plt
import time as t

times = []
mistakes = 0

print("This program will help you type faster. You will have the to type the word 'programming' as fast as you can five times in a row")
input("Press Enter to continue.")

while len(times) < 5:
    start = t.time()
    word = input ("Type the word: ")
    end = t.time()
    time_elapsed = end - start

    times.append(time_elapsed)

    if (word.lower() != "programming"):
        mistakes += 1
print("You made " + str(mistakes) + " mistakes.")
print("Now Let's see your evolution")
t.sleep(3)

x = [1,2,3,4,5]
y = times

plt.plot(x,y)
plt.show()

