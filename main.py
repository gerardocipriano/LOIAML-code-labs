import cv2
import numpy as np

class ImageHelper:
    @staticmethod
    def read_color_image(path):
        """Reads a color image from disk given its path."""
        return cv2.imread(path, cv2.IMREAD_COLOR)
    
    @staticmethod
    def read_gray_image(path):
        """Reads a grayscale image from disk given its path."""
        return cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    
    @staticmethod
    def read_image(path):
        """Reads an image from disk unchanged given its path."""
        return cv2.imread(path, cv2.IMREAD_UNCHANGED)
    
    @staticmethod
    def save_image(image, name, extension, path):
        """Saves an image to disk given its name, extension, and path."""
        cv2.imwrite(f"{path}/{name}.{extension}", image)
    
    @staticmethod
    def get_image_info(image):
        """Returns all necessary information to describe an image."""
        height, width = image.shape[:2]
        channels = image.shape[2] if len(image.shape) == 3 else 1
        return height, width, channels
    
    
    @staticmethod
    def show_image(image, title="Image"):
        """Displays an image in a window with the given title."""
        cv2.imshow(title, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    @staticmethod
    def show_image_grid(images, rows, cols, title="Image Grid"):
        """Displays a grid of images in a window with the given title."""
        grid = np.zeros((rows*images[0].shape[0], cols*images[0].shape[1]), dtype=np.uint8)
        for i in range(rows):
            for j in range(cols):
                grid[i*images[0].shape[0]:(i+1)*images[0].shape[0],
                     j*images[0].shape[1]:(j+1)*images[0].shape[1]] = images[i*cols+j]
        cv2.imshow(title, grid)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    @staticmethod
    def swap_red_blue(image):
        """Swaps the red and blue channels of an RGB image."""
        return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    @staticmethod
    def swap_blue_red(image):
        """Swaps the blue and red channels of a BGR image."""
        return cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
    @staticmethod
    def get_channels(image):
        """Returns the list of channels in an image."""
        if len(image.shape) == 3:
            return ["Blue", "Green", "Red"] if image.shape[2] == 3 else ["Gray"]
        else:
            return ["Gray"]
    
    @staticmethod
    def get_channel(image, index):
        """Returns a specific channel of an image given its index (0-based)."""
        if len(image.shape) == 3:
            return image[:,:,index]
        else:
            return image
    
    @staticmethod
    def show_channel(image, index):
        """Displays a channel of an image given its index (0-based)."""
        ImageHelper.show_image(ImageHelper.get_channel(image, index), title=f"Channel {index}")
    
    @staticmethod
    def merge_channels(channels):
        """Merges multiple channels into a single image."""
        if len(channels) == 1:
            return channels[0]
        else:
            return cv2.merge(channels)
        
    @staticmethod
    def get_channels(image_path):
        """
        Restituisce la lista dei canali/piani presenti in un'immagine.

        Args:
        image_path (str): percorso dell'immagine.

        Returns:
        channels (list): lista dei canali/piani presenti nell'immagine.
        """
        image = cv2.imread(image_path)
        channels = cv2.split(image)
        return channels
    
    @staticmethod
    def get_channel(image_path, channel_index):
        """
        Restituisce uno specifico piano/canale dato l'indice.

        Args:
        image_path (str): percorso dell'immagine.
        channel_index (int): indice del canale/piano.

        Returns:
        channel (numpy.ndarray): matrice che rappresenta il canale/piano specificato.
        """
        image = cv2.imread(image_path)
        channels = cv2.split(image)
        channel = channels[channel_index]
        return channel
    
    @staticmethod
    def show_channel_with_values(image_path, channel_index):
        """
        Mostra un piano a video con i suoi valori all'interno di ogni pixel.

        Args:
        image_path (str): percorso dell'immagine.
        channel_index (int): indice del canale/piano.

        Returns:
        None
        """
        channel = ImageHelper.get_channel(image_path, channel_index)
        shape = channel.shape
        values = np.zeros(shape, dtype=np.uint8)
        for i in range(shape[0]):
            for j in range(shape[1]):
                value = channel[i][j]
                values[i][j] = value
        cv2.imshow('Channel with values', values)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    @staticmethod
    def merge_channels(channels):
        """
        Unisce più piani in un'unica immagine.

        Args:
        channels (list): lista dei canali/piani.

        Returns:
        merged_image (numpy.ndarray): matrice che rappresenta l'immagine ottenuta dalla fusione dei canali/piani.
        """
        merged_image = cv2.merge(channels)
        return merged_image
    


# Leggi un'immagine dal disco come "a colori"
image_path = "imgs/kitten.png"
image = ImageHelper.read_image(image_path)

# Usa il metodo describe per ottenere le informazioni sull'immagine
image_info= ImageHelper.get_image_info(image)
print(image_info)
ImageHelper.show_image(image)
ImageHelper.show_channel_with_values(image_path,1)


