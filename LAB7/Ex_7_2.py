import threading
import time


# inheriting threading class in Thread module
class Philosopher(threading.Thread):
    running = True  # used to check if everyone is finished eating

    def __init__(self, index, forkOnLeft, forkOnRight):
        threading.Thread.__init__(self)
        self.index = index
        self.forkOnLeft = forkOnLeft
        self.forkOnRight = forkOnRight

    def run(self):
        while (self.running):
            # Philosopher is thinking (but really is sleeping).
            time.sleep(10)
            print('Philosopher %s is hungry.' % self.index)
            self.dine()

    def dine(self):
        # if both the semaphores(forks) are free, then philosopher will eat
        leftFork = self.forkOnLeft
        rightFork = self.forkOnRight

        while self.running:
            leftFork.acquire()  # wait operation on left fork
            locked = rightFork.acquire(False)

            print(str(self.index) + " " + str(locked)) # for my understanding

            if locked: # if right fork is not available leave left fork
                break
            leftFork.release()
            print('Philosopher %s swaps forks.' % self.index)
            leftFork, rightFork = rightFork, leftFork
        else: # executed when while condition becomes false; skipped when while is broke
            return

        self.dining()
        # release both the fork after dining
        rightFork.release()
        leftFork.release()

    def dining(self):
        print('Philosopher %s starts eating. ' % self.index)
        time.sleep(10)
        print('Philosopher %s finishes eating and leaves to think.' % self.index)


def main():
    forks = [threading.Semaphore() for n in range(5)]  # initialising array of semaphore i.e forks

    # here (i+1)%5 is used to get right and left forks circularly between 1-5
    philosophers = [Philosopher(i, forks[i % 5], forks[(i + 1) % 5])
                    for i in range(5)]

    Philosopher.running = True
    for p in philosophers: p.start()
    time.sleep(30)
    Philosopher.running = False
    print("Now we're finishing.")


if __name__ == "__main__":
    main()

# code based on cppsecrets.com