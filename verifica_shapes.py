"""
Script para verificar o shape das imagens de natureza.
"""
from skimage.io import imread
import os

img_dir = 'images/' # Diretório das imagens
img1_path = os.path.join(img_dir, 'natureza1.png') # Caminho da primeira imagem
img2_path = os.path.join(img_dir, 'natureza2.png') # Caminho da segunda imagem
img2_ajustada_path = os.path.join(img_dir, 'natureza2_ajustada.png') # Caminho da imagem ajustada

img1 = imread(img1_path) # Leitura da primeira imagem
print(f"natureza1.png shape: {img1.shape}") # Exibe o shape da primeira imagem

if os.path.exists(img2_path): # Verifica se a segunda imagem existe
    img2 = imread(img2_path) # Leitura da segunda imagem
    print(f"natureza2.png shape: {img2.shape}") # Exibe o shape da segunda imagem
else:# Se a segunda imagem não existir
    print("natureza2.png não encontrado.") # Mensagem de erro

if os.path.exists(img2_ajustada_path): # Verifica se a imagem ajustada existe
    img2a = imread(img2_ajustada_path) # Leitura da imagem ajustada
    print(f"natureza2_ajustada.png shape: {img2a.shape}") # Exibe o shape da imagem ajustada
else: # Se a imagem ajustada não existir
    print("natureza2_ajustada.png não encontrado.") # Mensagem de erro