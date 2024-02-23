# VeloxNet - Frontend

Frontend da aplicação, desenvolvido com Vue.js.

## Como Rodar o Frontend

Siga estas instruções para configurar e executar o frontend localmente.

### Pré-requisitos

- Node.js instalado (versão 20.0.x)
- Yarn instalado (versão mais recente recomendada)

### Instalação do Node.js e Yarn

#### macOS

1. Instale o Homebrew (se já não estiver instalado):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. Instale o Node.js e o Yarn usando o Homebrew:
   ```bash
   brew install node
   brew install yarn
   ```

#### Linux

1. Instale o Node.js e o Yarn usando o gerenciador de pacotes do seu sistema (por exemplo, apt, yum, pacman):
   ```bash
   # Instalação do Node.js
   sudo apt install nodejs
   # Instalação do Yarn
   npm install -g yarn
   ```

#### Windows

- Você pode baixar e instalar o Node.js e o Yarn a partir de seus sites oficiais:
  - [Node.js](https://nodejs.org/)
  - [Yarn](https://yarnpkg.com/)

### Instalação das Dependências

```bash
cd frontend
yarn install
```

### Executando o Servidor de Desenvolvimento

```bash
yarn serve
```

Agora você pode acessar o frontend em [http://localhost:8080/](http://localhost:8080/).

## Referências

- **Vue.js**: [Documentação oficial do Vue.js](https://vuejs.org/)

## Tema

Para a composição dos templates foi utilizado o tema [Vue Material Dashboard 2](https://www.creative-tim.com/product/vue-material-dashboard), um pacote baseado em bootstrap e com componentes prontos para o Vue.js, construído por [Creative-Tim](https://www.creative-tim.com/).

## Ícones

Para criação dos ícones usados no navegador e em alguns sistemas operacionais como Windows, Android e IOS, foi utilizada a plataforma [RealFaviconGenerator](https://realfavicongenerator.net/).

## Inspiração

- [Conectell](https://conectell.com.br/)
- [Rapeedo](https://rapeedo.com.br/)

## Tutoriais Seguidos

- [Como fazer deploy de uma aplicação Vue.js na Vercel](https://www.youtube.com/watch?v=LjqGkfyDg-Y)
