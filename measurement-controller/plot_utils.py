import os
import json
import matplotlib.pyplot as plt

def draw_bitrate_graph(data, save_path):
    bitrates = [interval['sum']['bits_per_second'] for interval in data.get('intervals', []) if 'sum' in interval and 'bits_per_second' in interval['sum']]
    
    print("Bitrates:", bitrates)

    if not bitrates:
        print("No bitrate data found in intervals.")
        return

    plt.figure(figsize=(10,5))
    plt.plot(bitrates, marker='o')
    plt.title('Iperf3 Test Bitrate Over Time')
    plt.xlabel('Interval')
    plt.ylabel('Bitrate (bits/sec)')
    plt.grid(True)

    plt.savefig(save_path)
    plt.close()

def main():
    results_dir = os.environ.get("RESULTS_DIR", "/results")
    files = [f for f in os.listdir(results_dir) if f.endswith('.json')]
    if not files:
        print("No results found.")
        return

    latest_file = max(files, key=lambda f: os.path.getctime(os.path.join(results_dir, f)))
    filepath = os.path.join(results_dir, latest_file)

    with open(filepath) as f:
        data = json.load(f)

    image_path = os.path.join(results_dir, 'latest_plot.png')
    draw_bitrate_graph(data, image_path)
    print(f"Plot saved to {image_path}")

if __name__ == "__main__":
    main()
