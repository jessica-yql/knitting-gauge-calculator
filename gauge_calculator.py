
# Gauge calculator for knitting pattern sizes XS–5XL

sizes = ["XS", "S", "M", "L", "XL", "2XL", "3XL", "4XL", "5XL"]

# Gauge (stitches or rows per 10 cm)
stitch_gauge = 27
row_gauge = 40

# Choose what you're calculating: "sts" or "rows"
unit = input("Calculate stitches or rows? (sts/rows): ").strip().lower()

gauge = stitch_gauge if unit == "sts" else row_gauge

# Your existing measurement and stitch/row count
current_count = float(input(f"How many {unit} do you currently have? "))
current_cm = float(input("What is your measurement in cm? "))

# Regular garment measurements for each size
print("\nEnter the regular garment measurement (cm) for each size:")
regular_cm = {}

for size in sizes:
    regular_cm[size] = float(input(f"{size}: "))

# Calculate the ratio against regular size S
regular_s = regular_cm["S"]
ratio = current_cm / regular_s

# Calculate the count needed for each size
print("\n--- Results ---")
print(f"Gauge: {gauge} {unit} per 10 cm")
print(f"Your measurement: {current_cm:g} cm")
print(f"Regular size S measurement: {regular_s:g} cm")
print(f"Measurement ratio: {ratio:.3f}\n")

print(f"{'Size':<6} {'Regular cm':>12} {'Ratio':>8} {'Needed cm':>12} {'Needed ' + unit:>12}")
print("-" * 54)

for size in sizes:
    size_ratio = current_cm / regular_s
    needed_cm = regular_cm[size] * ratio
    needed_count = needed_cm * gauge / 10

    print(
        f"{size:<6} "
        f"{regular_cm[size]:>12.1f} "
        f"{ratio:>8.3f} "
        f"{needed_cm:>12.1f} "
        f"{needed_count:>12.1f}"
    )
