import pandas as pd

df = pd.read_csv("labs_test_data.csv")

df = df.drop(columns=["Unnamed: 0"])

print(df.isnull().sum())

df.fillna({
    "Fee": 0,
    "Discount": 0,
    "Discount Percentage": 0,
    "Discounted Fee": 0,
    "Test Type": "Not Specified"
}, inplace=True)


df["Fee"] = pd.to_numeric(df["Fee"], errors='coerce').fillna(0)
df["Discount"] = pd.to_numeric(df["Discount"], errors='coerce').fillna(0)
df["Discount Percentage"] = pd.to_numeric(df["Discount Percentage"], errors='coerce').fillna(0)
df["Discounted Fee"] = pd.to_numeric(df["Discounted Fee"], errors='coerce').fillna(0)


df["Savings"] = df["Fee"] - df["Discounted Fee"]

df.drop_duplicates(inplace=True)


df = df.rename(columns={
    "Lab ID": "lab_id",
    "Lab Name": "lab_name",
    "Test ID": "test_id",
    "Test Name": "test_name",
    "Fee": "fee",
    "Discount": "discount",
    "Discount Percentage": "discount_percentage",
    "Discounted Fee": "discounted_fee",
    "Test Type": "test_type"
})


df.to_csv("lab_tests_data_cleaned.csv", index=False)
print("Transformed data saved to 'lab_tests_data_cleaned.csv'")
print("Data transformation completed successfully.")

