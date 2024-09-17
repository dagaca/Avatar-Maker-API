# Avatar-Maker-API

The Personal Avatar Generation API allows users to create custom avatars based on their physical attributes or style preferences through text input. This API generates unique avatars based on the user's input and optimizes them for various platforms.

## Features

- **Avatar Creation**: Generate avatars based on user descriptions.
- **Background Color Customization**: Customize the avatar with a specified background color.
- **High Quality**: Produce realistic and detailed avatar images.

## Installation

### Requirements

- Python 3.x
- Flask==2.2.5
- Werkzeug==2.2.3
- flasgger==0.9.7.1
- python-dotenv==0.21.0
- Pillow==10.3.0
- requests==2.32.2

### Steps

1. **Clone the Repository:**

   ```bash
   git clone <repository_url>
   cd <repository_name>

2. **Install Dependencies:**

   '''bash
   pip install -r requirements.txt
   Set Up Environment Variables:

3. **Create a .env file with the following content:**

   ```bash
   RESULT_FOLDER=results
   LOG_DIR=logs
   LOG_FILE=app.log
   API_URL=https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev
   HUGGINGFACE_API_TOKEN=your_token_here

4. **Run the Application:**

   ```bash
   python run.py

## Usage
### Avatar Creation
The API allows you to create an avatar by sending a POST request as follows:

**Endpoint:**
   ```bash
   POST /generate_avatar
   ```

**Request Body:**
   ```bash
   {
     "description": "A young person with curly hair and glasses, wearing a blue jacket.",
     "background_color": "light blue"
   }
   ```

**description:** (string) A textual description for generating the avatar.
**background_color:** (string) The background color for the avatar.

**Response:**

Upon success, the generated avatar will be returned as a PNG file for download.

**Error Responses**
**400 Bad Request:** When required fields are missing or invalid.
**500 Internal Server Error:** When an unexpected error occurs on the server side.

## Avatar Gallery: Explore Unique Creations

Here are 10 unique avatars created using the Personal Avatar Generation API, each based on a distinct description and background color.

1. Description: "A futuristic astronaut floating in space, wearing a high-tech spacesuit with a visor reflecting the stars."
Background Color: "midnight blue"
![avatar_1](https://github.com/user-attachments/assets/b3fa13b7-5f85-452c-a161-dbf8e7b5d836)


2. Description: "A young woman in a vibrant floral dress, standing in a sunflower field with a wide-brimmed hat."
Background Color: "soft yellow"


3. Description: "A bold superhero with a flowing red cape and a mask, standing tall on a city rooftop at night."
Background Color: "dark purple"


4. Description: "A gentle forest elf with pointed ears, wearing a cloak made of leaves, standing among ancient trees."
Background Color: "forest green"


5. Description: "A chic businesswoman with short hair and glasses, holding a tablet, dressed in a black blazer."
Background Color: "light gray"


6. Description: "A young boy playing in the snow, bundled up in a bright red scarf and a wooly hat."
Background Color: "snow white"


7. Description: "An elegant ballerina in a white tutu, gracefully posing on a stage under soft golden lights."
Background Color: "soft gold"


8. Description: "A medieval knight in shining armor, holding a sword and shield, standing in front of a castle."
Background Color: "royal blue"


9. Description: "A retro-styled young man with a slicked-back hairstyle, wearing a leather jacket and sunglasses."
Background Color: "fiery orange"


10. Description: "A mystical sorceress with glowing hands, casting a spell, her long purple robe billowing around her."
Background Color: "twilight violet"

## Contributing
If you would like to contribute, please submit a pull request or open an issue on GitHub.
