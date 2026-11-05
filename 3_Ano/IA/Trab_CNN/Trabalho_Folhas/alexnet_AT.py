import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import os
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import math
import time
import io, contextlib # Para tirar mensagem do tensorflow ao carregar dataset

# --- CONFIGURAÇÕES GLOBAIS ---
BASE_DIR = 'BaseFolhas'
IMG_SIZE = (150, 150)

# --- FUNÇÕES AUXILIARES ---
def carregar_dataset(batch_size):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        raw_train_ds = tf.keras.utils.image_dataset_from_directory(
            BASE_DIR,
            validation_split=0.2,
            subset="training",
            seed=123,
            image_size=IMG_SIZE,
            batch_size=batch_size
        )
        raw_test_ds = tf.keras.utils.image_dataset_from_directory(
            BASE_DIR,
            validation_split=0.2,
            subset="validation",
            seed=123,
            image_size=IMG_SIZE,
            batch_size=batch_size
        )
    class_names = getattr(raw_train_ds, 'class_names', None)
    AUTOTUNE = tf.data.AUTOTUNE
    train_ds = raw_train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
    test_ds = raw_test_ds.cache().prefetch(buffer_size=AUTOTUNE)
    return train_ds, test_ds, class_names

def modelo_alexnet(num_classes, learning_rate):
    model = tf.keras.Sequential([
        tf.keras.Input(shape=(150,150,3)), tf.keras.layers.Rescaling(1./255),
        tf.keras.layers.Conv2D(96, kernel_size=(11, 11), strides=(4, 4), activation='relu'),
        tf.keras.layers.MaxPooling2D(pool_size=(3, 3), strides=(2, 2)),
        tf.keras.layers.Conv2D(256, kernel_size=(5, 5), padding='same', activation='relu'),
        tf.keras.layers.MaxPooling2D(pool_size=(3, 3), strides=(2, 2)),
        tf.keras.layers.Conv2D(384, kernel_size=(3, 3), padding='same', activation='relu'),
        tf.keras.layers.Conv2D(384, kernel_size=(3, 3), padding='same', activation='relu'),
        tf.keras.layers.Conv2D(256, kernel_size=(3, 3), padding='same', activation='relu'),
        tf.keras.layers.MaxPooling2D(pool_size=(3, 3), strides=(2, 2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(4096, activation='relu'),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(4096, activation='relu'),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(num_classes, activation='softmax')
    ])
    optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)
    model.compile(optimizer=optimizer,
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model

def construir_treinar_modelo(epochs, batch_size, learning_rate, num_classes, is_final_run=False):
    if not is_final_run:
        print(f"--- INICIANDO TESTE COM: LR={learning_rate}, BATCH={batch_size}, ÉPOCAS={epochs} ---")
    
    train_ds, test_ds, _ = carregar_dataset(batch_size)
    model = modelo_alexnet(num_classes, learning_rate)
    
    start_time = time.time()
    history = model.fit(train_ds, validation_data=test_ds, epochs=epochs, verbose=1)
    end_time = time.time()
    
    final_val_accuracy = max(history.history['val_accuracy'])
    
    if not is_final_run:
        print(f"--- TESTE CONCLUÍDO ---")
        print(f"Acurácia máxima de validação: {final_val_accuracy:.4f}")
        print(f"Tempo de treinamento: {end_time - start_time:.2f} segundos\n")
    
    # Retorna o modelo junto para a fase final
    return final_val_accuracy, history, model

def plotar_curvas_finais(history):
    """Gera os gráficos de acurácia e perda do treinamento final."""
    print("--- GERANDO GRÁFICOS DE ACURÁCIA E PERDA ---")
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    epochs_range = range(len(acc))

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

def plotar_matriz_confusao(model, test_ds, class_names):
    """Calcula e plota a matriz de confusão."""
    print("--- CALCULANDO MATRIZ DE CONFUSÃO ---")
    y_true = []
    y_pred = []
    for images, labels in test_ds:
        preds = model.predict(images, verbose=0)
        y_true.extend(labels.numpy())
        y_pred.extend(np.argmax(preds, axis=1))

    cm = confusion_matrix(y_true, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=class_names)

    fig, ax = plt.subplots(figsize=(9, 7))
    disp.plot(cmap=plt.cm.Blues, ax=ax, xticks_rotation='vertical')
    plt.title("Matriz de Confusão - Classificação de Folhas")
    plt.tight_layout()
    plt.show()

# --- SCRIPT PRINCIPAL DE AUTO-TUNING ---
_, _, class_names = carregar_dataset(32)
num_classes = len(class_names)


# --- FASE 1: TESTE DA TAXA DE APRENDIZADO (Learning Rate) ---
print("="*50)
print("FASE 1: AJUSTE DA TAXA DE APRENDIZADO")
print("="*50)
learning_rates_to_test = [0.01, 0.001, 0.0001]
batch_size_fixed = 32
epochs_fixed = 5 # Usar mais épocas para ter uma ideia melhor da curva
results_lr = {}
for lr in learning_rates_to_test:
    acc, _, _ = construir_treinar_modelo(epochs_fixed, batch_size_fixed, lr, num_classes)
    results_lr[lr] = acc
best_lr = max(results_lr, key=results_lr.get)
print(f"\n--- RESULTADO FASE 1 ---")
print(f"Resultados (LR: Acurácia): { {k: f'{v:.4f}' for k, v in results_lr.items()} }")
print(f"Melhor Taxa de Aprendizado: {best_lr}\n")


# --- FASE 2: TESTE DO TAMANHO DO BATCH (Batch Size) ---
print("="*50)
print("FASE 2: AJUSTE DO TAMANHO DO BATCH")
print("="*50)
batch_sizes_to_test = [16, 32, 64]
results_batch = {}
for bs in batch_sizes_to_test:
    acc, _, _ = construir_treinar_modelo(epochs_fixed, bs, best_lr, num_classes)
    results_batch[bs] = acc
best_batch_size = max(results_batch, key=results_batch.get)
print(f"\n--- RESULTADO FASE 2 ---")
print(f"Resultados (Batch Size: Acurácia): { {k: f'{v:.4f}' for k, v in results_batch.items()} }")
print(f"Melhor Tamanho de Batch: {best_batch_size}\n")


# --- FASE 3: TESTE DO NÚMERO DE ÉPOCAS ---
print("="*50)
print("FASE 3: AJUSTE DO NÚMERO DE ÉPOCAS")
print("="*50)
epochs_to_test = [5, 10, 15] # poucas épocas pois demora pra rodar
results_epochs = {}
for ep in epochs_to_test:
    acc, _, _ = construir_treinar_modelo(ep, best_batch_size, best_lr, num_classes)
    results_epochs[ep] = acc
best_epochs = max(results_epochs, key=results_epochs.get)
print(f"\n--- RESULTADO FASE 3 ---")
print(f"Resultados (Épocas: Acurácia): { {k: f'{v:.4f}' for k, v in results_epochs.items()} }")
print(f"Melhor Número de Épocas para o teste: {best_epochs}\n")

# --- CONCLUSÃO DO AUTO-TUNING ---
print("="*50)
print("AUTO-TUNING CONCLUÍDO")
print("="*50)
print(f"Melhor configuração encontrada:")
print(f"  - Taxa de Aprendizado: {best_lr}")
print(f"  - Tamanho do Batch: {best_batch_size}")
print(f"  - Número de Épocas: {best_epochs}")
print("\n")


# --- FASE 4: TREINAMENTO FINAL E AVALIAÇÃO COM OS MELHORES PARÂMETROS ---
print("="*50)
print("FASE 4: TREINAMENTO FINAL E AVALIAÇÃO")
print("="*50)
print("Iniciando treinamento final com a melhor configuração...")

# Treina o modelo final
final_accuracy, final_history, final_model = construir_treinar_modelo(
    epochs=best_epochs,
    batch_size=best_batch_size,
    learning_rate=best_lr,
    num_classes=num_classes,
    is_final_run=True # Flag para não imprimir mensagens de teste
)

print(f"\n--- TREINAMENTO FINAL CONCLUÍDO ---")
print(f"Acurácia máxima de validação alcançada: {final_accuracy:.4f}")

# Gera os gráficos de avaliação
plotar_curvas_finais(final_history)

# Recarrega o dataset de teste para garantir que não foi consumido
_, final_test_ds, _ = carregar_dataset(best_batch_size)
plotar_matriz_confusao(final_model, final_test_ds, class_names)

print("\n--- FIM DA EXECUÇÃO ---")