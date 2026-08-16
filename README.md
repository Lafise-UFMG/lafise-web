# Sistema Web LAFISE - Laboratório de Fisiologia do Exercício

![HTML5](https://img.shields.io/badge/HTML5-orange.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.3-purple.svg)
![GitHub Pages](https://img.shields.io/badge/Hospedagem-GitHub%20Pages-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## Descrição

Site institucional do **Laboratório de Fisiologia do Exercício (LAFISE)** da Universidade Federal de Minas Gerais. Apresenta informações sobre o laboratório, sua história, equipe e publicações científicas.

Este site é totalmente estático (HTML/CSS) e é hospedado via **GitHub Pages** a partir da pasta `docs/`.

## ✨ Características Principais

- **Landing Page Moderna**: Apresentação completa do laboratório com design responsivo
- **Navegação Intuitiva**: Navbar com links organizados para todas as seções
- **Design Responsivo**: Interface adaptada para dispositivos móveis e desktop
- **Cores Institucionais**: Paleta de cores em vermelho e branco conforme solicitado

## 🚀 Páginas do Site

1. **Página Inicial** (`index.html`): Apresentação do laboratório
2. **História** (`historia.html`)
3. **Artigos** (`artigos.html`): publicações científicas do LAFISE (1984–2021)
4. **Processo Seletivo** (`processo-seletivo.html`): informações sobre seleção do Mestrado/Doutorado em Ciências do Esporte
5. **Integrantes** (`integrantes.html`): professores, doutorandos, mestrandos e iniciação científica
6. **Linhas de Pesquisa** (`linhas-pesquisa.html`)

## 🛠️ Tecnologias Utilizadas

- **HTML5** e **CSS3** (estilos customizados com variáveis CSS)
- **Bootstrap 5.3.3** (via CDN)
- **Font Awesome 6.5.0** (via CDN)

## 📁 Estrutura do Projeto

```
lafise-web/
├── docs/                     # Site publicado pelo GitHub Pages
│   ├── index.html
│   ├── historia.html
│   ├── artigos.html
│   ├── processo-seletivo.html
│   ├── integrantes.html
│   ├── linhas-pesquisa.html
│   └── static/
│       ├── css/style.css
│       └── images/logo.png
├── .gitignore
└── README.md
```

## 🔧 Como visualizar localmente

Não é necessário nenhum servidor de aplicação — basta abrir os arquivos HTML no navegador, ou servir a pasta `docs/` com um servidor estático simples:

```bash
cd docs
python3 -m http.server 8000
```

O site estará disponível em `http://127.0.0.1:8000/`.

## 🌐 Publicando no GitHub Pages

1. No GitHub, acesse **Settings → Pages** do repositório
2. Em **Build and deployment**, selecione a fonte **Deploy from a branch**
3. Escolha a branch `main` e a pasta **`/docs`**
4. Salve — o site ficará disponível em `https://<usuario>.github.io/<repositorio>/`

## 🎨 Design e Estilo

### Cores Principais

- **Vermelho Principal**: `#cc2936`
- **Vermelho Escuro**: `#a02128`
- **Vermelho Claro**: `#e85a5a`
- **Branco**: `#ffffff`

### Componentes Visuais

- **Navbar**: Fixa no topo com logo e navegação responsiva
- **Hero Section**: Seção de destaque na página inicial
- **Cards**: Layout em cards para organização do conteúdo
- **Icons**: Font Awesome para ícones consistentes
- **Footer**: Rodapé com informações institucionais

## 📱 Responsividade

O site foi desenvolvido com foco em responsividade, garantindo uma experiência consistente em desktop, tablet e mobile, usando os breakpoints padrão do Bootstrap (`sm`, `md`, `lg`, `xl`, `xxl`).

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua alteração (`git checkout -b feature/AmazingFeature`)
3. Edite os arquivos HTML/CSS em `docs/`
4. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
5. Push para a branch (`git push origin feature/AmazingFeature`)
6. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👥 Equipe de Desenvolvimento

- **Desenvolvedor Principal**: Sistema desenvolvido para o LAFISE
- **Instituição**: Universidade Federal de Minas Gerais
- **Laboratório**: Laboratório de Fisiologia do Exercício

## 📞 Contato

Para dúvidas ou sugestões sobre o sistema:

- **Email**: lafise@ufmg.br
- **Website**: [EEFFTO - UFMG](https://www.eeffto.ufmg.br/)
- **Endereço**: Escola de Educação Física, Fisioterapia e Terapia Ocupacional - UFMG

---

**LAFISE - Laboratório de Fisiologia do Exercício | UFMG**
