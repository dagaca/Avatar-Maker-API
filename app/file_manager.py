"""
This module manages file operations including saving generated images in the results folder.
"""
import os
import uuid
from PIL import Image
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def save_result_file(image: Image, suffix='.png') -> str:
    """
    Save the avatar image to the results folder located in the main directory (one level above app)
    and return the path.

    Args:
        image (PIL.Image): The generated avatar image.
        suffix (str): The file extension, default is '.png'.

    Returns:
        str: The path to the saved image in the results folder.
    """
    # Get the app's parent directory (one level above app)
    main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    # Get the results directory from .env file
    results_dir = os.getenv('RESULT_FOLDER', 'results')

    # Combine the main directory with the relative results path from .env
    full_results_dir = os.path.join(main_dir, results_dir)

    # Ensure the results folder exists
    os.makedirs(full_results_dir, exist_ok=True)

    # Generate a unique filename for the image
    file_name = f"avatar_{uuid.uuid4().hex}{suffix}"

    # Create the full file path
    file_path = os.path.join(full_results_dir, file_name)

    # Save the image to the results folder
    image.save(file_path, format='PNG')

    return file_path
