<div align="center">
  <img src="/data/logo_tucuxi2.png"><br>
</div>
# curumim
Gera informações pessoais de brasileiros, como: ID, Nome (linkado sobrenome da mãe), Nome da Mãe, nascimento, sexo e CPF válido.

## Necessidade
As vezes precisamos fazer processamento com informações de dados reais. Assim, quando queremos resolver isso rapidamente vamos na 
internet e baixamos em algum lugar.
Devemos ter muito cuidado, essa informações podem violar o direito de informações pessoais.

## Solução
Esse simples script gera a quantidade de dados simulados de nomes e sobrenomes brasileiros que você precisa para testar seus programas.

### Campos disponíveis:
```
Identificador;
Nome;
Nome da Mãe;
Data nascimento;
Sexo;
CPF válido.
```
Basta executar em um terminal:
>python curumim.py -n 100 -s ',' -o output.tsv

```
Legenda:
-n = número de registros
-s = Delimitador de coluna [default='\t']
-o = Arquivo de saída
```

