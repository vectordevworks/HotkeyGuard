# ProtegeAtalhos

<a href="README.md">
  <img src="https://flagcdn.com/gb.svg" width="20" alt="Inglês"> Inglês
</a>
|
<a href="README_DE.md">
  <img src="https://flagcdn.com/de.svg" width="20" alt="Alemão"> Alemão
</a>
|
<a href="README_ES.md">
  <img src="https://flagcdn.com/es.svg" width="20" alt="Espanhol"> Espanhol
</a>
|
<a href="README_FR.md">
  <img src="https://flagcdn.com/fr.svg" width="20" alt="Francês"> Francês
</a>
|
<a href="README_JA.md">
  <img src="https://flagcdn.com/jp.svg" width="20" alt="Japonês"> Japonês
</a>
|
<a href="README_KO.md">
  <img src="https://flagcdn.com/kr.svg" width="20" alt="Coreano"> Coreano
</a>
|
<strong>
  <img src="https://flagcdn.com/pt.svg" width="20" alt="Português"> Português
</strong>
|
<a href="README_RU.md">
  <img src="https://flagcdn.com/ru.svg" width="20" alt="Russo"> Russo
</a>
|
<a href="README_ZH_CN.md">
  <img src="https://flagcdn.com/cn.svg" width="20" alt="Chinês simplificado"> Chinês simplificado
</a>
|
<a href="README_TR.md">
  <img src="https://flagcdn.com/tr.svg" width="20" alt="Turco"> Turco
</a>

O ProtegeAtalhos é uma aplicação de ambiente de trabalho leve, desenvolvida em Python, que permite bloquear determinados atalhos de teclado no Windows. A sua interface gráfica intuitiva facilita o controlo de atalhos que podem ser acionados acidentalmente e permite gerir facilmente as proteções pretendidas.

## Visão geral

A aplicação monitoriza os eventos do teclado no Windows e bloqueia os atalhos selecionados. A proteção não é ativada automaticamente quando a aplicação é iniciada. Para a ativar, é necessário clicar no botão **Iniciar** na interface.

## Funcionalidades

- **Bloqueio de Shift + Delete:** Bloqueia o atalho utilizado para eliminar ficheiros permanentemente.
- **Bloqueio de F1 específico por aplicação:** Bloqueia a tecla F1 no Google Chrome, Microsoft Edge, Mozilla Firefox, Brave, Opera e no Ambiente de Trabalho do Windows / Explorador de Ficheiros.
- **Proteções selecionáveis:** Permite ativar ou desativar individualmente os bloqueios de Shift + Delete e F1 através da interface.
- **Minimização para a área de notificação:** Permite minimizar a aplicação para a área de notificação do sistema.
- **Suporte multilingue:** Disponibiliza suporte para turco, inglês, alemão, francês, espanhol, português, russo, japonês, chinês simplificado e coreano.
- **Interface com deslocamento:** Permite percorrer o conteúdo da janela da aplicação.

O bloqueio de F1 está ativo apenas nas aplicações mencionadas acima. A tecla F1 não é bloqueada noutras aplicações nem em jogos.

## Requisitos

- Windows
- Python
- Pillow 13.0.0
- pystray 0.19.5

Os módulos `tkinter`, `ctypes`, `json`, `math`, `os` e `pathlib` fazem parte da biblioteca padrão do Python.

Para utilizar a funcionalidade de minimização para a área de notificação, é necessário ter instalados tanto o Pillow como o pystray.

## Instalação

1. Transfira os ficheiros do projeto para o seu computador ou clone o repositório.
2. Abra a pasta do projeto.
3. Abra o PowerShell nessa pasta.
4. Instale as dependências necessárias do Python:

```powershell
py -m pip install -r requirements.txt
```

Conteúdo do ficheiro `requirements.txt`:

```text
Pillow==13.0.0
pystray==0.19.5
```

5. Inicie a aplicação:

```powershell
pyw .\HotkeyGuard.pyw
```

Em alternativa, pode utilizar:

```powershell
pythonw .\HotkeyGuard.pyw
```

## Ambiente virtual (Opcional)

Pode utilizar um ambiente virtual para manter as dependências do Python isoladas dos restantes projetos:

1. Crie um ambiente virtual:

```powershell
py -m venv .venv
```

2. Ative o ambiente virtual:

```powershell
.\.venv\Scripts\Activate.ps1
```

3. Instale as dependências necessárias:

```powershell
py -m pip install -r requirements.txt
```

4. Quando terminar, desative o ambiente virtual:

```powershell
deactivate
```

## Utilização

1. Execute o ficheiro `HotkeyGuard.pyw`.
2. Selecione na interface os atalhos que pretende bloquear.
3. Clique no botão **Iniciar** para ativar a proteção.
4. Consulte o estado da proteção através da interface da aplicação.
5. Utilize a opção de minimização para colocar a aplicação na área de notificação do sistema. Para utilizar esta funcionalidade, é necessário ter instalados o Pillow e o pystray.

A preferência de idioma é guardada na seguinte localização:

```text
%USERPROFILE%\.vectordevworks\shortcut_blocker\config.json
```

Este ficheiro guarda apenas a preferência de idioma. As opções de bloqueio de atalhos podem ser selecionadas nas definições da aplicação; não deve assumir que estas opções são guardadas no ficheiro de configuração.

## Compilação (Criação de EXE)

O PyInstaller é utilizado para converter a aplicação Python num único ficheiro EXE.

### 1. Instalação do PyInstaller

Instale a versão 6.22.3 do PyInstaller:

```powershell
py -m pip install pyinstaller==6.22.3
```

### 2. Aceder à pasta do projeto

Abra o PowerShell na pasta do projeto.

### 3. Executar o script de compilação

Execute o seguinte comando para iniciar o script `embed_icon.ps1`:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

**Nota:** O parâmetro `-ExecutionPolicy Bypass` é utilizado porque o Windows pode impedir a execução de scripts PowerShell devido à política de execução configurada. Esta opção aplica-se apenas ao processo do PowerShell iniciado por este comando e não altera as definições de segurança de todo o sistema.

### 4. Processo de compilação

O script de compilação executa as seguintes operações:

1. Verifica a existência do ficheiro Python principal e do ficheiro `assets\icon.png`.
2. Confirma que o PyInstaller está instalado e disponível.
3. Elimina as pastas antigas `dist` e `build`.
4. Compila a aplicação num único ficheiro EXE, sem apresentar uma janela de consola.
5. Inclui a pasta `assets` e o ícone da aplicação na compilação.
6. Verifica se o ficheiro EXE foi gerado corretamente.

### 5. Resultado da compilação

Após a conclusão bem-sucedida da compilação, o ficheiro EXE será criado na seguinte localização:

```text
dist\HotkeyGuard.exe
```

**Ordem dos passos para compilar uma nova versão:**

1. Abra o PowerShell.
2. Certifique-se de que o PyInstaller está instalado.
3. Aceda à pasta do projeto.
4. Execute o script de compilação.
5. Localize o ficheiro EXE gerado na pasta `dist`.

## Desenvolvedor

**vectordevworks**

## Licença

Consulte o ficheiro `LICENSE` no repositório do projeto para obter informações sobre os termos da licença.