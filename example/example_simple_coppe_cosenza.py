"""
Aplicação do modelo COPPE-COSENZA.

Este exemplo foi baseado na dissertação de mestrado de:

    MACHADO, Maurício Thalles de Miranda.
    Modelagem COPPE-Cosenza de Hierarquia Fuzzy em indicadores de
      sustentabilidade de distribuidoras de energia elétrica.
    Gilson Brito Alves Lima, orientador.
    Niterói, 2019.
    78 f. : il.

Fonte: <https://app.uff.br/riuff/bitstream/1/10762/1/MODELAGEM%20COPPE-COSENZA%20DE%20HIERARQUIA%20FUZZY%20EM%20INDICADORES%20DE%20SUSTENTABILIDADE%20DE%20DISTRIBUIDORAS%20DE%20ENERGIA%20EL%C3%89TRICA.pdf>
"""
from typing import List, NewType

import pandas as pd
from scipy.stats import mode

from simple_coppe_cosenza import coppe_cosenza

df = pd.DataFrame({
    # FATORES
    'criterios': ['e1', 'e2', 'e3',   # Critérios econômicos
                  'a1', 'a2', 'a3',   # Critérios ambientais
                  's1', 's2', 's3'],  # Critérios sociais
    # DEMANDAS
    'especialista_1': ['cr', 'co', 'cr', 'pc', 'pc', 'co', 'co', 'pc', 'cr'],
    'especialista_2': ['co', 'pc', 'cr', 'pc', 'co', 'pc', 'pc', 'co', 'cr'],
    'especialista_3': ['co', 'pc', 'cr', 'co', 'pc', 'co', 'pc', 'co', 'cr'],
    'especialista_4': ['cr', 'co', 'cr', 'co', 'pc', 'co', 'co', 'cr', 'cr'],
    'especialista_5': ['cr', 'cr', 'cr', 'co', 'co', 'pc', 'pc', 'co', 'cr'],
    'especialista_6': ['co', 'co', 'cr', 'co', 'pc', 'co', 'pc', 'co', 'cr'],
    'especialista_7': ['co', 'cr', 'cr', 'co', 'co', 'cr', 'co', 'pc', 'cr'],
    # OFERTAS
    # 2015 #
    'empresa_1_2015': ['bo', 'ex', 'ex', 're', 'bo', 'ex', 'ex', 'in', 're'],
    'empresa_2_2015': ['re', 're', 'bo', 're', 'bo', 'bo', 'bo', 're', 're'],
    'empresa_3_2015': ['ex', 'bo', 're', 're', 'bo', 'bo', 'bo', 'bo', 're'],
    'empresa_4_2015': ['ex', 'ex', 'ex', 're', 're', 'bo', 're', 'bo', 're'],
    'empresa_5_2015': ['bo', 'bo', 're', 're', 're', 're', 're', 'in', 'in'],
    # 2016 #
    'empresa_1_2016': ['bo', 'ex', 'ex', 'ex', 'bo', 'ex', 'ex', 're', 're'],
    'empresa_2_2016': ['re', 're', 'bo', 're', 'bo', 're', 'bo', 're', 'bo'],
    'empresa_3_2016': ['bo', 'bo', 're', 're', 'bo', 'bo', 'bo', 'bo', 're'],
    'empresa_4_2016': ['ex', 'ex', 'bo', 're', 'in', 'bo', 're', 'bo', 're'],
    'empresa_5_2016': ['bo', 'bo', 'in', 're', 're', 're', 're', 'in', 're']})

fatores: List[str] = []

for i in df.index:
    fatores.extend(list(mode(df.iloc[i][1:8]).mode))

FloatMatrix = NewType('FloatMatrix', List[List[float]])

resultado_2015: FloatMatrix = []
resultado_2016: FloatMatrix = []

for empresa_2015 in df.iloc[:, 8:13]:
    resultado_2015.append(
        coppe_cosenza(oferta=df[empresa_2015], demanda=fatores)
    )

for empresa_2016 in df.iloc[:, 13:]:
    resultado_2016.append(
        coppe_cosenza(oferta=df[empresa_2016], demanda=fatores)
    )

score_2015 = score_2016 = pd.DataFrame()

for i, score in enumerate(resultado_2015):
    score_2015[f'score_{i+1}'] = score

for i, score in enumerate(resultado_2016):
    score_2016[f'score_{i+1}'] = score

print(score_2015.sum())
print(score_2016.sum())
