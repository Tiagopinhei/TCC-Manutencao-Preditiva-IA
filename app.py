importar gradio como gr
import numpy as np
import pandas as pd
from scipy.stats import kurtosis
import joblib
import matplotlib.pyplot as plt

# 1. CARREGANDO O CÉREBRO DA IA
tentar :
    modelo_rf = joblib.load( 'modelo_ia_rolamentos.pkl' )
    modelo_carregado = True
exceto :
    modelo_carregado = False

# 2. DICIONÁRIO DE DIAGNÓSTICOS (Padrão Industrial)
def  gerar_diagnóstico ( resultado ):
    dicionário = {
        0 : ( "✅ STATUS NORMAL" , "Máquina operando perfeitamente. Níveis de vibração dentro da norma ISO 20816." ),
        1 : ( "🚨 FALHA NA PISTA INTERNA" , "Risco crítico! Impacto cíclico de alta energia detectado. Planejar substituição do mancal." ),
        2 : ( "⚠️ FALHA NA PISTA EXTERNA" , "Anomalia detectada no anel fixo. Verifique folgas e lubrificação." ),
        3 : ( "🟠 FALHA NA ESFERA" , "Desgaste nos elementos rolantes. Acompanhar evolução do Fator de Crista de perto." )
    }
    titulo, msg = dicionario.get(resultado, ( "❓ ERRO" , "Diagnóstico inconclusivo." ))
    retornar  f" {título} \n\n {msg} "

# 3. FUNÇÃO PARA ABA DE ARQUIVO (Coletor Real)
def  analisar_arquivo ( arquivo ):
    # TRAVA DE SEGURANÇA 1: Se o usuário não colocou o arquivo
    Se o arquivo for  None :
        return  "⚠️ ATENÇÃO: Por favor, faça o upload de um arquivo .csv ou .txt primeiro!" , 0 , 0 , 0 , Nenhum
        
    # TRAVA DE SEGURANÇA 2: Se o cérebro da IA ​​não carregar
    se  não for modelo_carregado:
        return  "❌ Erro Crítico: Modelo IA não encontrado no servidor." , 0 , 0 , 0 , Nenhum
        
    tentar :
        df = pd.read_csv(arquivo.name, header= None )
        sinal_bruto = pd.to_numeric(df.iloc[:, 0 ], errors= 'coerce' ).dropna().values
        
        # Fórmulas de Engenharia
        rms = np.sqrt(np.mean(sinal_bruto** 2 ))
        curto = curtose(sinal_bruto, fisher= False )
        pico = np. max (np. abs (sinal_bruto))
        crista = pico / rms se rms > 0  senão  0
        
        # Previsão da IA
        entrada = np.array([[rms, curt, crista]])
        resultado = modelo_rf.predict(entrada)[ 0 ]
        veredicto = gerar_diagnóstico(resultado)
        
        # Osciloscópio Virtual (Gráfico)
        fig, ax = plt.subplots(figsize=( 8 , 3 ))
        ax.plot(sinal_bruto[: 1000 ], color= '#2905C3' , linewidth= 1 )
        ax.set_title( "Forma de Onda (Time-Domain)" , fontsize= 10 )
        ax.set_ylabel( "Aceleração (g)" , fontsize= 8 )
        ax.grid( True , linestyle= '--' , alpha= 0.6 )
        plt.tight_layout()
        
        retorno veredicto, redondo (rms, 4 ), redondo (curt, 2 ), redondo (crista, 2 ), figo
    exceto Exception como e:
        return  f"❌ Erro ao ler arquivo: Certifique-se de que é um CSV válido. Detalhe: {e} " , 0 , 0 , 0 , None

# 4. FUNÇÃO PARA A ABA MANUAL (Simulação)
def  analisar_manual ( rms, curt, crista ):
    se  não for modelo_carregado:
        return  "Erro: Modelo IA não encontrado."
    entrada = np.array([[rms, curt, crista]])
    resultado = modelo_rf.predict(entrada)[ 0 ]
    return gerar_diagnóstico(resultado)

# 5. CONSTRUÇÃO DA INTERFACE GRÁFICA (Design Profissional/Industrial)
tema = gr.themes.Base(
    preliminar_hue= "slate" ,   # Tons de cinza metálico e azul escuro
    matiz_secundário = "zinco" ,
    matiz_neutro = "zinco" ,
    fonte=[gr.themes.GoogleFont( "Inter" ), "ui-sans-serif" , "system-ui" , "sans-serif" ],
    font_mono=[gr.themes.GoogleFont( "JetBrains Mono" ), "ui-monospace" , "monospace" ]
). definir (
    button_primary_background_fill= "*primary_600" ,
    button_primary_background_fill_hover= "*primary_700" ,
    block_title_text_weight= "600" ,
    largura_da_borda_do_bloco= "1px" ,
    sombra_bloco= "*shadow_drop_lg"
)

com gr.Blocks(theme=tema, title= "Sistema Preditivo Multiclasse" ) como site:
    gr.Markdown( "# ⚙️ Sistema Especialista de Manutenção Preditiva" )
    gr.Markdown( "**Engenharia Mecânica - UFPI** | Diagnóstico de Rolamentos via Machine Learning" )
    
    com gr.Tabs():
        
        # PRIMEIRA ABA: ARQUIVOS REAIS
        with gr.Tab( "📥 Upload de Dados (Analisador de Vibração)" ):
            com gr.Row():
                com gr.Column(scale= 1 ):
                    arquivo_entrada = gr.File(label= "Arquivo .csv do coletor" , file_types=[ ".csv" , ".txt" ])
                    btn_arquivo = gr.Button( "⚡ PROCESSAR SINAL" , variante= "primário" )
                com gr.Column(scale= 2 ):
                    saida_texto_arq = gr.Textbox(label= "Laudo da Inteligência Artificial" , linhas= 3 )
                    com gr.Row():
                        out_rms = gr.Number(label= "RMS Calculado" )
                        out_curt = gr.Number(label= "Curtose Calculada" )
                        out_crist = gr.Number(label= "F. Crista Calculado" )
                    saida_grafico = gr.Plot(label= "Osciloscópio Virtual" )
            
            btn_arquivo.click(analisar_arquivo, inputs=arquivo_entrada, outputs=[saida_texto_arq, out_rms, out_curt, out_crist, saida_grafico])

        # SEGUNDA ABA: MANUAL DE INSERÇÃO
        with gr.Tab( "🎛️ Manual de Simulação (Modo Engenheiro)" ):
            gr.Markdown( "*Utilize os controles abaixo para simular níveis de vibração e testar a resposta do modelo.*" )
            com gr.Row():
                com gr.Column():
                    in_rms = gr.Slider( 0 , 0.5 , value= 0.07 , label= "Energia Global (RMS)" )
                    in_curt = gr.Slider( 2 , 15 , value= 2.8 , label= "Impactos (Curtose)" )
                    in_crist = gr.Slider( 1 , 10 , value= 3.1 , label= "Picos (Fator de Crista)" )
                    btn_manual = gr.Button( "🔍 DIAGNÓSTICO SIMULAR" )
                com gr.Column():
                    saida_texto_man = gr.Textbox(label= "Laudo da Inteligência Artificial" , linhas= 4 )
                    
            btn_manual.click(analisar_manual, inputs=[in_rms, in_curt, in_crist], outputs=saida_texto_man)

site.lançar()
