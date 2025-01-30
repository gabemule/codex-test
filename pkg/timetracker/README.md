# 🕒 Git Time Tracker

> Análise inteligente de tempo baseada no histórico do Git

## 📖 Sumário
- [🎯 Visão Geral](#-visão-geral)
- [⚙️ Como Funciona](#️-como-funciona)
- [📊 Fórmulas e Multiplicadores](#-fórmulas-e-multiplicadores)
- [📋 Relatórios Gerados](#-relatórios-gerados)
- [🚀 Como Usar](#-como-usar)
- [❓ FAQ](#-faq)

## 🎯 Visão Geral

O Git Time Tracker é uma ferramenta que analisa o histórico do Git para gerar estimativas precisas do tempo gasto em desenvolvimento. Ele considera diversos fatores como:

- 📝 Quantidade e tipo de arquivos modificados
- 🔄 Linhas adicionadas e removidas
- 🏗️ Complexidade das mudanças
- 🎨 Natureza do trabalho (feature, fix, etc)

### Para Não-Técnicos
Imagine que você está reformando uma casa. Algumas tarefas são simples (como pintar uma parede), outras são complexas (como refazer a instalação elétrica). Da mesma forma, em desenvolvimento:

- Uma mudança pequena em um arquivo (como corrigir um texto) leva pouco tempo
- Uma nova funcionalidade complexa (como um sistema de pagamento) leva mais tempo
- Remover código geralmente é mais rápido que adicionar
- Diferentes tipos de arquivo exigem diferentes níveis de esforço

O Git Time Tracker analisa todas essas nuances para estimar quanto tempo cada mudança realmente levou.

### Benefícios
- 📈 Estimativas mais precisas para projetos futuros
- 📊 Visibilidade do esforço real de desenvolvimento
- 🎯 Identificação de áreas que precisam de mais recursos
- 📅 Melhor planejamento de sprints e releases

## ⚙️ Como Funciona

### 1. Análise de Commits

Para cada commit, analisamos:

```javascript
{
  // Metadados do commit
  hash: "abc123",
  author: "Dev Name",
  date: "2024-01-30",
  message: "feat: new payment system",
  
  // Estatísticas
  stats: {
    filesChanged: 5,
    additions: 200,
    deletions: 50,
    fileTypes: {
      "js": 2,
      "css": 1,
      "test": 2
    }
  }
}
```

### 2. Cálculo de Complexidade

A complexidade é calculada considerando dois aspectos:

#### 2.1 Complexidade Estrutural 🏗️
Relacionada a mudanças na estrutura/interface:
```javascript
const STRUCTURAL_PATTERNS = [
  '/components/',
  '/layouts/',
  '/pages/',
  '/views/',
  '/styles/',
  '/assets/',
  '/themes/'
];
```

#### 2.2 Complexidade Algorítmica 🧮
Relacionada a mudanças na lógica/processamento:
```javascript
const ALGORITHMIC_PATTERNS = [
  '/utils/',
  '/helpers/',
  '/services/',
  '/hooks/',
  '/commands/',
  '/lib/',
  '/core/'
];
```

### 3. Estimativa de Tempo

O tempo é calculado em duas partes:

#### 3.1 Tempo de Planejamento 🤔
```javascript
planningTime = baseTime * 
  complexityMultiplier *
  typeRatio *
  planningMultiplier *
  commitTypeMultiplier;
```

#### 3.2 Tempo de Implementação ⌨️
```javascript
implementationTime = 
  (addedLines * baseTime * complexityMultiplier * typeMultiplier) +
  (deletedLines * baseTime * complexityMultiplier * DELETION_FACTOR * typeMultiplier);
```

## 📊 Fórmulas e Multiplicadores

### Tipos de Arquivo

| Tipo | Extensões | Tempo Base (Planning) | Tempo Base (Implementation) |
|------|-----------|----------------------|---------------------------|
| 💻 Lógica | js, ts, jsx, tsx | 1.0h | 2.4min/linha |
| ⚙️ Config | json, yml, env | 0.25h | 0.6min/linha |
| 🎨 Estilo | css, scss, less | 0.5h | 1.2min/linha |
| 📝 Docs | md, txt, html | 0.3h | 0.9min/linha |

### Níveis de Complexidade

#### Estrutural
| Nível | Multiplicador | Descrição |
|-------|--------------|------------|
| 🟢 Trivial | 0.5 | Mudanças muito simples |
| 🟦 Básico | 0.8 | Mudanças básicas |
| 🟨 Moderado | 1.2 | Mudanças moderadas |
| 🟧 Complexo | 1.6 | Mudanças complexas |
| 🟥 Muito Complexo | 2.0 | Mudanças muito complexas |

#### Algorítmico
| Nível | Multiplicador | Descrição |
|-------|--------------|------------|
| 🟢 Trivial | 0.5 | Mudanças muito simples |
| 🟦 Básico | 1.0 | Mudanças básicas |
| 🟨 Moderado | 1.5 | Mudanças moderadas |
| 🟧 Complexo | 2.0 | Mudanças complexas |
| 🟥 Muito Complexo | 2.5 | Mudanças muito complexas |

### Tipos de Commit

| Tipo | Multiplicador | Descrição |
|------|--------------|------------|
| ✨ Feature | 1.0 | Tempo base |
| 🐛 Fix | 0.5 | Metade do tempo |
| 📦 Publish | 0.1 | 10% do tempo |
| 🔀 Merge | 0.0 | Sem tempo adicional |
| ⚡ Default | 0.8 | 80% do tempo base |

### Outros Multiplicadores

| Fator | Valor | Descrição |
|-------|-------|-----------|
| 📝 Planning Base | 0.3 | 30% do tempo base |
| 📈 Planning Net Weight | 0.7 | +70% pelo net ratio |
| 📉 Planning Deletion | 0.2 | -80% para deleções |
| 🗑️ Deletion Time | 0.1 | 10% do tempo para deleções |

## 📋 Relatórios Gerados

### 1. Análise de Mudanças (analyze-git-changes.md)
```markdown
# Git Changes Analysis

## Overall Statistics
- Total Commits: 40
- Total Files Changed: 286
- Total Lines Added: 16592
- Total Lines Deleted: 2251
- Total Hours Estimated: 996.06
```

### 2. Relatório de Horas (git-hours-report.md)
```markdown
# Relatório de Horas do Git

## Resumo do Projeto
- Período: 2024-06-18 - 2025-01-23
- Dias Totais: 219
- Dias com Commits: 17
- Total de Horas: 996.06
```

## 🚀 Como Usar

### Instalação

1. Clone o repositório Codex dentro do seu projeto:
```bash
git clone https://github.com/Akad-Seguros/front-codex.git .codex
```

### Execução

Você pode executar a análise de duas formas:

1. Script único (recomendado):
```bash
node .codex/pkg/timetracker/index.js
```

2. Scripts individuais:
```bash
# Análise de mudanças
node .codex/pkg/timetracker/analyze-git-changes.js

# Relatório de horas
node .codex/pkg/timetracker/git-hours-report.js
```

### Exemplos de Saída

1. Para um commit de feature:
```
feat: new payment system
- Files: 5 (3 js, 2 test)
- Added: 200 lines
- Complexity: ALGORITHMIC/COMPLEX
- Time: 4.5h (1.5h planning + 3h implementation)
```

2. Para um commit de fix:
```
fix: payment validation
- Files: 1 (1 js)
- Changed: 10 lines
- Complexity: ALGORITHMIC/BASIC
- Time: 0.4h (0.1h planning + 0.3h implementation)
```

## ❓ FAQ

### 1. Por que os tempos são diferentes do tempo real gasto?
O sistema calcula uma estimativa baseada em médias e padrões. O tempo real pode variar devido a:
- 🧠 Experiência do desenvolvedor
- 🔍 Complexidade do domínio
- 🐛 Debugging não previsto
- 📚 Pesquisa e aprendizado

### 2. Como são tratados commits de merge?
Commits de merge recebem multiplicador 0.0, pois:
- 🤖 Geralmente são automáticos
- 🔄 Não representam trabalho adicional
- ⚡ São resultado de trabalho já contabilizado

### 3. Por que deleções têm peso menor?
Remover código geralmente é mais rápido que adicionar porque:
- 🎯 O escopo já é conhecido
- 📝 Não requer documentação
- 🧪 Menos testes necessários

### 4. Como melhorar a precisão das estimativas?
- ✍️ Use mensagens de commit descritivas
- 🎯 Faça commits atômicos
- 📏 Mantenha um padrão de commits
- 📊 Ajuste os multiplicadores conforme feedback

### 5. Limitações Conhecidas
- 🤔 Não considera tempo de pesquisa
- 📚 Não inclui tempo de documentação externa
- 🤝 Não contabiliza tempo em reuniões
- 🐛 Debugging pode ser subestimado

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor, leia nosso guia de contribuição para mais detalhes.
