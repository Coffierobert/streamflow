
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
