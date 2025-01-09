# FocusShield

FocusShield é uma ferramenta simples para ajudar a melhorar sua produtividade, bloqueando o acesso a sites específicos durante determinados períodos. Com uma interface amigável e fácil de usar, você pode definir um horário de bloqueio e garantir que não se distraia durante o trabalho ou estudo.

## Funcionalidades

- **Bloqueio de sites**: Escolha uma lista de sites para serem bloqueados.
- **Controle de horários**: Defina um horário de início e fim para o bloqueio.
- **Gerenciamento em tempo real**: Ative, pause ou encerre o bloqueio a qualquer momento.
- **Integração com o sistema**: Modifica o arquivo de hosts do sistema para implementar o bloqueio.

## Requisitos

- Python 3.6 ou superior.
- Biblioteca `colorama` (instale com `pip install colorama`).
- Permissões de administrador (ou superusuário/root).

## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/ArielRSousa/focusshield.git
   cd focusshield
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Certifique-se de executar o script com permissão de administrador/sudo.

## Como Usar

1. Execute o script principal:

   ```bash
   python main.py
   ```

2. Siga as instruções no menu:

   - Opção [1]: Defina os horários de bloqueio e inicie o bloqueio.
   - Opção [2]: Pause ou encerre o bloqueio imediatamente.
   - Opção [3]: Saia do programa.

3. O bloqueio é aplicado automaticamente dentro dos horários definidos e verifica periodicamente se deve ser ativado ou desativado.

## Estrutura do Projeto

- **main.py**: Script principal que gerencia a interface com o usuário.
- **focus\_shield.py**: Implementação da lógica de bloqueio e desbloqueio de sites.
- **banner.py**: Exibe um banner estilizado e uma animação de carregamento.

## Exemplo de Uso

Ao executar o script, você verá algo como:

```
[1] Definir horários e INICIAR BLOQUEIO
[2] PARAR/PAUSAR (desbloquear agora)
[3] Sair
Selecione uma opção: 1
Digite o horário de INÍCIO do bloqueio (HH:MM): 09:00
Digite o horário de FIM do bloqueio (HH:MM): 17:00
Horários definidos: 09:00 - 17:00
Iniciando o loop de bloqueio (Ctrl + C para interromper a qualquer momento)
```

## Notas Importantes

- **Arquivo de Hosts**: O FocusShield modifica o arquivo de hosts do sistema para redirecionar os sites bloqueados para `127.0.0.1`.
- **Permissões**: Certifique-se de executar o script com permissões adequadas, caso contrário, o bloqueio não funcionará.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para melhorar este projeto.

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE).

