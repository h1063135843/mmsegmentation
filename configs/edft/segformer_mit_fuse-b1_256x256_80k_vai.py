_base_ = ['./segformer_mit_fuse-b0_256x256_80k_vai.py']

# model settings
model = dict(
    pretrained='pretrain/mit_b1.pth',
    backbone=dict(
        embed_dims=64,
        num_heads=[1, 2, 5, 8],
        num_layers=[2, 2, 2, 2],
        weight=0.4),
    decode_head=dict(in_channels=[64, 128, 320, 512]))
