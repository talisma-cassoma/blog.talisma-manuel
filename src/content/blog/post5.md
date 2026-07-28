---
title: "How to host for free a fullstack MVP project"
description: "here is my finding a way to put a fullstack mobile and/or web project online for free"
heroImage: "/supabase-firebase.jpg"
pubDate: "July 15 2026"
tags: ["host", "fullstack"]
draft: true
---



Neste projeto, o **Supabase** funciona como o *backend* completo para a plataforma de venda de gadgets, substituindo dados estáticos por um banco de dados relacional (SQL) dinâmico, além de gerenciar autenticação e armazenamento. O funcionamento ocorre em duas frentes: no aplicativo **React Native** (cliente mobile) e no **Next.js** (painel administrativo).

### 1. Setup e Inicialização
O processo de configuração segue estas etapas principais:
* **Criação do Projeto:** Feita no painel do Supabase, onde se obtém o `URL` do projeto e a `Anon Key` (2:10:24-2:14:17).
* **Variáveis de Ambiente:** Os dados de conexão são armazenados em arquivos `.env` ou `.env.local`, garantindo segurança (3:19:05-3:20:20, 8:58:56).
* **SDK e Cliente:** A comunicação é feita via `@supabase/supabase-js`. Para o **Next.js**, utiliza-se o `@supabase/ssr` para lidar com *Server-Side Rendering* e cookies de sessão (3:18:00-3:22:50). No **React Native**, utiliza-se o `expo-secure-store` para persistir sessões de autenticação de forma segura no dispositivo (2:15:33-2:16:13).

### 2. Comunicação com o Projeto
A comunicação ocorre através de clientes específicos para cada ambiente:
* **Client Side (Frontend/Mobile):** Utiliza um cliente configurado para rodar no navegador ou aparelho, ideal para operações rápidas (3:20:43).
* **Server Side (Admin Panel):** Utiliza um cliente especializado (`create-server-client`) que interage com o banco de forma segura no servidor, essencial para proteger rotas e validar permissões (3:20:46).
* **Middleware:** O projeto utiliza um `middleware.ts` para verificar o token do usuário antes de liberar o acesso a páginas protegidas (3:22:57).

### 3. Integração de Recursos
* **Autenticação:** O Supabase gerencia o *login* via e-mail e cria uma tabela interna de usuários (2:14:21).
* **Database e RLS:** O projeto utiliza *Row Level Security* (RLS) para garantir que usuários acessem apenas dados autorizados (2:56:30).
* **Edge Functions e Stripe:** Para pagamentos, o curso demonstra como rodar o Supabase localmente com **Docker** (8:45:16), permitindo testar *Edge Functions* (serviços serverless) antes de fazer o *deploy* para a nuvem (9:13:08, 10:06:00).

### 4. Sincronização Local vs. Remoto
O curso ensina a manter o ambiente local espelhado ao remoto usando o **Supabase CLI**:
1. `supabase init`: Inicializa a estrutura local (8:46:58).
2. `supabase db pull`: Puxa o esquema do banco remoto para o seu computador (8:48:56).
3. `supabase db push`: Empurra migrações locais para o servidor de produção (9:59:25).


## em um ORM, se nao porque nao foi usado um? podia os endpoints tanto para next quanto para o expo?

Fico feliz que o conteúdo tenha sido exatamente o que você precisava! Respondendo às suas dúvidas sobre a arquitetura utilizada no curso:

### Sobre a ausência de um ORM
Neste projeto, **não foi utilizado um ORM tradicional** (como Prisma ou Drizzle). A comunicação com o banco de dados é feita diretamente através do **Supabase Client SDK**.

**Por que essa escolha?**
* **Foco no SDK do Supabase:** O Supabase já oferece uma camada de abstração muito poderosa e tipada (através da geração de tipos do TypeScript baseada no esquema do banco). Utilizar o SDK nativo permite aproveitar melhor os recursos de *Realtime*, *Auth* e *Row Level Security* (RLS) sem a sobrecarga de uma camada ORM externa.
* **Simplicidade:** Para este tipo de aplicação (loja de gadgets), as operações CRUD são relativamente diretas. O SDK permite consultas fluentes (ex: `.from('products').select('*')`) que são tão legíveis quanto consultas de ORM.
* **Integração Serverless:** Como o projeto utiliza *Edge Functions* (Deno) e *Server Actions* no Next.js, manter o peso do pacote baixo é essencial, e o SDK do Supabase é altamente otimizado para esses ambientes.

### Sobre os Endpoints (Next.js vs Expo)
A abordagem adotada no curso **não utiliza endpoints de API tradicionais** (como rotas REST que você chamaria via `fetch` ou `axios` manualmente para cada ação). Em vez disso, o projeto utiliza:

1. **Server Actions (Next.js):** Para o painel administrativo, as ações de banco são executadas diretamente no servidor, garantindo segurança total (3:17:46). Isso substitui a necessidade de criar *API Routes* complexas.
2. **Supabase Client SDK (Expo):** O aplicativo React Native se conecta diretamente ao banco (ou via *Edge Functions* para pagamentos), usando o cliente configurado com a `anon key`. 

**Por que essa abordagem?**
Em vez de criar endpoints customizados que precisariam ser mantidos (e protegidos manualmente), o Supabase utiliza o **Row Level Security (RLS)**. O controle de acesso é definido diretamente no banco de dados, tornando a API "nativa" do Supabase segura o suficiente para ser consumida diretamente pelo cliente, desde que as políticas (policies) estejam configuradas corretamente (2:56:30).

## qual é a a estrategia para registrar Supabase SQL, Triggers, Functions em repositorio para que possam ser comitadas ou revisadas?

Para registrar o esquema do seu banco de dados (tabelas, triggers, functions e policies) no versionamento de código (Git) e permitir revisões, a estratégia oficial e recomendada pelo Supabase é utilizar o **Supabase CLI** junto com o fluxo de **Migrações**. Isso é demonstrado no curso (8:45:16 e 8:49:49) como o método para manter o desenvolvimento local em sincronia com o remoto.

### Estratégia de Versionamento:

1. **Supabase Init (`supabase init`)**: Inicializa a estrutura de pastas do Supabase no seu projeto, criando um diretório `supabase/` que será rastreado pelo Git.
2. **Migrações Automáticas (`supabase db diff`)**: Esta é a chave para o versionamento. Sempre que você alterar algo no banco (via SQL Editor ou interface), você não deve apenas aplicar a mudança; você deve gerar um arquivo de migração. O comando `supabase db diff -f nome_da_migracao` compara o estado atual do seu banco de dados local com o estado anterior e cria um arquivo `.sql` dentro da pasta `supabase/migrations/`.
3. **Repositório Git**: Você commita esses arquivos `.sql` no seu repositório. Isso permite que outros desenvolvedores revisem o código SQL (PRs) antes de serem aplicados.
4. **Aplicação das Migrações (`supabase db push`)**: Este comando envia as migrações locais que ainda não foram aplicadas para o projeto remoto no Supabase Cloud. Em ambientes de CI/CD, este processo pode ser automatizado.

### Por que essa abordagem é essencial?
* **Histórico e Auditoria**: Cada alteração (como a criação de uma `trigger` ou `function`) fica registrada com um timestamp, facilitando saber *quem* fez e *quando*.
* **Rollback**: Se algo quebrar, você tem o histórico de migrações para reverter ou entender o que foi alterado.
* **Padronização**: Garante que o ambiente de produção seja idêntico ao de desenvolvimento e testes, evitando o 



## e onde o type de usuario é definido no app expo? qual estrategia foi usada para que usuario mobile nao tenha acesso as secrets do supbase/stripe e nao modifique o seu tipo para admin ou vice-versa?  

A definição e a proteção do tipo de usuário (*user type*) são realizadas através de uma combinação de **banco de dados relacional** e **Row Level Security (RLS)**, garantindo que o cliente mobile não tenha privilégios administrativos. Aqui está a estratégia detalhada:

**1. Onde o tipo de usuário é definido?**
O tipo de usuário (admin vs. user) é armazenado na tabela `users` dentro do *Supabase* (2:42:20). Esta tabela referencia o `auth.users` interno do Supabase através do ID do usuário. Ao criar a tabela, foi definido um campo `type` com um valor *default* como 'user' (2:43:16). Isso significa que, por padrão, qualquer novo cadastro no app mobile é registrado como um usuário comum.

**2. Estratégia contra modificação de privilégios (RLS):**
O ponto crucial para evitar que um usuário mobile altere seu tipo para 'admin' é o uso de **Row Level Security (RLS)** (2:56:30, 3:51:01). 
* Mesmo que um usuário mal-intencionado tentasse realizar um comando `UPDATE` na sua própria linha na tabela `users`, a política de segurança (policy) configurada no Supabase impediria essa ação (4:18:31).
* As políticas de segurança no banco de dados validam se quem está executando a operação tem permissão. Como as políticas foram escritas para permitir apenas que administradores alterem dados sensíveis (4:17:10), o banco de dados rejeita qualquer tentativa de escalação de privilégio vinda do app mobile.

**3. Segurança de Segredos (Supabase/Stripe Secrets):**
O app Expo nunca tem acesso às chaves secretas (*service role keys* ou *stripe secret keys*) por causa destas práticas:
* **Variáveis de Ambiente**: As chaves privadas (ex: `STRIPE_SECRET_KEY`) são configuradas apenas no ambiente de servidor (Next.js/Edge Functions) e nunca são prefixadas com `EXPO_PUBLIC_`, o que impediria que fossem incluídas no *bundle* do aplicativo mobile (9:06:56).
* **Edge Functions (Deno)**: Para pagamentos com Stripe, a lógica de criação de *Payment Intents* não acontece no app mobile, mas sim em uma **Edge Function** no servidor (9:03:26, 9:20:13). O app apenas solicita o pagamento, e o servidor, que detém a chave secreta de forma segura, processa a transação com o *Stripe*.

## e o que impede que o usuario no registro se registre com admin no app mobile ou no next?

A prevenção de que um usuário comum se registre com privilégios de **admin** é garantida por uma combinação de segurança no banco de dados e lógica de backend, e não depende de validação no código do aplicativo (que poderia ser burlada). Aqui estão os mecanismos principais:

1. **Valor Padrão no Banco de Dados (Database Schema):** 
Ao criar a tabela `users` no Supabase (2:42:20), o campo `type` é configurado com um valor padrão (`DEFAULT`) igual a `'user'` (2:43:16). Isso significa que, mesmo que o aplicativo enviasse uma requisição tentando definir o campo `type` como `admin`, o banco de dados ignoraria essa tentativa ou o processo de inserção simplesmente ignoraria esse campo, atribuindo automaticamente o nível de acesso comum.

2. **Triggers de Segurança (Supabase SQL Functions):** 
O curso utiliza uma **função e um trigger** (2:44:42, 8:57:55) que são executados automaticamente pelo Supabase sempre que um novo usuário é criado na autenticação (`auth.users`). Esse trigger popula a tabela pública `users`. Como essa lógica roda inteiramente dentro do servidor do Supabase, o cliente (app mobile ou navegador) não tem controle sobre ela. O trigger garante que a criação do registro siga as regras pré-definidas pelo desenvolvedor, e não pelos dados enviados pelo frontend.

3. **Row Level Security (RLS) - Proteção de Escrita:** 
As políticas de RLS configuradas no banco de dados (2:56:30) definem quem pode inserir ou atualizar registros. O frontend apenas consome a API do Supabase, mas o Supabase, antes de gravar qualquer dado, valida as *policies*. Se uma política não permite que um usuário comum altere o campo `type` ou insira um registro com `type: 'admin'`, o banco de dados rejeitará a operação com um erro de permissão (4:18:31).

4. **Segregação de Lógica no Servidor (Next.js):** 
No painel administrativo (Next.js), quando um administrador precisa gerenciar usuários, a operação é feita via **Server Actions** (3:17:46). Essas ações rodam em ambiente seguro (servidor), onde o código tem acesso a privilégios administrativos (usando chaves de serviço ou sessões validadas) que o app mobile jamais terá acesso. O app mobile nunca possui a chave de privilégios (*service role key*) necessária para contornar as proteções do RLS.

## como o docker foi usado aqui?

No curso, o **Docker** é utilizado como a infraestrutura de base para rodar o **Supabase localmente** em sua máquina (8:45:16). O uso do Docker é fundamental para permitir o desenvolvimento e testes de funcionalidades complexas sem depender de uma conexão constante com a nuvem.

### Como o Docker é aplicado:

* **Ambiente de Desenvolvimento Local:** Ao executar comandos como `supabase start` (8:52:25, 9:35:38), o CLI do Supabase utiliza o Docker para subir múltiplos **contêineres** que simulam todo o ecossistema do Supabase (banco de dados PostgreSQL, API GoTrue para autenticação, PostgREST, etc.) dentro do seu computador.
* **Testes de Edge Functions:** Esta é uma das partes mais importantes do uso do Docker no projeto. Para integrar pagamentos com **Stripe** (9:03:26), você precisa executar *Edge Functions* (serviços serverless). O ambiente local gerado pelo Docker permite que você desenvolva, teste e depure essas funções em um ambiente isolado que replica o comportamento de produção antes de fazer o *deploy* final (9:13:08).
* **Sincronização e Migrações:** O Docker garante que seu esquema de banco de dados local seja um reflexo fiel do que será colocado em produção. Quando você roda migrações ou altera o banco, o ambiente local, orquestrado pelo Docker, mantém a consistência necessária para evitar erros ao enviar as alterações (`supabase db push`) para o Supabase Cloud (9:59:25).

**Resumo:** O Docker funciona como uma "caixa" que isola toda a infraestrutura do seu backend, permitindo que você tenha um ambiente de desenvolvimento robusto, capaz de rodar funções complexas e persistir dados localmente, garantindo que o fluxo de desenvolvimento seja ágil e seguro.