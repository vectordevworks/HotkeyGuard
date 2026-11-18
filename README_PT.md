# Shortcut Blocker

<a href="README.md"><img src="https://flagcdn.com/gb.svg" width="20" alt="Inglês"> Inglês</a> |
<a href="README_DE.md"><img src="https://flagcdn.com/de.svg" width="20" alt="Alemão"> Alemão</a> |
<a href="README_ES.md"><img src="https://flagcdn.com/es.svg" width="20" alt="Espanhol"> Espanhol</a> |
<a href="README_FR.md"><img src="https://flagcdn.com/fr.svg" width="20" alt="Francês"> Francês</a> |
<a href="README_JA.md"><img src="https://flagcdn.com/jp.svg" width="20" alt="Japonês"> Japonês</a> |
<a href="README_KO.md"><img src="https://flagcdn.com/kr.svg" width="20" alt="Coreano"> Coreano</a> |
<a href="README_PT.md"><img src="https://flagcdn.com/pt.svg" width="20" alt="Português"> Português</a> |
<a href="README_RU.md"><img src="https://flagcdn.com/ru.svg" width="20" alt="Russo"> Russo</a> |
<a href="README_ZH_CN.md"><img src="https://flagcdn.com/cn.svg" width="20" alt="Chinês simplificado"> Chinês simplificado</a> |
<a href="README_TR.md"><img src="https://flagcdn.com/tr.svg" width="20" alt="Turco"> Turco</a>

Shortcut Blocker é um aplicativo leve para Windows que permite bloquear atalhos de teclado selecionados. Ele ajuda a evitar o uso acidental de combinações de teclas específicas.

## Visão geral

O aplicativo monitora os eventos do teclado do Windows e bloqueia os atalhos escolhidos. A proteção não é ativada automaticamente quando o aplicativo é aberto; clique em **Iniciar** na interface para ativá-la.

## Recursos

- **Bloqueio de Shift + Delete:** bloqueia o atalho de exclusão permanente.
- **Bloqueio de F1 por aplicativo:** bloqueia F1 no Chrome, Microsoft Edge, Firefox, Brave, Opera e na Área de Trabalho do Windows / Explorador de Arquivos.
- **Proteções selecionáveis:** ative ou desative separadamente o bloqueio de Shift + Delete e F1 pela interface.
- **Minimizar para a bandeja do sistema:** permite minimizar o aplicativo para a bandeja do sistema.
- **Vários idiomas:** turco, inglês, alemão, francês, espanhol, português, russo, japonês, chinês simplificado e coreano.
- **Interface com rolagem:** o conteúdo da janela pode ser rolado.

F1 é bloqueada somente nos aplicativos listados acima. Em outros aplicativos e jogos, F1 continua disponível.

## Requisitos

- Windows
- Python
- Pillow 13.0.0
- pystray 0.19.5

`tkinter`, `ctypes`, `json`, `math`, `os` e `pathlib` fazem parte da biblioteca padrão do Python.

Pillow e pystray são necessários para usar o recurso de minimização para a bandeja do sistema.

## Instalação

1. Baixe os arquivos do projeto ou clone o repositório.
2. Abra a pasta do projeto.
3. Abra o PowerShell nessa pasta.
4. Instale os pacotes Python necessários:

```powershell
py -m pip install -r requirements.txt
```

Conteúdo de `requirements.txt`:

```text
Pillow==13.0.0
pystray==0.19.5
```

5. Inicie o aplicativo:

```powershell
pyw .\ShortcutBlocker.pyw
```

Como alternativa:

```powershell
pythonw .\ShortcutBlocker.pyw
```

## Ambiente virtual (Opcional)

Você pode manter as dependências em um ambiente virtual separado:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
py deactivate 
```

## Uso

1. Execute `ShortcutBlocker.pyw`.
2. Selecione na interface os atalhos que deseja bloquear.
3. Clique em **Iniciar** para ativar a proteção.
4. Acompanhe o estado da proteção no aplicativo.
5. Use a opção de minimizar para enviar o aplicativo à bandeja do sistema. Pillow e pystray precisam estar instalados para esse recurso.

A preferência de idioma é armazenada em:

```text
%USERPROFILE%\.vectordevworks\shortcut_blocker\config.json
```

Esse arquivo armazena a seleção de idioma. As opções de bloqueio podem ser selecionadas no aplicativo; não presuma que elas sejam salvas no arquivo de configuração.

## Compilação (Criar um EXE)

O PyInstaller é necessário para criar o EXE. Instale-o separadamente:

```powershell
py -m pip install pyinstaller==6.22.3
```

Em seguida, abra o PowerShell na pasta do projeto e execute o script de compilação:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

O script realiza as seguintes tarefas:

1. Verifica o arquivo Python principal e `assets\icon.png`.
2. Confirma que o PyInstaller está disponível.
3. Remove as pastas antigas `dist` e `build`.
4. Cria um único EXE sem janela de console.
5. Inclui a pasta `assets` e o ícone do aplicativo na compilação.
6. Verifica se o EXE foi criado.

Após a compilação, o aplicativo estará em:

```text
dist\ShortcutBlocker.exe
```

## Desenvolvedor

**vectordevworks**

## Licença

Consulte o arquivo `LICENSE` no repositório do projeto para conhecer os termos da licença.
