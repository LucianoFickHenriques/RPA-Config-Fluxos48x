import pyautogui
import time

print("=======================================")
print("\nO script vai começar em 5 segundos.")
print("Mude para o navegador e clique na ÚNICA caixa de 'Hora' disponível!")
time.sleep(5)

# Gera a lista com os 48 horários
horarios = []
for periodo in ['AM', 'PM']:
    for hora in [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
        for minuto in ['00', '30']:
            horarios.append((str(hora), minuto, periodo))

total_horarios = len(horarios)

# Loop de preenchimento e criação de novas linhas
for i, (h, m, p) in enumerate(horarios):
    

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
    
    # Se NÃO for o último horário (11:30 PM), cria a nova linha
    if i < total_horarios - 1:
        
        pyautogui.press('tab') # Pula pro X
        pyautogui.press('tab') # Pula pro Adicionar
        
        pyautogui.press('enter')
        time.sleep(0.5) 
        
        # A CORREÇÃO DO ÚLTIMO HORÁRIO
        if i == total_horarios - 2: 
            # O botão "Adicionar" some e o foco cai no 'X' da penúltima linha.
            # Um único 'tab' avança o foco do 'X' para a 'Hora' da nova linha criada.
            pyautogui.press('tab') 
        else:
            # Caminho reverso normal quando o botão "Adicionar" desce junto com a nova linha
            pyautogui.hotkey('shift', 'tab') # Do Adicionar, volta pro X
            pyautogui.hotkey('shift', 'tab') # Volta pro AM/PM
            pyautogui.hotkey('shift', 'tab') # Volta pro Minuto
            pyautogui.hotkey('shift', 'tab') # Volta pra Hora
        
        time.sleep(0.1)

print("\n-------------")
print("RPA finalizado!")
print("---------------")
