import os
PROJECT_ROOT = os.getcwd()

rule all:
    input:
        "results/latest_plot.png"

rule clean:
    shell:
        """
        docker-compose down --remove-orphans > /dev/null 2>&1 || true
        rm -f server_started.txt
        rm -rf results/*
        mkdir -p results
        """

rule build_images:
    output:
        touch(".built")
    shell:
        """
        docker-compose build --no-cache > build.log 2>&1
        """

rule start_server:
    input:
        ".built"
    output:
        touch("server_started.txt")
    shell:
        """
        docker-compose up -d iperf3-server
        sleep 15
        """

rule run_iperf3_test:
    input:
        "server_started.txt"
    output:
        "results/iperf3_output.json"
    shell:
        """
        docker-compose run --rm iperf3-client \
        python3 /app/run_iperf_test.py > {output}
        """

rule plot_results:
    input:
        "results/iperf3_output.json"
    output:
        "results/latest_plot.png"
    shell:
        """
        docker-compose run --rm measurement-controller \
        python3 /app/controller.py
        touch {output}  # controller.py çıktıyı oluşturmazsa
        """