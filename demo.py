import random
import time


def generate_random():
    return random.randint(0, 100)


def transmit_data(data, interval):
    print("Transmitting data:", data, "at interval", interval)
    # Add code to transmit data to sink node


def average_data(data, interval):
    n = int(interval / 10)  # Number of samples to average
    avg = sum(data[-n:]) / n  # Average of last n samples
    transmit_data(avg, interval)


def run(interval):
    data = []
    while True:
        val = generate_random()
        data.append(val)
        if len(data) >= 6:  # Average and transmit data every minute (6*10s)
            average_data(data, interval)
            data = []
        time.sleep(10)


# Run program for different intervals
run(60)  # Transmit every minute
#run(120)  # Transmit every two minutes
#run(300)  # Transmit every five minutes




