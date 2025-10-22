from dataclasses import dataclass

@dataclass
class Persona:
    nombre: str

###data class

@dataclass

class PersonaDto(Persona):
    nombre: str
    edad: int
    cat: str
person = PersonaDto("Luis", 26, "Dev")

print(person)