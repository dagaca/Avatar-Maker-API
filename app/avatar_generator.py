"""
This module contains utility functions for avatar generation.
"""
import os
import io
import requests
from PIL import Image
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API URL and Bearer token from environment variables
API_URL = os.getenv('API_URL')
HEADERS = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_TOKEN')}"}

def optimize_description(description: str, background_color: str) -> str:
    """
    Optimize the provided description by adding necessary attributes for avatar generation.

    Args:
        description (str): The original description for the avatar.
        background_color (str): The background color for the avatar.

    Returns:
        str: The optimized description.
    """
    base_attributes = [
        "high-quality rendering",
        "realistic features",
        "vibrant colors",
        "clear facial expressions",
        "engaging appearance"
    ]

    optimized_description = (
        f"{description}. "
        f"Ensure the avatar has {', '.join(base_attributes)}. "
        f"The background color should be {background_color}. "
    )

    return optimized_description

def generate_avatar_from_description(description: str, background_color: str) -> Image:
    """
    Create an avatar based on the provided description and background color after optimization.

    Args:
        description (str): The description for the avatar.
        background_color (str): The background color for the avatar.

    Returns:
        Image: The created avatar image.

    Raises:
        requests.exceptions.RequestException: For errors related to the API request.
        ValueError: If the API request fails or returns an unexpected result.
    """
    # Optimize the input description before sending it to the API
    optimized_description = optimize_description(description, background_color)
    payload = {"inputs": optimized_description}

    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload, timeout=120)
        response.raise_for_status()  # Raise an error for bad status codes
    except requests.exceptions.RequestException as e:
        raise ValueError(f"API request failed: {e}") from e

    image_bytes = response.content
    image = Image.open(io.BytesIO(image_bytes))
    return image
