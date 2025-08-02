# iperf3 Measurement Pipeline

This project runs an `iperf3` network performance test inside Docker containers, processes the results, and generates a plot. The workflow is managed using **Snakemake**.

---

## Requirements

- **Docker** and **Docker Compose** installed
- **Python 3.10+**
- **Snakemake** (`pip install snakemake`)

Install Python dependencies:
```bash
pip install -r requirements.txt
```

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
docker-compose build
snakemake -j1 --latency-wait 5
```
This will:
1. Start the `iperf3-server`.
2. Run the `iperf3` client test.
3. Save output as `results/iperf3_output.json`.
4. Generate `results/latest_plot.png`.

---

## Step-by-Step Usage

### 1. Build containers
```bash
docker-compose build
```

### 2. Start only the server
```bash
snakemake server_started.txt
```

### 3. Run the iperf3 test
```bash
snakemake results/iperf3_output.json
```

### 4. Generate the plot
```bash
snakemake results/latest_plot.png
```

---

## Output Files
- `results/iperf3_output.json` — iperf3 test results in JSON
- `results/latest_plot.png` — bitrate plot from JSON data

---

## Troubleshooting

**1. Connection refused**
- Make sure the server is running:
```bash
docker-compose up -d iperf3-server
```

**2. Missing results**
- Ensure `results/` directory exists and is mounted in `docker-compose.yml`.

**3. Force re-run a step**
```bash
snakemake <target_file> --force -j1 --latency-wait 5
```
Example:
```bash
snakemake results/iperf3_output.json --force -j1 --latency-wait 5
```

---

## Notes
- `--latency-wait` prevents missing file errors caused by filesystem sync delays.
