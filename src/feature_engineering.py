import pandas as pd
from sklearn.preprocessing import LabelEncoder


def feature_engineering(input_path, output_path):

    df = pd.read_csv(input_path)

    columns_to_drop = [
        "EmployeeCount",
        "EmployeeNumber",
        "Over18",
        "StandardHours"
    ]

    df = df.drop(columns=columns_to_drop)

    df["Attrition"] = df["Attrition"].map({
        "No": 0,
        "Yes": 1
    })

    categorical_columns = df.select_dtypes(
        include="object"
    ).columns

    encoder = LabelEncoder()

    for col in categorical_columns:
        df[col] = encoder.fit_transform(df[col])

    df.to_csv(output_path, index=False)

    return df