import json
import matplotlib.pyplot as plt

with open("../results/iperf3_output.json") as f:
    data = json.load(f)

throughputs = [interval["sum"]["bits_per_second"] / 1e6 for interval in data["intervals"]]
plt.plot(throughputs)
plt.xlabel("Seconds")
plt.ylabel("Throughput (Mbps)")
plt.title("iperf3 Test Results")
plt.savefig("../results/latest_plot.png")
