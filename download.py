import kaggle

kaggle.api.dataset_download_files('ignazio/sentinel2-crop-mapping', path='data/sentinel2', unzip=True)

print("Dataset downloaded and unzipped successfully.")