import os
import zipfile


def unzip_folders(base_directory):
    """
    Unzips all folders in the specified directory into a new directory called 'unziped_data'.

    Parameters:
    base_directory (str): The directory containing the zipped folders.
    """
    unziped_data_directory = os.path.join(base_directory, 'unziped_data')

    # Create the 'unziped_data' directory if it doesn't exist
    os.makedirs(unziped_data_directory, exist_ok=True)

    # Iterate through each item in the base directory
    for item in os.listdir(base_directory):
        if item.endswith('.zip'):  # Check if the item is a zip file
            zip_path = os.path.join(base_directory, item)  # Full path to the zip file
            folder_name = item[:-4]  # Get the folder name without '.zip'
            extraction_path = os.path.join(unziped_data_directory, folder_name)  # Path for extraction

            # Create a new folder for extraction
            os.makedirs(extraction_path, exist_ok=True)

            # Unzip the folder
            try:
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(extraction_path)
                print(f"Unzipped '{item}' into '{extraction_path}'.")
            except zipfile.BadZipFile:
                print(f"Error: '{item}' is not a zip file or is corrupted.")
            except Exception as e:
                print(f"Error extracting '{item}': {e}")


# Example usage
base_directory = "C:\\Users\\kd0596\\Desktop\\2nd sem\\kim heejun"  # Change this to your actual path
unzip_folders(base_directory)


