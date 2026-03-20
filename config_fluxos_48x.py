import streamlit as st
import pyautogui
import time

# Configuração da página do Streamlit
st.set_page_config(page_title="RPA - Célula Técnica", layout="centered")
st.title("RPA: Insere Rotas - Célula Técnica")
st.write("Automatização de preenchimento de 48 horários (12:00 AM a 11:30 PM).")

def executar_automacao():
    # 1. Gera a lista com os 48 horários
    horarios = []
    for periodo in ['AM', 'PM']:
        for hora in [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
            for minuto in ['00', '30']:
                horarios.append((str(hora), minuto, periodo))

    # 2. Loop de preenchimento e criação de novas linhas
    total_horarios = len(horarios)
    
    for i, (h, m, p) in enumerate(horarios):
        # --- CONTORNO PARA O NÚMERO 1 ---
        if h == '1':
            pyautogui.write('2')      
            time.sleep(0.1)           
            pyautogui.press('up')     
        else:
            pyautogui.write(h)        
            
        time.sleep(0.1) 
        pyautogui.press('tab')    
        
        pyautogui.write(m)        
        time.sleep(0.1)
        pyautogui.press('tab')    
        
        pyautogui.write(p)        
        time.sleep(0.1)
        
        # Se NÃO for o último horário, cria a nova linha
        if i < total_horarios - 1:
            pyautogui.press('tab') # Pula pro X
            pyautogui.press('tab') # Pula pro Adicionar
            
            pyautogui.press('enter')
            time.sleep(0.5) # Aguarda a interface processar o clique
            
            # --- CORREÇÃO DOS ÚLTIMOS HORÁRIOS ---
            if i == total_horarios - 2: 
                # Penúltimo loop (11:00 PM criando a linha de 11:30 PM).
                # Aqui o botão "Adicionar" some. O foco muda de comportamento.
                # Se estiver fora de sincronia, ajuste a quantidade de shift+tabs abaixo.
                # Geralmente, se o botão some, o foco cai no X da linha de cima.
                pyautogui.hotkey('shift', 'tab') # Volta pro AM/PM
                pyautogui.hotkey('shift', 'tab') # Volta pro Minuto
                pyautogui.hotkey('shift', 'tab') # Volta pra Hora
            else:
                # Caminho reverso normal quando o botão "Adicionar" ainda existe
                pyautogui.hotkey('shift', 'tab') # Do Adicionar, volta pro X
                pyautogui.hotkey('shift', 'tab') # Volta pro AM/PM
                pyautogui.hotkey('shift', 'tab') # Volta pro Minuto
                pyautogui.hotkey('shift', 'tab') # Volta pra Hora
            
            time.sleep(0.1)

# Interface do Streamlit
st.divider()

if st.button("INICIAR PROCESSAMENTO"):
    aviso = st.warning("A automação vai começar em 5 segundos. Mude para a janela do sistema e clique na ÚNICA caixa de 'Hora' disponível!")
    
    # Contagem regressiva visual no Streamlit
    progress_bar = st.progress(0)
    for seg in range(5):
        time.sleep(1)
        progress_bar.progress((seg + 1) * 20)
        
    aviso.empty() # Limpa o aviso
    progress_bar.empty() # Limpa a barra
    
    with st.spinner("Executando automação. Não mexa no mouse ou teclado..."):
        executar_automacao()
        
    st.success("Log: Todos os 48 horários foram configurados com sucesso!")

st.divider()
st.caption("Grupo Apisul - Todos os direitos reservados | v1.0")