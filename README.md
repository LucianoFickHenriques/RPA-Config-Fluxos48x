# 🤖 RPA: Preenchimento de Horários

> Script em Python desenvoldida para sanar uma dor que é configurar 48 horários diferentes no ciclo de atualização de um fluxo de dados no workspace.

## 📌 Sobre a Automação
Preencher dezenas de campos de horário (ex: 12:00 AM, 12:30 AM...) em sistemas web costuma ser uma tarefa exaustiva. Este script utiliza a biblioteca `pyautogui` para assumir o controle do teclado e realizar o preenchimento em loop de forma rápida e precisa.

**Destaques do Código (Tratamento de Exceções de UI):**
* **Geração Dinâmica:** O código constrói a matriz de horários automaticamente usando loops aninhados (AM/PM > Horas > Minutos), não necessitando de listas hardcoded.
* **Bypass de Dropdown (Bug do Número 1):** Em alguns inputs de hora, digitar '1' aciona atalhos indesejados (como pular para as 10h). O script contorna isso de forma inteligente digitando '2' e usando a seta direcional para cima (`up`).
* **Navegação Reversa Dinâmica:** Após adicionar uma nova linha, o bot utiliza a combinação `Shift + Tab` para retornar aos campos vazios. Ele possui uma lógica matemática (`i == len(horarios) - 2`) para recalcular a quantidade de "Tabs" necessários na última iteração, prevenindo que o fluxo quebre quando o botão "Adicionar" desaparece da tela.

## 🛠️ Tecnologias e Pré-requisitos
* **Python 3.x**
* **PyAutoGUI:** Biblioteca para simulação de cliques e teclado.

Para instalar as dependências, execute no terminal:

```bash
pip install pyautogui
```

<br>
---
<p align="center">
  Desenvolvido por <b>Luciano Fick Henriques</b><br>
</p>

<p align="center">
  <a href="https://github.com/LucianoFickHenriques" target="_blank"><img src="https://github.githubassets.com/favicons/favicon-dark.png" width="18" alt="GitHub"></a>
  &nbsp;
  <a href="https://www.linkedin.com/in/luciano-fick-henriques-a701b9165/" target="_blank"><img src="https://static.licdn.com/aero-v1/sc/h/akt4ae504epesldzj74dzred8" width="20" alt="LinkedIn"></a>
</p>