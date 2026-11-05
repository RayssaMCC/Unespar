import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import os
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import math

# --- 1. CONFIGURAÇÕES ---
# Define o diretório que contém as imagens
base_dir = 'BaseFolhas' 
IMG_SIZE = (150, 150)
BATCH_SIZE = 32
EPOCHS = 15

# --- 2. CRIAR DATASETS DE TREINO E TESTE ---
# Carrega o dataset de treinamento (80% dos dados)
train_ds = tf.keras.utils.image_dataset_from_directory(
    base_dir,
    validation_split=0.2, 
    subset="training",
    seed=123,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE
)

# Carrega o dataset de validação/teste (20% dos dados)
test_ds = tf.keras.utils.image_dataset_from_directory(
    base_dir,
    validation_split=0.2, 
    subset="validation",
    seed=123,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE
)

# Obtém o nome das classes a partir dos diretórios e conta o número total
class_names = train_ds.class_names
print("Classes encontradas:", class_names)
num_classes = len(class_names)

# --- 3. MOSTRAR 1 EXEMPLO DE CADA CLASSE ---
print("\nExibindo exemplos de imagens...")
plt.figure(figsize=(10, 10))
# Pega um lote (batch) de imagens do dataset de treino
for images, labels in train_ds.take(1):
    # Para cada classe, encontra a primeira imagem no lote que corresponde a ela
    for i in range(num_classes):
        # Encontra o índice da primeira imagem que tem o rótulo 'i'
        idx_list = np.where(labels.numpy() == i)[0]
        if len(idx_list) > 0:
            ax = plt.subplot(math.ceil(num_classes / 3), 3, i + 1)
            plt.imshow(images[idx_list[0]].numpy().astype("uint8"))
            plt.title(class_names[i])
            plt.axis("off")
plt.tight_layout()
plt.show()

# --- 4. OTIMIZAR DATASET PARA DESEMPENHO ---
AUTOTUNE = tf.data.AUTOTUNE
train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
test_ds = test_ds.prefetch(buffer_size=AUTOTUNE)

# --- 5. CRIAR MODELO LIVRE ---
model = tf.keras.Sequential([
    # Camada de entrada
    tf.keras.Input(shape=(150, 150, 3)), tf.keras.layers.Rescaling(1./255),
    # Bloco Convolucional 1
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', padding='same'),
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', padding='same'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    # Bloco Convolucional 2
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu', padding='same'),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu', padding='same'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    # Bloco Convolucional 3
    tf.keras.layers.Conv2D(128, (3, 3), activation='relu', padding='same'),
    tf.keras.layers.Conv2D(128, (3, 3), activation='relu', padding='same'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    # Bloco de Classificação
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    # Camada de Saída
    tf.keras.layers.Dense(num_classes, activation='softmax')
])

# Configurar otimizador e função de perda
optimizer = tf.keras.optimizers.Adam(learning_rate=0.0001)

model.compile(optimizer=optimizer,
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# --- 6. TREINAR MODELO ---
print("\n--- INICIANDO TREINAMENTO DO MODELO LIVRE ---")
history = model.fit(train_ds, validation_data=test_ds, epochs=EPOCHS)
print("--- TREINAMENTO CONCLUÍDO ---\n")

# --- 7. PLOTAR GRÁFICOS DE ACURÁCIA E PERDA ---
print("--- GERANDO GRÁFICOS DE TREINAMENTO ---")
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(EPOCHS)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Acurácia de Treino')
plt.plot(epochs_range, val_acc, label='Acurácia de Validação')
plt.legend(loc='lower right')
plt.title('Curva de Acurácia')
plt.xlabel('Épocas')
plt.ylabel('Acurácia')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Perda de Treino')
plt.plot(epochs_range, val_loss, label='Perda de Validação')
plt.legend(loc='upper right')
plt.title('Curva de Perda (Loss)')
plt.xlabel('Épocas')
plt.ylabel('Perda')
plt.show()

# --- 8. PREVER NO CONJUNTO DE TESTE E GERAR MATRIZ DE CONFUSÃO ---
print("--- CALCULANDO MATRIZ DE CONFUSÃO ---")
y_true = []
y_pred = []

# Itera sobre o conjunto de teste para obter as previsões e os rótulos verdadeiros
for images, labels in test_ds:
    preds = model.predict(images, verbose=0)
    y_true.extend(labels.numpy())
    y_pred.extend(np.argmax(preds, axis=1))

# Calcula a matriz de confusão
cm = confusion_matrix(y_true, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=class_names)

# Plota a matriz de confusão
fig, ax = plt.subplots(figsize=(9, 7))
disp.plot(cmap=plt.cm.Blues, ax=ax, xticks_rotation='vertical')
plt.title("Matriz de Confusão - Modelo Livre")
plt.tight_layout()
plt.show()

print("\n--- FIM DA EXECUÇÃO ---")