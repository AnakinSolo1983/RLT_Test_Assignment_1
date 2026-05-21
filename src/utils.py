import pandas as pd             # Import pandas.
import matplotlib.pyplot as plt # Import matplotlib.

# Plot the document length histogram:
def document_length_histogram(csv_path):

    df = pd.read_csv(csv_path) # Read the CSV file.

    lengths = df["clean_text"].apply(len) # Get the document lengths.

    plt.figure(figsize=(10, 6)) # Set the figure size.

    plt.hist(lengths, bins=20) # Plot the histogram.

    plt.xlabel("Document Length") # Set the x-axis label.
    plt.ylabel("Count") # Set the y-axis label.

    # Set the title:
    plt.title(
        "Distribution of Document Lengths"
    )

    plt.show() # Show the plot.