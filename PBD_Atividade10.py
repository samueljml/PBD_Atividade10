import random
 
 
def scalar_multiply(escalar, vetor):
    return [escalar * i for i in vetor]
 

def vector_sum(vetores):
    resultado = vetores[0]
    for vetor in vetores[1:]:
        resultado = [resultado[i] + vetor[i] for i in range(len(vetor))]
    return resultado
 
 
def vector_mean(vetores):
    return scalar_multiply(1 / len(vetores), vector_sum(vetores))
 
 
def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))
 
 
def vector_subtract(v, w):
    return [v_i - w_i for v_i, w_i in zip(v, w)]
 
 
def sum_of_squares(v):
    return dot(v, v)
 
 
def squared_distance(v, w):
    return sum_of_squares(vector_subtract(v, w))
 
 
class KMeans:
    def __init__(self, k, means=None):
        self.k = k
        self.means = means
 
    def classify(self, ponto):
        return min(range(self.k), key=lambda i: squared_distance(ponto, self.means[i]))
 
    def train(self, pontos):
        self.means = random.sample(pontos, self.k)
        assigments = None
        while True:

            new_assigments = list(map(self.classify, pontos))
            if new_assigments == assigments:
                return
            assigments = new_assigments
            for i in range(self.k):
                i_points = [p for p, a in zip(pontos, assigments) if a == i]
                if i_points:
                    self.means[i] = vector_mean(i_points)
 
 
def obtem_melhor_k (base, i, limiar):
    base_dados = base[0]
    dados_escolhidos = base[1]
    
    k, m = 2, 0.0
    indice_menor_k = k
    while k <= i:
        kmeans = KMeans(k, dados_escolhidos)
        kmeans.train(base_dados)
        km = kmeans.means
        m = vector_mean(km)
        if (m[0] < limiar):
            indice_menor_k = k
        print(f'K={k} -> {m}')
        k = k + 1

    return indice_menor_k


def test_k_means ():
    dados = [[1], [3], [6], [7], [10], [11], [17], [20], [28]]
    dados_escolhidos = [[1], [10], [11], [28]]
    base = [dados, dados_escolhidos]

    i, limiar = 6, 12
    menor_k = obtem_melhor_k(base, i, limiar)
    print('==========================')
    print('Limiar =', limiar)
    print(f'O menor valor de K é', menor_k)

test_k_means()