# RectGAN
The World's First Generative Adversarial Network that generates rectangular images.  Loosely based off of the [Keras-GAN-Animeface-Character](https://github.com/forcecore/Keras-GAN-Animeface-Character).

This is still a work in progress and many essential features are not supported and/or not adhering to best practices for GANs.  I'm no expert in GANs, but I've merely created RectGAN to make it easier to work with training and generating rectangular images, since the vast majority of image data that I have is in that format.

## Example:

I downloaded about 500 horizontal images of beaches [from Pixabay.com](http://pixabay.com), resized them all to 256x192, and trained my GAN for about 37,100 epochs to arrive at the following collage:

![](sample.jpg)

Although they're nowhere near the [photo-quality faces that Nvidia generated](https://research.nvidia.com/publication/2017-10_Progressive-Growing-of), it's by far the best I've been able to generate on my 4 GB Geforce GTX 960M using only about 500 images and training for roughly 24 hours.

