# Título: Consumo de Álcool por Estudantes do Ensino Médio.
## Grupo: 04
## Integrantes
#   - Joyce 
#   - Juan 
#   - Lucas Santana Santos
#   - Pedro 


## Prof. Juliana Cristina Braga

## Bases de Dados: Student Alcohol Consumption.

# Link da Base de Dados (site: Kaggle) = https://www.kaggle.com/uciml/student-alcohol-consumption?select=student-mat.csv

# Os dados foram obtidos num inquérito a alunos dos cursos de matemática do ensino médio. Ele contém muitas informações sociais, de gênero e de estudo interessantes sobre os alunos.

# As informações reunidas se referem ao ano de 2016.





# Analise de dados

# mat - https://drive.google.com/file/d/1uKaUsLSUS9zPC8abN0nQ97zuow321Q9U/view?usp=sharing
import pandas as pd
codigo = "1uKaUsLSUS9zPC8abN0nQ97zuow321Q9U"
file = "https://drive.google.com/u/3/uc?id=" + codigo + "&export=download"
dados = pd.read_csv(file)
dados

## Explorando a base de dados

# Principais características da base de dados:



print('Estatisticas Gerais:\n')
print(dados.describe())

print("(Linhas , Colunas) : ", dados.shape)

print('Informações Gerais:\n')
print(dados.info())

print("Colunas: \n",dados.columns)

# Descrição das Colunas

"""
Atributos para os conjuntos de dados student-mat.csv (curso de matemática):

school - escola do aluno (binário: 'GP' - Gabriel Pereira ou 'MS' - Mousinho da Silveira)
sex - sexo do aluno (binário: 'F' - feminino ou 'M' - masculino)
age - idade do aluno (numérico: de 15 a 22)
address - tipo de endereço residencial do aluno (binário: 'U' - urbano ou 'R' - rural)
famsize - tamanho da família (binário: 'LE3' - menor ou igual a 3 ou 'GT3' - maior que 3)
Pstatus - status de coabitação dos pais (binário: 'T' - vivendo juntos ou 'A' - separados)
Medu - escolaridade da mãe (numérico: 0 - nenhuma, 1 - ensino fundamental (4ª série), 2 - 5ª a 9ª série, 3 - ensino médio ou 4 - ensino superior)
Fedu - escolaridade do pai (numérico: 0 - nenhuma, 1 - ensino fundamental (4º ano), 2 - 5º ao 9º ano, 3 - ensino médio ou 4 - ensino superior)
Mjob - trabalho da mãe (nominal: 'professora', 'cuidados de saúde' relacionados, 'serviços' civis (por exemplo, administrativo ou policial), 'em_ casa' ou 'outro')
Fjob - trabalho do pai (nominal: 'professor', 'saúde' relacionado, 'serviços' civis (por exemplo, administrativo ou policial), 'em_ casa' ou 'outro')
reason - razão para escolher esta escola (nominal: perto de 'casa', 'reputação' da escola, preferência de 'curso' ou 'outra')
guardian - tutor do aluno (nominal: 'mãe', 'pai' ou 'outro')
traveltime - tempo de viagem de casa para a escola (numérico: 1 - <15 min., 2 - 15 a 30 min., 3 - 30 min. a 1 hora, ou 4 -> 1 hora)
studytime - tempo de estudo semanal (numérico: 1 - <2 horas, 2 - 2 a 5 horas, 3 - 5 a 10 horas, ou 4 -> 10 horas)
failures - número de falhas de classe anteriores (numérico: n se 1 <= n <3, senão 4)
schoolup - suporte educacional extra (binário: sim ou não)
famsup - apoio educacional à família (binário: sim ou não)
paid - aulas extras pagas dentro da disciplina Matemática (binário: sim ou não)
activities - atividades extracurriculares (binárias: sim ou não)
nursery - frequentou creche (binário: sim ou não)
higher - deseja cursar o ensino superior (binário: sim ou não)
internet - acesso à internet em casa (binário: sim ou não)
romantic - com um relacionamento romântico (binário: sim ou não)
famrel - qualidade das relações familiares (numérico: de 1 - muito ruim a 5 - excelente)
freetime - tempo livre depois da escola (numérico: de 1 - muito baixo a 5 - muito alto)
goout - sair com amigos (numérico: de 1 - muito baixo a 5 - muito alto)
Dalc - consumo de álcool durante o trabalho (numérico: de 1 - muito baixo a 5 - muito alto)
Walc - consumo de álcool no fim de semana (numérico: de 1 - muito baixo a 5 - muito alto)
health - estado de saúde atual (numérico: de 1 - muito ruim a 5 - muito bom)
absences - número de faltas escolares (numérico: de 0 a 93)

Essas notas estão relacionadas com a matéria do curso:

G1 - nota do primeiro período (numérico: de 0 a 20)
G2 - nota do segundo período (numérico: de 0 a 20)
G3 - nota final (numérico: de 0 a 20, meta de saída)
"""

# Parte I. Estatística Descritiva – Medidas

## Média

# * Qual a média de idade dos estudantes?

media = dados["age"].mean()
print("A média é de %.2f" %media , "anos.")

# * Conforme a idade aumenta, os jovens tendem a beber mais no final de semana?


j = dados.groupby('age')['Walc'].mean()
print("Analisando as médias e os valores, obtemos o seguinte:")
print(j)
print("Com base nos dados, observamos uma tendência para beber no final de semana com o aumento das idades.")

## Mediana

# * Qual a mediana do tempo livre dos estudantes depois da escola?

mediana = dados["freetime"].median()
print("A mediana do tempo livre é de", mediana)

# * Qual a mediana do número de vezes que os estudantes saem com amigos?

mediana = dados["goout"].mean()
print("A mediana é de %.2f"%mediana, "vezes.")

## Moda

# * Qual a moda do consumo de álcool durante o dia útil?

moda1 = dados["Dalc"].mode()
print("A moda é de",moda1.to_string(index=False), ", o que representa um consumo muito baixo durante os dias uteis.")

# * Qual a moda do consumo de álcool no fim de semana?


moda2 = dados["Walc"].mode()
print("A moda é de", moda2.to_string(index=False), ", significa, também, um consumo de álcool muito baixo no fim de semana.")

## Desvio Padrão

# * Qual o desvio padrão do número de faltas?

dp_faltas = dados.absences.std()
print("O desvio padrão é %.2f"% dp_faltas)

# * Qual o desvio padrão de cada um dos períodos e da nota final?


dp_p1 = dados.G1.std()
dp_p2 = dados.G2.std()
dp_final = dados.G3.std()
print("O desvio padrão do primeiro período é %.2f"% dp_p1 )
print("O desvio padrão do segundo período é %.2f"% dp_p2 )
print("O desvio padrão da nota final é %.2f"% dp_final )

## Amplitude

# * Qual amplitude das notas finais dos alunos?


amplitude = (dados['G3'].max() - dados['G3'].min())
print("A amplitude é de" ,amplitude)

# * Qual amplitude de faltas dos alunos?


amplitude = (dados['absences'].max() - dados['absences'].min())
print("A amplitide de faltas é de ", amplitude)

## Regressão

# * Qual seria o valor previsto para o consumo de álcool no final de semana para alguém com 30 anos e 40 anos?

import numpy as np
a,b = np.polyfit(x=dados["age"], y =dados["Walc"], deg = 1)

x = 30
y = a*x +b
print("Para alguém com 30 anos, o valor futuro que representaria o possível consumo de álcool é %.2f"% y,"representando um valor quase alto.")

x = 40
y = a*x +b
print("Para alguém com 40 anos, o valor futuro que representaria o possível consumo de álcool é %.2f"% y,"demosntrando um valor muito alto.")

# * Qual a relação familiar prevista para um estudante com 20 anos e depois com 30 anos?

m,b = np.polyfit(x=dados["age"], y =dados["famrel"], deg = 1)

x1 = 20
y1 = m*x1 + b

x2 = 30
y2 = m*x2 + b

print("Analisando os resultados, com 20 e 30 anos a relação seria caracterizada como muito boa. Sendo %.2f"% y1,"para 20 anos e %.2f"% y2,"para 30 anos.")

## Correlações (não se aplica)


corr = dados.corr()
print("As correlações são possíveis, porém não são significativas, visto que todas tendem a zero.")
corr

# Parte II - Gráficos


## Categorização de cada variável








# * **school**: Qualitativa  nominal
# * **sex**: Qualitativa nominal
# * **age**: Quantitativa discreta
# * **adress**: Qualitativa nominal
# * **famsize**: Qualitativa ordinal
# * **Pstatus**: Qualitativa nominal
# * **Medu**: Qualitativa ordinal, embora seja representada por números inteiros
# * **Fedu**: Qualitativa ordinal, embora seja representada por números inteiros
# * **Mjob**: Qualitativa nominal
# * **Fjob**: Qualitativa nominal
# * **reason**: Qualitativa nominal
# * **guardian** :Qualitativa nominal
# * **traveltime**: Quantitativa discreta
# * **studytime**: Quantitativa discreta
# * **failures**: Quantitativa discreta
# * **schoolup**: Qualitativa nominal
# * **famsup**: Qualitativa nominal
# * **paid**: Qualitativa nominal
# * **activities**: Qualitativa nominal
# * **nursery**: Qualitativa nominal
# * **higher**: Qualitativa nominal
# * **internet**: Qualitativa nominal
# * **romantic**: Qualitativa nominal
# * **famrel**: Qualitativa ordinal, embora seja representada por números inteiros
# * **freetime**: Qualitativa ordinal, embora seja representada por números inteiros
# * **goout**: Qualitativa ordinal, embora seja representada por números inteiros
# * **Dalc**: Qualitativa ordinal, embora seja representada por números inteiros
# * **Walc**: Qualitativa ordinal, embora seja representada por números inteiros
# * **health**: Qualitativa ordinal, embora seja representada por números inteiros
# * **absences**: Quantitativa discreta
# * **G1**: Quantitativa discreta
# * **G2**: Quantitativa discreta
# * **G3**: Quantitativa discreta

## Gráficos

#rodar célula para funcionar as bibliotecas utilizadas
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import median

dalcmed = dados.groupby('famrel')['Dalc'].mean()
relfam = dados.famrel.sort_values().unique()
plt.bar(relfam, dalcmed)
plt.xlabel('Qualidade da relação familiar')
plt.ylabel('Consumo alcoólico durante a semana')
plt.title('Relação do consumo de álcool durante a semana com a qualidade das relações familiares', size = 15)
plt.show()

walcmed = dados.groupby('famrel')['Walc'].mean()
relfam = dados.famrel.sort_values().unique()
plt.bar(relfam, walcmed, color = 'red')
plt.xlabel('Qualidade da relação familiar')
plt.ylabel('Consumo alcoólico aos fins de semana')
plt.title('Relação do consumo alcoólico aos fins de semana com a qualidade das relações familiares', size = 15)
plt.show()

rotulos = dados.famsup.unique()
plt.pie(dados.groupby('famsup')['famsup'].count(), labels = rotulos)
plt.title('Apoio familiar nos estudos', size = 15)

faltasord = dados.sort_values(by = 'absences')
faltasord.plot(x = 'absences', y = 'G3', title = 'Relação do número de faltas com a nota final', ylabel = 'Nota final (de 0 a 20)')

sexm = dados.query('sex == "M"')
sexf = dados.query('sex == "F"')
plt.hist(sexm.age, label='Masculino', bins = 10, color = 'blue', alpha = 0.3)
plt.hist(sexf.age, label='Feminino', bins = 10, color = 'red', alpha = 0.3)
plt.legend(loc = 'upper right')
plt.ylabel('Frequência das idades')
plt.xlabel('Idade')
plt.title('Distribuição da idade dos alunos pelo sexo')
plt.show()

plt.boxplot(dados.absences, showmeans = True)
plt.ylabel('Número de Faltas')
plt.title('Frequência do número de faltas', size = 15)

print('Relação da nota final com o consumo de álcool durante a semana')
sns.stripplot(x = 'Dalc', y = 'G3', data = dados, hue = 'famsup', size = 10)

print('Relação do consumo de álcool durante a semana com a saúde mental dos alunos')
dados1 = dados.sort_values(by = 'Dalc')
sns.barplot(x = 'Dalc', y = 'health', hue = 'school', data = dados1, estimator = median, capsize = .2)

print('Relação do consumo de álcool aos finais de semana com a saúde mental dos alunos')
dados2 = dados.sort_values(by = 'Walc')
sns.barplot(x = 'Walc', y = 'health', hue = 'school', data = dados2, estimator = median, capsize = .2)

# Parte III - Iteração sobre a tabela


# * Qual a média geral de cada aluno?

for indice,valor in dados.iterrows():
  media = (valor.G1 + valor.G2 + valor.G3)/3
  print(f"Aluno {indice}","média geral: %.2f"%media)

# * Se o nivel de estudo do pai e da mãe forem bons, o estudante tende a ter apoio familiar?

total_espc = 0
total_geral = 0

tot_sim_geral = 0
tot_sim_espc = 0

for indice,valor in dados.iterrows():
  if valor.famsup == "yes" or valor.famsup == "no":
    total_geral = total_geral + 1

  if valor.famsup == "yes":
    tot_sim_geral = tot_sim_geral + 1

  if (valor.Fedu >= 4) and (valor.Medu >= 4):
    if valor.famsup == "yes" or valor.famsup == "no":
      total_espc = total_espc + 1
    if valor.famsup == "yes":
      tot_sim_espc = tot_sim_espc + 1

porc_geral = (tot_sim_geral/total_geral)*100
porc = (tot_sim_espc/total_espc)*100

print("A porcentagem de apoio geral é de %.2f"%porc_geral,"%", "enquanto o apoio para pais de alto nivel de escolaridade é de %.2f"%porc,"%.")
print("Logo, podemos concluir que sim, com a maior escolaridade dos pais há uma maior tendência a haver apoio familiar.")  

# * Ter relação familiar ruim faz os estudantes beberem mais no final de semana?



tot_bebe_geral = 0

tot_bebe1 = 0
tot_bebe2 = 0

for indice,valor in dados.iterrows():
  if (valor.Walc == 4) or (valor.Walc == 5):
      tot_bebe_geral = tot_bebe_geral + 1

  if (valor.famrel == 1) or (valor.famrel == 2):
    if (valor.Walc == 4) or (valor.Walc == 5):
      tot_bebe1 = tot_bebe1 + 1

  if (valor.famrel == 4) or (valor.famrel == 5):
    if (valor.Walc == 4) or (valor.Walc == 5):
      tot_bebe2 = tot_bebe2 + 1

porc1 = (tot_bebe1/tot_bebe_geral)*100
porc2 = (tot_bebe2/tot_bebe_geral)*100

print("Para familias sem boa relação a porcentagem de alunos que bebem muito nos finais de semana é de %.2f"%porc1,"%","enquanto para familias com boas relações a porcentagem é de %.2f"%porc2,"%") 

# * Os estudantes que possuem um tempo maior pra chegar à escola faltam mais?


qnt_tmenor = 0
faltas_tmenor = 0

qnt_tmaior = 0
faltas_tmaior = 0

for indice,valor in dados.iterrows():
  if valor.traveltime < 3:
    qnt_tmenor = qnt_tmenor + 1
    faltas_tmenor = faltas_tmenor + valor.absences

  if valor.traveltime >= 3:
    qnt_tmaior = qnt_tmaior + 1
    faltas_tmaior = faltas_tmaior + valor.absences

total_faltas = faltas_tmenor + faltas_tmaior
total_pessoas = qnt_tmenor + qnt_tmaior

porc_tmenor_faltas = (faltas_tmenor/total_faltas)*100
porc_tmaior_faltas = (faltas_tmaior/total_faltas)*100

print("Apesar de parecer estranho, a porcentagem de falta dos estudantes que demoram mais pra chegar á escola é %.2f"%porc_tmaior_faltas ,"%","enquanto os que chegam mais rápido possuem %.2f"%porc_tmenor_faltas, "% de faltas.")
print("Logo, concluimos que o tempo de viagem até a escola não é um parâmetro para determinar a razão das faltas.")


# * Os estudantes que bebem na semana faltam mais?


tot_p = dados["absences"].count()
soma1 = 0
soma2 = 0

for indice,valor in dados.iterrows():
  if valor.Dalc >= 3:    
    soma1 = soma1 + valor.absences

  if valor.Dalc <= 3:
      soma2 = soma2 + valor.absences

soma_t = soma1 + soma2
porc1 = (soma1/soma_t)*100
porc2 = (soma2/soma_t)*100

print("A porcentagem de estudantes que bebem bastante na semana e faltam é %.2f"%porc1,"%")
print("A porcentagem de estudantes que bebem pouco na semana e faltam é %.2f"%porc2,"%")
print("Portanto, concluimos que o tanto que o estudante bebe durante a semana não é um parâmetro para determinar a quantidade de faltas dele.")