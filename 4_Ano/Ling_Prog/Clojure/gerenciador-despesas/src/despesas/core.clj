
(ns despesas.core
  (:import [java.math BigDecimal]
           [java.time LocalDate]
           [java.time.format DateTimeFormatter]))

;; ==========================================
;; CONFIGURACOES E CONVERSAO DE DATAS
;; ==========================================

;; Define o formato de data utilizado no sistema
(def formato-data
  (DateTimeFormatter/ofPattern "dd-MM-uuuu"))

;; Converte uma data de texto para o formato LocalDate
(defn converter-data [data]
  (LocalDate/parse data formato-data))


;; ==========================================
;; DADOS INICIAIS
;; ==========================================

;; Vetor com algumas despesas para iniciar o sistema
(def despesas-iniciais
  [{:descricao "Mercado"
    :categoria "Alimentacao"
    :valor 350.00M
    :data "02-11-2026"}

   {:descricao "Combustivel"
    :categoria "Transporte"
    :valor 180.00M
    :data "05-11-2026"}

   {:descricao "Cinema"
    :categoria "Lazer"
    :valor 65.00M
    :data "10-11-2026"}

   {:descricao "Restaurante"
    :categoria "Alimentacao"
    :valor 90.00M
    :data "12-11-2026"}

   {:descricao "Onibus"
    :categoria "Transporte"
    :valor 25.00M
    :data "15-11-2026"}])


;; ==========================================
;; CADASTRO DE DESPESAS
;; ==========================================

;; Adiciona uma nova despesa sem alterar o vetor original
(defn adicionar-despesa
  [despesas descricao categoria valor data]

  (conj despesas
        {:descricao descricao
         :categoria categoria
         :valor valor
         :data data}))


;; ==========================================
;; LISTAGEM E FILTROS
;; ==========================================

;; Percorre e exibe todas as despesas cadastradas
(defn listar-despesas [despesas]
  (doseq [despesa despesas]
    (println despesa)))

;; Exibe os resultados ou informa quando nao existem registros
(defn exibir-resultados [despesas]
  (if (empty? despesas)
    (println "Nenhuma despesa encontrada.")
    (listar-despesas despesas)))

;; Retorna somente as despesas de uma categoria
(defn filtrar-categoria
  [despesas categoria]

  (filter
   #(= (:categoria %) categoria)
   despesas))

;; Retorna despesas dentro de um intervalo de datas
(defn filtrar-periodo
  [despesas inicio fim]

  (let [data-inicio (converter-data inicio)
        data-fim (converter-data fim)]

    (filter
     #(let [data-despesa (converter-data (:data %))]
        (and
         (not (.isBefore data-despesa data-inicio))
         (not (.isAfter data-despesa data-fim))))
     despesas)))

;; Retorna despesas com valor igual ou superior ao mínimo
(defn filtrar-valor-minimo
  [despesas valor-minimo]

  (filter
   #(>= (:valor %) valor-minimo)
   despesas))


;; ==========================================
;; CALCULOS FINANCEIROS
;; ==========================================

;; Soma os valores de todas as despesas
(defn calcular-total [despesas]

  (reduce
   + 0M
   (map :valor despesas)))

;; Calcula a media dos valores das despesas
(defn calcular-media [despesas]

  (if (empty? despesas)
    0M
    (/ (calcular-total despesas)
       (count despesas))))

;; Identifica a despesa de maior valor
(defn maior-despesa [despesas]

  (when (seq despesas)
    (apply max-key :valor despesas)))


;; ==========================================
;; RELATORIOS E RESUMO FINANCEIRO
;; ==========================================

;; Agrupa as despesas por categoria e calcula os totais
(defn total-por-categoria [despesas]

  (->> despesas
       (group-by :categoria)
       (map (fn [[categoria itens]]
              {:categoria categoria
               :total (calcular-total itens)}))
       (sort-by :total >)))

;; Reune as principais informacoes financeiras
(defn gerar-resumo [despesas]

  {:quantidade (count despesas)
   :total (calcular-total despesas)
   :media (calcular-media despesas)
   :maior-despesa (maior-despesa despesas)
   :categorias (total-por-categoria despesas)})


;; ==========================================
;; INTERFACE E MENU PRINCIPAL
;; ==========================================

;; Exibe as opcoes disponiveis para o usuario
(defn exibir-menu []

  (println "\n===== GERENCIADOR DE DESPESAS =====")
  (println "1 - Listar despesas")
  (println "2 - Cadastrar despesa")
  (println "3 - Filtrar por categoria")
  (println "4 - Filtrar por periodo")
  (println "5 - Filtrar por valor minimo")
  (println "6 - Consultar total de gastos")
  (println "7 - Relatorio por categoria")
  (println "8 - Resumo financeiro")
  (println "0 - Sair")
  (print "Escolha uma opcao: ")
  (flush))


;; Controla as opcoes do sistema e atualiza as despesas
(defn menu [despesas]

  (exibir-menu)

  (let [opcao (read-line)]

    (case opcao

      ;; Opcao 1: lista todas as despesas
      "1"
      (do
        (println "\n--- DESPESAS CADASTRADAS ---")
        (listar-despesas despesas)
        (recur despesas))

      ;; Opcao 2: cadastra uma nova despesa
      "2"
      (do
        (println "Descricao:")
        (let [descricao (read-line)]
          (println "Categoria:")
          (let [categoria (read-line)]
            (println "Valor:")
            (let [valor (BigDecimal. (read-line))]
              (println "Data (DD-MM-AAAA):")
              (let [data (read-line)
                    novas-despesas
                    (adicionar-despesa
                     despesas descricao categoria valor data)]
                (println "Despesa cadastrada!")
                (recur novas-despesas))))))

      ;; Opcao 3: filtra despesas por categoria
      "3"
      (do
        (println "Informe a categoria:")
        (let [categoria (read-line)
              resultado (filtrar-categoria despesas categoria)]
          (exibir-resultados resultado)
          (recur despesas)))

      ;; Opcao 4: filtra despesas por periodo
      "4"
      (do
        (println "Data inicial (DD-MM-AAAA):")
        (let [inicio (read-line)]
          (println "Data final (DD-MM-AAAA):")
          (let [fim (read-line)
                resultado (filtrar-periodo despesas inicio fim)]
            (println "\n--- DESPESAS NO PERIODO ---")
            (exibir-resultados resultado)
            (recur despesas))))

      ;; Opcao 5: filtra despesas por valor minimo
      "5"
      (do
        (println "Informe o valor minimo:")
        (let [valor-minimo (BigDecimal. (read-line))
              resultado (filtrar-valor-minimo despesas valor-minimo)]
          (println "\n--- DESPESAS IGUAIS OU SUPERIORES AO VALOR INFORMADO ---")
          (exibir-resultados resultado)
          (recur despesas)))

      ;; Opcao 6: calcula o total gasto
      "6"
      (do
        (println "Total gasto:" (calcular-total despesas))
        (recur despesas))

      ;; Opcao 7: apresenta os gastos por categoria
      "7"
      (do
        (println "\n--- GASTOS POR CATEGORIA ---")
        (doseq [item (total-por-categoria despesas)]
          (println (:categoria item) ":" (:total item)))
        (recur despesas))

      ;; Opcao 8: apresenta o resumo financeiro
      "8"
      (do
        (println "\n--- RESUMO FINANCEIRO ---")
        (let [resumo (gerar-resumo despesas)]
          (println "Quantidade:" (:quantidade resumo))
          (println "Total:" (:total resumo))
          (println "Media:" (:media resumo))
          (println "Maior despesa:" (:maior-despesa resumo)))
        (recur despesas))

      ;; Opcao 0: encerra a aplicacao
      "0"
      (println "Encerrando aplicacao...")

      ;; Trata opcoes que nao existem no menu
      (do
        (println "Opcao invalida!")
        (recur despesas)))))



;; ==========================================
;; INICIALIZACAO DA APLICACAO
;; ==========================================
(defn -main []

  (println "Bem-vindo ao Gerenciador de Despesas!")

  (menu despesas-iniciais))
