
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Step 3: Load streamflow data
def load_streamflow(filename):
    """Read the CSV and return dates and five gauge flow columns."""
    data = np.genfromtxt(
        filename,
        delimiter=",",
        dtype=str,
        skip_header=1
    )

    dates = np.array(data[:, 0], dtype="datetime64[m]")
    flows = data[:, 1:6].astype(float)

    return dates, flows


# Step 3: Plot streamflow data
def plot_streamflow(dates, flows, sites):
    """Plot streamflow for all five monitoring sites."""
    plt.figure(figsize=(10, 6))

    for i, site in enumerate(sites):
        plt.plot(dates, flows[:, i], label=site)

    plt.title("Provo River Streamflow Data (2021)")
    plt.xlabel("Date")
    plt.ylabel("Flowrate (cfs)")
    plt.legend(title="Site Numbers")
    plt.grid(True)

    plt.gca().xaxis.set_major_formatter(
        mdates.DateFormatter("%Y-%m-%d")
    )
    plt.gca().xaxis.set_major_locator(
        mdates.DayLocator(interval=4)
    )

    plt.xticks(rotation=45)
    plt.tight_layout()

    # Step 4: Save graph before displaying it
    plt.savefig("provo_streamflow.png", dpi=150,
                bbox_inches="tight")

    plt.show()


# Main program
sites = [
    "10163000",
    "10155200",
    "10155500",
    "10154200",
    "10155000"
]

dates, flows = load_streamflow(
    "June-2021-Provo-River-Streamflow-Rates.csv"
)

plot_streamflow(dates, flows, sites)


# Step 5: Create streamflow summary table
import csv

def summarize_streamflow(dates, flows, sites):
    summary = []

    print("\nPROVO RIVER STREAMFLOW SUMMARY")
    print("-" * 90)
    print(f"{'Site':<12} {'Min (cfs)':>12} {'Max (cfs)':>12} "
          f"{'Mean (cfs)':>12} {'Date/Time of Max':>22}")

    for i, site in enumerate(sites):
        values = flows[:, i]

        minimum = np.min(values)
        maximum = np.max(values)
        average = np.mean(values)

        max_index = np.argmax(values)
        max_date = str(dates[max_index])

        summary.append([
            site,
            round(float(minimum), 2),
            round(float(maximum), 2),
            round(float(average), 2),
            max_date
        ])

        print(f"{site:<12} {minimum:>12.2f} {maximum:>12.2f} "
              f"{average:>12.2f} {max_date:>22}")

    with open("streamflow_summary.csv", "w",
              newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Site", "Minimum (cfs)", "Maximum (cfs)",
            "Average (cfs)", "Date/Time of Maximum"
        ])

        writer.writerows(summary)

    print("\nSummary saved to streamflow_summary.csv")


summarize_streamflow(dates, flows, sites)
