def mostrar_integrantes():
  
    print("="*50)
    print("EXAMEN TRANSVERSAL DRY7122")
    print("INTEGRANTES DEL GRUPO")
    print("="*50)
    
    integrantes = [
        "Daniela Ponce",
        "Cristhian Contreras", 
        "Guillermo Aguilera",
        "Deyvi Rodriguez"
    ]
    
    print("\nLista de Integrantes:")
    print("-" * 30)
    
    for i, integrante in enumerate(integrantes, 1):
        print(f"{i}. {integrante}")
    
    print("-" * 30)
    print(f"Total de integrantes: {len(integrantes)}")
    print("="*50)

if __name__ == "__main__":
    mostrar_integrantes()