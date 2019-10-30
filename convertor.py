import csv

txt_file = open("nounlist.txt", "r")
csv_file = open("nounlist.csv", "w")
csv_writer = csv.writer(csv_file)

txt_str = txt_file.read().split("\n")

csv_writer.writerows([i] for i in txt_str)

txt_file.close()
csv_file.close()