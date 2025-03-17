import time
import math
import multiprocessing
import numpy as np

# --- Terminal Color Codes ---
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_RED = "\033[91m"
COLOR_RESET = "\033[0m"

# -------------------------------
# CPU Workload Simulations (per app)
# -------------------------------

def cpu_xcode_compilation(_):
    result = 0.0
    for i in range(1, 10**6):
        result += (i ** 0.5) * (i ** 0.33) / (i % 100 + 1)
    return result

def cpu_logic_pro_audio_mix(_):
    result = 0.0
    for i in range(1, 10**6):
        result += math.sin(i % 360) * math.tan(i % 180 + 1)
    return result

def cpu_final_cut_rendering(_):
    result = 0.0
    for i in range(1, 10**6):
        result += (i % 255) * math.log(i + 1)
    return result

def cpu_blender_rendering(_):
    result = 0.0
    for i in range(1, 10**6):
        result += (i ** 0.8) * math.cos(i % 100) * math.sqrt(i)
    return result

def cpu_davinci_export(_):
    result = 0
    for i in range(1, 10**6):
        result += i * (i % 256)
    return result

# Helper for multiprocessing
def execute_task(task_func):
    return task_func(0)

# -------------------------------
# Run All CPU Workload Benchmarks
# -------------------------------

def run_all_cpu_benchmarks():
    cpu_workloads = [
        {"app": "Xcode Compilation", "task": cpu_xcode_compilation},
        {"app": "Logic Pro X Audio Mixing", "task": cpu_logic_pro_audio_mix},
        {"app": "Final Cut Pro Rendering", "task": cpu_final_cut_rendering},
        {"app": "Blender CPU Rendering", "task": cpu_blender_rendering},
        {"app": "DaVinci Resolve Export", "task": cpu_davinci_export},
    ]

    for workload in cpu_workloads:
        run_cpu_task(workload["task"], workload["app"])

def run_cpu_task(task_function, app_name):
    print(f"\n=== CPU BENCHMARK START: {app_name} ===")
    cpu_count = multiprocessing.cpu_count()
    print(f"Using {cpu_count} logical cores...")

    start = time.time()
    with multiprocessing.Pool(cpu_count) as pool:
        results = pool.map(task_function, range(cpu_count))
    end = time.time()

    duration = end - start
    print(f"{app_name} CPU Workload Completed in {duration:.2f} seconds.")
    print(f"=== CPU BENCHMARK END: {app_name} ===")

    # Interpretation with color
    if duration < 15:
        comment = f"{COLOR_GREEN}Excellent – ideal for professional and creative workloads.{COLOR_RESET}"
    elif duration < 25:
        comment = f"{COLOR_YELLOW}Good – great for most content creation and development tasks.{COLOR_RESET}"
    else:
        comment = f"{COLOR_RED}Moderate – sufficient for general productivity but not optimal for heavy workflows.{COLOR_RESET}"

    print(f"📝 Interpretation for {app_name}: {comment}\n")

# -------------------------------
# Memory Benchmark for All Application Scenarios
# -------------------------------

def run_all_memory_benchmarks():
    memory_workloads = [
        {"app": "Google Chrome (30+ tabs)", "size_gb": 4},
        {"app": "Logic Pro X (large music project)", "size_gb": 8},
        {"app": "Final Cut Pro (4K proxy editing)", "size_gb": 12},
        {"app": "Adobe After Effects (VFX-heavy)", "size_gb": 16},
        {"app": "Blender 3D Rendering (scene export)", "size_gb": 20},
        {"app": "DaVinci Resolve (High-End 4K+ Edit)", "size_gb": 24},
    ]

    for workload in memory_workloads:
        memory_test(size_gb=workload["size_gb"], workload_name=workload["app"])

# -------------------------------
# Memory Benchmark Function
# -------------------------------

def memory_test(size_gb=4, workload_name="General Workload"):
    print("=== MEMORY BENCHMARK START ===")
    print(f"Running Memory Benchmark simulating: **{workload_name}**")
    print(f"Allocating ~{size_gb}GB of memory...\n")

    size = int((size_gb * 1024**3) / 8)  # Number of float64 elements
    start = time.time()

    try:
        arr = np.ones(size, dtype=np.float64)
        arr *= 2.5
        sum_result = np.sum(arr)
        end = time.time()
        duration = end - start
        print(f"Memory Test Completed in {duration:.2f} seconds.")
        print(f"Sum of array: {sum_result:.2e}")
    except MemoryError:
        print("MemoryError: Allocation failed. Try using a smaller size.")
        duration = None

    print("=== MEMORY BENCHMARK END ===\n")

    if duration:
        if duration < 10:
            comment = f"{COLOR_GREEN}Excellent memory speed – great for large media projects, 3D rendering, and multitasking.{COLOR_RESET}"
        elif duration < 20:
            comment = f"{COLOR_YELLOW}Good memory speed – suitable for video editing and dev workflows.{COLOR_RESET}"
        else:
            comment = f"{COLOR_RED}Moderate memory performance – fine for general tasks and light creative work.{COLOR_RESET}"

        print(f"📝 Interpretation for {workload_name}: {comment}\n")

# -------------------------------
# Main Entry Point
# -------------------------------

if __name__ == "__main__":
    print("System Benchmark Starting...\n")

    # Run All CPU Workload Benchmarks
    run_all_cpu_benchmarks()

    # Run All Memory Workload Benchmarks
    print("Starting Automatic Memory Workload Benchmarks...\n")
    run_all_memory_benchmarks()

    print("\nAll benchmarks completed.")