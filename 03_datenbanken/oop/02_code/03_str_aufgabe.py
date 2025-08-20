from __future__ import annotations

class City:
    def __init__(self, name: str, population: int) -> None:
        self.name = name
        self.pop = population
    
    def __str__(self) -> str:
        return f'name: {self.name}, population: {self.pop}'

    def compare_population(self, city: City) ->str:
        if self.pop > city.pop:
            return f'{self.name} hat eine höhere Einwohnerzahl als {city.name}'
        elif self.pop == city.pop:
            return f'{self.name} hat die gleiche Einwohnerzahl als {city.name}'
        else:
            return f'{self.name} hat die wenigere Einwohnerzahl als {city.name}'

munich = City('München', 1600000)
hamburg = City('Hamburg', 1450000)

print(munich)
print(hamburg)

print(hamburg.compare_population(munich))