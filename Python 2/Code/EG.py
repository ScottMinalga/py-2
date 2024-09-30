### Project: Lists and Real Estate Analyzer
### Name: Elizabeth Gallagher

def main():
    import csv
    listPrices = []  # List for all the prices
    getDataInput = (lambda f: [row for row in csv.reader(f)][1:])(open('RealEstateData.csv', 'r'))
    for record in getDataInput: record[8] = float(record[8]); listPrices.append(record[8])  # ;print(record)
    listPrices.sort()
    # for record in listPrices: print(record)

    # getMin() # Needs to be 1,551.00
    # print(f"{'Minimum:':20s} {(min(listPrices)):15,.2f}")

    # getMax() # Needs to be 884,790.00
    # print(f"{'Maximum:':20s} {(max(listPrices)):15,.2f}")

    # getSum() # Needs to be 230,632,100.00
    # print(f"{'Sum:':20s} {(sum(listPrices)):15,.2f}") # Works dont remove

    # lambda -> getAverage() # Needs to be 234,144.26
    # print(f"{'Average:':20s} {(lambda x, y: sum(x) / len(y)) (listPrices, listPrices):15,.2f}") # Works dont remove

    # lambda -> getMedian() # Needs to be 213,750.00
    # print(f"{'Median:':20s} {(lambda p: p[(((len(p) / 2) -1) (len(p) / 2)) // 2] if len(p) % 2 == 0 else p[len(p) // 2]) (listPrices):15,.2f}") # Works dont remove

    propertyResidential = []  # List for all the property types
    getDataInput = (lambda f: [row for row in csv.reader(f)][1:])(open('RealEstateData.csv', 'r'))
    for record in getDataInput: record[7] = (record[7]); propertyResidential.append(record[7])  # ;print(record)
    propertyResidential.sort()
    for record in propertyResidential: print(record)


main()