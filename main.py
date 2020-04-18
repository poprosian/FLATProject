import csv
from modify_csv import  modify
import plots

modify()


reviewData = []
with open("data/modified_reviews.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for line in reader:
        reviewData.append(line)




plots.plotHighestReviews(reviewData)
