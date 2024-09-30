import csv,time

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds to execute.")
        return result
    return wrapper

#Make function to read the file but skip the header
def getDataInput(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        return list(reader)[1:]  # skip the header

#Make function to figure out the median
def getMedian(prices):
    prices = sorted(prices)
    n = len(prices)
    if n % 2 == 1:
        return prices[n // 2]
    else:
        return (prices[(n-1) // 2] + prices[n // 2]) / 2

#Make the main function
@timeit
def main():
    records = getDataInput("RealEstateData.csv")
    prices = []
    city_totals = {}
    property_type_totals = {}
    zip_code_totals = {}

    for record in records:
        city = record[1]           #city
        property_type = record[7]  #property type
        zip_code = record[2]       #zip code
        price = float(record[8])   #price

        prices.append(price)

        city_totals[city] = city_totals.get(city, 0) + price
        property_type_totals[property_type] = property_type_totals.get(property_type, 0) + price
        zip_code_totals[zip_code] = zip_code_totals.get(zip_code, 0) + price

    #print statement for main data
    print(f"Summary by Price")
    print(f"{'Minimum:':20} ${min(prices):,.2f}")
    print(f"{'Maximum:':20} ${max(prices):,.2f}")
    print(f"{'Sum:':20} ${sum(prices):,.2f}")
    print(f"{'Avg:':20} ${sum(prices) / len(prices):,.2f}")
    print(f"{'Median:':20} ${getMedian(prices):,.2f}")
    print(f"\nSummary by Property Type")

    #loops that will give me my values per catogory
    for key, value in property_type_totals.items():
        print(f"{key+':':20} ${value:,.2f}")
    print(f"\nSummary by City")
    for key, value in city_totals.items():
        print(f"{key+':':20} ${value:,.2f}")
    print(f"\nSummary by Zip Code")
    for key, value in zip_code_totals.items():
        print(f"{key+':':20} ${value:,.2f}")

if __name__ == "__main__":
    main()
