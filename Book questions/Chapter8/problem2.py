import pandas as pd

data = {
    "Name": ["Ali", "Sara", "Omar", "Fatima"],
    "Age": [20, 22, 19, 21],
    "Score": [85, 92, 78, 95]
}
df = pd.DataFrame(data)

high_scorers = df[df["Score"] > 80]
print(high_scorers[["Name", "Score"]])