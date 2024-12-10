import time
from typing import List

import matplotlib.pyplot as plt
import psutil


class SortingAnalyzer:
    def __init__(self, filename: str):
        """
        Inicializa o analisador com o arquivo de listagem
        """
        self.filename = filename
        self.data = self._load_data()

    def _load_data(self) -> List[str]:
        """
        Carrega os dados do arquivo de listagem
        """
        with open(self.filename, 'r') as file:
            return [line.strip() for line in file.readlines()]

    def _measure_time_and_memory(self, sort_func, data: List[str]):
        """
        Mede o tempo e memória de execução de um algoritmo
        """
        # Copia os dados para não afetar o array original
        data_copy = data.copy()

        # Marca início e memória inicial
        process = psutil.Process()
        memory_start = process.memory_info().rss / 1024 / 1024  # MB
        start_time = time.time()

        # Executa o algoritmo
        sorted_data = sort_func(data_copy)

        # Marca fim e memória final
        end_time = time.time()
        memory_end = process.memory_info().rss / 1024 / 1024  # MB

        return {
            'time': end_time - start_time,
            'memory': memory_end - memory_start,
            'sorted_data': sorted_data
        }

    def bubble_sort(self, arr: List[str]) -> List[str]:
        """
        Implementação do Bubble Sort
        Complexidade: O(n²)
        """
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def merge_sort(self, arr: List[str]) -> List[str]:
        """
        Implementação do Merge Sort
        Complexidade: O(n log n)
        """
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        return self._merge(left, right)

    def _merge(self, left: List[str], right: List[str]) -> List[str]:
        """
        Função auxiliar para o Merge Sort
        """
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def quick_sort(self, arr: List[str]) -> List[str]:
        """
        Implementação do Quick Sort
        Complexidade: O(n log n) média, O(n²) pior caso
        """
        if len(arr) <= 1:
            return arr

        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        return self.quick_sort(left) + middle + self.quick_sort(right)

    def analyze_all(self):
        """
        Analisa todos os algoritmos de ordenação
        """
        algorithms = {
            'Bubble Sort': self.bubble_sort,
            'Merge Sort': self.merge_sort,
            'Quick Sort': self.quick_sort,
            'Python Sort': sorted
        }

        results = {}

        for name, algorithm in algorithms.items():
            print(f"\nAnalisando {name}...")
            result = self._measure_time_and_memory(algorithm, self.data)
            results[name] = result

            print(f"Tempo de execução: {result['time']:.4f} segundos")
            print(f"Consumo de memória: {result['memory']:.2f} MB")

        return results

    def plot_results(self, results):
        """
        Plota os resultados em gráficos
        """
        algorithms = list(results.keys())
        times = [results[algo]['time'] for algo in algorithms]
        memories = [results[algo]['memory'] for algo in algorithms]

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

        # Gráfico de tempo
        ax1.bar(algorithms, times)
        ax1.set_title('Tempo de Execução')
        ax1.set_ylabel('Segundos')
        plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45)

        # Gráfico de memória
        ax2.bar(algorithms, memories)
        ax2.set_title('Consumo de Memória')
        ax2.set_ylabel('MB')
        plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45)

        plt.tight_layout()
        plt.savefig('sorting_analysis.png')
        plt.close()


def main():
    analyzer = SortingAnalyzer('/Users/gtauber/Documents/Development/College/2024/T4/PB/tp1/list_files.txt')
    results = analyzer.analyze_all()
    analyzer.plot_results(results)


if __name__ == "__main__":
    main()