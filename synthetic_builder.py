import json
import os
import numpy as np
import cv2

class SyntheticBuilder:
    def __init__(self, config_path):
        with open(config_path, 'r') as f:
            self.config = json.load(f)
        self.output_dir = self.config['output_dir']
        self.training_dir = os.path.join(self.output_dir, 'training')
        self.test_dir = os.path.join(self.output_dir, 'test')
        self.validation_dir = os.path.join(self.output_dir, 'validation')
        os.makedirs(self.training_dir, exist_ok=True)
        os.makedirs(self.test_dir, exist_ok=True)
        os.makedirs(self.validation_dir, exist_ok=True)

    def build(self):
        for i in range(self.config['num_training']):
            synthetic_image, class_idx = self.create_synthetic_object()
            synthetic_image = self.apply_preprocessing(synthetic_image,class_idx)
            if self.config['save_on_disk']:
                if self.config['as_png']:
                    cv2.imwrite(os.path.join(self.training_dir, f'training_{i}.png'), synthetic_image)
                else:
                    np.save(os.path.join(self.training_dir, f'training_{i}.npy'), synthetic_image)

        for i in range(self.config['num_test']):
            synthetic_image, class_idx = self.create_synthetic_object()
            synthetic_image = self.apply_preprocessing(synthetic_image,class_idx)
            if self.config['save_on_disk']:
                if self.config['as_png']:
                    cv2.imwrite(os.path.join(self.test_dir, f'test_{i}.png'), synthetic_image)
                else:
                    np.save(os.path.join(self.test_dir, f'test_{i}.npy'), synthetic_image)

        for i in range(self.config['num_validation']):
            synthetic_image, class_idx = self.create_synthetic_object()
            synthetic_image = self.apply_preprocessing(synthetic_image,class_idx)
            if self.config['save_on_disk']:
                if self.config['as_png']:
                    cv2.imwrite(os.path.join(self.validation_dir, f'validation_{i}.png'), synthetic_image)
                else:
                    np.save(os.path.join(self.validation_dir, f'validation_{i}.npy'), synthetic_image)

    def create_synthetic_object(self):
        # Create a black background image
        synthetic_image = np.zeros((64, 64, 3), dtype=np.uint8)

        # Randomly choose one of the three classes
        class_idx = np.random.randint(3)

        if class_idx == 0:
            # Draw a green circle
            center = (np.random.randint(10, 54), np.random.randint(10, 54))
            radius = np.random.randint(5, 10)
            color = (0, 255, 0)
            cv2.circle(synthetic_image, center, radius, color, -1)
        elif class_idx == 1:
            # Draw a red triangle
            points = np.array([[[np.random.randint(10, 54), np.random.randint(10, 54)],
                                [np.random.randint(10, 54), np.random.randint(10, 54)],
                                [np.random.randint(10, 54), np.random.randint(10, 54)]]])
            color = (0, 0, 255)
            cv2.fillPoly(synthetic_image, points, color)
        else:
            # Draw a yellow square
            x1 = np.random.randint(10, 44)
            y1 = np.random.randint(10, 44)
            x2 = x1 + np.random.randint(10, 20)
            y2 = y1 + np.random.randint(10, 20)
            color = (0, 255, 255)
            cv2.rectangle(synthetic_image, (x1,y1), (x2,y2), color,-1)

        return synthetic_image,class_idx

    def apply_preprocessing(self,image,class_idx):
        if class_idx == 0:
            # Apply preprocessing to the green circle
            preprocessed_image = cv2.GaussianBlur(image,(5,5),0)
        elif class_idx == 1:
            # Apply preprocessing to the red triangle
            kernel = np.ones((5,5),np.uint8)
            preprocessed_image = cv2.erode(image,kernel,iterations = 1)
        else:
            # Apply preprocessing to the yellow square
            preprocessed_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

        return preprocessed_image
    
def main():
    # Load the configuration file
    with open('config.json', 'r') as f:
        config = json.load(f)

    # Create an instance of the SyntheticBuilder class
    builder = SyntheticBuilder('config.json')

    # Build the synthetic dataset
    builder.build()

if __name__ == '__main__':
    main()