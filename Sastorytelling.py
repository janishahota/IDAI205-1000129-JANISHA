import pandas as pd

def clean_instagram_data(file_path, save_path):
    # Load dataset with correct encoding and explicit dtype handling
    df = pd.read_csv(file_path, encoding="ISO-8859-1", dtype=str, low_memory=False)

    # Remove leading/trailing spaces from column names
    df.columns = df.columns.str.strip()

    # Drop duplicate rows
    df = df.drop_duplicates()

    # Handle missing values (fill forward method)
    df.ffill(inplace=True)

    # Convert numerical columns to appropriate types
    numeric_cols = [
        "Impressions", "From Home", "From Hashtags", "From Explore", "From Other",
        "Saves", "Comments", "Shares", "Likes", "Profile Visits", "Follows"
    ]
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

    # Calculate total impressions
    df["Total Impressions"] = df["From Home"] + df["From Hashtags"] + df["From Explore"] + df["From Other"]

    # Calculate percentage of each source
    df["Home %"] = (df["From Home"] / df["Total Impressions"]) * 100
    df["Hashtags %"] = (df["From Hashtags"] / df["Total Impressions"]) * 100
    df["Explore %"] = (df["From Explore"] / df["Total Impressions"]) * 100
    df["Other %"] = (df["From Other"] / df["Total Impressions"]) * 100

    # Calculate engagement rates using the original Impressions column
    df["Like Rate"] = (df["Likes"] / df["Impressions"]) * 100
    df["Follow Rate"] = (df["Follows"] / df["Impressions"]) * 100
    df["Comment Rate"] = (df["Comments"] / df["Impressions"]) * 100
    df["Share Rate"] = (df["Shares"] / df["Impressions"]) * 100
    df["Save Rate"] = (df["Saves"] / df["Impressions"]) * 100

    # Save cleaned dataset
    df.to_csv(save_path, index=False)
    print(f"✅ Data cleaning complete! Saved as '{save_path}'.")

    return df

cleaned_df = clean_instagram_data("/Users/hota/Downloads/Instagram data.csv", "/Users/hota/Downloads/cleaned_instagram_data.csv")
