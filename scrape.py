import requests
import pandas as pd

url_list = [
    "https://www.marham.pk/api/lab/tests-optimized?lab_id=2",
    "https://www.marham.pk/api/lab/tests-optimized?lab_id=9",
    "https://www.marham.pk/api/lab/tests-optimized?lab_id=7",
    "https://www.marham.pk/api/lab/tests-optimized?lab_id=15",
    "https://www.marham.pk/api/lab/tests-optimized?lab_id=16",
    "https://www.marham.pk/api/lab/tests-optimized?lab_id=1",
    "https://www.marham.pk/api/lab/tests-optimized?lab_id=27",
    "https://www.marham.pk/api/lab/tests-optimized?lab_id=37",
    "https://www.marham.pk/api/lab/tests-optimized?lab_id=21",
    "https://www.marham.pk/api/lab/tests-optimized?lab_id=31"
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

save_test_data = []  # List to store all test data

for url in url_list:
    lab_id = url.split("lab_id=")[-1]
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        response_json = response.json()

        # Check if "tests" key is available
        if "tests" in response_json:
            lab_name = response_json.get("name")

            for test in response_json["tests"]:
                test_info = [
                    lab_id,                      # Lab ID
                    lab_name,                    # Lab Name
                    test.get("id"),             # Test ID
                    test.get("name"),           # Test Name
                    test.get("fee"),            # Fee
                    test.get("discount"),       # Discount
                    test.get("discountPercentage"), # Discount Percentage
                    test.get("discountedFee"),  # Discounted Fee
                    test.get("type")            # Test Type
                ]
                save_test_data.append(test_info)


df = pd.DataFrame(save_test_data, columns=[
    "Lab ID", "Lab Name", "Test ID", "Test Name", "Fee", "Discount", "Discount Percentage", "Discounted Fee", "Test Type"
])


df.to_csv("labs_test_data.csv")

print("Data saved successfully to 'lab_tests_data.csv'")