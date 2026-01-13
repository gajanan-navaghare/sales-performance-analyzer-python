import pandas as pd

# ---------- DATA LOADING ----------
def load_data():
    try:
        df = pd.read_csv("sales_data.csv")   # pandas usage
        return df.values.tolist()            # Convert to Python list
    except FileNotFoundError:
        print("sales_data.csv not found. Keep it in the same folder.")
        return []


# ---------- REVENUE CALCULATION ----------
def calculate_revenue(data):
    processed = []
    for row in data:
        date, product, region, qty, price = row
        revenue = int(qty) * int(price)
        processed.append((date, product, region, revenue))
    return processed


# ---------- TOTAL REVENUE ----------
def total_revenue(data):
    total = 0
    for item in data:
        total += item[3]
    return total


# ---------- GROUPING LOGIC ----------
def group_by(data, index):
    result = {}
    for item in data:
        key = item[index]
        result[key] = result.get(key, 0) + item[3]
    return result


# ---------- TOP PERFORMER ----------
def top_performer(grouped_data):
    return max(grouped_data, key=grouped_data.get)


# ---------- MAIN ----------
def main():
    raw_data = load_data()

    if not raw_data:
        return

    sales_data = calculate_revenue(raw_data)

    print("\n--- SALES PERFORMANCE ANALYZER ---\n")

    print("Total Revenue:", total_revenue(sales_data))

    product_sales = group_by(sales_data, 1)
    print("\nRevenue by Product:")
    for k, v in product_sales.items():
        print(f"{k}: {v}")

    region_sales = group_by(sales_data, 2)
    print("\nRevenue by Region:")
    for k, v in region_sales.items():
        print(f"{k}: {v}")

    print("\nTop Selling Product:", top_performer(product_sales))
    print("Top Performing Region:", top_performer(region_sales))


if __name__ == "__main__":
    main()

