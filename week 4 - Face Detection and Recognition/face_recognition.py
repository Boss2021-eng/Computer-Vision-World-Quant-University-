# **AI Lab: Deep Learning for Computer Vision**
# **WorldQuant University**
#
#

# **Usage Guidelines**
#
# This file is licensed under Creative Commons Attribution-NonCommercial-
# NoDerivatives 4.0 International.
#
# You **can** :
#
#   * ✓ Download this file
#   * ✓ Post this file in public repositories
#
# You **must always** :
#
#   * ✓ Give credit to WorldQuant University for the creation of this file
#   * ✓ Provide a link to the license
#
# You **cannot** :
#
#   * ✗ Create derivatives or adaptations of this file
#   * ✗ Use this file for commercial purposes
#
# Failure to follow these guidelines is a violation of your terms of service and
# could lead to your expulsion from WorldQuant University and the revocation
# your certificate.
#
#

# Import needed libraries

# Load MTCNN, Resnet, and the embedding data

mtcnn = ...

resnet = ...
embedding_data = ...

resnet = resnet.eval()


# Fill in the locate_face function
def locate_faces(image):
    ...
    


# Fill in the determine_name_dist function
def determine_name_dist(cropped_image, threshold=0.9):
    ...
    


# Fill in the label_face function
def label_face(name, dist, box, axis):
    ...
    


# Fill in the add_labels_to_image function
def add_labels_to_image(image):
    ...


# This file © 2024 by WorldQuant University is licensed under CC BY-NC-ND 4.0.
