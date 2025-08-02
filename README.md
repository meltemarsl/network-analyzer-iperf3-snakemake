# iperf3 Measurement Pipeline

This project runs an `iperf3` network performance test inside Docker containers, processes the results, and generates a plot. The workflow is managed using **Snakemake**.

---

## Requirements

- **Docker** and **Docker Compose** installed
- **Python 3.10+**
- **Snakemake** (`pip install snakemake`)

---

## Project Structure
```
client/                   # iperf3 client container
measurement-controller/   # plotting container
results/                  # output JSON + plot
docker-compose.yml
Snakefile
requirements.txt
```

---

## Quick Start (Single Command)
Run the entire workflow from server start to plot generation:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
snakemake -j1 --latency-wait 5

```
This will:
1. Start the `iperf3-server`.
2. Run the `iperf3` client test.
3. Save output as `results/iperf3_output.json`.
4. Generate `results/latest_plot.png`.

---

## Output Files
- `results/iperf3_output.json` — iperf3 test results in JSON
- `results/latest_plot.png` — bitrate plot from JSON data

---

## Notes
- `--latency-wait` prevents missing file errors caused by filesystem sync delays.
