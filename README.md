# OBJETIVO

O objetivo do trabalho é colocar em prática a implementação de Sockets (tanto com UDP
quanto com TCP), os conceitos de representação externa de dados e comunicação em grupo.

# DESCRIÇÃO GERAL

1. A primeira parte do trabalho consiste em, utilizando UDP, implementar uma
    calculadora remota que execute as 4 operações básicas (+,-,·,÷) de números decimais.
    Descreva o formato para cada tipo das mensagem (Request e Response).
    
2. A segunda parte do trabalho consistem em implementar um Chat usando TCP. O Chat
    deve suportar múltiplos clientes e um servidor. Todos os clientes devem estar na
    mesma sala do chat (i.e., as mensagens enviadas por um cliente devem ser recebidas
    por todos os clientes). Comandos que o usuário (i.e., cliente) pode enviar:
       a. /ENTRAR: ao usar esse comando, ele é requisitado a digitar IP, porta do
          servidor e nickname que deseja usar no chat (não precisa tratar nicknames
          repetidos);
       b. Uma vez conectado, o cliente pode enviar mensagens para a sala do chat;
       c. /USUARIOS: ao enviar esse comando, o cliente recebe a lista de usuários
          atualmente conectados ao chat;
       d. /SAIR: ao enviar esse comando, uma mensagem é enviada à sala do chat
          informando que o usuário está saindo e encerra a participação no chat.
    É papel do servidor receber as requisições dos clientes e encaminhar as mensagens
    recebidas para todos eles. Descreva o formato para cada tipo das mensagem. Não
    pode usar comunicação em grupo.
3. A terceira parte do trabalho consiste em implementar um ambiente inteligente (e.g.,
    casa, escritório, sala de aula, clínica médica, carro, etc) com as seguintes condições e
    restrições:
       a. Uma aplicação (Móvel, Desktop ou Web) deve ser implementada para permitir
          ao usuário conectar e visualizar o status dos objetos do ambiente inteligente,
          além de atuar e ler dados dos objetos.
       b. A aplicação deve se conectar a um servidor, chamado de Gateway, que se
          comunica com cada um dos objetos “inteligentes” do local. A comunicação
          entre a aplicação (Móvel, Desktop ou Web) e o Gateway deve ser
          implementada utilizando TCP e as mensagens definidas com Protocol Buffers.
       c. Deve haver, pelo menos, dois tipos de mensagens (e.g., Request e Response)
          cujos formatos devem ser definidos pelo grupo.
       d. O ambiente inteligente deve conter, no mínimo, 3 equipamentos (e.g.,
       lâmpadas, ar-condicionado, TV, tablet, sistema de som, sistema de irrigação).
       e. A comunicação do Gateway com os equipamentos fica a critério da equipe.
       Tais equipamentos podem ser todos simulados por software (e.g., um
       processo para cada equipamento), que envia de forma periódica seu status (ou
       quando ele se modifica) e recebe os comandos para ligar/desligar ou realizar
       alguma operação (e.g., aumentar a temperatura).
       f. O Gateway deve ter uma funcionalidade de descoberta de equipamentos
       inteligentes, usando comunicação em grupo. Ao iniciar o Gateway, ele deve
       enviar uma mensagem solicitando que os equipamentos se identifiquem.
       g. Ao iniciar o processo dos equipamentos inteligentes, estes devem enviar
       mensagem se identificando para o Gateway. A identificação significa enviar
       seu tipo (e.g., lâmpadas, ar-condicionado, etc), IP e Porta para o Gateway.
       h. Pelo menos um dos equipamentos deve atuar como um sensor contínuo, que
       envia a cada ciclo de X segundos um valor para o Gateway (e.g., um sensor de
       temperatura).
       i. Pelo menos um dos equipamentos deve ter comportamento de um atuador
       (i.e., recebe comandos para modificar seu status, como desligar uma
       lâmpada).
