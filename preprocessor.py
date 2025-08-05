def preprocess(df, region_df):
    # Merge region data
    df = df.merge(region_df, on='NOC', how='left')

    # Drop duplicates
    df.drop_duplicates(inplace=True)

    # One-hot encoding or label encoding not needed yet
    # Standardize column names
    df.rename(columns={'region': 'Region', 'Games': 'Edition'}, inplace=True)

    # Fill missing medals with empty
    df['Medal'] = df['Medal'].fillna('No Medal')

    # Remove rows with missing essential info
    df = df[df['Year'].notna() & df['Sport'].notna() & df['Season'].notna()]

    return df