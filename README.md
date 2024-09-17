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

![avatar_1](https://github.com/user-attachments/assets/be6d73e3-270a-46a7-b846-b5f47a32d290)



2. Description: "A young woman in a vibrant floral dress, standing in a sunflower field with a wide-brimmed hat."

Background Color: "soft yellow"

![avatar_2](https://github.com/user-attachments/assets/2fed81e0-2bf7-4c48-a693-ce7f43f37755)



3. Description: "A bold superhero with a flowing red cape and a mask, standing tall on a city rooftop at night."

Background Color: "dark purple"

![avatar_3](https://github.com/user-attachments/assets/25414605-f0a5-4389-87b2-ce2ac3dc52eb)



4. Description: "A gentle forest elf with pointed ears, wearing a cloak made of leaves, standing among ancient trees."

Background Color: "forest green"

![avatar_4](https://github.com/user-attachments/assets/8cd452cb-a24b-4fab-bede-24953755b061)



5. Description: "A chic businesswoman with short hair and glasses, holding a tablet, dressed in a black blazer."

Background Color: "light gray"

![avatar (5)](https://github.com/user-attachments/assets/977dc4fe-cf62-4811-be56-c5a75968c13b)



6. Description: "A young boy playing in the snow, bundled up in a bright red scarf and a wooly hat."

Background Color: "snow white"

![avatar_6](https://github.com/user-attachments/assets/3ff60b18-444b-4bc6-8845-3c3cd1aeb542)



7. Description: "An elegant ballerina in a white tutu, gracefully posing on a stage under soft golden lights."

Background Color: "soft gold"

![avatar_7](https://github.com/user-attachments/assets/cd22504c-4ea4-4e8d-bb2c-eeeefa5c7568)



8. Description: "A medieval knight in shining armor, holding a sword and shield, standing in front of a castle."

Background Color: "royal blue"

![avatar_8](https://github.com/user-attachments/assets/c79047af-8d84-46ae-9ef6-1dc44582e6ef)



9. Description: "A retro-styled young man with a slicked-back hairstyle, wearing a leather jacket and sunglasses."

Background Color: "fiery orange"

![avatar_9](https://github.com/user-attachments/assets/fb026941-175e-4e6f-8336-dffcde5279e3)



10. Description: "A mystical sorceress with glowing hands, casting a spell, her long purple robe billowing around her."

Background Color: "twilight violet"

![avatar (10)](https://github.com/user-attachments/assets/7a280338-0ece-4717-b4eb-e30577348ffe)

## Postman Collection and Swagger UI

To help with API testing, we have included:

**Postman Collection:** A Postman collection file that contains all the endpoints of the API.
**Swagger UI:** Swagger UI is automatically generated for the API, making it easy to explore the available endpoints.

### Swagger UI
You can access the Swagger documentation at the following URL when the application is running:

   ```bash
   http://localhost:5000/apidocs/
   ```

Here is a screenshot of the Swagger UI interface:

![image](https://github.com/user-attachments/assets/c7c0d2e7-7a7e-47e2-9c23-d49826f77a39)


### Postman Collection
Download the Postman Collection from this repository to import into your Postman workspace for easier testing.

Postman Collection File: [Avatar-Maker-API Postman Collection](postman/Avatar-Maker-API.postman_collection.json)

## Contributing
If you would like to contribute, please submit a pull request or open an issue on GitHub.
