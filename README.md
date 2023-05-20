# Class companion

This project was made for my university to help visually impaired students to be better aware of their surroundings.

## How to use

1. First you'll have to set up a few Cognitive Services on Azure.

   - Computer vision
   - Speech service
   - Translator

   Now that you have them you can build a config.json with the following structure:

   ```
    {
    "credentials": {
    "vision": {
      "subskey": "your-key",
      "endpoint": "your-enpdoint"
            },
        }
    }
   ```

2. Install dependencies:

   > pip install -r requirements.txt

3. Run project:

   > python3 -m app.main
