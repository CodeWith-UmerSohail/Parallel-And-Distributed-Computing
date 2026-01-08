import concurrent.futures
import time
import random

# Simulated bank transactions
transactions = [
    {"id": 101, "amount": 1200},
    {"id": 102, "amount": 5400},
    {"id": 103, "amount": 2300},
    {"id": 104, "amount": 9800},
    {"id": 105, "amount": 4100},
    {"id": 106, "amount": 7600},
    {"id": 107, "amount": 1500},
    {"id": 108, "amount": 8900},
    {"id": 109, "amount": 3100},
    {"id": 110, "amount": 6700},
]


def fraud_check(amount):
    """
    CPU-intensive fraud detection simulation.
    Larger amounts require more computation.
    """
    score = 0
    for i in range(amount * 500):
        score += i % 7
    return score


def process_transaction(transaction):
    """
    Analyze a single transaction.
    """
    risk_score = fraud_check(transaction["amount"])
    print(f"💳 Transaction {transaction['id']} | Amount: ${transaction['amount']} | Risk Score: {risk_score}")
    return risk_score


if __name__ == "__main__":
    print("=" * 70)
    print("    BANK TRANSACTION RISK ANALYSIS SYSTEM")
    print("    Sequential vs Thread Pool vs Process Pool")
    print("=" * 70)

    # ============================================================
    # METHOD 1: Sequential Execution
    # ============================================================
    print("\n🔄 METHOD 1: SEQUENTIAL EXECUTION\n")
    start = time.perf_counter()

    for tx in transactions:
        process_transaction(tx)

    sequential_time = time.perf_counter() - start
    print(f"\n⏱️ Sequential Time: {sequential_time:.2f} seconds\n")

    # ============================================================
    # METHOD 2: Thread Pool Execution
    # ============================================================
    print("🧵 METHOD 2: THREAD POOL EXECUTION (4 workers)\n")
    start = time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(process_transaction, tx) for tx in transactions]
        concurrent.futures.wait(futures)

    thread_time = time.perf_counter() - start
    print(f"\n⏱️ Thread Pool Time: {thread_time:.2f} seconds\n")

    # ============================================================
    # METHOD 3: Process Pool Execution
    # ============================================================
    print("⚙️ METHOD 3: PROCESS POOL EXECUTION (4 workers)\n")
    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(process_transaction, tx) for tx in transactions]
        concurrent.futures.wait(futures)

    process_time = time.perf_counter() - start
    print(f"\n⏱️ Process Pool Time: {process_time:.2f} seconds\n")

    # ============================================================
    # PERFORMANCE SUMMARY
    # ============================================================
    print("=" * 70)
    print("📊 PERFORMANCE SUMMARY")
    print("=" * 70)
    print(f"Sequential:   {sequential_time:.2f} seconds")
    print(f"Thread Pool:  {thread_time:.2f} seconds")
    print(f"Process Pool: {process_time:.2f} seconds")

    print("\n🚀 Speedup:")
    print(f"Thread Pool Speedup:  {sequential_time / thread_time:.2f}x")
    print(f"Process Pool Speedup: {sequential_time / process_time:.2f}x")
    print("=" * 70)
