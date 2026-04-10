# -*- coding: utf-8 -*-
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import os
from sklearn.model_selection import StratifiedKFold # <--- IMPORTANTE

# --- CONFIGURAÇÕES ---
base_dir = 'BaseFolhas'
IMG_SIZE = (150, 150)
BATCH_SIZE = 32
EPOCHS = 5
N_SPLITS = 5  # Número de "folds" para a Validação Cruzada

# 1. Carregar TODOS os caminhos de imagem e seus rótulos primeiro
print("--- INDEXANDO ARQUIVOS DE IMAGEM ---")
all_image_paths = []
all_labels = []
class_names = sorted([d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))])
class_map = {name: i for i, name in enumerate(class_names)}

for class_name in class_names:
    class_dir = os.path.join(base_dir, class_name)
    for filepath in os.listdir(class_dir):
        all_image_paths.append(os.path.join(class_dir, filepath))
        all_labels.append(class_map[class_name])

# Converter para arrays numpy para o Scikit-learn
all_image_paths = np.array(all_image_paths)
all_labels = np.array(all_labels)
print(f"Encontradas {len(all_image_paths)} imagens em {len(class_names)} classes.")


# Função para carregar e pré-processar uma imagem a partir do caminho
def load_and_preprocess_image(path, label):
    image = tf.io.read_file(path)
    image = tf.io.decode_jpeg(image, channels=3)
    image = tf.image.resize(image, IMG_SIZE)
    return image, label

# Função para criar o modelo (precisamos criar um novo a cada fold) 
def create_model(num_classes):
    model = tf.keras.Sequential([
        tf.keras.layers.Rescaling(1./255, input_shape=(150, 150, 3)),
        tf.keras.layers.Conv2D(6, kernel_size=(5, 5), activation='sigmoid', padding='same'),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
        tf.keras.layers.Conv2D(16, kernel_size=(5, 5), activation='sigmoid'),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(120, activation='sigmoid'),
        tf.keras.layers.Dense(84, activation='sigmoid'),
        tf.keras.layers.Dense(num_classes, activation='softmax')
    ])
    optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
    model.compile(optimizer=optimizer,
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model

# 2. Configurar a Validação Cruzada Estratificada
skf = StratifiedKFold(n_splits=N_SPLITS, shuffle=True, random_state=42)
fold_accuracies = []

# 3. Loop de treinamento para cada fold
print(f"\n--- INICIANDO VALIDAÇÃO CRUZADA DE {N_SPLITS} FOLDS ---")
for fold, (train_indices, val_indices) in enumerate(skf.split(all_image_paths, all_labels)):
    print(f"\n--- TREINANDO FOLD {fold + 1}/{N_SPLITS} ---")

    # Separar os dados do fold atual
    train_paths, val_paths = all_image_paths[train_indices], all_image_paths[val_indices]
    train_labels, val_labels = all_labels[train_indices], all_labels[val_indices]

    # Criar datasets do TensorFlow para este fold
    train_ds = tf.data.Dataset.from_tensor_slices((train_paths, train_labels))
    val_ds = tf.data.Dataset.from_tensor_slices((val_paths, val_labels))

    # Aplicar pré-processamento e otimizações
    AUTOTUNE = tf.data.AUTOTUNE
    train_ds = train_ds.map(load_and_preprocess_image, num_parallel_calls=AUTOTUNE).cache().shuffle(buffer_size=len(train_paths)).batch(BATCH_SIZE).prefetch(buffer_size=AUTOTUNE)
    val_ds = val_ds.map(load_and_preprocess_image, num_parallel_calls=AUTOTUNE).cache().batch(BATCH_SIZE).prefetch(buffer_size=AUTOTUNE)

    # Criar um novo modelo para este fold
    model = create_model(len(class_names))

    # Treinar o modelo
    history = model.fit(train_ds, validation_data=val_ds, epochs=EPOCHS, verbose=1)

    # Salvar a acurácia de validação final deste fold
    final_val_accuracy = history.history['val_accuracy'][-1]
    fold_accuracies.append(final_val_accuracy)
    print(f"Acurácia de validação para o Fold {fold + 1}: {final_val_accuracy:.4f}")

# 4. Calcular e exibir os resultados finais
print("\n\n--- RESULTADOS FINAIS DA VALIDAÇÃO CRUZADA ---")
print(f"Acurácias de cada fold: {[f'{acc:.4f}' for acc in fold_accuracies]}")
print(f"Acurácia Média: {np.mean(fold_accuracies):.4f}")
print(f"Desvio Padrão: {np.std(fold_accuracies):.4f}")