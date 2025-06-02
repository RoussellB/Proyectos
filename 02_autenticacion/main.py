import csv
import hashlib
import os
import re
from datetime import datetime

ARCHIVO_USUARIOS = "02_autenticacion/usuarios.csv"

# Función para encriptar la contraseña
def hash_contraseña(contraseña):
    return hashlib.sha256(contraseña.encode()).hexdigest()

# Validación de correo electrónico
def es_correo_electrónico_válido(email):
    return re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email) is not None

# Cargar usuarios del archivo CSV
def cargar_usuarios():
    usuarios = []
    if not os.path.exists(ARCHIVO_USUARIOS):
        return usuarios
    try:
        with open(ARCHIVO_USUARIOS, mode='r', newline='') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                usuarios.append(fila)
    except Exception as e:
        print(f"⚠ Error al cargar usuarios: {e}")
    return usuarios

# Guardar un nuevo usuario
def guardar_usuario(email, contraseña_hash, fecha_registro):
    try:
        archivo_existe = os.path.exists(ARCHIVO_USUARIOS)
        with open(ARCHIVO_USUARIOS, mode='a', newline='') as archivo:
            campos = ['email', 'contraseña', 'fecha']
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            if not archivo_existe:
                escritor.writeheader()
            escritor.writerow({'email': email, 'contraseña': contraseña_hash, 'fecha': fecha_registro})
    except Exception as e:
        print(f"⚠ Error al guardar usuario: {e}")

# Registro de usuario
def registrar_usuario():
    print("\n📝 Registro de nuevo usuario")
    email = input("Email: ").strip()
    if not es_correo_electrónico_válido(email):
        print("❌ Email inválido.")
        return
    contraseña = input("Contraseña: ").strip()
    usuarios = cargar_usuarios()
    if any(u['email'] == email for u in usuarios):
        print("❌ El usuario ya está registrado.")
        return
    contraseña_hash = hash_contraseña(contraseña)
    fecha_registro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    guardar_usuario(email, contraseña_hash, fecha_registro)
    print("✔ Usuario registrado correctamente.")

# Inicio de sesión
def iniciar_sesión_usuario():
    print("\n🔐 Iniciar sesión")
    email = input("Email: ").strip()
    contraseña = input("Contraseña: ").strip()
    contraseña_hash = hash_contraseña(contraseña)
    usuarios = cargar_usuarios()
    for usuario in usuarios:
        if usuario['email'] == email and usuario['contraseña'] == contraseña_hash:
            print(f"✔ Bienvenido, {email}")
            menu_usuario(usuario)
            return
    print("❌ Usuario o contraseña incorrecta.")

# Menú del usuario autenticado
def menu_usuario(usuario):
    while True:
        print("\n👤 Opciones")
        print("1. Ver mi información")
        print("2. Cerrar sesión")
        print("3. Salir")
        opcion = input("> ")
        if opcion == '1':
            print(f"\nEmail: {usuario['email']}")
            print(f"Registrado el: {usuario['fecha']}")
        elif opcion == '2':
            print("🔒 Sesión cerrada.")
            return
        elif opcion == '3':
            print("👋 Adiós.")
            exit()
        else:
            print("❌ Opción inválida.")

# Función principal
def main():
    while True:
        print("\nBienvenido al sistema 🛡️")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("> ")
        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            iniciar_sesión_usuario()
        elif opcion == '3':
            print("👋 Hasta luego.")
            break
        else:
            print("❌ Opción inválida.")

if __name__ == "__main__":
    os.makedirs("02_autenticacion", exist_ok=True)
    main()
