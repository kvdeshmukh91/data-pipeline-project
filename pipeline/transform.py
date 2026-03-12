def transform_data(df):
    df = df.dropna()
    df["sepal_area"] = df["sepal_length"] * df["sepal_width"]
    return df