# Sistema Web LAFISE - Laboratório de Fisiologia do Exercício

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Django](https://img.shields.io/badge/Django-5.1.4-green.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.7-purple.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## Descrição

Sistema web desenvolvido para o **Laboratório de Fisiologia do Exercício (LAFISE)** da Universidade Federal de Minas Gerais. Esta ferramenta de documentação e gerenciamento centraliza informações sobre materiais, métodos, equipamentos, equipe e atividades do laboratório.

## ✨ Características Principais

- **Landing Page Moderna**: Apresentação completa do laboratório com design responsivo
- **Navegação Intuitiva**: Navbar com links organizados para todas as seções
- **Design Responsivo**: Interface adaptada para dispositivos móveis e desktop
- **Cores Institucionais**: Paleta de cores em vermelho e branco conforme solicitado
- **Sistema Modular**: Arquitetura bem estruturada e de fácil manutenção

## 🚀 Funcionalidades

### Páginas Implementadas

1. **Página Inicial**: Landing page com apresentação do laboratório
2. **Principais Referências Bibliográficas**: Compilação de literatura científica
3. **Agenda**: Cronograma de eventos e atividades do laboratório
4. **Métodos e Softwares**: Ferramentas computacionais e metodologias
5. **Métodos**: Metodologias de pesquisa (em desenvolvimento)
6. **Artigos**: Publicações científicas (em desenvolvimento)
7. **Equipamentos**: Catálogo de equipamentos (em desenvolvimento)
8. **Integrantes**: Apresentação da equipe completa
9. **Grupo do Cafezinho**: Encontros informais da equipe
10. **História**: Trajetória e evolução do laboratório

### Recursos Técnicos

- Interface responsiva com Bootstrap 5.3.7
- Ícones Font Awesome para melhor experiência visual
- Navegação com dropdown menus
- Cards informativos e layouts modernos
- Sistema de cores customizado
- Animações CSS suaves

## 🛠️ Tecnologias Utilizadas

- **Backend**: Django 5.1.4
- **Frontend**: Bootstrap 5.3.7
- **Ícones**: Font Awesome 6.5.0
- **Linguagem**: Python 3.10+
- **Banco de Dados**: SQLite (desenvolvimento)
- **CSS**: Estilos customizados com variáveis CSS

## 📋 Pré-requisitos

- Python 3.10 ou superior
- pip (gerenciador de pacotes Python)
- Git

## 🔧 Instalação e Configuração

### 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd lafise-web
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv .venv

# No Linux/Mac:
source .venv/bin/activate

# No Windows:
.venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install django==5.1.4 pillow
```

### 4. Execute as migrações

```bash
python manage.py migrate
```

### 5. Crie um superusuário (opcional)

```bash
python manage.py createsuperuser
```

### 6. Execute o servidor de desenvolvimento

```bash
python manage.py runserver
```

O sistema estará disponível em: `http://127.0.0.1:8000/`

## 📁 Estrutura do Projeto

```
lafise-web/
├── lafise_project/          # Configurações principais do Django
│   ├── __init__.py
│   ├── settings.py          # Configurações do projeto
│   ├── urls.py              # URLs principais
│   └── wsgi.py
├── core/                    # App principal
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py              # URLs do app
│   └── views.py             # Views das páginas
├── templates/               # Templates HTML
│   ├── base.html            # Template base
│   └── core/                # Templates específicos
│       ├── home.html
│       ├── referencias.html
│       ├── agenda.html
│       ├── metodos_softwares.html
│       ├── integrantes.html
│       ├── grupo_cafezinho.html
│       ├── historia.html
│       ├── metodos.html
│       ├── artigos.html
│       └── equipamentos.html
├── static/                  # Arquivos estáticos
│   ├── css/
│   │   └── style.css        # Estilos customizados
│   ├── js/
│   └── images/
│       └── logo.png         # Logo do laboratório
├── manage.py                # Script de gerenciamento Django
├── logo.png                 # Logo original
└── README.md               # Este arquivo
```

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

## 🔗 URLs Disponíveis

- `/` - Página inicial
- `/referencias/` - Principais referências bibliográficas
- `/agenda/` - Agenda do laboratório
- `/metodos-softwares/` - Métodos e softwares
- `/metodos/` - Métodos de pesquisa
- `/artigos/` - Artigos publicados
- `/equipamentos/` - Equipamentos do laboratório
- `/integrantes/` - Integrantes da equipe
- `/grupo-cafezinho/` - Grupo do cafezinho
- `/historia/` - História do laboratório
- `/admin/` - Painel administrativo Django

## 📱 Responsividade

O sistema foi desenvolvido com foco em responsividade, garantindo uma experiência consistente em:

- **Desktop**: Layouts em múltiplas colunas
- **Tablet**: Adaptação automática dos elementos
- **Mobile**: Interface otimizada para telas pequenas

### Breakpoints Bootstrap

- **sm**: ≥576px (smartphones)
- **md**: ≥768px (tablets)
- **lg**: ≥992px (desktops)
- **xl**: ≥1200px (desktops grandes)
- **xxl**: ≥1400px (desktops extra grandes)

## 🚀 Deploy e Produção

### Configurações para Produção

1. **Variáveis de Ambiente**:
   - Configure `DEBUG = False`
   - Defina uma `SECRET_KEY` segura
   - Configure `ALLOWED_HOSTS`

2. **Banco de Dados**:
   - Migre de SQLite para PostgreSQL/MySQL
   - Configure as credenciais do banco

3. **Arquivos Estáticos**:
   - Configure `STATIC_ROOT`
   - Execute `python manage.py collectstatic`

4. **Servidor Web**:
   - Use Gunicorn + Nginx
   - Configure SSL/HTTPS

### Exemplo de Deploy com Gunicorn

```bash
pip install gunicorn
gunicorn lafise_project.wsgi:application --bind 0.0.0.0:8000
```

## 🤝 Contribuição

### Como Contribuir

1. Fork o projeto
2. Crie uma branch para sua funcionalidade (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

### Padrões de Código

- Siga as convenções PEP 8 para Python
- Use nomes descritivos para variáveis e funções
- Adicione comentários para código complexo
- Mantenha templates organizados e semânticos

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

## 🔮 Próximas Funcionalidades

- [ ] Sistema de autenticação de usuários
- [ ] Painel administrativo personalizado
- [ ] Sistema de upload de documentos
- [ ] Calendário interativo
- [ ] Sistema de notificações
- [ ] API REST para integração
- [ ] Dashboard com métricas
- [ ] Sistema de comentários
- [ ] Integração com redes sociais
- [ ] Exportação de relatórios

## 📊 Status do Projeto

- ✅ **Concluído**: Estrutura base, navegação, páginas principais
- 🚧 **Em Desenvolvimento**: Páginas de conteúdo específico
- 📋 **Planejado**: Funcionalidades avançadas e integrações

---

**LAFISE - Laboratório de Fisiologia do Exercício | UFMG - 2025**
