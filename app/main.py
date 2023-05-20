from app.classes.image_processing import ImageProcessing
from app.classes.image_conversion import ImageConversion
from app.classes.sound import SoundEngine
from app.classes.output_interface import OutputInterface
from app.utils.image import write_image, get_image_name
from app.utils.constants import TEXT_FILE_PATH, IMAGE_NAME
from app.services.computer_vision import get_photo_description

sound_engine = SoundEngine("man", TEXT_FILE_PATH)
image_processing = ImageProcessing()
interface = OutputInterface("800x600")
image_conversion = ImageConversion()


capture = image_conversion.take_picture()

def update_frame():
    frame = image_conversion.get_frame()

    if frame is not None:
        image_conversion.convert_opencv_to_pillow_image()
        processed_photo =  image_conversion.processed_photo
        
        interface.update_frame(processed_photo)

        image_name = get_image_name(IMAGE_NAME)
        write_image(image_name, frame)
        print("Screenshot taken")
        
        description = get_photo_description('.jpg', frame)
        description_from_text = image_processing.read_text_in_image(image_name)
   
        if description_from_text:
            description = "Text in front of you " + description_from_text 
            interface.update_label(description)
        

        sound_engine.say_text_outloud(description)
        interface.update_label(description)

    interface.schedule_next_update(update_frame)

update_frame()

interface.run()