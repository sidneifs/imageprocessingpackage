"""
Script para ajustar o tamanho de natureza2.png para o mesmo de natureza1.png.
Salva a nova imagem como natureza2_ajustada.png na pasta images/.
"""
from skimage.io import imread, imsave #, imsave
from skimage.transform import resize #, resize
import os #, resize

img_dir = 'images/' # Diretório das imagens
img1_path = os.path.join(img_dir, 'natureza1.png') # Caminho da primeira imagem
img2_path = os.path.join(img_dir, 'natureza2.png') # Caminho da segunda imagem
img2_out = os.path.join(img_dir, 'natureza2_ajustada.png') # Caminho da imagem ajustada

# Leitura das imagens
img1 = imread(img1_path) # Leitura da primeira imagem
img2 = imread(img2_path) # Leitura da segunda imagem

# Redimensiona img2 para o shape de img1
img2_resized = resize(img2, img1.shape, anti_aliasing=True, preserve_range=True).astype(img1.dtype) # Mantém o tipo de dado original

# Salva imagem ajustada
imsave(img2_out, img2_resized) # Salva a imagem ajustada
print(f'Imagem ajustada salva em: {img2_out}') # Mensagem de confirmação
