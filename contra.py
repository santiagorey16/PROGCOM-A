import string

# ---------- Listas de apoyo ----------

COLORES = {
    "red", "blue", "green", "yellow", "black", "white", "orange", "purple",
    "pink", "brown", "gray", "grey",
    "rojo", "azul", "verde", "amarillo", "negro", "blanco", "naranja",
    "morado", "rosa", "cafe", "marron", "gris",
    "rouge", "bleu", "vert", "jaune", "noir", "blanc"
}

PALABRAS_EXTRANJERAS_4 = {
    "blue", "pink", "love", "time", "life", "code", "book", "game"
}

PALABRAS_ES_4 = {
    "amor", "vida", "casa", "perro", "gato", "luz", "sol", "luna"
}

# ---------- Reglas ----------

def regla_1_longitud(password: str) -> bool:
    return len(password) >= 12

def regla_2_tipos_caracteres(password: str) -> bool:
    tiene_mayus = any(c.isupper() for c in password)
    tiene_minus = any(c.islower() for c in password)
    tiene_num = any(c.isdigit() for c in password)
    tiene_simbolo = any(not c.isalnum() for c in password)
    return tiene_mayus and tiene_minus and tiene_num and tiene_simbolo

def regla_3_color(password: str) -> bool:
    pw = password.lower()
    return any(color in pw for color in COLORES)

def regla_4_no_empieza_ni_termina_num(password: str) -> bool:
    if not password:
        return False
    return not password[0].isdigit() and not password[-1].isdigit()

def regla_5_palabra_extranjera_4(password: str) -> bool:
    pw = password.lower()
    for palabra in PALABRAS_EXTRANJERAS_4:
        if palabra in pw and palabra not in PALABRAS_ES_4:
            return True
    return False

# ---------- Validador que solo devuelve la PRIMERA regla que falla ----------

def validar_password_primera_regla(password: str):
    if not regla_1_longitud(password):
        return False, 1, "La contraseña debe tener mínimo 12 caracteres."
    if not regla_2_tipos_caracteres(password):
        return False, 2, "Debe tener mayúsculas, minúsculas, números y símbolos."
    if not regla_3_color(password):
        return False, 3, "Debe incluir el nombre de un color (ej. 'blue', 'rojo', 'green')."
    if not regla_4_no_empieza_ni_termina_num(password):
        return False, 4, "No puede empezar ni terminar con un número."
    if not regla_5_palabra_extranjera_4(password):
        return False, 5, "Debe contener una palabra de 4 letras en otro idioma (ej. 'blue', 'pink', 'love')."
    return True, None, None

# ---------- Juego principal ----------

if __name__ == "__main__":
    MAX_INTENTOS = 5
    intentos = 0

    print("🎮 Bienvenido al *Juego de la Contraseña*")
    print("Debes crear una contraseña que cumpla primero con esta regla:")
    print("1️⃣ Mínimo 12 caracteres.")

    while intentos < MAX_INTENTOS:
        pwd = input(f"👉 Intento {intentos + 1}: escribe tu contraseña: ")

        if pwd.lower() == "salir":
            print("👋 Has salido del juego. ¡Hasta luego!")
            break

        intentos += 1
        valida, num_regla, mensaje = validar_password_primera_regla(pwd)

        if valida:
            print("\n✅ ¡GANASTE! Tu contraseña cumple las 5 reglas del juego 🎉")
            print(f"Lo lograste en {intentos} intento(s).")
            print("\n las reglas eran:" \
            "\n1️⃣ Mínimo 12 caracteres." \
            "\n2️⃣ Debe tener mayúsculas, minúsculas, números y símbolos." \
            "\n3️⃣ Debe incluir el nombre de un color (ej. 'blue', 'rojo', 'green')." \
            "\n4️⃣ No puede empezar ni terminar con un número." \
            "\n5️⃣ Debe contener una palabra de 4 letras en otro idioma (ej. 'blue', 'pink', 'love').")
            break
        else:
            print(f"\n❌ Aún no sirve. Estás fallando en la Regla {num_regla}:")
            print("   →", mensaje)

            if intentos < MAX_INTENTOS:
                print(f"Te quedan {MAX_INTENTOS - intentos} intento(s). Intenta de nuevo.\n")
            else:
                print("\n💀 Te quedaste sin intentos. ¡Juego terminado!")
                print("\n las reglas eran:" \
                "\n1️⃣ Mínimo 12 caracteres." \
                "\n2️⃣ Debe tener mayúsculas, minúsculas, números y símbolos." \
                "\n3️⃣ Debe incluir el nombre de un color (ej. 'blue', 'rojo', 'green')." \
                "\n4️⃣ No puede empezar ni terminar con un número." \
                "\n5️⃣ Debe contener una palabra de 4 letras en otro idioma (ej. 'blue', 'pink', 'love').")
                print("Vuelve a ejecutar el programa para jugar otra vez.")