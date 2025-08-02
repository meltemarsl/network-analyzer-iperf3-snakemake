import subprocess
import os
import json
import sys

def start_test():
    output_dir = "/results"
    os.makedirs(output_dir, exist_ok=True)
    output_file = f"{output_dir}/iperf3_output.json"
    
    try:
        result = subprocess.run(
            ["iperf3", "-c", "iperf3-server", "-t", "10", "-J"],
            capture_output=True,
            text=True
        )
        
        json_output = result.stdout
        
        json.loads(json_output)  
        
        with open(output_file, "w") as f:
            f.write(json_output)
            
    except (subprocess.CalledProcessError, json.JSONDecodeError) as e:
        print(f"Test failed: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    start_test()