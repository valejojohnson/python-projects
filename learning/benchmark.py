import time
import math
import multiprocessing
import numpy as np

# --- Terminal Color Codes ---
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_RED = "\033[91m"
COLOR_RESET = "\033[0m"

# --- Summary Containers ---
cpu_results_summary = []
memory_results_summary = []

# --- Global variable for CPU ramp-up test scale ---
cpu_ramp_scale = 100000  # This value will be dynamically updated during the ramp test

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

# --- Multiprocessing-safe helper function ---
def execute_task(task_func):
    return task_func(0)

# -------------------------------
# CPU Ramp-Up Task (Top-Level, Not Nested)
# -------------------------------

def cpu_ramp_task(_):
    global cpu_ramp_scale
    result = 0.0
    for i in range(1, cpu_ramp_scale):
        result += math.sqrt(i) * math.log(i + 1)
    return result

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

    if duration < 15:
        rating = "Excellent"
        comment = f"{COLOR_GREEN}Excellent – ideal for professional and creative workloads.{COLOR_RESET}"
    elif duration < 25:
        rating = "Good"
        comment = f"{COLOR_YELLOW}Good – great for most content creation and development tasks.{COLOR_RESET}"
    else:
        rating = "Moderate"
        comment = f"{COLOR_RED}Moderate – sufficient for general productivity but not optimal for heavy workflows.{COLOR_RESET}"

    cpu_results_summary.append({
        "app": app_name,
        "duration": duration,
        "comment": comment,
        "rating": rating
    })

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

    size = int((size_gb * 1024**3) / 8)
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
            rating = "Excellent"
            comment = f"{COLOR_GREEN}Excellent memory speed – great for large media projects, 3D rendering, and multitasking.{COLOR_RESET}"
        elif duration < 20:
            rating = "Good"
            comment = f"{COLOR_YELLOW}Good memory speed – suitable for video editing and dev workflows.{COLOR_RESET}"
        else:
            rating = "Moderate"
            comment = f"{COLOR_RED}Moderate memory performance – fine for general tasks and light creative work.{COLOR_RESET}"

        memory_results_summary.append({
            "app": workload_name,
            "duration": duration,
            "comment": comment,
            "rating": rating
        })

        print(f"📝 Interpretation for {workload_name}: {comment}\n")

# -------------------------------
# CPU Ramp-Up Test (Using Top-Level Function)
# -------------------------------

def run_cpu_ramp_test():
    global cpu_ramp_scale
    print("\n=== CPU RAMP-UP STRESS TEST ===")
    cpu_count = multiprocessing.cpu_count()

    for scale in [10**5, 2 * 10**5, 4 * 10**5, 8 * 10**5, 10**6]:
        cpu_ramp_scale = scale
        print(f"\nRunning ramp-up CPU test with loop scale: {scale:,}")
        start = time.time()

        with multiprocessing.Pool(cpu_count) as pool:
            results = pool.map(cpu_ramp_task, range(cpu_count))

        end = time.time()
        duration = end - start
        print(f"Ramp scale {scale:,} completed in {duration:.2f} seconds.")

# -------------------------------
# Memory Ramp-Up Test
# -------------------------------

def run_memory_ramp_test():
    print("\n=== MEMORY RAMP-UP STRESS TEST ===")
    for size_gb in [4, 8, 12, 16, 20, 24, 28]:
        print(f"\nAllocating ~{size_gb}GB of memory...")
        try:
            size = int((size_gb * 1024**3) / 8)
            start = time.time()
            arr = np.ones(size, dtype=np.float64)
            arr *= 2.5
            sum_result = np.sum(arr)
            end = time.time()
            duration = end - start
            print(f"Ramp memory test {size_gb}GB completed in {duration:.2f} seconds. Sum: {sum_result:.2e}")
        except MemoryError:
            print(f"MemoryError: Allocation failed at {size_gb}GB. System limit reached.")
            break

# -------------------------------
# Final System Summary
# -------------------------------

def summarize_system_performance():
    print("\n" + "="*50)
    print("📊 FINAL SYSTEM PERFORMANCE SUMMARY")
    print("="*50)

    all_ratings = [r["rating"] for r in cpu_results_summary + memory_results_summary]

    excellent = all_ratings.count("Excellent")
    good = all_ratings.count("Good")
    moderate = all_ratings.count("Moderate")

    print(f"\n🧠 {COLOR_GREEN}Excellent Ratings: {excellent}{COLOR_RESET}")
    print(f"💡 {COLOR_YELLOW}Good Ratings: {good}{COLOR_RESET}")
    print(f"⚠️  {COLOR_RED}Moderate Ratings: {moderate}{COLOR_RESET}\n")

    if moderate == 0:
        print(f"{COLOR_GREEN}✅ Your system shows no major limitations. It's highly optimized for professional workloads, creative tasks, and multitasking.{COLOR_RESET}\n")
    else:
        print(f"{COLOR_YELLOW}⚠️ Summary Insights:{COLOR_RESET}")
        if any(r["rating"] == "Moderate" for r in cpu_results_summary):
            print("- CPU performance may limit you in high-end rendering, compiling, or export tasks.")
        if any(r["rating"] == "Moderate" for r in memory_results_summary):
            print("- Memory speed or capacity may bottleneck heavy media editing or multitasking workflows.")
        print(f"{COLOR_YELLOW}\n🎯 Recommendation: Monitor actual resource usage during work. If you notice slowness, consider a memory upgrade or faster CPU cores in future systems.{COLOR_RESET}")

# -------------------------------
# Main Entry Point
# -------------------------------

if __name__ == "__main__":
    print("System Benchmark Starting...\n")
    run_all_cpu_benchmarks()
    print("Starting Automatic Memory Workload Benchmarks...\n")
    run_all_memory_benchmarks()
    summarize_system_performance()
    run_cpu_ramp_test()
    run_memory_ramp_test()
    print("\nAll benchmarks completed.")