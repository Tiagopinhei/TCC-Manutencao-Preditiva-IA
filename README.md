# ⚙️ SIMP 4.0: Sistema Integrado de Manutenção Preditiva via IA

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Random%20Forest-orange)
![Gradio](https://img.shields.io/badge/Interface-Gradio-lightgrey)
![Status](https://img.shields.io/badge/Status-Concluído-success)
![Engenharia Mecânica](https://img.shields.io/badge/Engenharia-Mecânica-darkred)

O **SIMP 4.0** é um sistema especialista multiclasse em nuvem, desenvolvido para diagnosticar automaticamente falhas em rolamentos de motores de indução e sistemas rotativos utilizando **Inteligência Artificial** e **Análise de Vibrações**. 

Este projeto foi desenvolvido como Trabalho de Conclusão de Curso (TCC) em Engenharia Mecânica na Universidade Federal do Piauí (UFPI).

## 🎯 O Problema vs. A Solução
Na engenharia de manutenção, falhas inesperadas em mancais causam paradas catastróficas (*downtime*) e perdas financeiras milionárias. Métodos tradicionais dependem de análises manuais demoradas e limites estáticos de alarme.

O **SIMP 4.0** resolve isso processando sinais brutos de vibração (arquivos `.csv` provenientes de sensores IoT/acelerômetros) e utilizando um modelo de *Machine Learning* para inferir não apenas a presença da falha, mas a sua localização exata e severidade, gerando laudos em milissegundos.

## 🧠 Arquitetura e Inteligência Artificial

O motor de inferência utiliza o algoritmo **Random Forest** treinado e validado com o banco de dados da *Case Western Reserve University* (CWRU). O modelo obteve uma **acurácia global validada de 98,91%**.

A pipeline de dados extrai indicadores estatísticos críticos no domínio do tempo, baseados nas normas ISO 20816 e NBR 10082:
* **Valor RMS:** Avalia a severidade global e a dissipação contínua de energia mecânica.
* **Curtose:** Mede a impulsividade geométrica, essencial para detectar choques agudos e falhas incipientes (*spalling/pitting*).
* **Fator de Crista:** Relaciona picos de impacto isolados com a energia global do sistema.

### 📊 Diagnóstico Multiclasse
O sistema classifica o ativo em 4 estados de integridade:
1. ✅ **Operação Normal**
2. 🚨 **Falha na Pista Interna (Inner Race)**
3. ⚠️ **Falha na Pista Externa (Outer Race)**
4. 🟠 **Falha nos Elementos Rolantes (Ball)**

## 💻 Funcionalidades da Interface (HMI)

A interface foi construída com **Gradio** para atuar como uma verdadeira ferramenta de PCM (Planejamento e Controle de Manutenção) no chão de fábrica:
* **Osciloscópio Virtual:** Visualização imediata da forma de onda temporal do sinal importado.
* **Tradução Física da Análise:** A IA explica o comportamento cinemático do defeito (ex: *ressonância estrutural*, *impactos erráticos na gaiola*).
* **Impacto Operacional e Financeiro:** Tradução do risco mecânico para a linguagem de gestão (ex: *aumento de arraste*, *risco de queima do estator*).
* **Prescrição de OS:** Geração de plano de ação (intervenção tribológica, redução de carga, substituição).
* **Exportação RDT:** Download automático do Relatório de Diagnóstico Técnico em formato `.txt` para integração com sistemas ERP (SAP, Fracttal).


