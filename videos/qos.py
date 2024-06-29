# qos.py
import random
import psutil


def measure_qos():
    # Simulate QoS measurement
    latency = random.uniform(50, 100)  # Simulate latency in ms
    bit_rate = random.uniform(1000, 5000)  # Simulate bit rate in kbps
    sync_skew = random.uniform(0, 50)  # Simulate sync skew in ms
    playback_jitter = random.uniform(0, 10)  # Simulate playback jitter in ms
    packet_loss = random.uniform(0, 1)  # Simulate packet loss percentage

    return {
        "latency": latency,
        "bit_rate": bit_rate,
        "sync_skew": sync_skew,
        "playback_jitter": playback_jitter,
        "packet_loss": packet_loss,
    }
