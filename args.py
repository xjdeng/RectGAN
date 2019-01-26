#!/usr/bin/env python3

class Args :
    # dataset size... Use positive number to sample subset of the full dataset.
    dataset_sz = -1

    # Archive outputs of training here for animating later.
    anim_dir = "anim"
    
    data_dir = "j:/hep/sk/done_front/"
    
    """
    
    Supported aspect ratios:
        
    1:4 - 64x256 
    1:2 - 64x128, 128x256
    9:16 - 144x256
    3:4 - 192x256, 96x128
    2:3 - 128x192, 64x96
    1:1 - 64x64, 128x128, 256x256
    3:2 - 192x128, 96x64
    4:3 - 256x192, 128x96
    16:9 - 256x144
    2:1 - 128x64, 256x128
    4:1 - 256x64
    
    Make sure w and h below reflect one of the supported aspect ratios above!
    Aspect ratios are in the form w x h
    
    """

    w = 256
    h = 192
    
    
    # alpha, used by leaky relu of D and G networks.
    #alpha_D = 0.2
    #alpha_G = 0.2
    alpha_D = 0.2
    alpha_G = 0.2
    
    d_lr = 0.0002
    g_lr = d_lr/2

    # batch size, during training.
    #batch_sz = 16
    batch_sz = 16
    
    batch_len = 100

    # Length of the noise vector to generate the faces from.
    # Latent space z
    noise_shape = (1, 1, 8)
    #noise_shape = (1, 1, 8)

    # GAN training can be ruined any moment if not careful.
    # Archive some snapshots in this directory.
    snapshot_dir = "./snapshots"

    # dropout probability
    dropout = 0.0


    # noisy label magnitude
    #label_noise = 0.1
    label_noise = 0.1

    # history to keep. Slower training but higher quality.
    #history_sz = 8
    history_sz = 8

    genw = "gen.hdf5"
    discw = "disc.hdf5"

    # Weight initialization function.
    #kernel_initializer = 'Orthogonal'
    #kernel_initializer = 'RandomNormal'
    # Same as default in Keras, but good for GAN, says
    # https://github.com/gheinrich/DIGITS-GAN/blob/master/examples/weight-init/README.md#experiments-with-lenet-on-mnist
    kernel_initializer = 'glorot_uniform'

    # Since DCGAN paper, everybody uses 0.5 and for me, it works the best too.
    # I tried 0.9, 0.1.
    #adam_beta = 0.5
    adam_beta = 0.5

    # BatchNormalization matters too.
    bn_momentum = 0.3
