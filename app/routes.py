"""
This module contains the API routes for the Flask application.
Logging is handled within this file, while utility functions are imported.
"""
from flask import request, jsonify, send_file
from app import app
from app.avatar_generator import generate_avatar_from_description
from app.file_manager import save_result_file

@app.route('/health_check', methods=['GET'])
def health_check():
    """
    Health check endpoint to verify the API is running.
    ---
    summary: Health check
    responses:
      200:
        description: API is healthy
    """
    app.logger.info("Health check request received.")
    return "OK", 200

@app.route('/generate_avatar', methods=['POST'])
def generate_avatar():
    """
    Generate Avatar from Description
    ---
    summary: Generate a custom avatar image
    description: |
      This endpoint generates a custom avatar image based on the provided text description.
      The description should include details such as physical appearance or clothing style,
      and the system will return an avatar image representing that description.

    parameters:
      - in: body
        name: body
        description: JSON object containing the avatar description and background color.
        schema:
          type: object
          required:
            - description
            - background_color
          properties:
            description:
              type: string
              description: A textual description for generating the avatar (e.g., "A young person with glasses")
              example: "A young person with curly hair and glasses, 
                        wearing a blue jacket."
            background_color:
              type: string
              description: Background color for the avatar (e.g., "blue", "red").
              example: "light blue"
    
    responses:
      200:
        description: Returns the generated avatar image as a PNG file.
        content:
          image/png:
            schema:
              type: string
              format: binary
              description: The binary image content of the generated avatar.
      400:
        description: Bad request due to missing or invalid data in the request body.
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
                  example: "Description is required"
      500:
        description: Internal server error during avatar generation.
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
                  example: "Internal Server Error: An unexpected error occurred."

    """
    app.logger.info("Received request to generate avatar.")

    try:
        # Get the description and background color from the request body
        data = request.json
        description = data.get('description')
        background_color = data.get('background_color')

        if not description:
            app.logger.warning("No description provided.")
            return jsonify({"error": "Description is required"}), 400

        if not background_color:
            app.logger.warning("No background color provided.")
            return jsonify({"error": "Background color is required"}), 400

        # Generate avatar based on the description and background color
        avatar_image = generate_avatar_from_description(description, background_color)
        app.logger.info("Avatar created successfully.")

        # Save the avatar image to the results folder
        result_image_path = save_result_file(avatar_image)
        app.logger.info(f"Avatar saved at {result_image_path}.")

        # Send the file to the client
        return send_file(
            result_image_path,
            as_attachment=True,
            download_name="avatar.png",
            mimetype="image/png"
        )

    except ValueError as ve:
        app.logger.error(f"ValueError: {str(ve)}")
        return jsonify({"error": f"Bad Request: {str(ve)}"}), 400
    except KeyError as ke:
        app.logger.error(f"KeyError: {str(ke)}")
        return jsonify({"error": f"Bad Request: {str(ke)}"}), 400
    except Exception as e:
        app.logger.error(f"Unexpected error: {str(e)}")
        return jsonify({"error": f"Internal Server Error: {str(e)}"}), 500
