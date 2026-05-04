import pandas as pd

# assign each csv file to a variable
listing2401 = pd.read_csv("data/raw/CRMLSListing202401.csv")
listing2402 = pd.read_csv("data/raw/CRMLSListing202402.csv")     
listing2403 = pd.read_csv("data/raw/CRMLSListing202403.csv")
listing2404 = pd.read_csv("data/raw/CRMLSListing202404.csv")
listing2405 = pd.read_csv("data/raw/CRMLSListing202405.csv")
listing2406 = pd.read_csv("data/raw/CRMLSListing202406.csv")
listing2407 = pd.read_csv("data/raw/CRMLSListing202407.csv")
listing2408 = pd.read_csv("data/raw/CRMLSListing202408.csv")
listing2409 = pd.read_csv("data/raw/CRMLSListing202409.csv")
listing2410 = pd.read_csv("data/raw/CRMLSListing202410.csv")
listing2411 = pd.read_csv("data/raw/CRMLSListing202411.csv")
listing2412 = pd.read_csv("data/raw/CRMLSListing202412.csv")
listing2501 = pd.read_csv("data/raw/CRMLSListing202501.csv")    
listing2502 = pd.read_csv("data/raw/CRMLSListing202502.csv")
listing2503 = pd.read_csv("data/raw/CRMLSListing202503.csv")
listing2504 = pd.read_csv("data/raw/CRMLSListing202504.csv")
listing2505 = pd.read_csv("data/raw/CRMLSListing202505.csv")
listing2506 = pd.read_csv("data/raw/CRMLSListing202506.csv")
listing2507 = pd.read_csv("data/raw/CRMLSListing202507.csv")
listing2508 = pd.read_csv("data/raw/CRMLSListing202508.csv")
listing2509 = pd.read_csv("data/raw/CRMLSListing202509.csv")
listing2510 = pd.read_csv("data/raw/CRMLSListing202510.csv")
listing2511 = pd.read_csv("data/raw/CRMLSListing202511.csv")
listing2512 = pd.read_csv("data/raw/CRMLSListing202512.csv")
listing2601 = pd.read_csv("data/raw/CRMLSListing202601.csv")  
listing2602 = pd.read_csv("data/raw/CRMLSListing202602.csv")
listing2603 = pd.read_csv("data/raw/CRMLSListing202603.csv")

# verify row counts                 
print("2401: " + str(listing2401["PropertyType"].value_counts()))   #17007 residential rows 01/24
print("2402: " + str(listing2402["PropertyType"].value_counts()))   #17490 residential rows 02/24
print("2403: " + str(listing2403["PropertyType"].value_counts()))   #20501 residential rows 03/24
print("2404: " + str(listing2404["PropertyType"].value_counts()))   #24025 residential rows 04/24
print("2405: " + str(listing2405["PropertyType"].value_counts()))   #25447 residential rows 05/24
print("2406: " + str(listing2406["PropertyType"].value_counts()))   #23310 residential rows 06/24
print("2407: " + str(listing2407["PropertyType"].value_counts()))   #23019 residential rows 07/24
print("2408: " + str(listing2408["PropertyType"].value_counts()))   #22215 residential rows 08/24
print("2409: " + str(listing2409["PropertyType"].value_counts()))   #22257 residential rows 09/24
print("2410: " + str(listing2410["PropertyType"].value_counts())) #21921 residential rows 10/24
print("2411: " + str(listing2411["PropertyType"].value_counts())) #15108 residential rows 11/24
print("2412: " + str(listing2412["PropertyType"].value_counts())) #10694 residential rows 12/24
print("2501: " + str(listing2501["PropertyType"].value_counts()))   #22690 residential rows 01/25
print("2502: " + str(listing2502["PropertyType"].value_counts()))   #21930 residential rows 02/25
print("2503: " + str(listing2503["PropertyType"].value_counts()))   #25104 residential rows 03/25
print("2504: " + str(listing2504["PropertyType"].value_counts()))   #26695 residential rows 04/25
print("2505: " + str(listing2505["PropertyType"].value_counts()))   #26438 residential rows 05/25
print("2506: " + str(listing2506["PropertyType"].value_counts()))   #17056 residential rows 06/25
print("2507: " + str(listing2507["PropertyType"].value_counts()))   #17194 residential rows 07/25
print("2508: " + str(listing2508["PropertyType"].value_counts()))   #15658 residential rows 08/25
print("2509: " + str(listing2509["PropertyType"].value_counts()))   #16859 residential rows 09/25
print("2510: " + str(listing2510["PropertyType"].value_counts())) #17186 residential rows 10/25
print("2511: " + str(listing2511["PropertyType"].value_counts())) #12194 residential rows 11/25
print("2512: " + str(listing2512["PropertyType"].value_counts())) #10516 residential rows 12/25
print("2601: " + str(listing2601["PropertyType"].value_counts()))   #22108 residential rows 01/26
print("2602: " + str(listing2602["PropertyType"].value_counts()))   #19997 residential rows 02/26
print("2603: " + str(listing2603["PropertyType"].value_counts()))   #25564 residential rows 03/26

listing = pd.concat([listing2401, listing2402, listing2403, listing2404, listing2405, listing2406, listing2407, listing2408, listing2409, listing2410, listing2411, listing2412,
                     listing2501, listing2502, listing2503, listing2504, listing2505, listing2506,  listing2507, listing2508, listing2509, listing2510, listing2511, listing2512,
                     listing2601, listing2602, listing2603])

print(listing["PropertyType"].value_counts())           # 540135 Residential rows after concatenation
print(listing.head())

# filter listing dataset to only include residential properties
listing = listing[listing["PropertyType"] == "Residential"]
print(listing["PropertyType"].value_counts())           # 540135 Residential rows after filtering
listing.to_csv("data/residential_listings.csv", index=False)  # save filtered listings dataset to CSV