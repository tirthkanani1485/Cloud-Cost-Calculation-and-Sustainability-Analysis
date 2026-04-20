import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Cloud Pricing (Approx Values)
# -------------------------------
pricing = {
    "AWS": {"storage": 2, "compute": 5, "data": 1},
    "Azure": {"storage": 2.2, "compute": 5.5, "data": 1.2},
    "GCP": {"storage": 2.1, "compute": 4.8, "data": 1}
}

# -------------------------------
# User Input
# -------------------------------
print("----- Cloud Cost Calculator -----")
storage = float(input("Enter Storage (GB): "))
compute = float(input("Enter Compute Hours: "))
data_transfer = float(input("Enter Data Transfer (GB): "))

# -------------------------------
# Cost Calculation Function
# -------------------------------
def calculate_cost(storage, compute, data_transfer):
    results = []

    for provider in pricing:
        storage_cost = storage * pricing[provider]["storage"]
        compute_cost = compute * pricing[provider]["compute"]
        data_cost = data_transfer * pricing[provider]["data"]

        total = storage_cost + compute_cost + data_cost

        print(f"\n--- {provider} ---")
        print(f"Storage Cost: ₹{storage_cost}")
        print(f"Compute Cost: ₹{compute_cost}")
        print(f"Data Transfer Cost: ₹{data_cost}")
        print(f"Total Cost: ₹{total}")

        results.append([provider, storage_cost, compute_cost, data_cost, total])

    return pd.DataFrame(results, columns=[
        "Provider", "Storage Cost", "Compute Cost", "Data Transfer Cost", "Total Cost"
    ])

# -------------------------------
# Single Scenario Result
# -------------------------------
df = calculate_cost(storage, compute, data_transfer)

# -------------------------------
# Save to CSV
# -------------------------------
df.to_csv("cloud_cost_results.csv", index=False)
print("\n✅ Results saved to cloud_cost_results.csv")

# -------------------------------
# Graph for Single Scenario
# -------------------------------
plt.figure(figsize=(8, 5))
plt.bar(df["Provider"], df["Total Cost"])
plt.title("Cloud Cost Comparison (User Input)")
plt.xlabel("Provider")
plt.ylabel("Cost (₹)")
plt.grid()
plt.show()

# -------------------------------
# Multiple Scenarios (Auto)
# -------------------------------
print("\n----- Running Multiple Scenarios -----")

scenarios = [
    [50, 20, 10],    # Small
    [100, 50, 20],   # Medium
    [200, 100, 50]   # Large
]

all_results = []

for i, scenario in enumerate(scenarios):
    s, c, d = scenario
    print(f"\nScenario {i+1}: Storage={s}, Compute={c}, Data={d}")
    temp_df = calculate_cost(s, c, d)
    temp_df["Scenario"] = f"Scenario {i+1}"
    all_results.append(temp_df)

final_df = pd.concat(all_results)

# Save all scenarios
final_df.to_csv("all_scenarios_cost.csv", index=False)
print("\n✅ All scenario results saved to all_scenarios_cost.csv")

# -------------------------------
# Graph for Multiple Scenarios
# -------------------------------
for scenario in final_df["Scenario"].unique():
    data = final_df[final_df["Scenario"] == scenario]
    
    plt.figure()
    plt.bar(data["Provider"], data["Total Cost"])
    plt.title(f"Cloud Cost - {scenario}")
    plt.xlabel("Provider")
    plt.ylabel("Cost (₹)")
    plt.grid()
    plt.show()

print("\n🎉 Project Execution Completed Successfully!")