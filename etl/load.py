def load_data(df, output_path):
    """Save the DataFrame as a CSV file."""
    df.to_csv(output_path, index=False)