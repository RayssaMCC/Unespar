# ESTE CÓDIGO VAI LER DE UMA PASTA E SALVAR AS IMAGENS AUMENTADAS EM OUTRA
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array, save_img
import numpy as np
import os

# --- CONFIGURAÇÕES ---
# 1. Defina a pasta com as imagens que precisam ser aumentadas
PASTA_ENTRADA = 'Potato___healthy'

# 2. Defina o nome da nova pasta onde as imagens aumentadas serão salvas
PASTA_SAIDA = 'Potato___healthy_aumentado'

# 3. Defina o número total de imagens que você deseja no final
TOTAL_IMAGENS_DESEJADO = 1000
# --- FIM DAS CONFIGURAÇÕES ---


# Cria o gerador de imagens com as transformações (data augmentation)
datagen = ImageDataGenerator(
    rotation_range=30,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    brightness_range=[0.8, 1.2],
    fill_mode='nearest'
)

def aumentar_categoria_especifica():
    """
    Lê imagens de uma pasta de categoria específica, aplica data augmentation
    e salva os novos arquivos em uma nova pasta.
    """
    print(f"Iniciando aumento de dados para a categoria '{PASTA_ENTRADA}'...")

    # Cria a pasta de saída se ela não existir
    if not os.path.exists(PASTA_SAIDA):
        os.makedirs(PASTA_SAIDA)
        print(f"Pasta de saída '{PASTA_SAIDA}' criada com sucesso.")

    # Lista as imagens na pasta de entrada
    arquivos_originais = [f for f in os.listdir(PASTA_ENTRADA) if f.endswith(('.png', '.JPG', '.jpeg'))]
    num_originais = len(arquivos_originais)

    if num_originais == 0:
        print(f"ERRO: Nenhuma imagem encontrada na pasta '{PASTA_ENTRADA}'.")
        return

    print(f"Encontradas {num_originais} imagens originais.")

    # Copia as imagens originais para a pasta de destino
    for arquivo in arquivos_originais:
        caminho_original = os.path.join(PASTA_ENTRADA, arquivo)
        caminho_destino = os.path.join(PASTA_SAIDA, arquivo)
        tf.io.gfile.copy(caminho_original, caminho_destino, overwrite=True)
    print(f"{num_originais} imagens originais copiadas para '{PASTA_SAIDA}'.")

    # Calcula quantas imagens precisam ser geradas
    num_a_gerar = TOTAL_IMAGENS_DESEJADO - num_originais

    if num_a_gerar <= 0:
        print("O número de imagens desejado já foi atingido. Nenhuma imagem nova será gerada.")
        return

    print(f"É necessário gerar {num_a_gerar} novas imagens para atingir a meta de {TOTAL_IMAGENS_DESEJADO}.")

    # Loop para gerar imagens até atingir o total
    imagens_geradas = 0
    while imagens_geradas < num_a_gerar:
        for nome_arquivo in arquivos_originais:
            if imagens_geradas >= num_a_gerar:
                break 

            caminho_completo = os.path.join(PASTA_ENTRADA, nome_arquivo)
            imagem = load_img(caminho_completo)
            array_imagem = img_to_array(imagem)
            array_imagem = np.expand_dims(array_imagem, axis=0)

            iterator = datagen.flow(array_imagem, batch_size=1)
            batch = next(iterator)
            imagem_aumentada = batch[0].astype('uint8')
            
            nome_base, extensao = os.path.splitext(nome_arquivo)
            novo_nome = f"{nome_base}_aug_{imagens_geradas + 1}{extensao}"
            caminho_salvar = os.path.join(PASTA_SAIDA, novo_nome)

            save_img(caminho_salvar, imagem_aumentada)
            imagens_geradas += 1

    print(f"\nProcesso concluído! {imagens_geradas} novas imagens foram geradas.")
    total_final = len(os.listdir(PASTA_SAIDA))
    print(f"A pasta '{PASTA_SAIDA}' agora contém {total_final} imagens.")


if __name__ == '__main__':
    aumentar_categoria_especifica()