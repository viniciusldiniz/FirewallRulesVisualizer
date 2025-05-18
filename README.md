# 🔥 Firewall Rules Visualizer

## 🔐 Visualize e entenda as regras do seu firewall como nunca antes

---

### 📖 Sobre o projeto

Gerenciar regras de firewall pode ser um desafio, especialmente para quem lida com configurações complexas em múltiplas máquinas ou ambientes híbridos (Linux e Windows).  
Este projeto entrega uma solução simples e poderosa: um script que captura as regras ativas do seu firewall local (iptables, ufw ou Firewall do Windows) e gera um relatório HTML interativo, claro e fácil de interpretar.

Com essa ferramenta, você pode:

- **Visualizar regras detalhadas** em formato legível, evitando confusão com saídas complexas do terminal.  
- **Identificar portas abertas e bloqueadas** rapidamente.  
- **Detectar regras permissivas ou mal configuradas** que podem representar riscos à segurança.  
- **Facilitar auditorias e treinamentos** ao apresentar as regras de forma visual e acessível.

Ideal para profissionais de segurança, administradores de rede e estudantes que desejam aprofundar seu entendimento sobre firewalls e fortalecer sua postura de segurança.

---

### 🚀 Funcionalidades principais

- Suporte multiplataforma: Linux (iptables) e Windows (Firewall do Windows).  
- Geração automática de relatório HTML com visualização estilizada.  
- Script simples, leve e fácil de adaptar para outras plataformas ou ferramentas.  
- Exibe regras completas com detalhes relevantes para análise.  

---

### ⚙️ Como usar

#### Pré-requisitos

- Python 3.x instalado.  
- Permissão de administrador (Linux: sudo, Windows: execute no cmd/powershell com privilégios).  

#### Passos para executar

1. Clone o repositório:
```bash
git clone https://github.com/seuusuario/firewall-visualizer.git
cd firewall-visualizer
