# Trabalho 03 - Análise de Grafos Eulerianos

## 📝 Descrição

Este projeto implementa um analisador de grafos que determina se um grafo é **Euleriano**, **Semi-Euleriano** ou **Não-Euleriano**, baseado no teorema de Euler sobre caminhos e ciclos eulerianos. O programa também gera visualizações gráficas dos grafos analisados.

## 🎯 Objetivo

O objetivo principal é analisar diferentes grafos e classificá-los segundo os critérios eulerianos:

- **Euleriano**: Possui um ciclo euleriano (todos os vértices têm grau par)
- **Semi-Euleriano**: Possui um caminho euleriano (exatamente dois vértices têm grau ímpar)
- **Não-Euleriano**: Não possui caminho nem ciclo euleriano (mais de dois vértices têm grau ímpar)

## 🚀 Funcionalidades

- ✅ Leitura de grafos a partir de arquivos de texto
- ✅ Análise automática da condição euleriana
- ✅ Geração de visualizações gráficas dos grafos
- ✅ Processamento em lote de múltiplos arquivos
- ✅ Análise de datasets grandes (como Email-Enron.txt)

## 📁 Estrutura do Projeto

```
trabalho03-grafos/
├── script.py           # Código principal do analisador
├── Email-Enron.txt     # Dataset de emails da Enron (367.663 arestas)
├── grafo1.txt          # Grafo de teste 1
├── grafo2.txt          # Grafo de teste 2
├── grafo3.txt          # Grafo de teste 3
├── grafo4.txt          # Grafo de teste 4
└── README.md           # Este arquivo
```

## 🛠️ Dependências

Para executar o projeto, você precisa instalar as seguintes bibliotecas Python:

```bash
pip install matplotlib networkx
```

### Bibliotecas utilizadas:
- **matplotlib**: Para geração de gráficos e visualizações
- **networkx**: Para manipulação e análise de grafos

## 🔧 Como Usar

### 1. Preparação do ambiente

```bash
# Clone o repositório
git clone https://github.com/devNatanfreitas/trabalho03-grafos.git
cd trabalho03-grafos

# Instale as dependências
pip install matplotlib networkx
```

### 2. Execução

```bash
python script.py
```

### 3. Formato dos arquivos de entrada

Os arquivos de entrada devem seguir o formato:
```
vértice1 vértice2
vértice1 vértice3
vértice2 vértice4
...
```

Onde cada linha representa uma aresta entre dois vértices.

## 📊 Saída do Programa

O programa gera:

1. **Saída no console**: Classificação de cada grafo
   ```
   Resultado para grafo1.txt: É Euleriano
   Resultado para grafo2.txt: Semi-Euleriano
   Resultado para grafo3.txt: Não é Euleriano
   ...
   ```

2. **Imagens PNG**: Visualizações gráficas salvas como:
   - `grafo1.png`
   - `grafo2.png`
   - `Email-Enron.png`
   - etc.

## 🔬 Algoritmo

### Teorema de Euler
O algoritmo baseia-se no teorema de Euler para grafos conexos:

- **Ciclo Euleriano**: Existe se e somente se todos os vértices têm grau par
- **Caminho Euleriano**: Existe se e somente se há exatamente 0 ou 2 vértices de grau ímpar

### Implementação
```python
def is_eulerian(self):
    odd = 0
    for v in self.adj:
        if len(self.adj[v]) % 2 != 0:
            odd += 1
    
    if odd > 2:
        return 0    # Não é Euleriano
    elif odd == 2:
        return 1    # Semi-Euleriano
    else:
        return 2    # É Euleriano
```

## 📈 Datasets

### Email-Enron.txt
- **Origem**: Dataset de comunicações por email da empresa Enron
- **Tamanho**: 367.663 arestas
- **Descrição**: Grafo que representa comunicações entre funcionários

### grafos1-4.txt
- Grafos de teste menores para validação do algoritmo
- Diferentes topologias para testar todos os casos (Euleriano, Semi-Euleriano, Não-Euleriano)

## 🎨 Visualização

O programa utiliza NetworkX e Matplotlib para gerar visualizações dos grafos com:
- Nós destacados em azul claro
- Arestas em cinza
- Labels nos vértices
- Título indicando o nome do arquivo

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto é desenvolvido para fins educacionais como parte do curso de Teoria dos Grafos.

## 👥 Autor

- **devNatanfreitas** - [GitHub](https://github.com/devNatanfreitas)

---

⭐ Se este projeto foi útil para você, considere dar uma estrela no repositório!