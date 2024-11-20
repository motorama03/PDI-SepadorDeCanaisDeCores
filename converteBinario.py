from PIL import Image

def calcular_media_rgb(input_path, output_p2_path, output_p3_path):
    # Carregar a imagem no formato PPM (P3)
    imagem = Image.open(input_path)
    imagem = imagem.convert("RGB")  # Garantir que esteja no modo RGB
    
    largura, altura = imagem.size
    pixels_p2 = []  # Para escala de cinza (P2)
    pixels_p3 = []  # Para média dos valores RGB (P3)

    # Mesmo código usado para gerar toodas as imagens aternando somente entre os valores da média do RGB
    for y in range(altura):
        linha_p2 = []
        linha_p3 = []
        for x in range(largura):
            r, g, b = imagem.getpixel((x, y))
            media = (r + g + b) // 3  # Cálculo da média RGB
            linha_p2.append(media)
            linha_p3.append((255, 255, media))  # Mantém a média para RGB no P3
        pixels_p2.append(linha_p2)
        pixels_p3.append(linha_p3)

    # Salvar a imagem em escala de cinza (P2)
    #with open(output_p2_path, 'w') as f:
    #    f.write("P2\n")
    #    f.write(f"{largura} {altura}\n255\n")
    #    for linha in pixels_p2:
    #        f.write(" ".join(map(str, linha)) + "\n")
    #print(f"Imagem em escala de cinza (P2) salva em {output_p2_path}")

    # Salvar a imagem com média dos valores RGB (P3)
    with open(output_p3_path, 'w') as f:
        f.write("P3\n")
        f.write(f"{largura} {altura}\n255\n")
        for linha in pixels_p3:
            for r, g, b in linha:
                f.write(f"{r} {g} {b} ")
            f.write("\n")
    print(f"Imagem com média RGB (P3) salva em {output_p3_path}")


def converter_pgm_para_pbm_binario(input_path, output_path, limiar=128):
    # Carregar a imagem PGM (escala de cinza)
    imagem = Image.open(input_path)
    imagem = imagem.convert("L")  # Garantir que esteja em escala de cinza

    # Binarização com o limiar (PBM em ASCII - P1)
    imagem_binarizada = imagem.point(lambda p: 1 if p > limiar else 0)
    
    # Salvar como PBM ASCII (P1)
    with open(output_path, 'w') as f:
        f.write("P1\n")
        f.write(f"{imagem.width} {imagem.height}\n")
        for y in range(imagem.height):
            linha = "".join(str(imagem_binarizada.getpixel((x, y))) + " " for x in range(imagem.width))
            f.write(linha.strip() + "\n")
    print(f"Arquivo PBM binário salvo em {output_path}")

def aplicar_negativo(input_path, output_path):
    # Carregar a imagem binarizada (escala de cinza)
    imagem = Image.open(input_path)
    imagem = imagem.convert("L")  # Garantir que esteja em escala de cinza

    # Aplicar o negativo
    imagem_negativa = imagem.point(lambda p: 255 - p)
 
    # Salvar a imagem no formato PGM ASCII (P2)
    with open(output_path, 'w') as f:
        f.write("P2\n")
        f.write(f"{imagem.width} {imagem.height}\n255\n")
        for y in range(imagem.height):
            linha = " ".join(str(imagem_negativa.getpixel((x, y))) for x in range(imagem.width))
            f.write(linha + "\n")
    print(f"Imagem negativa PGM salva em {output_path}")

# Caminhos dos arquivos de entrada e saída
caminho_ppm_entrada = "/home/matias/Documentos/BCC2024-2/PDI/converteBinario/Fig4.ppm"
caminho_p2_saida = "/home/matias/Documentos/BCC2024-2/PDI/Fig4_escala_cinza.pgm"
caminho_p3_saida = "/home/matias/Documentos/BCC2024-2/PDI/RGmax.ppm"
caminho_pgm_entrada = "/home/matias/Documentos/BCC2024-2/PDI/converteBinario/Entrada.pgm"
caminho_pbm_saida = "/home/matias/Documentos/BCC2024-2/PDI/converteBinario/Saida.pbm"
caminho_pgm_negativo = "/home/matias/Documentos/BCC2024-2/PDI/converteBinario/Negativo.pgm"

# Calcular média RGB e salvar imagens P2 e P3
calcular_media_rgb(caminho_ppm_entrada, caminho_p2_saida, caminho_p3_saida)

# Definir o limiar e converter para PBM
limiar = 128
#converter_pgm_para_pbm_binario(caminho_pgm_entrada, caminho_pbm_saida, limiar)

# Aplicar o negativo na imagem binarizada e salvar como PGM (P2)
#aplicar_negativo(caminho_pgm_entrada, caminho_pgm_negativo)
