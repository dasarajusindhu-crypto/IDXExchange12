import pandas as pd

# assign variables for each sold dataset
sold2401 = pd.read_csv("data/raw/CRMLSSold202401.csv")   
sold2402 = pd.read_csv("data/raw/CRMLSSold202402.csv")
sold2403 = pd.read_csv("data/raw/CRMLSSold202403.csv")
sold2404 = pd.read_csv("data/raw/CRMLSSold202404.csv",
                    dtype={
                        "WaterfrontYN": "string",
                        "ElementarySchool": "string",
                        "BuilderName": "string",
                        "CoBuyerAgentFirstName": "string",
                        "PostalCode": "string"
                    }
                )
sold2405 = pd.read_csv("data/raw/CRMLSSold202405.csv")
sold2406 = pd.read_csv("data/raw/CRMLSSold202406.csv")
sold2407 = pd.read_csv("data/raw/CRMLSSold202407.csv")
sold2408 = pd.read_csv("data/raw/CRMLSSold202408.csv")
sold2409 = pd.read_csv("data/raw/CRMLSSold202409.csv")
sold2410 = pd.read_csv("data/raw/CRMLSSold202410.csv")
sold2411 = pd.read_csv("data/raw/CRMLSSold202411.csv")
sold2412 = pd.read_csv("data/raw/CRMLSSold202412.csv")
sold2501 = pd.read_csv("data/raw/CRMLSSold202501.csv")    
sold2502 = pd.read_csv("data/raw/CRMLSSold202502.csv")
sold2503 = pd.read_csv("data/raw/CRMLSSold202503.csv")
sold2504 = pd.read_csv("data/raw/CRMLSSold202504.csv")
sold2505 = pd.read_csv("data/raw/CRMLSSold202505.csv")
sold2506 = pd.read_csv("data/raw/CRMLSSold202506.csv",
                     dtype={
                        "WaterfrontYN": "string",
                        "ElementarySchool": "string",
                        "BuilderName": "string",
                        "CoBuyerAgentFirstName": "string",
                        "PostalCode": "string"
                    }
                )
sold2507 = pd.read_csv("data/raw/CRMLSSold202507.csv")
sold2508 = pd.read_csv("data/raw/CRMLSSold202508.csv")
sold2509 = pd.read_csv("data/raw/CRMLSSold202509.csv")
sold2510 = pd.read_csv("data/raw/CRMLSSold202510.csv")
sold2511 = pd.read_csv("data/raw/CRMLSSold202511.csv")
sold2512 = pd.read_csv("data/raw/CRMLSSold202512.csv")
sold2601 = pd.read_csv("data/raw/CRMLSSold202601.csv",    
                     dtype={
                        "WaterfrontYN": "string",
                        "ElementarySchool": "string",
                        "BuilderName": "string",
                        "CoBuyerAgentFirstName": "string",
                        "PostalCode": "string"
                    }
                )    
sold2602 = pd.read_csv("data/raw/CRMLSSold202602.csv")
sold2603 = pd.read_csv("data/raw/CRMLSSold202603.csv")

# verify row counts for residential properties              
#print("2401: " + str(sold41["PropertyType"].value_counts()))  # 11203 residential rows 01/24
#print("2402: " + str(sold42["PropertyType"].value_counts()))  # 13063 residential rows 02/24
#print("2403: " + str(sold43["PropertyType"].value_counts()))  # 20501 residential rows 03/24
#print("2404: " + str(sold44["PropertyType"].value_counts()))  # 24025 residential rows 04/24
#print("2405: " + str(sold45["PropertyType"].value_counts()))  # 25447 residential rows 05/24  
#print("2406: " + str(sold46["PropertyType"].value_counts()))  # 23310 residential rows 06/24
#print("2407: " + str(sold47["PropertyType"].value_counts()))  # 23019 residential rows 07/24
#print("2408: " + str(sold48["PropertyType"].value_counts()))  # 22215 residential rows 08/24
#print("2409: " + str(sold49["PropertyType"].value_counts()))  # 22257 residential rows 09/24
#print("2410: " + str(sold410["PropertyType"].value_counts())) # 21921 residential rows 10/24
#print("2411: " + str(sold411["PropertyType"].value_counts())) # 15108 residential rows 11/24
#print("2412: " + str(sold412["PropertyType"].value_counts())) # 10694 residential rows 12/24 
#print("2501: " + str(sold51["PropertyType"].value_counts()))  # 22690 residential rows 01/25
#print("2502: " + str(sold52["PropertyType"].value_counts()))  # 21930 residential rows 02/25
#print("2503: " + str(sold53["PropertyType"].value_counts()))  # 25104 residential rows 03/25
#print("2504: " + str(sold54["PropertyType"].value_counts()))  # 26695 residential rows 04/25
#print("2505: " + str(sold55["PropertyType"].value_counts()))  # 26438 residential rows 05/25
#print("2506: " + str(sold56["PropertyType"].value_counts()))  # 17056 residential rows 06/25
#print("2507: " + str(sold57["PropertyType"].value_counts()))  # 17194 residential rows 07/25
#print("2508: " + str(sold58["PropertyType"].value_counts()))  # 15658 residential rows 08/25
#print("2509: " + str(sold59["PropertyType"].value_counts()))  # 16859 residential rows 09/25
#print("2510: " + str(sold510["PropertyType"].value_counts())) # 17186 residential rows 10/25
#print("2511: " + str(sold511["PropertyType"].value_counts())) # 12194 residential rows 11/25
#print("2512: " + str(sold512["PropertyType"].value_counts())) # 10516 residential rows 12/25
#print("2601: " + str(sold61["PropertyType"].value_counts()))  # 22108 residential rows 01/26
#print("2602: " + str(sold62["PropertyType"].value_counts()))  # 19997 residential rows 02/26 
#print("2603: " + str(sold63["PropertyType"].value_counts()))  # 25564 residential rows 03/26 



sold = pd.concat([sold2401, sold2402, sold2403, sold2404, sold2405, sold2406, sold2407, sold2408, sold2409, sold2410, sold2411, sold2412,
                  sold2501, sold2502, sold2503, sold2504, sold2505, sold2506, sold2507, sold2508, sold2509, sold2510, sold2511, sold2512,
                  sold2601, sold2602, sold2603])

print(sold["PropertyType"].value_counts())          # 398011 Residential rows after concatenation

# filter sold dataset to only include residential properties
sold = sold[sold["PropertyType"] == "Residential"]
print(sold["PropertyType"].value_counts())          # 398011 Residential rows after filtering
sold.to_csv("data/residential_sold.csv", index=False) # save filtered sold dataset to CSV