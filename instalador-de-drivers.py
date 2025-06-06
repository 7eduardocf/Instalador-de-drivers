import os
import subprocess

def instalar_drivers(pasta_drivers):
    if not os.path.exists(pasta_drivers):
        print(f"❌ A pasta '{pasta_drivers}' não foi encontrada.")
        return

    arquivos_inf = []
    for raiz, _, arquivos in os.walk(pasta_drivers):
        for arquivo in arquivos:
            if arquivo.lower().endswith('.inf'):
                caminho_completo = os.path.join(raiz, arquivo)
                arquivos_inf.append(caminho_completo)

    if not arquivos_inf:
        print("⚠️ Nenhum arquivo .inf encontrado na pasta.")
        return

    print(f"🔧 Iniciando a instalação de {len(arquivos_inf)} drivers...\n")

    for driver in arquivos_inf:
        print(f"📦 Instalando: {driver}")
        resultado = subprocess.run(
            ["pnputil", "/add-driver", driver, "/install"],
            capture_output=True,
            text=True,
            shell=True
        )
        if resultado.returncode == 0:
            print("✅ Instalado com sucesso.\n")
        else:
            print(f"❌ Erro ao instalar:\n{resultado.stderr}\n")

pasta = r"C:\Drivers"
instalar_drivers(pasta)
