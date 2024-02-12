import os
import rembg  # rembg==2.0.40

def remove_background(input_path, output_path):
    with open(input_path, "rb") as input_file:
        input_data = input_file.read()

    output_data = rembg.remove(input_data)

    with open(output_path, "wb") as output_file:
        output_file.write(output_data)

def process_images_in_folder(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # List all files in the input folder
    input_files = os.listdir(input_folder)

    for input_file in input_files:
        # Check if the file is an image (you can add more checks if needed)
        if input_file.lower().endswith(('.png', '.jpg', '.jpeg')):
            # Construct input and output paths
            input_path = os.path.join(input_folder, input_file)
            output_path = os.path.join(output_folder, f"output_{input_file}")

            # Remove background
            remove_background(input_path, output_path)

# Replace 'your_input_folder' and 'your_output_folder' with your actual folder paths
input_folder_path = 'C:\\Users\\Usman\\Desktop\\Ez360 Images'
output_folder_path = 'C:\\Users\\Usman\\Desktop\\exterior 4'

# Process images in the folder
process_images_in_folder(input_folder_path, output_folder_path)

# import os
# import torch
# from torchvision import models, transforms
# from PIL import Image
# import numpy as np

# def remove_background(input_path, output_path):
#     # Load the DeepLabV3 model pre-trained on COCO dataset
#     model = models.segmentation.deeplabv3_resnet101(pretrained=True)
#     model.eval()

#     # Load the image
#     input_image = Image.open(input_path)

#     # Preprocess the image
#     preprocess = transforms.Compose([
#         transforms.ToTensor(),
#         transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
#     ])
#     input_tensor = preprocess(input_image)
#     input_batch = input_tensor.unsqueeze(0)

#     # Make prediction
#     with torch.no_grad():
#         output = model(input_batch)['out'][0]
#     output_predictions = output.argmax(0)

#     # Create a mask where background is 0 and foreground is 1
#     mask = (output_predictions != 0).float()

#     # Convert the mask to a PIL Image
#     mask_image = Image.fromarray((mask * 255).numpy().astype('uint8'), mode='L')

#     # Create a new image with a transparent background
#     result = Image.new("RGBA", input_image.size, (0, 0, 0, 0))
#     result.paste(input_image, mask=mask_image)

#     # Post-process to remove artifacts
#     result_array = np.array(result)
#     result_array[result_array[:, :, 3] < 128] = [0, 0, 0, 0]
#     result = Image.fromarray(result_array)

#     # Save the result as PNG
#     output_path, _ = os.path.splitext(output_path)
#     result.save(output_path + '.png')

# def process_images_in_folder(input_folder, output_folder):
#     # Create the output folder if it doesn't exist
#     os.makedirs(output_folder, exist_ok=True)

#     # List all files in the input folder
#     input_files = os.listdir(input_folder)

#     for input_file in input_files:
#         # Check if the file is an image (you can add more checks if needed)
#         if input_file.lower().endswith(('.png', '.jpg', '.jpeg')):
#             # Construct input and output paths
#             input_path = os.path.join(input_folder, input_file)
#             output_path = os.path.join(output_folder, f"output_{input_file}")

#             # Remove background
#             remove_background(input_path, output_path)

# # Replace 'your_input_folder' and 'your_output_folder' with your actual folder paths
# input_folder_path = 'C:\\Users\\Usman\\Desktop\\Ez360 Images'
# output_folder_path = 'C:\\Users\\Usman\\Desktop\\output_images'

# # Process images in the folder
# process_images_in_folder(input_folder_path, output_folder_path)