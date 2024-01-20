import pandas as pd

roadster_df = pd.read_csv(
    r"F:\GUVI_DATA_SCIENCE\Project\Myntra-T-Shirt-Image-Extraction-Application\Datasets\roadster.csv"
)

frisker_df = pd.read_csv(
    r"F:\GUVI_DATA_SCIENCE\Project\Myntra-T-Shirt-Image-Extraction-Application\Datasets\frisker.csv"
)

hrx_df = pd.read_csv(
    r"F:\GUVI_DATA_SCIENCE\Project\Myntra-T-Shirt-Image-Extraction-Application\Datasets\hrx.csv"
)

wrogn_df = pd.read_csv(
    r"F:\GUVI_DATA_SCIENCE\Project\Myntra-T-Shirt-Image-Extraction-Application\Datasets\wrogn.csv"
)

tommy_hilfiger_df = pd.read_csv(
    r"F:\GUVI_DATA_SCIENCE\Project\Myntra-T-Shirt-Image-Extraction-Application\Datasets\tommy_hilfiger.csv"
)

myntra_dataset = pd.concat([roadster_df, frisker_df, hrx_df, wrogn_df, tommy_hilfiger_df], axis=0)

# Saving to a CSV file
myntra_dataset.to_csv(r'F:\GUVI_DATA_SCIENCE\Project\Myntra-T-Shirt-Image-Extraction-Application\Datasets\myntra_dataset.csv', index = False)